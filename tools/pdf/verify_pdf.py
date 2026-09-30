#!/usr/bin/env python3
"""Automatic checks on the generated PDF edition of the book.

    tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow.pdf [build/openstack-the-day-after-tomorrow.log]

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

try:
    import pymupdf
except ImportError:  # pragma: no cover
    import fitz as pymupdf  # older package name

MIN_PAGES, MAX_PAGES = 95, 140         # the v1.0 PDF had 116 pages
PAGE_W, PAGE_H = 481.9, 680.3          # 17 x 24 cm, in points
MIN_SIZE = 300_000                     # bytes
EXPECTED_FIGURES = ["1.1", "4.1", "5.1", "14.1", "20.1"]   # captions, numbered by chapter
TABLE_MARKERS = [
    "Keep temporarily with an exit condition",         # chapter 15
    "Weighted score",                                  # chapter 18
    "What can wait, and until when?",                  # appendix B
]

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
    return re.sub(r"\s+", " ", s)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    pdf_path = sys.argv[1]
    log_path = sys.argv[2] if len(sys.argv) > 2 else None
    root = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.abspath(os.path.join(root, "..", ".."))

    # 1. file
    if not os.path.isfile(pdf_path):
        fail(f"{pdf_path} does not exist")
        return finish()
    size = os.path.getsize(pdf_path)
    if size < MIN_SIZE:
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
    if doc.metadata.get("title") != "OpenStack, the Day After Tomorrow":
        fail(f"unexpected PDF title metadata: {doc.metadata.get('title')!r}")
    if doc.metadata.get("author") != "Soufian Zaouam":
        fail(f"unexpected PDF author metadata: {doc.metadata.get('author')!r}")

    # 2. pages
    n = doc.page_count
    if not MIN_PAGES <= n <= MAX_PAGES:
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

    # 3. front matter
    if "OpenStack, the Day After Tomorrow" not in pages[0] or "Soufian Zaouam" not in pages[0]:
        fail("title page does not carry the title and the author")
    else:
        ok("title page")
    if "Creative Commons" not in pages[1] or "4.0 International" not in pages[1]:
        fail("licence notice missing from the copyright page")
    else:
        ok("copyright page with licence")
    if not any(p.startswith("Contents") or " Contents " in p[:40] for p in pages[2:5]):
        fail("table of contents not found in pages 3-5")
    else:
        ok("table of contents")
    toc = doc.get_toc()
    if len(toc) < 30:
        fail(f"PDF bookmarks: only {len(toc)} entries")
    else:
        ok(f"{len(toc)} PDF bookmarks")

    # 4. + 5. chapters and their body text, in order
    sources = (sorted(glob.glob(os.path.join(repo, "chapters", "*.md")))
               + sorted(glob.glob(os.path.join(repo, "appendices", "appendix-*.md")))
               + [os.path.join(repo, "appendices", "references-and-further-reading.md")])
    last_pos = 0
    for src in sources:
        name = os.path.basename(src)
        if name == "00-front-matter.md":
            continue
        with open(src, encoding="utf-8") as f:
            md = f.read()
        m = re.search(r"^# (?:Chapter \d+ — |Appendix [A-F] — )?(.+)$", md, re.M)
        title = norm(m.group(1))
        # the first body paragraph (skip headings, part line, tables, quotes, images)
        body = None
        for para in md.split("\n\n"):
            t = para.strip()
            if not t or t.startswith(("#", "*", ">", "|", "!", "-", "1.", "---", "[")):
                continue
            body = norm(t)
            break
        pos = full.find(title, last_pos)
        if pos < 0:
            fail(f"{name}: heading {title!r} not found after position {last_pos}")
            continue
        last_pos = pos
        if body:
            sample = body[:60]
            if sample not in full:
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
    #    (a Form XObject with a few hundred drawing paths), captions numbered as expected
    caps = []
    for i, p in enumerate(doc):
        for num in re.findall(r"Figure (\d+\.\d+): ", pages[i]):
            caps.append(num)
            if not p.get_xobjects() or len(p.get_drawings()) < 50:
                fail(f"page {i+1}: caption of Figure {num} without an embedded figure")
    if caps != EXPECTED_FIGURES:
        fail(f"figure captions {caps} differ from the expected {EXPECTED_FIGURES}")
    else:
        ok(f"{len(caps)} figures embedded with numbered captions")

    # 8. tables
    for marker in TABLE_MARKERS:
        if marker not in full:
            fail(f"table content not found: {marker!r}")
    ok("tables present")

    # 9. page numbers: the last line of a main-matter page is its arabic number
    numbers = []
    for i, p in enumerate(doc):
        lines = [l.strip() for l in p.get_text().splitlines() if l.strip()]
        if lines and re.fullmatch(r"\d{1,3}", lines[-1]):
            numbers.append(int(lines[-1]))
    if len(numbers) < n * 0.7:
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
        if first.startswith("# ") and re.match(r"# (Chapter \d+|Appendix [A-F]) — ", first) and norm(first[2:]) in full:
            fail(f"raw Markdown heading left in the text: {first[2:]!r}")
    for i, p in enumerate(pages):
        if re.search(r"\]\([^)]*\.md\)", p) or "Contents ·" in p:
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
