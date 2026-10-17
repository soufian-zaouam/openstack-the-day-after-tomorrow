#!/usr/bin/env python3
"""Check that a translated edition stays in step with the original (chapters/, appendices/).

    python3 tools/check_editions.py              # every edition (fr, ar)
    python3 tools/check_editions.py fr           # one edition
    python3 tools/check_editions.py ar --complete   # require every file (release check)

Exit code 0 when every check passes, 1 otherwise. For every source file of the
English edition the script finds its counterpart in the edition (same chapter
number or appendix letter, see fr/STYLE.md and ar/STYLE.md) and compares the
structure of the two:

  * the file exists, carries the part line (Partie / Annexes, الجزء / الملاحق)
    when the original does, and a navigation footer whose links resolve
  * same number of level-1 and level-2 headings, of paragraphs, of bullet and
    numbered list items, of table rows, of figures and figure captions
  * same number of boxed passages of each kind (Technical note / Principle /
    From the field, in the words of each language)
  * the same inline `code` spans and the same URLs, in the same order (commands,
    options and links are not translated)
  * every "Chapter N" / "Appendix X" cross-reference of the original has a
    counterpart (chapitre N / annexe X, الفصل N / الملحق X)
  * the typography of the language: for French, narrow no-break space before
    : ; ! ?, inside « », no-break space before %, typographic apostrophes, no
    straight quotes; for Arabic, Arabic comma, semicolon and question mark
    after Arabic words, « » rather than straight quotes, no tatweel, and the
    <div dir="rtl"> wrapper that GitHub needs to display the file right-to-left
  * the README of the edition lists every chapter file of the edition, and
    every chapter link of that README resolves

An edition marked "in progress" (ar, see TRANSLATIONS.md) may still lack
files: a missing counterpart is reported as not yet translated, not as a
failure, and a progress summary is printed; --complete makes it a failure,
for the release check. The files that exist are checked in full.

The counts are structural, not textual: the script does not judge the
translation, it makes sure nothing was dropped, merged or left in English.
"""
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NNBSP, NBSP = " ", " "
ENGLISH_TITLES = ("OpenStack, the Day After Tomorrow: Operating Mission-Critical OpenStack Platforms",)
ABJAD = {"أ": "A", "ب": "B", "ج": "C", "د": "D", "هـ": "E", "ه": "E", "و": "F"}

EDITIONS = {
    "fr": {
        "name": "French edition",
        "dir": "fr",
        "complete": True,                 # every English file must have a counterpart
        "front": {                        # files whose French name differs from a number/letter pattern
            "00-front-matter.md": "00-pages-liminaires.md",
            "00-how-to-read-this-book.md": "00-comment-lire-ce-livre.md",
            "00-introduction.md": "00-introduction.md",
            "references-and-further-reading.md": "references-et-lectures-complementaires.md",
        },
        "appendix_prefix": "annexe-",     # fr/appendices/annexe-X-<slug>.md
        "boxes": {
            "technote": r"^> \*\*Note technique",
            "principle": r"^> \*\*Principe",
            "fromfield": r"^> \*\*Sur le terrain",
        },
        "part_line": r"^\*Partie [IVX]+ — ",
        "appendices_line": r"^\*Annexes\*",
        "caption": r"^\*Figure \d+\.\d+",
        "chapter_ref": r"\b(?:[Cc]hapitres?) (\d+)",
        "appendix_ref": r"\b[Aa]nnexes? ([A-F])",
        "allowed_extra": {                # deliberate differences, see fr/STYLE.md
            "00-pages-liminaires.md": {"paragraphs": 1},   # the note that presents the French edition
            "annexe-f-glossaire.md": {"paragraphs": 1},     # the entry on "capacité" (capability / capacity)
        },
        "wrapper": None,
    },
    "ar": {
        "name": "Arabic edition",
        "dir": "ar",
        "complete": False,                # being translated by the community: files may be missing
        "front": {},                      # Arabic files carry the English file names (see ar/STYLE.md)
        "appendix_prefix": "appendix-",
        "boxes": {
            "technote": r"^> \*\*ملاحظة تقنية",
            "principle": r"^> \*\*مبدأ",
            "fromfield": r"^> \*\*من الميدان",
        },
        "part_line": r"^\*الجزء .+ — ",
        "appendices_line": r"^\*الملاحق\*",
        "caption": r"^\*الشكل \d+\.\d+",
        "chapter_ref": r"(?:الفصل|الفصلين|الفصول|الفصلَين)\s+(\d+)",
        "appendix_ref": r"(?:الملحق|الملحقين|الملاحق|الملحقَين)\s+(أ|ب|ج|د|هـ|ه|و)(?![ء-ي])",
        "allowed_extra": {                # deliberate differences, see ar/STYLE.md
            "00-front-matter.md": {"paragraphs": 1},   # the note that presents the Arabic edition
        },
        "wrapper": "rtl",                 # every file is wrapped in <div dir="rtl"> … </div>
    },
}
BOXES_EN = {
    "technote": r"^> \*\*Technical note",
    "principle": r"^> \*\*Principle",
    "fromfield": r"^> \*\*From the field",
}

failures = []


def fail(msg):
    failures.append(msg)
    print(f"FAIL  {msg}")


def counterpart(en_path, E):
    name = os.path.basename(en_path)
    sub = os.path.join(E["dir"], "chapters" if "/chapters/" in en_path else "appendices")
    if name in E["front"]:
        return os.path.join(ROOT, sub, E["front"][name])
    if not E["front"] and (name.startswith("00-") or name.startswith("references-")):
        return os.path.join(ROOT, sub, name)      # same name as the English file
    m = re.match(r"^(\d\d)-", name)
    if m:
        hits = glob.glob(os.path.join(ROOT, sub, f"{m.group(1)}-*.md"))
        if len(hits) > 1:
            fail(f"{sub}: several files for chapter {m.group(1)}: {[os.path.basename(h) for h in hits]}")
        return hits[0] if hits else os.path.join(ROOT, sub, f"{m.group(1)}-<missing>.md")
    m = re.match(r"^appendix-([a-f])-", name)
    if m:
        hits = glob.glob(os.path.join(ROOT, sub, f"{E['appendix_prefix']}{m.group(1)}-*.md"))
        return hits[0] if hits else os.path.join(ROOT, sub, f"{E['appendix_prefix']}{m.group(1)}-<missing>.md")
    if not E["front"]:   # same name as the English file
        return os.path.join(ROOT, sub, name)
    return None


def strip_wrapper(md):
    """Drop the <div dir="rtl"> … </div> lines of a right-to-left file."""
    return re.sub(r'^\s*</?div[^>]*>\s*$', "", md, flags=re.M)


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "`", text)


def structure(md, caption_re):
    body = strip_code(strip_wrapper(md))
    lines = body.splitlines()
    return {
        "h1": sum(1 for l in lines if l.startswith("# ")),
        "h2": sum(1 for l in lines if l.startswith("## ")),
        "bullets": sum(1 for l in lines if re.match(r"^\s*[-*] ", l)),
        "numbered": sum(1 for l in lines if re.match(r"^\s*\d+\. ", l)),
        "table_rows": sum(1 for l in lines if l.startswith("|") and not re.match(r"^\|[\s:-]+\|", l)),
        "figures": sum(1 for l in lines if l.startswith("![")),
        "captions": sum(1 for l in lines if re.match(caption_re, l)),
        "quotes": sum(1 for l in lines if l.startswith("> ")),
        "rules": sum(1 for l in lines if l.strip() == "---"),
        "paragraphs": len([b for b in re.split(r"\n\s*\n", body.strip()) if b.strip()]),
        # the arrows of the loops: → in the left-to-right editions, ← in the right-to-left one
        "arrows": body.count("→") + body.count("←"),
    }


def inline_code(md):
    md = re.sub(r"```.*?```", "", md, flags=re.S)
    return re.findall(r"`[^`\n]+`", md)


def urls(md):
    return re.findall(r"https?://[^\s)>\]]+", md)


def nav_links(md, path, complete=True):
    """Return the .md links of the navigation footer (last paragraph) and check they resolve.
    In an edition in progress a link may point to a chapter not yet translated,
    provided the file name is that of an English source."""
    last = strip_wrapper(md).strip().split("\n\n")[-1]
    links = re.findall(r"\]\(([^)]+\.md)\)", last)
    for l in links:
        target = os.path.normpath(os.path.join(os.path.dirname(path), l))
        if os.path.isfile(target):
            continue
        name = os.path.basename(l)
        if not complete and (os.path.isfile(os.path.join(ROOT, "chapters", name))
                             or os.path.isfile(os.path.join(ROOT, "appendices", name))):
            continue
        fail(f"{os.path.relpath(path, ROOT)}: navigation link does not resolve: {l}")
    return links


def prose_lines(md):
    """The lines of a file, outside code, URLs and link targets, with the quoted English title removed."""
    text = strip_code(md)
    text = re.sub(r"\]\([^)]*\)", "]()", text)
    text = re.sub(r"https?://\S+", "", text)
    for title in ENGLISH_TITLES:
        text = text.replace(title, "")
    return list(enumerate(text.splitlines(), 1))


def check_typography_fr(path, md):
    rel = os.path.relpath(path, ROOT)
    for i, line in prose_lines(md):
        if re.search(r"[^\s  ]( )[:;!?](\s|$)", line) and not re.search(r"\d ?: ?\d", line):
            fail(f"{rel}:{i}: ordinary space before high punctuation (use U+202F)")
        if re.search(r"[A-Za-zÀ-ÿ»)][:;!?](?=\s)", line) and not line.startswith("#") and "http" not in line:
            # a colon glued to a word: allowed only inside code or at the start of a line of a table header
            if not re.match(r"^\|", line):
                fail(f"{rel}:{i}: missing space before high punctuation")
        if re.search(r"« [^ ]|[^ ] »", line) or "«" in line and f"«{NNBSP}" not in line and "« " in line:
            fail(f"{rel}:{i}: guillemets without narrow no-break space")
        if re.search(r"\d %", line) or re.search(r"\d%", line):
            fail(f"{rel}:{i}: percent sign without no-break space")
        if "'" in line:
            fail(f"{rel}:{i}: straight apostrophe (use ’)")
        if '"' in line:
            fail(f"{rel}:{i}: straight double quote (use « » or “ ”)")
        if re.search(r"\b(Chapter|Appendix|Figure \d+\.\d+:|Contents|Part [IVX]+ —)\b", line):
            fail(f"{rel}:{i}: English structural marker left in the text")


def check_typography_ar(path, md):
    rel = os.path.relpath(path, ROOT)
    lines = md.strip().splitlines()
    if not lines or lines[0].strip() != '<div dir="rtl">' or (len(lines) > 1 and lines[1].strip()):
        fail(f"{rel}: must start with <div dir=\"rtl\"> followed by an empty line")
    if not lines or lines[-1].strip() != "</div>" or (len(lines) > 1 and lines[-2].strip()):
        fail(f"{rel}: must end with </div> preceded by an empty line")
    inner = "\n".join(lines[1:-1])
    if re.search(r"</?div", inner):
        fail(f"{rel}: a div tag inside the file (one wrapper per file)")
    for i, line in prose_lines(md):
        if line.lstrip().startswith("<"):
            continue
        if re.search(r"[ء-يٰ-ۓ][,;?]", line):
            fail(f"{rel}:{i}: Latin punctuation after an Arabic word (use ، ؛ ؟)")
        if '"' in line:
            fail(f"{rel}:{i}: straight double quote (use « »)")
        if "'" in line:
            fail(f"{rel}:{i}: straight apostrophe")
        # tatweel is allowed in "هـ" (abjad letter) and in a prefix attached to a Latin word (بـOpenStack)
        if re.search(r"(?<!ه)\u0640(?![A-Za-z0-9`*_\[])", line):
            fail(f"{rel}:{i}: tatweel (U+0640) in the text")
        if re.search(r"[٠-٩]", line):
            fail(f"{rel}:{i}: Arabic-Indic digits (the edition uses 0-9)")
        if re.search(r"\b(Chapter|Appendix|Figure \d+\.\d+:|Contents|Part [IVX]+ —)\b", line):
            fail(f"{rel}:{i}: English structural marker left in the text")
        if "→" in line and not line.lstrip().startswith("["):   # the navigation footer keeps both arrows
            fail(f"{rel}:{i}: → in a right-to-left text (the loops are written with ←)")


TYPOGRAPHY = {"fr": check_typography_fr, "ar": check_typography_ar}


def check_edition(code, complete):
    E = EDITIONS[code]
    complete = complete or E["complete"]
    before = len(failures)
    print(f"== {E['name']} ({E['dir']}/)")
    en_files = (sorted(glob.glob(os.path.join(ROOT, "chapters", "*.md")))
                + sorted(glob.glob(os.path.join(ROOT, "appendices", "*.md"))))
    seen = set()
    missing = []
    for en in en_files:
        rel = os.path.relpath(en, ROOT)
        tr = counterpart(en, E)
        if not tr or not os.path.isfile(tr):
            target = os.path.relpath(tr, ROOT) if tr else "?"
            if complete:
                fail(f"{rel}: no counterpart in {E['dir']}/ ({target})")
            else:
                missing.append(rel)
            continue
        seen.add(os.path.abspath(tr))
        trrel = os.path.relpath(tr, ROOT)
        en_md = open(en, encoding="utf-8").read()
        tr_md = open(tr, encoding="utf-8").read()
        se = structure(en_md, r"^\*Figure \d+\.\d+")
        st = structure(tr_md, E["caption"])
        for k, extra in E["allowed_extra"].get(os.path.basename(tr), {}).items():
            se[k] += extra
        for k in se:
            if se[k] != st[k]:
                fail(f"{trrel}: {k} {st[k]} vs {se[k]} in {rel}")
        for kind, pe in BOXES_EN.items():
            ne = len(re.findall(pe, en_md, re.M))
            nt = len(re.findall(E["boxes"][kind], tr_md, re.M))
            if ne != nt:
                fail(f"{trrel}: {kind} boxes {nt} vs {ne} in {rel}")
        if re.search(r"^\*Part [IVX]+ — ", en_md, re.M) and not re.search(E["part_line"], tr_md, re.M):
            fail(f"{trrel}: part line missing")
        if re.search(r"^\*Appendices\*", en_md, re.M) and not re.search(E["appendices_line"], tr_md, re.M):
            fail(f"{trrel}: appendices line missing")
        ce, ct = inline_code(en_md), inline_code(tr_md)
        if ce != ct:
            fail(f"{trrel}: inline code differs from {rel}: {sorted(set(ce) ^ set(ct))[:5]}")
        ue, ut = urls(en_md), urls(tr_md)
        if [u.replace(" ", "") for u in ue] != ut and ue != ut:
            fail(f"{trrel}: URLs differ from {rel}: {sorted(set(ue) ^ set(ut))[:5]}")
        refs_en = set(re.findall(r"\b(?:Chapter|Chapters) (\d+)", en_md))
        refs_tr = set(re.findall(E["chapter_ref"], tr_md))
        if refs_en != refs_tr:
            fail(f"{trrel}: chapter cross-references {sorted(refs_tr)} vs {sorted(refs_en)} in {rel}")
        apps_en = set(re.findall(r"\bAppendi(?:x|ces) ([A-F])", en_md))
        apps_tr = {ABJAD.get(a, a) for a in re.findall(E["appendix_ref"], tr_md)}
        if apps_en != apps_tr:
            fail(f"{trrel}: appendix cross-references {sorted(apps_tr)} vs {sorted(apps_en)} in {rel}")
        ne, nt = nav_links(en_md, en), nav_links(tr_md, tr, complete)
        if len(ne) != len(nt):
            fail(f"{trrel}: navigation footer has {len(nt)} links, {len(ne)} in {rel}")
        TYPOGRAPHY[code](tr, tr_md)
    # orphan files
    for tr in (glob.glob(os.path.join(ROOT, E["dir"], "chapters", "*.md"))
               + glob.glob(os.path.join(ROOT, E["dir"], "appendices", "*.md"))):
        if os.path.abspath(tr) not in seen:
            fail(f"{os.path.relpath(tr, ROOT)}: no English counterpart")
    # README of the edition: every existing chapter linked, every link resolves
    readme = os.path.join(ROOT, E["dir"], "README.md")
    if os.path.isfile(readme):
        md = open(readme, encoding="utf-8").read()
        links = re.findall(r"\]\(((?:chapters|appendices)/[^)]+\.md)\)", md)
        for l in set(links):
            if not os.path.isfile(os.path.join(ROOT, E["dir"], l)):
                fail(f"{E['dir']}/README.md: link does not resolve: {l}")
        for tr in seen:
            rel = os.path.relpath(tr, os.path.join(ROOT, E["dir"]))
            if rel not in links:
                fail(f"{E['dir']}/README.md: {rel} is not linked from the table of contents")
    else:
        fail(f"{E['dir']}/README.md is missing")
    # the figures of the edition exist for every English one (only for a complete edition)
    for svg in glob.glob(os.path.join(ROOT, "assets", "figures", "*.svg")):
        name = os.path.basename(svg)
        if complete and not os.path.isfile(os.path.join(ROOT, "assets", "figures", E["dir"], name)):
            fail(f"assets/figures/{E['dir']}/{name} is missing")
    done = len(seen)
    total = len(en_files)
    if missing:
        print(f"      {done}/{total} files translated; not yet translated: {len(missing)}")
    else:
        print(f"      {done}/{total} files translated")
    print(f"      {len(failures) - before} failure(s)")
    return done, total


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    complete = "--complete" in sys.argv[1:]
    codes = args or list(EDITIONS)
    for code in codes:
        if code not in EDITIONS:
            print(f"unknown edition {code!r}; known: {', '.join(EDITIONS)}")
            return 2
        check_edition(code, complete)
    print()
    if failures:
        print(f"{len(failures)} check(s) failed")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
