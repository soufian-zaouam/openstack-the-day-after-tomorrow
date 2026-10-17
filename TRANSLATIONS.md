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

The English edition is the reference; the French edition is complete and maintained by the author. **The Arabic edition exists as a complete first draft**: every file is translated and passes the structural checks, but each chapter still needs a full review by a second reader (linguistic and technical) before it is marked *translated*. Reviewing a draft chapter is the most useful contribution right now: claim it with a *Translate a chapter* issue ("Review a merged draft in depth"), read it against the English, and open a pull request with your corrections. Figures: the French and Arabic figures are complete (`assets/figures/fr/`, `assets/figures/ar/`).

## Chapters

| File (English) | Chapter | French | Arabic | Issue / PR |
| --- | --- | --- | --- | --- |
| `00-front-matter.md` | Front matter | translated | draft | |
| `00-how-to-read-this-book.md` | How to Read This Book | translated | draft | |
| `00-introduction.md` | Introduction | translated | draft | |
| `01-openstack-doesnt-end-at-deployment.md` | 1 — OpenStack Doesn't End at Deployment | translated | draft | |
| `02-the-enemy-is-loss-of-control.md` | 2 — The Enemy Is Loss of Control | translated | draft | |
| `03-why-good-platforms-become-difficult-to-operate.md` | 3 — Why Good Platforms Become Difficult to Operate | translated | draft | |
| `04-the-control-loop.md` | 4 — The Control Loop | translated | draft | |
| `05-assessing-platform-control.md` | 5 — Assessing Platform Control | translated | draft | |
| `06-measuring-control.md` | 6 — Measuring Control | translated | draft | |
| `07-when-control-is-already-lost.md` | 7 — When Control Is Already Lost | translated | draft | |
| `08-visibility-before-action.md` | 8 — Visibility Before Action | translated | draft | |
| `09-stability-and-change.md` | 9 — Stability and Change | translated | draft | |
| `10-recovery-is-a-feature.md` | 10 — Recovery Is a Feature | translated | draft | |
| `11-documentation-is-operational-memory.md` | 11 — Documentation Is Operational Memory | translated | draft | |
| `12-building-the-team-behind-the-platform.md` | 12 — Building the Team Behind the Platform | translated | draft | |
| `13-decision-rights.md` | 13 — Decision Rights | translated | draft | |
| `14-upgrades-backports-and-upstream-alignment.md` | 14 — Upgrades, Backports and Upstream Alignment | translated | draft | |
| `15-complexity-technical-debt-and-simplification.md` | 15 — Complexity, Technical Debt and Simplification | translated | draft | |
| `16-automation-and-operational-complexity.md` | 16 — Automation and Operational Complexity | translated | draft | |
| `17-security-is-platform-work.md` | 17 — Security Is Platform Work | translated | draft | |
| `18-evolving-a-mission-critical-platform.md` | 18 — Evolving a Mission-Critical Platform | translated | draft | |
| `19-when-the-safe-decision-is-to-stop.md` | 19 — When the Safe Decision Is to Stop | translated | draft | |
| `20-security-capacity-and-business-criticality.md` | 20 — Security, Capacity and Business Criticality | translated | draft | |
| `21-conclusion-keeping-openstack-under-control.md` | Conclusion: Keeping OpenStack Under Control | translated | draft | |

## Appendices

| File (English) | Appendix | French | Arabic | Issue / PR |
| --- | --- | --- | --- | --- |
| `appendix-a-the-control-decision-framework.md` | A — The Control Decision Framework | translated | draft | |
| `appendix-b-the-control-assessment-worksheet.md` | B — The Control Assessment Worksheet | translated | draft | |
| `appendix-c-a-minimum-change-decision-record.md` | C — A Minimum Change Decision Record | translated | draft | |
| `appendix-d-control-review-questions.md` | D — Control Review Questions | translated | draft | |
| `appendix-e-operating-principles-at-a-glance.md` | E — Operating Principles at a Glance | translated | draft | |
| `appendix-f-glossary.md` | F — Glossary | translated | draft | |
| `references-and-further-reading.md` | References and Further Reading | translated | draft | |

## Figures

The Arabic figures are generated from the English ones by `tools/figures/translate_figure.py` and a label map in `tools/figures/ar/` (see `ar/STYLE.md`).

| Figure | Chapter | French | Arabic |
| --- | --- | --- | --- |
| 1.1 | 1 | translated | translated |
| 4.1 | 4 | translated | translated |
| 5.1 | 5 | translated | translated |
| 14.1 | 14 | translated | translated |
| 20.1 | 20 | translated | translated |

## Other documents

| Document | English | French | Arabic |
| --- | --- | --- | --- |
| README (presentation and table of contents) | `README.md` | `fr/README.md` | `ar/README.md` |
| Contribution guide | `CONTRIBUTING.md` (reference) | `fr/CONTRIBUTING.md` (summary) | `ar/CONTRIBUTING.md` (summary) |
| Editorial guide and glossary | — | `fr/STYLE.md` | `ar/STYLE.md` |
