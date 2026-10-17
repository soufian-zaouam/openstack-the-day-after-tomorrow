# Changelog

All published versions of *OpenStack, the Day After Tomorrow* are listed here, newest first.
Each version corresponds to a Git tag and a [GitHub Release](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases) carrying the PDF, which is generated from the Markdown sources by the [build workflow](tools/pdf/README.md).

Versioning scheme:

- **Major** (`v2.0`): substantial rewrite, new parts or chapters, change of structure.
- **Minor** (`v1.1`): revised or expanded sections, new figures, corrections that change the technical content.
- Simple typo fixes are batched into the next minor version rather than released on their own.

## [Unreleased]

The repository becomes an open editorial project: the book can be translated, reviewed and corrected by the OpenStack community, starting with an Arabic edition.

- Arabic edition, *OpenStack، بعد غد*, started under `ar/` with the same layout as the French one: `ar/STYLE.md` (method, structural markers, right-to-left conventions and the terminology glossary), `ar/README.md`, `ar/CONTRIBUTING.md`, and a complete first draft of every chapter and appendix, one Markdown file per chapter with the English file names, to be reviewed chapter by chapter by the community before the edition is considered final. Each file is wrapped in `<div dir="rtl">` so that GitHub displays it right-to-left. The state of every chapter is in `TRANSLATIONS.md`.
- The Arabic PDF, `openstack-the-day-after-tomorrow-ar.pdf`, built by the same toolchain with LuaLaTeX (babel `bidi=basic`, Amiri and Noto Kufi Arabic), verified by the same checks; while the edition is in progress the workflow builds a preview from the chapters that exist and releases the PDF only once the edition is complete. The Arabic figures are generated from the English ones, mirrored so that the flows read right-to-left.
- Community process: `CONTRIBUTING.md` rewritten (what the licence allows, how to translate, review and correct a chapter with or without Git, editorial rules, terminology decisions, who decides), summarised in French (`fr/CONTRIBUTING.md`) and Arabic (`ar/CONTRIBUTING.md`); `TRANSLATIONS.md` tracks the chapters; `CONTRIBUTORS.md` credits the translators and reviewers; issue templates to claim a chapter, report a translation problem and discuss a term; a pull request template; the *Errata* template asks for the edition.
- Tooling: `tools/check_editions.py` checks every translated edition (strictly for French, progressively for Arabic), `tools/pdf/build.sh` and `verify_pdf.py` know the Arabic edition and editions in progress, the Lua filter recognises the Arabic markers and numbers chapters from their headings, `tools/figures/translate_figure.py` writes right-to-left and mirrored figures.

French edition of the book, *OpenStack, après-demain : exploiter des plateformes OpenStack critiques*, maintained in this repository alongside the original. Same text, same structure, same version number.

- The full French text under `fr/` (`fr/chapters/`, `fr/appendices/`), one Markdown file per chapter, with the same chapter numbers and appendix letters as the English files, a French table of contents (`fr/README.md`) and an editorial guide fixing the method and the terminology (`fr/STYLE.md`).
- The five figures redrawn with French labels (`assets/figures/fr/`), generated from the English SVG files by `tools/figures/`, which keeps the drawing and replaces the text.
- The French PDF, `openstack-the-day-after-tomorrow-fr.pdf`, built by the same toolchain (`tools/pdf/build.sh fr`), verified by the same checks, and published with every release alongside the English PDF. Same page size, fonts and layout.
- `tools/check_editions.py` verifies that the two editions stay in step (files, headings, boxed passages, figures, tables, code, links, cross-references, French typography); the workflow runs it before building.
- English text: the URL of the Galera *Monitoring the Cluster* reference is corrected (it contained stray spaces).

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

[Unreleased]: https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/compare/v1.1...HEAD
[v1.1]: https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/tag/v1.1
[v1.0]: https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/tag/v1.0
