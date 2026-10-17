-- book.lua — pandoc Lua filter that turns the GitHub-oriented Markdown
-- chapters into a LaTeX book.
--
-- What it does:
--   * drops the navigation footers ("← Previous · Contents · Next →")
--   * turns "*Part I — Title*" lines into \part{Title} (once per part) and
--     inserts \mainmatter before Part I
--   * "# Chapter N — Title"  -> numbered chapter "Title" (the counter is set
--     from N, so that an edition built from part of its chapters keeps the
--     numbering of the book)
--     "# Appendix X — Title" -> lettered appendix (\appendix before the first)
--     other level-1 headings -> unnumbered chapters listed in the contents
--   * turns the Technical note / Principle / From the field quotations into
--     tcolorbox environments (defined in header.tex)
--   * turns "![Figure X.Y](path)" + "*Figure X.Y: caption*" into a real
--     figure with a caption (LaTeX numbers it X.Y by itself)
--
-- The structural markers exist in three languages: English (the original
-- edition), French (fr/, see fr/STYLE.md) and Arabic (ar/, see ar/STYLE.md).
-- The language is taken from the "lang" metadata of the edition
-- (tools/pdf/metadata*.yaml). The French edition also writes narrow no-break
-- spaces (U+202F) before high punctuation and inside « »; they become \, in
-- LaTeX because the heading font has no glyph for them. The Arabic files are
-- wrapped in <div dir="rtl"> for GitHub; the filter unwraps those divs, since
-- the whole Arabic document is right-to-left (see tools/pdf/header-ar.tex).

local stringify = pandoc.utils.stringify

local MARKERS = {
  en = {
    part = "^Part %u+ — ", chapter = "^Chapter %d+ — (.*)$", appendix = "^Appendix %u — (.*)$",
    chapter_number = "^Chapter (%d+) — ",
    appendices = "Appendices", references = "^References",
    technote = "^Technical note", principle = "^Principle", fromfield = "^From the field",
    figure = "^Figure %d+%.%d+:", figure_rest = "^Figure %d+%.%d+:%s*(.*)$",
    appendix_part = "Appendices",
  },
  fr = {
    part = "^Partie %u+ — ", chapter = "^Chapitre %d+ — (.*)$", appendix = "^Annexe %u — (.*)$",
    chapter_number = "^Chapitre (%d+) — ",
    appendices = "Annexes", references = "^Références",
    technote = "^Note technique", principle = "^Principe", fromfield = "^Sur le terrain",
    figure = "^Figure %d+%.%d+[^:]*:", figure_rest = "^Figure %d+%.%d+[^:]*:%s*(.*)$",
    appendix_part = "Annexes",
  },
  ar = {
    part = "^الجزء .- — ", chapter = "^الفصل %d+ — (.*)$", appendix = "^الملحق [^ ]+ — (.*)$",
    chapter_number = "^الفصل (%d+) — ",
    appendices = "الملاحق", references = "^المراجع",
    technote = "^ملاحظة تقنية", principle = "^مبدأ", fromfield = "^من الميدان",
    figure = "^الشكل %d+%.%d+:", figure_rest = "^الشكل %d+%.%d+:%s*(.*)$",
    appendix_part = "الملاحق",
  },
}
local M = MARKERS.en
local NNBSP = "\u{202F}"

local seen_parts = {}
local mainmatter_done = false
local appendix_done = false
local backmatter_done = false

local function raw(tex)
  return pandoc.RawBlock("latex", (tex:gsub(NNBSP, "\\,")))
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
  if label:match(M.technote) then return "technote" end
  if label:match(M.principle) then return "principle" end
  if label:match(M.fromfield) then return "fromfield" end
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
  local rest = text:match(M.figure_rest)
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

local function unwrap_direction_divs(blocks)
  -- <div dir="rtl"> … </div> around a whole file (Arabic edition): keep the
  -- content, drop the wrapper
  local flat = pandoc.List()
  for _, b in ipairs(blocks) do
    if b.t == "Div" and b.attributes.dir then
      flat:extend(unwrap_direction_divs(b.content))
    else
      flat:insert(b)
    end
  end
  return flat
end

function Pandoc(doc)
  local lang = doc.meta.lang and stringify(doc.meta.lang) or "en"
  M = MARKERS[lang:sub(1, 2)] or MARKERS.en
  local out = pandoc.List()
  local blocks = unwrap_direction_divs(doc.blocks)
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
           and stringify(b):match(M.part) then
      local title = stringify(b):gsub(M.part, "")
      if not seen_parts[title] then
        seen_parts[title] = true
        if not mainmatter_done then out:insert(raw("\\mainmatter")); mainmatter_done = true end
        out:insert(raw("\\part{" .. title .. "}"))
      end
      i = i + 1
    elseif b.t == "Para" and stringify(b) == M.appendices then
      i = i + 1

    -- level-1 headings
    elseif b.t == "Header" and b.level == 1 then
      local text = stringify(b)
      local chap = text:match(M.chapter)
      local app = text:match(M.appendix)
      if chap then
        local n = text:match(M.chapter_number)
        if n then out:insert(raw("\\setcounter{chapter}{" .. (tonumber(n) - 1) .. "}")) end
        out:insert(pandoc.Header(1, pandoc.read(chap, "markdown").blocks[1].content))
      elseif app then
        if not appendix_done then
          out:insert(raw("\\appendix\\ifdefined\\bookappendixnumbering\\bookappendixnumbering\\fi\n\\part*{" .. M.appendix_part .. "}"))
          appendix_done = true
        end
        out:insert(pandoc.Header(1, pandoc.read(app, "markdown").blocks[1].content))
      else
        if text:match(M.references) and not backmatter_done then
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
           and stringify(nxt):match(M.figure) then
      out:insert(figure_from(b, nxt))
      i = i + 2

    else
      out:insert(b)
      i = i + 1
    end
  end
  doc.blocks = out
  -- narrow no-break spaces (French punctuation): keep them unbreakable in
  -- LaTeX without relying on the fonts having the glyph
  if FORMAT:match("latex") then
    doc = doc:walk({
      Str = function(el)
        if not el.text:find(NNBSP, 1, true) then return nil end
        local parts = pandoc.List()
        local first = true
        for piece in (el.text .. NNBSP):gmatch("(.-)" .. NNBSP) do
          if not first then parts:insert(pandoc.RawInline("latex", "\\,")) end
          if piece ~= "" then parts:insert(pandoc.Str(piece)) end
          first = false
        end
        return parts
      end,
    })
  end
  return doc
end
