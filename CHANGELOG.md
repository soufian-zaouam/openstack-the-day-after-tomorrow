# Changelog

All published versions of *OpenStack, the Day After Tomorrow* are listed here, newest first.
Each version corresponds to a Git tag and a [GitHub Release](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases) carrying the PDF, which is generated from the Markdown sources by the [build workflow](tools/pdf/README.md).

Versioning scheme:

- **Major** (`v2.0`): substantial rewrite, new parts or chapters, change of structure.
- **Minor** (`v1.1`): revised or expanded sections, new figures, corrections that change the technical content.
- Simple typo fixes are batched into the next minor version rather than released on their own.

## [v1.3] — 2026-10-25

Technical correction to Chapter 20, in both editions.

- Chapter 20, technical note on host maintenance (both editions): instances with SR-IOV `direct` ports can be live-migrated with the libvirt driver since the Train release (Nova 20.0.0), at the cost of a brief loss of that interface in the guest; only `direct-physical` ports stay with PCI passthrough among the instances that cannot be live-migrated. Reference to the Nova Train release notes added.
- README (both editions): link to [OpenStack Operator Skills](https://github.com/soufian-zaouam/openstack-operator-skills), the book's operating method as Agent Skills for Claude, among the companion resources.

## [v1.2] — 2026-10-17

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

[v1.2]: https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/tag/v1.2
[v1.1]: https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/tag/v1.1
[v1.0]: https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/tag/v1.0
