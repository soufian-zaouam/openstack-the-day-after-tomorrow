#!/usr/bin/env python3
"""Automatic checks on the generated PDF edition of the book.

    tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow.pdf [build/openstack-the-day-after-tomorrow.log]
    tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow-fr.pdf [build/openstack-the-day-after-tomorrow-fr.log]
    tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow-ar.pdf [build/openstack-the-day-after-tomorrow-ar.log]

The edition (English, French or Arabic) is recognised from the PDF file name
(a "-fr" or "-ar" suffix) or given with --edition en|fr|ar; the expectations
that depend on the language (title, sources, contents heading, figure
captions, table samples) come from the EDITIONS table below.

An edition still being translated is built by build.sh from the chapters that
exist, which it lists in build/<name>.missing next to the PDF. When that file
is present the checks that depend on completeness are relaxed: the page count
has no minimum, only the figures and tables of the chapters present are
expected, and the number of bookmarks is scaled down.

The Arabic text comes out of the PDF in presentation forms, without reliable
spaces and with the neutral characters reordered, so the Arabic edition is
compared on a normalised key: letters and digits only, after compatibility
decomposition, without diacritics.

Exit code 0 when every check passes, 1 otherwise. The checks:

  1. the file exists, is not empty and is a valid, non-encrypted PDF
  2. the page count is within the expected range and the page size is the book's
  3. the front matter is there: title page, licence, table of contents
  4. every chapter and appendix of the Markdown sources appears as a heading
     in the PDF, in order
  5. a sample of body text from every chapter is present (not just the heading)
  6. no unexpected blank page
  7. the figures are embedded (text of every figure is found on a page that
     also carries a vector drawing) and their captions are numbered
  8. the tables are present
  9. the running page numbers are consistent (arabic numbers 1..N in order)
 10. obvious rendering errors: LaTeX error markers left in the text, missing
     characters or overfull boxes reported in the XeLaTeX log, unresolved
     references ("??")
"""
import glob
import os
import re
import sys
import unicodedata

try:
    import pymupdf
except ImportError:  # pragma: no cover
    import fitz as pymupdf  # older package name

MIN_PAGES, MAX_PAGES = 95, 150         # the v1.0 PDF had 116 pages; French runs ~10 % longer
PAGE_W, PAGE_H = 481.9, 680.3          # 17 x 24 cm, in points
MIN_SIZE = 300_000                     # bytes
EXPECTED_FIGURES = ["1.1", "4.1", "5.1", "14.1", "20.1"]   # captions, numbered by chapter

EDITIONS = {
    # caption_re is matched on the normalised page text (see key()); the table
    # markers name the source file they come from, for editions in progress
    "en": {
        "title": "OpenStack, the Day After Tomorrow",
        "chapters": "chapters", "appendices": "appendices",
        "front_matter": "00-front-matter.md",
        "appendix_glob": "appendix-*.md", "references": "references-and-further-reading.md",
        "heading_re": r"^# (?:Chapter \d+ — |Appendix [A-F] — )?(.+)$",
        "numbered_re": r"# (Chapter \d+|Appendix [A-F]) — ",
        "contents": "Contents", "nav_contents": "Contents ·",
        "caption_re": r"Figure (\d+\.\d+)\s?: ",
        "table_markers": [
            ("15-", "Keep temporarily with an exit condition"),
            ("18-", "Weighted score"),
            ("appendix-b-", "What can wait, and until when?"),
        ],
    },
    "fr": {
        "title": "OpenStack, après-demain",
        "chapters": "fr/chapters", "appendices": "fr/appendices",
        "front_matter": "00-pages-liminaires.md",
        "appendix_glob": "annexe-*.md", "references": "references-et-lectures-complementaires.md",
        "heading_re": r"^# (?:Chapitre \d+ — |Annexe [A-F] — )?(.+)$",
        "numbered_re": r"# (Chapitre \d+|Annexe [A-F]) — ",
        "contents": "Table des matières", "nav_contents": "Sommaire ·",
        "caption_re": r"Figure (\d+\.\d+)\s?: ",
        "table_markers": [
            ("15-", "Conserver temporairement avec une condition de sortie"),
            ("18-", "Score pondéré"),
            ("annexe-b-", "Qu'est-ce qui peut attendre, et jusqu'à quand ?"),
        ],
    },
    "ar": {
        "title": "OpenStack، بعد غد",
        "chapters": "ar/chapters", "appendices": "ar/appendices",
        "front_matter": "00-front-matter.md",
        "appendix_glob": "appendix-*.md", "references": "references-and-further-reading.md",
        "heading_re": r"^# (?:الفصل \d+ — |الملحق \S+ — )?(.+)$",
        "numbered_re": r"# (الفصل \d+|الملحق \S+) — ",
        "contents": "المحتويات", "nav_contents": "المحتويات ·",
        "caption_re": r"الشكل(\d+\.\d+):",
        "table_markers": [
            ("15-", "الاحتفاظ مؤقّتًا بشرط خروج"),
            ("18-", "الدرجة المرجّحة"),
            ("appendix-b-", "ما الذي يمكنه الانتظار، وإلى متى؟"),
        ],
        "rtl": True,
    },
}

failures = []
warnings = []


def fail(msg):
    failures.append(msg)
    print(f"FAIL  {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"WARN  {msg}")


def ok(msg):
    print(f"ok    {msg}")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("ﬀ", "ff").replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬃ", "ffi")
    s = s.replace("\u00a0", " ").replace("\u202f", " ")
    return re.sub(r"\s+", " ", s)


ARABIC_MARKS = re.compile(r"[\u064b-\u0652\u0670\u0640]")   # tashkīl, superscript alef, tatweel


def key(s, rtl=False):
    """The comparison form of a text: norm() for the Latin editions; for the
    right-to-left edition, letters and digits only (compatibility-decomposed,
    presentation forms folded back, diacritics dropped), since the extracted
    Arabic text keeps neither its spaces nor the order of its punctuation."""
    if not rtl:
        return norm(s)
    s = unicodedata.normalize("NFKC", s)
    s = ARABIC_MARKS.sub("", s)
    return "".join(c for c in s if c.isalnum() or c == ".")


def caption_key(s, rtl=False):
    """Like key(), but keeps the punctuation: the caption regex of the Arabic
    edition needs the colon that follows the figure number."""
    if not rtl:
        return s
    s = ARABIC_MARKS.sub("", unicodedata.normalize("NFKC", s))
    return re.sub(r"\s+", "", s)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--edition")]
    opts = [a for a in sys.argv[1:] if a.startswith("--edition")]
    if len(args) < 1:
        print(__doc__)
        return 2
    pdf_path = args[0]
    log_path = args[1] if len(args) > 1 else None
    edition = opts[0].split("=", 1)[1] if opts and "=" in opts[0] else ("fr" if pdf_path.endswith("-fr.pdf") else "ar" if pdf_path.endswith("-ar.pdf") else "en")
    E = EDITIONS[edition]
    rtl = E.get("rtl", False)
    print(f"edition: {edition}")
    root = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.abspath(os.path.join(root, "..", ".."))
    missing_path = re.sub(r"\.pdf$", ".missing", pdf_path)
    partial = os.path.isfile(missing_path) and os.path.getsize(missing_path) > 0
    if partial:
        with open(missing_path, encoding="utf-8") as f:
            not_translated = [l.strip() for l in f if l.strip()]
        warn(f"edition in progress: {len(not_translated)} source(s) not yet translated; completeness checks relaxed")

    # 1. file
    if not os.path.isfile(pdf_path):
        fail(f"{pdf_path} does not exist")
        return finish()
    size = os.path.getsize(pdf_path)
    if size < MIN_SIZE and not partial:
        fail(f"PDF is suspiciously small ({size} bytes)")
    else:
        ok(f"PDF exists ({size // 1024} KiB)")
    try:
        doc = pymupdf.open(pdf_path)
    except Exception as e:  # noqa: BLE001
        fail(f"PDF cannot be opened: {e}")
        return finish()
    if doc.is_encrypted:
        fail("PDF is encrypted")
    if doc.metadata.get("title") != E["title"]:
        fail(f"unexpected PDF title metadata: {doc.metadata.get('title')!r}")
    if doc.metadata.get("author") != "Soufian Zaouam":
        fail(f"unexpected PDF author metadata: {doc.metadata.get('author')!r}")

    # 2. pages
    n = doc.page_count
    if partial:
        if n > MAX_PAGES:
            fail(f"page count {n} above the expected maximum {MAX_PAGES}")
        else:
            ok(f"{n} pages (edition in progress)")
    elif not MIN_PAGES <= n <= MAX_PAGES:
        fail(f"page count {n} outside the expected range {MIN_PAGES}-{MAX_PAGES}")
    else:
        ok(f"{n} pages")
    r = doc[0].rect
    if abs(r.width - PAGE_W) > 2 or abs(r.height - PAGE_H) > 2:
        fail(f"page size {r.width:.1f}x{r.height:.1f} pt is not 17x24 cm")
    else:
        ok("page size 17 x 24 cm")

    pages = [norm(p.get_text()) for p in doc]
    full = " ".join(pages)
    keys = [key(p, rtl) for p in pages]          # comparison form of every page
    fullkey = " ".join(keys)

    # 3. front matter
    if key(E["title"], rtl) not in keys[0] or "Soufian Zaouam" not in pages[0]:
        fail("title page does not carry the title and the author")
    else:
        ok("title page")
    if ("Creative Commons" not in pages[1] and "BY-NC-ND" not in pages[1]) or "4.0" not in pages[1]:
        fail("licence notice missing from the copyright page")
    else:
        ok("copyright page with licence")
    contents = key(E["contents"], rtl)
    if not any(k.startswith(contents) or f" {contents} " in k[:60] or (rtl and contents in k[:60]) for k in keys[2:5]):
        fail("table of contents not found in pages 3-5")
    else:
        ok("table of contents")
    toc = doc.get_toc()
    sources = (sorted(glob.glob(os.path.join(repo, E["chapters"], "*.md")))
               + sorted(glob.glob(os.path.join(repo, E["appendices"], E["appendix_glob"])))
               + [os.path.join(repo, E["appendices"], E["references"])])
    sources = [s for s in sources if os.path.isfile(s)]
    min_toc = 30 if not partial else max(1, len(sources) - 1)   # about one bookmark per file, at least
    if len(toc) < min_toc:
        fail(f"PDF bookmarks: only {len(toc)} entries")
    else:
        ok(f"{len(toc)} PDF bookmarks")

    # 4. + 5. chapters and their body text, in order
    last_pos = 0
    for src in sources:
        name = os.path.basename(src)
        if name == E["front_matter"]:
            continue
        with open(src, encoding="utf-8") as f:
            md = f.read()
        m = re.search(E["heading_re"], md, re.M)
        title = key(m.group(1), rtl)
        # the first body paragraph (skip headings, part line, tables, quotes, images, div wrappers)
        body = None
        for para in md.split("\n\n"):
            t = para.strip()
            if not t or t.startswith(("#", "*", ">", "|", "!", "-", "1.", "---", "[", "<")):
                continue
            body = key(t, rtl)
            break
        pos = fullkey.find(title, last_pos)
        if pos < 0:
            fail(f"{name}: heading {title!r} not found after position {last_pos}")
            continue
        last_pos = pos
        if body:
            sample = body[:60]
            if sample not in fullkey:
                fail(f"{name}: body text sample not found: {sample!r}")
    ok("every chapter and appendix heading found in order, with body text")

    # 6. blank pages
    blank = []
    for i, p in enumerate(doc):
        if not pages[i].strip() and not p.get_drawings() and not p.get_images():
            blank.append(i + 1)
    if blank:
        fail(f"blank pages: {blank}")
    else:
        ok("no blank page")

    # 7. figures: every caption sits on a page that embeds a vector figure
    #    (a Form XObject carrying the boxes and arrows of the drawing: a few
    #    hundred paths when the text is outlined, as in the English figures,
    #    a few dozen when it is real text, as in the French ones), captions
    #    numbered as expected
    caps = []
    for i, p in enumerate(doc):
        for num in re.findall(E["caption_re"], caption_key(pages[i], rtl)):
            caps.append(num)
            if not p.get_xobjects() or len(p.get_drawings()) < 8:
                fail(f"page {i+1}: caption of Figure {num} without an embedded figure")
    expected = EXPECTED_FIGURES
    if partial:   # only the figures of the chapters present
        present = {os.path.basename(s)[:3] for s in sources}
        expected = [f for f in EXPECTED_FIGURES if f"{int(f.split('.')[0]):02d}-" in present]
    if caps != expected:
        fail(f"figure captions {caps} differ from the expected {expected}")
    else:
        ok(f"{len(caps)} figures embedded with numbered captions")

    # 8. tables
    for prefix, marker in E["table_markers"]:
        if partial and not any(os.path.basename(s).startswith(prefix) for s in sources):
            continue
        if key(marker, rtl) not in fullkey:
            fail(f"table content not found: {marker!r}")
    ok("tables present")

    # 9. page numbers: the last line of a main-matter page is its arabic number
    numbers = []
    for i, p in enumerate(doc):
        lines = [l.strip() for l in p.get_text().splitlines() if l.strip()]
        if lines and re.fullmatch(r"\d{1,3}", lines[-1]):
            numbers.append(int(lines[-1]))
    if len(numbers) < n * (0.4 if partial else 0.7):
        fail(f"page numbers found on only {len(numbers)} of {n} pages")
    else:
        gaps = [(a, b) for a, b in zip(numbers, numbers[1:]) if b != a + 1]
        if gaps:
            fail(f"page numbering is not consecutive at {gaps[:5]}")
        else:
            ok(f"page numbers 1..{numbers[-1]} consecutive")

    # 10. rendering errors
    for marker in ("??", "\\begin{", "\\end{", "\\textbf", "\\emph", "[FAIL", "<<<"):
        if marker in full:
            fail(f"suspicious text in the PDF: {marker!r}")
    for src in sources:
        with open(src, encoding="utf-8") as f:
            first = f.readline().strip()
        if first.startswith("# ") and re.match(E["numbered_re"], first) and norm(first[2:]) in full:
            fail(f"raw Markdown heading left in the text: {first[2:]!r}")
    for i, p in enumerate(pages):
        if re.search(r"\]\([^)]*\.md\)", p) or E["nav_contents"] in p or (rtl and ".md" in keys[i] + p and "](" in p):
            fail(f"page {i+1}: Markdown navigation link left in the text")
    if log_path and os.path.isfile(log_path):
        with open(log_path, encoding="utf-8", errors="replace") as f:
            log = f.read()
        missing = len(re.findall(r"^Missing character", log, re.M))
        if missing:
            fail(f"XeLaTeX log: {missing} 'Missing character' warning(s) — a glyph is absent from the fonts")
        errors = re.findall(r"^!.*$|^\./.*:\d+: .*Error.*$", log, re.M)
        if errors:
            fail(f"XeLaTeX log: {len(errors)} error(s), first: {errors[0].strip()}")
        over = [float(x) for x in re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)", log)]
        bad = [x for x in over if x > 10]
        if bad:
            fail(f"XeLaTeX log: {len(bad)} line(s) overflow the margin by more than 10pt (max {max(bad):.1f}pt)")
        elif over:
            warn(f"XeLaTeX log: {len(over)} slightly overfull line(s) (max {max(over):.1f}pt)")
        if "Rerun to get" in log or "Label(s) may have changed" in log:
            fail("XeLaTeX log says another pass is needed (table of contents or references not stable)")
        ok("XeLaTeX log clean")
    else:
        warn("no XeLaTeX log given; log checks skipped")

    return finish()


def finish():
    print()
    if failures:
        print(f"{len(failures)} check(s) failed, {len(warnings)} warning(s)")
        return 1
    print(f"all checks passed, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
