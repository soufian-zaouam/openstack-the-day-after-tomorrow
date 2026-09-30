-- book.lua — pandoc Lua filter that turns the GitHub-oriented Markdown
-- chapters into a LaTeX book.
--
-- What it does:
--   * drops the navigation footers ("← Previous · Contents · Next →")
--   * turns "*Part I — Title*" lines into \part{Title} (once per part) and
--     inserts \mainmatter before Part I
--   * "# Chapter N — Title"  -> numbered chapter "Title"
--     "# Appendix X — Title" -> lettered appendix (\appendix before the first)
--     other level-1 headings -> unnumbered chapters listed in the contents
--   * turns the Technical note / Principle / From the field quotations into
--     tcolorbox environments (defined in header.tex)
--   * turns "![Figure X.Y](path)" + "*Figure X.Y: caption*" into a real
--     figure with a caption (LaTeX numbers it X.Y by itself)

local stringify = pandoc.utils.stringify

local seen_parts = {}
local mainmatter_done = false
local appendix_done = false
local backmatter_done = false

local function raw(tex)
  return pandoc.RawBlock("latex", tex)
end

local function is_nav_para(block)
  if block.t ~= "Para" then return false end
  local has_md_link = false
  for _, inl in ipairs(block.content) do
    if inl.t == "Link" and inl.target:match("%.md$") then has_md_link = true end
  end
  return has_md_link
end

local function box_kind(bq)
  local first = bq.content[1]
  if not first or first.t ~= "Para" then return nil end
  local lead = first.content[1]
  if not lead or lead.t ~= "Strong" then return nil end
  local label = stringify(lead)
  if label:match("^Technical note") then return "technote" end
  if label:match("^Principle") then return "principle" end
  if label:match("^From the field") then return "fromfield" end
  return nil
end

local function first_image(block)
  -- the image paragraph is parsed by pandoc either as Para{Image} or, with
  -- implicit_figures, as Figure{Plain{Image}}
  if block.t == "Para" and #block.content == 1 and block.content[1].t == "Image" then
    return block.content[1]
  end
  if block.t == "Figure" and #block.content == 1 and block.content[1].t == "Plain"
     and #block.content[1].content == 1 and block.content[1].content[1].t == "Image" then
    return block.content[1].content[1]
  end
  return nil
end

local function figure_from(img_block, cap_para)
  local img = first_image(img_block)
  local caption = cap_para.content[1].content        -- inlines inside Emph
  -- strip the "Figure X.Y:" prefix: LaTeX numbers figures itself
  local text = stringify(caption)
  local rest = text:match("^Figure %d+%.%d+:%s*(.*)$")
  local cap_inlines
  if rest then
    cap_inlines = pandoc.Inlines(pandoc.Str(rest))
    -- keep inline formatting if any: re-parse as markdown
    cap_inlines = pandoc.read(rest, "markdown").blocks[1].content
  else
    cap_inlines = caption
  end
  -- the SVG figures are converted to PDF by build.sh into build/figures/
  img.src = img.src:gsub("^.*/([^/]+)%.svg$", "build/figures/%1.pdf")
  img.caption = cap_inlines
  img.attr = pandoc.Attr("", {}, {width = "100%"})
  local fig = pandoc.Figure({pandoc.Plain({img})}, {long = {pandoc.Plain(cap_inlines)}})
  return fig
end

function Pandoc(doc)
  local out = pandoc.List()
  local blocks = doc.blocks
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    local nxt = blocks[i + 1]

    -- navigation footer: HorizontalRule followed by a paragraph of .md links
    if b.t == "HorizontalRule" and nxt and is_nav_para(nxt) then
      i = i + 2
    elseif is_nav_para(b) then
      i = i + 1

    -- part lines
    elseif b.t == "Para" and #b.content == 1 and b.content[1].t == "Emph"
           and stringify(b):match("^Part %u+ — ") then
      local title = stringify(b):gsub("^Part %u+ — ", "")
      if not seen_parts[title] then
        seen_parts[title] = true
        if not mainmatter_done then out:insert(raw("\\mainmatter")); mainmatter_done = true end
        out:insert(raw("\\part{" .. title .. "}"))
      end
      i = i + 1
    elseif b.t == "Para" and stringify(b) == "Appendices" then
      i = i + 1

    -- level-1 headings
    elseif b.t == "Header" and b.level == 1 then
      local text = stringify(b)
      local chap = text:match("^Chapter %d+ — (.*)$")
      local app = text:match("^Appendix %u — (.*)$")
      if chap then
        out:insert(pandoc.Header(1, pandoc.read(chap, "markdown").blocks[1].content))
      elseif app then
        if not appendix_done then
          out:insert(raw("\\appendix\n\\part*{Appendices}"))
          appendix_done = true
        end
        out:insert(pandoc.Header(1, pandoc.read(app, "markdown").blocks[1].content))
      else
        if text:match("^References") and not backmatter_done then
          out:insert(raw("\\backmatter")); backmatter_done = true
        end
        out:insert(raw("\\chapter*{" .. text .. "}\n\\addcontentsline{toc}{chapter}{" .. text .. "}\n\\markboth{" .. text .. "}{" .. text .. "}"))
      end
      i = i + 1

    -- boxed passages
    elseif b.t == "BlockQuote" and box_kind(b) then
      local kind = box_kind(b)
      out:insert(raw("\\begin{" .. kind .. "}"))
      for _, inner in ipairs(b.content) do out:insert(inner) end
      out:insert(raw("\\end{" .. kind .. "}"))
      i = i + 1

    -- figures: image paragraph followed by an italic caption paragraph
    elseif first_image(b)
           and nxt and nxt.t == "Para" and #nxt.content == 1 and nxt.content[1].t == "Emph"
           and stringify(nxt):match("^Figure %d+%.%d+:") then
      out:insert(figure_from(b, nxt))
      i = i + 2

    else
      out:insert(b)
      i = i + 1
    end
  end
  doc.blocks = out
  return doc
end
