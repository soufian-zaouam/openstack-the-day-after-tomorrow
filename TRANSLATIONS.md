# Translations: state of the editions

This page shows, for every file of the book, whether it exists in each edition and in what state. It is updated by the pull requests that merge or change a chapter. Live claims (who is translating what right now) are the [open issues labelled *translation*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues?q=is%3Aissue+is%3Aopen+label%3Atranslation); open translations under review are the [open pull requests labelled *translation*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/pulls?q=is%3Apr+is%3Aopen+label%3Atranslation).

How to contribute to a translation: [CONTRIBUTING.md](CONTRIBUTING.md). Arabic guide and glossary: [`ar/STYLE.md`](ar/STYLE.md). French guide: [`fr/STYLE.md`](fr/STYLE.md).

**States**

| State | Meaning |
| --- | --- |
| not started | nobody has claimed the file; open a *Translate a chapter* issue to take it |
| in review | a pull request exists and is being reviewed; comments welcome |
| translated | merged; the file is in the repository and in the PDF of the edition |
| draft | merged as a first draft that still needs a full review by a second reader (see the pull request or issue in the last column) |
| needs update | the English text changed after the translation; the file must be revised |

The English edition is the reference; the French edition is complete and maintained by the author. Figures: the French figures are complete (`assets/figures/fr/`); the Arabic figures are listed at the end.

## Chapters

| File (English) | Chapter | French | Arabic | Issue / PR |
| --- | --- | --- | --- | --- |
| `00-front-matter.md` | Front matter | translated | draft | |
| `00-how-to-read-this-book.md` | How to Read This Book | translated | not started | |
| `00-introduction.md` | Introduction | translated | not started | |
| `01-openstack-doesnt-end-at-deployment.md` | 1 — OpenStack Doesn't End at Deployment | translated | not started | |
| `02-the-enemy-is-loss-of-control.md` | 2 — The Enemy Is Loss of Control | translated | not started | |
| `03-why-good-platforms-become-difficult-to-operate.md` | 3 — Why Good Platforms Become Difficult to Operate | translated | not started | |
| `04-the-control-loop.md` | 4 — The Control Loop | translated | draft | |
| `05-assessing-platform-control.md` | 5 — Assessing Platform Control | translated | not started | |
| `06-measuring-control.md` | 6 — Measuring Control | translated | not started | |
| `07-when-control-is-already-lost.md` | 7 — When Control Is Already Lost | translated | not started | |
| `08-visibility-before-action.md` | 8 — Visibility Before Action | translated | not started | |
| `09-stability-and-change.md` | 9 — Stability and Change | translated | not started | |
| `10-recovery-is-a-feature.md` | 10 — Recovery Is a Feature | translated | not started | |
| `11-documentation-is-operational-memory.md` | 11 — Documentation Is Operational Memory | translated | not started | |
| `12-building-the-team-behind-the-platform.md` | 12 — Building the Team Behind the Platform | translated | not started | |
| `13-decision-rights.md` | 13 — Decision Rights | translated | not started | |
| `14-upgrades-backports-and-upstream-alignment.md` | 14 — Upgrades, Backports and Upstream Alignment | translated | not started | |
| `15-complexity-technical-debt-and-simplification.md` | 15 — Complexity, Technical Debt and Simplification | translated | not started | |
| `16-automation-and-operational-complexity.md` | 16 — Automation and Operational Complexity | translated | not started | |
| `17-security-is-platform-work.md` | 17 — Security Is Platform Work | translated | not started | |
| `18-evolving-a-mission-critical-platform.md` | 18 — Evolving a Mission-Critical Platform | translated | not started | |
| `19-when-the-safe-decision-is-to-stop.md` | 19 — When the Safe Decision Is to Stop | translated | not started | |
| `20-security-capacity-and-business-criticality.md` | 20 — Security, Capacity and Business Criticality | translated | not started | |
| `21-conclusion-keeping-openstack-under-control.md` | Conclusion: Keeping OpenStack Under Control | translated | not started | |

## Appendices

| File (English) | Appendix | French | Arabic | Issue / PR |
| --- | --- | --- | --- | --- |
| `appendix-a-the-control-decision-framework.md` | A — The Control Decision Framework | translated | not started | |
| `appendix-b-the-control-assessment-worksheet.md` | B — The Control Assessment Worksheet | translated | not started | |
| `appendix-c-a-minimum-change-decision-record.md` | C — A Minimum Change Decision Record | translated | not started | |
| `appendix-d-control-review-questions.md` | D — Control Review Questions | translated | not started | |
| `appendix-e-operating-principles-at-a-glance.md` | E — Operating Principles at a Glance | translated | not started | |
| `appendix-f-glossary.md` | F — Glossary | translated | not started | |
| `references-and-further-reading.md` | References and Further Reading | translated | not started | |

## Figures

The Arabic figures are generated from the English ones by `tools/figures/translate_figure.py` and a label map in `tools/figures/ar/` (see `ar/STYLE.md`).

| Figure | Chapter | French | Arabic |
| --- | --- | --- | --- |
| 1.1 | 1 | translated | not started |
| 4.1 | 4 | translated | translated |
| 5.1 | 5 | translated | not started |
| 14.1 | 14 | translated | not started |
| 20.1 | 20 | translated | not started |

## Other documents

| Document | English | French | Arabic |
| --- | --- | --- | --- |
| README (presentation and table of contents) | `README.md` | `fr/README.md` | `ar/README.md` |
| Contribution guide | `CONTRIBUTING.md` (reference) | `fr/CONTRIBUTING.md` (summary) | `ar/CONTRIBUTING.md` (summary) |
| Editorial guide and glossary | — | `fr/STYLE.md` | `ar/STYLE.md` |
