# Changelog

All published versions of *OpenStack, the Day After Tomorrow* are listed here, newest first.
Each version corresponds to a Git tag and a [GitHub Release](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases) carrying the PDF, which is generated from the Markdown sources by the [build workflow](tools/pdf/README.md).

Versioning scheme:

- **Major** (`v2.0`): substantial rewrite, new parts or chapters, change of structure.
- **Minor** (`v1.1`): revised or expanded sections, new figures, corrections that change the technical content.
- Simple typo fixes are batched into the next minor version rather than released on their own.

## [v1.1] — 2026-09-30

First edition whose PDF is generated automatically from the Markdown sources, by GitHub Actions (pandoc + XeLaTeX). Same text as v1.0.

- The full text is published in this repository as Markdown, one file per chapter (`chapters/`, `appendices/`), with the five figures as SVG (`assets/figures/`). Readable directly on GitHub.
- The PDF is rebuilt and verified on every push (`tools/pdf/`, `.github/workflows/build-book.yml`); a version tag publishes it as a release.
- Copyright page corrected: the licence (CC BY-NC-ND 4.0), the version and the source repository are now stated; the "All rights reserved" notice of v1.0 is gone.
- Same page size, fonts and layout as v1.0 (17 × 24 cm, TeX Gyre Pagella / Heros); 114 pages instead of 116.
- README rewritten around the online table of contents; CONTRIBUTING updated accordingly.

## [v1.0] — 2026-09-13

First public edition.

- 20 chapters in six parts, plus appendices and references
- Five figures
- Format: PDF, English (Oxford spelling)

[v1.1]: https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/tag/v1.1
[v1.0]: https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/tag/v1.0
