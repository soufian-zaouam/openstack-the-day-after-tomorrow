# Building the PDF editions

The PDFs distributed on the [Releases](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases) page are generated from the Markdown sources of this repository by the GitHub Actions workflow [`build-book.yml`](../../.github/workflows/build-book.yml): the English edition from `chapters/`, `appendices/` and `assets/figures/`, the French edition from `fr/chapters/`, `fr/appendices/` and `assets/figures/fr/`, the Arabic edition from `ar/chapters/`, `ar/appendices/` and `assets/figures/ar/`. Nothing is edited by hand between the Markdown and the PDF.

## Toolchain

| Step | Tool |
| --- | --- |
| Markdown → LaTeX | [pandoc](https://pandoc.org) 3.x, with the custom template `template.tex`, the metadata in `metadata.yaml` (English), `metadata-fr.yaml` (French) or `metadata-ar.yaml` (Arabic), the layout in `header.tex` (plus `header-fr.tex` for the French caption separator, `header-ar.tex` for the Arabic fonts, direction and labels) and the Lua filter `filters/book.lua` |
| LaTeX → PDF | XeLaTeX (TeX Live), three passes, for the English and French editions; LuaLaTeX for the Arabic edition (babel's `bidi=basic` algorithm lays out the mixed Arabic/Latin text) |
| Figures | `rsvg-convert` (librsvg) turns the SVG figures into vector PDF |
| Fonts | TeX Gyre Pagella (text), TeX Gyre Heros (headings), DejaVu Sans Mono (code) — the fonts of the original edition; Liberation Sans for the text of the French figures; Amiri (text) and Noto Kufi Arabic (headings) for the Arabic edition, Noto Sans Arabic for its figures, with DejaVu Sans as a fallback for the glyphs Amiri lacks |
| Checks | `verify_pdf.py` (PyMuPDF), `../check_editions.py` (parity of the translated editions with the original) |

The Lua filter is what turns the GitHub-oriented Markdown into a book: it drops the navigation footers, turns the *Part* lines into part pages, numbers the chapters (from the number in the heading, so that an edition built from part of its chapters keeps the numbering of the book) and letters the appendices, turns the *Technical note* / *Principle* / *From the field* quotations into coloured boxes, and turns the figure images and their italic captions into numbered figures. It recognises the structural markers of the three languages (*Part / Partie / الجزء*, *Chapter / Chapitre / الفصل*, *Appendix / Annexe / الملحق*, *Technical note / Note technique / ملاحظة تقنية*, *Principle / Principe / مبدأ*, *From the field / Sur le terrain / من الميدان*), chosen from the `lang` metadata of the edition; for the French edition it also turns the narrow no-break spaces of the French punctuation into `\,`, because the heading font has no glyph for them; for the Arabic edition it removes the `<div dir="rtl">` wrappers that GitHub needs, since the whole document is right-to-left, and letters the appendices with the abjad sequence (أ ب ج د هـ و). The editions share the template, the layout and the page size; only the metadata, the fonts of the Arabic edition, the title page and the sources differ.

**The Arabic edition** is right-to-left. In the Markdown, each file is wrapped in `<div dir="rtl">` … `</div>`, which GitHub honours; nothing else is needed, the browser's bidirectional algorithm orders the Latin names, commands and numbers inside the Arabic text. In the PDF, LuaLaTeX with babel (`bidi=basic`) does the same; Latin letters switch to the fonts of the original edition. While the edition is being translated, `build.sh ar` builds the chapters that exist and lists the missing ones in `build/openstack-the-day-after-tomorrow-ar.missing`; `verify_pdf.py` then relaxes the checks that depend on completeness, and the workflow keeps the PDF as a preview artifact without releasing it. Once every file exists, set `PARTIAL_OK=0` in the `ar` case of `build.sh` so that a missing chapter fails the build again.

## Building locally

On Debian or Ubuntu:

```bash
sudo apt-get install pandoc texlive-xetex texlive-luatex texlive-latex-recommended texlive-latex-extra \
                     texlive-lang-french texlive-lang-arabic \
                     texlive-fonts-recommended fonts-texgyre lmodern fonts-dejavu-core fonts-liberation \
                     fonts-hosny-amiri fonts-noto-core librsvg2-bin poppler-utils
pip install pymupdf

bash tools/pdf/build.sh en v1.2   # English edition ("build.sh v1.2" and "build.sh" also work)
python3 tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow.pdf build/openstack-the-day-after-tomorrow.log

bash tools/pdf/build.sh fr v1.2   # French edition
python3 tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow-fr.pdf build/openstack-the-day-after-tomorrow-fr.log

bash tools/pdf/build.sh ar v1.2   # Arabic edition (the chapters translated so far)
python3 tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow-ar.pdf build/openstack-the-day-after-tomorrow-ar.log

python3 tools/check_editions.py   # the translated editions are in step with the original
```

Everything is written to `build/`, which is ignored by Git. The version given to `build.sh` is printed on the copyright page. `verify_pdf.py` recognises the edition from the file name (`-fr` or `-ar` suffix) or from `--edition=fr|ar`. Only `check_editions.py` is needed to check a translation; it has no dependency beyond Python 3.

## What the workflow does

- On every push to `main` and on pull requests: checks that the translated editions are in step with the English one (`tools/check_editions.py`) and that the translated figures match their label maps (`tools/figures/`), builds the three PDFs (the Arabic one from the chapters translated so far), runs the checks on each, renders a few preview pages, and keeps the PDFs and the logs as workflow artifacts (90 days).
- On a version tag (`git tag v1.2 && git push origin v1.2`): the same, then publishes a GitHub Release carrying the PDFs (`openstack-the-day-after-tomorrow-v1.2.pdf`, `openstack-the-day-after-tomorrow-fr-v1.2.pdf`, and `openstack-the-day-after-tomorrow-ar-v1.2.pdf` once the Arabic edition is complete), with release notes taken from the matching section of `CHANGELOG.md`.
- By hand (*Actions → Build the PDF edition → Run workflow*): builds, and creates the release when a tag name is given.

## Checks performed on every build

`verify_pdf.py` fails the build if the PDF is missing, empty, encrypted or has wrong metadata; if the page count leaves the expected range or the page size is not 17 × 24 cm; if the title page, licence notice, table of contents or PDF bookmarks are missing; if any chapter or appendix heading is missing or out of order, or its first paragraph cannot be found; if a page is blank; if a figure caption is not on a page that embeds a vector figure, or the captions are not the expected ones; if a table is missing; if the page numbers are not consecutive; or if the XeLaTeX log reports errors, missing glyphs, lines overflowing the margin by more than 10 pt, or an unstable table of contents. The expectations that depend on the language (title, source directories, contents heading, table samples) are in its `EDITIONS` table.

`check_editions.py` compares every English source file with its counterpart in each translated edition: same headings, paragraphs, list items, table rows, figures, boxed passages of each kind, inline code and URLs, chapter and appendix cross-references, navigation links that resolve, the typography of the language (French: narrow no-break spaces, guillemets, apostrophes; Arabic: Arabic punctuation, guillemets, no tatweel, Western digits, the `<div dir="rtl">` wrapper), and a table of contents that lists every file of the edition. The French edition must be complete; the Arabic edition may still lack files, which are reported as not yet translated (`--complete` makes them failures, for the release check).

## The translated figures

The figures of the original edition were exported with their text outlined, so they cannot be edited directly. `tools/figures/translate_figure.py` keeps the drawing of an English SVG and replaces each text line by a real `<text>` element taken from a label map in `tools/figures/fr/` or `tools/figures/ar/` (one JSON file per figure, with the line numbers that `tools/figures/debug_runs.py` prints). To change a label, edit the map and regenerate:

```bash
python3 tools/figures/translate_figure.py assets/figures/figure-4-1.svg tools/figures/fr/figure-4-1.json assets/figures/fr/figure-4-1.svg
python3 tools/figures/translate_figure.py assets/figures/figure-4-1.svg tools/figures/ar/figure-4-1.json assets/figures/ar/figure-4-1.svg
```

The Arabic maps set `"direction": "rtl"` (the text is shaped right-to-left) and `"mirror": true` (the drawing is flipped horizontally, so that a flow drawn left-to-right reads right-to-left); anchors keep their visual meaning. The workflow checks that the committed translated figures are exactly what the maps produce.

## Releasing a new version

1. Update `CHANGELOG.md` (new `## [vX.Y] — date` section) and `CITATION.cff` (`version`, `date-released`).
2. Commit and push to `main`; check that the build is green (both editions).
3. Tag and push: `git tag vX.Y && git push origin vX.Y`. The workflow creates the release with both PDFs.
