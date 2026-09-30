# Building the PDF edition

The PDF distributed on the [Releases](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases) page is generated from the Markdown sources of this repository (`chapters/`, `appendices/`, `assets/figures/`) by the GitHub Actions workflow [`build-book.yml`](../../.github/workflows/build-book.yml). Nothing is edited by hand between the Markdown and the PDF.

## Toolchain

| Step | Tool |
| --- | --- |
| Markdown → LaTeX | [pandoc](https://pandoc.org) 3.x, with the custom template `template.tex`, the metadata in `metadata.yaml`, the layout in `header.tex` and the Lua filter `filters/book.lua` |
| LaTeX → PDF | XeLaTeX (TeX Live), three passes |
| Figures | `rsvg-convert` (librsvg) turns the SVG figures into vector PDF |
| Fonts | TeX Gyre Pagella (text), TeX Gyre Heros (headings), DejaVu Sans Mono (code) — the fonts of the original edition |
| Checks | `verify_pdf.py` (PyMuPDF) |

The Lua filter is what turns the GitHub-oriented Markdown into a book: it drops the navigation footers, turns the *Part* lines into part pages, numbers the chapters and letters the appendices, turns the *Technical note* / *Principle* / *From the field* quotations into coloured boxes, and turns the figure images and their italic captions into numbered figures.

## Building locally

On Debian or Ubuntu:

```bash
sudo apt-get install pandoc texlive-xetex texlive-latex-recommended texlive-latex-extra \
                     texlive-fonts-recommended lmodern fonts-dejavu-core librsvg2-bin poppler-utils
pip install pymupdf

tools/pdf/build.sh v1.1        # or without argument for a development build
python3 tools/pdf/verify_pdf.py build/openstack-the-day-after-tomorrow.pdf build/openstack-the-day-after-tomorrow.log
```

Everything is written to `build/`, which is ignored by Git. The version given to `build.sh` is printed on the copyright page.

## What the workflow does

- On every push to `main` and on pull requests: builds the PDF, runs the checks, renders a few preview pages, and keeps the PDF and the logs as workflow artifacts (90 days).
- On a version tag (`git tag v1.2 && git push origin v1.2`): the same, then publishes a GitHub Release carrying the PDF, with release notes taken from the matching section of `CHANGELOG.md`.
- By hand (*Actions → Build the PDF edition → Run workflow*): builds, and creates the release when a tag name is given.

## Checks performed on every build

`verify_pdf.py` fails the build if the PDF is missing, empty, encrypted or has wrong metadata; if the page count leaves the expected range or the page size is not 17 × 24 cm; if the title page, licence notice, table of contents or PDF bookmarks are missing; if any chapter or appendix heading is missing or out of order, or its first paragraph cannot be found; if a page is blank; if a figure caption is not on a page that embeds a vector figure, or the captions are not the expected ones; if a table is missing; if the page numbers are not consecutive; or if the XeLaTeX log reports errors, missing glyphs, lines overflowing the margin by more than 10 pt, or an unstable table of contents.

## Releasing a new version

1. Update `CHANGELOG.md` (new `## [vX.Y] — date` section) and `CITATION.cff` (`version`, `date-released`).
2. Commit and push to `main`; check that the build is green.
3. Tag and push: `git tag vX.Y && git push origin vX.Y`. The workflow creates the release with the PDF.
