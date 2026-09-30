# OpenStack, the Day After Tomorrow

### Operating Mission-Critical OpenStack Platforms

**Author: Soufian Zaouam**

[![Download the PDF](https://img.shields.io/badge/Download-PDF%20(latest%20release)-2ea44f?style=for-the-badge)](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/latest)
[![Version](https://img.shields.io/github/v/release/soufian-zaouam/openstack-the-day-after-tomorrow?label=version&style=for-the-badge)](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey?style=for-the-badge)](LICENSE)

This is the author's official repository for the book *OpenStack, the Day After Tomorrow*. It is the reference place to download the current edition, follow new versions, and report errors.

The book is published freely, as a **PDF** (see [Download](#download)) and as **Markdown, one file per chapter, readable directly on GitHub** (see [Read the book on GitHub](#read-the-book-on-github)). It is an **independent, personal contribution to the OpenStack community**. It is not a publication of the OpenStack Foundation (OpenInfra Foundation), of a publisher, or of any employer or client, and it does not describe any specific organisation's platform.

---

## About the book

Most OpenStack material stops where the real work begins: the platform is deployed, the services answer, the first tenants are onboarded. This book is about what comes next — the years during which a platform has to stay stable, observable, upgradable, secure and, above all, understandable by the people who operate it.

Its central thesis is that operating OpenStack in production is not only a technical problem. It is also a problem of visibility, stability, organisation, governance and risk management. A platform can be perfectly functional and still be hard to operate, hard to evolve, hard to secure, and hard to hand over.

It is one operator's experience and point of view, not a standard or a reference manual. Where the right answer depends on the deployment or the backend, the text says so.

The book draws on more than five years of running OpenStack platforms in production (Day-2 operations, reliability, upgrades, incident handling, team building). Real experience has been generalised into patterns and principles; no client, employer, project or environment is described or identifiable.

**What you will find inside** (20 chapters in six parts, plus appendices)

- *Understanding the problem* — why OpenStack doesn't end at deployment, why the real enemy is loss of control, and the control loop that runs through the whole book
- *Assessing control* — how to assess and measure how much control an organisation actually has over its platform, and what to do when it is already lost
- *Operating with control* — visibility before action, stability and change, and recovery as a feature rather than an afterthought
- *The organisation behind the platform* — documentation as operational memory, building the team, decision rights
- *Evolving without losing control* — upgrades, backports and upstream alignment; complexity, technical debt and simplification; automation; security as platform work
- *Decisions from the field* — two worked decisions where technical evidence, business impact and operational constraints collided
- Appendices: a control decision framework, a control assessment worksheet, a minimum change decision record, control review questions, operating principles at a glance, and a glossary

Throughout, *Technical note*, *Principle* and *From the field* boxes separate documented OpenStack behaviour, the author's operating principles, and situations drawn from real operations.

## Read the book on GitHub

The full text of the book is published in this repository as Markdown, **one file per chapter**, so that it can be read directly on GitHub, searched, linked to and quoted by section. The text is that of the PDF, which is generated from these very files; the five figures are provided as SVG in [`assets/figures/`](assets/figures/).

Start with [How to Read This Book](chapters/00-how-to-read-this-book.md), then follow the *Previous / Contents / Next* links at the bottom of every chapter. The PDF remains available for offline reading (see [Download](#download)).

| | Chapter |
| --- | --- |
| | [Front matter](chapters/00-front-matter.md) |
| | [How to Read This Book](chapters/00-how-to-read-this-book.md) |
| | [Introduction](chapters/00-introduction.md) |
| **Part I — Understanding the Problem** | |
| 1 | [OpenStack Doesn't End at Deployment](chapters/01-openstack-doesnt-end-at-deployment.md) |
| 2 | [The Enemy Is Loss of Control](chapters/02-the-enemy-is-loss-of-control.md) |
| 3 | [Why Good Platforms Become Difficult to Operate](chapters/03-why-good-platforms-become-difficult-to-operate.md) |
| 4 | [The Control Loop](chapters/04-the-control-loop.md) |
| **Part II — Assessing Control** | |
| 5 | [Assessing Platform Control](chapters/05-assessing-platform-control.md) |
| 6 | [Measuring Control](chapters/06-measuring-control.md) |
| 7 | [When Control Is Already Lost](chapters/07-when-control-is-already-lost.md) |
| **Part III — Operating with Control** | |
| 8 | [Visibility Before Action](chapters/08-visibility-before-action.md) |
| 9 | [Stability and Change](chapters/09-stability-and-change.md) |
| 10 | [Recovery Is a Feature](chapters/10-recovery-is-a-feature.md) |
| **Part IV — The Organization Behind the Platform** | |
| 11 | [Documentation Is Operational Memory](chapters/11-documentation-is-operational-memory.md) |
| 12 | [Building the Team Behind the Platform](chapters/12-building-the-team-behind-the-platform.md) |
| 13 | [Decision Rights](chapters/13-decision-rights.md) |
| **Part V — Evolving Without Losing Control** | |
| 14 | [Upgrades, Backports and Upstream Alignment](chapters/14-upgrades-backports-and-upstream-alignment.md) |
| 15 | [Complexity, Technical Debt and Simplification](chapters/15-complexity-technical-debt-and-simplification.md) |
| 16 | [Automation and Operational Complexity](chapters/16-automation-and-operational-complexity.md) |
| 17 | [Security Is Platform Work](chapters/17-security-is-platform-work.md) |
| 18 | [Evolving a Mission-Critical Platform](chapters/18-evolving-a-mission-critical-platform.md) |
| **Part VI — Decisions from the Field** | |
| 19 | [When the Safe Decision Is to Stop](chapters/19-when-the-safe-decision-is-to-stop.md) |
| 20 | [Security, Capacity and Business Criticality](chapters/20-security-capacity-and-business-criticality.md) |
| | [Conclusion: Keeping OpenStack Under Control](chapters/21-conclusion-keeping-openstack-under-control.md) |
| **Appendices** | |
| A | [The Control Decision Framework](appendices/appendix-a-the-control-decision-framework.md) |
| B | [The Control Assessment Worksheet](appendices/appendix-b-the-control-assessment-worksheet.md) |
| C | [A Minimum Change Decision Record](appendices/appendix-c-a-minimum-change-decision-record.md) |
| D | [Control Review Questions](appendices/appendix-d-control-review-questions.md) |
| E | [Operating Principles at a Glance](appendices/appendix-e-operating-principles-at-a-glance.md) |
| F | [Glossary](appendices/appendix-f-glossary.md) |
| | [References and Further Reading](appendices/references-and-further-reading.md) |

**Short path for managers and sponsors** (as suggested in *How to Read This Book*): the [Introduction](chapters/00-introduction.md), Chapters [1](chapters/01-openstack-doesnt-end-at-deployment.md) to [3](chapters/03-why-good-platforms-become-difficult-to-operate.md), Chapter [7](chapters/07-when-control-is-already-lost.md), the last section of Chapter [12](chapters/12-building-the-team-behind-the-platform.md), Chapters [13](chapters/13-decision-rights.md) and [14](chapters/14-upgrades-backports-and-upstream-alignment.md) up to the first technical note, Chapters [19](chapters/19-when-the-safe-decision-is-to-stop.md) and [20](chapters/20-security-capacity-and-business-criticality.md), the [Conclusion](chapters/21-conclusion-keeping-openstack-under-control.md), and Appendices [D](appendices/appendix-d-control-review-questions.md) and [E](appendices/appendix-e-operating-principles-at-a-glance.md).

### Repository layout

```text
openstack-the-day-after-tomorrow/
├── README.md              this page: presentation and table of contents
├── chapters/              front matter, introduction, chapters 1–20 and the conclusion (one Markdown file each)
├── appendices/            appendices A–F and the references
├── assets/figures/        the book's figures (SVG)
├── tools/pdf/             how the PDF is generated from the Markdown (pandoc + XeLaTeX)
├── .github/workflows/     build-book.yml: builds, verifies and releases the PDF
├── CHANGELOG.md           published versions
├── CONTRIBUTING.md        how to report errata and suggestions
├── CITATION.cff           machine-readable citation
└── LICENSE                CC BY-NC-ND 4.0
```

Throughout the text, three kinds of boxed passage from the PDF are rendered as quotations: **Technical note** (verifiable OpenStack facts, with a reference), **Principle** (an operating rule the book recommends) and **From the field** (an operational situation and the decision it required).

## Companion resources

<a href="https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow-guide"><img src="https://raw.githubusercontent.com/soufian-zaouam/openstack-the-day-after-tomorrow-guide/main/images/01-cover.png" width="480" alt="OpenStack, the Day After Tomorrow — Short Guide"></a>

- **[Short Guide](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow-guide)** — the book's ideas in 18 illustrated pages, one idea and one figure per page. The quickest way in, and a shared reference for teams and sponsors.
- **[OpenStack Production Guide](https://github.com/soufian-zaouam/openstack-production-guide)** — the practical companion: troubleshooting by symptom, by command and by error message, the *One Command, One Investigation* series (20 episodes), and six anonymised incident cases in RCA format. Several *From the field* passages of the book are developed there with their technical file.

## Who it is for

- Engineers and platform teams who operate, or are about to inherit, an OpenStack platform
- Architects and platform leads responsible for the reliability and evolution of a private cloud
- CTOs, CIOs and programme leaders who need to understand what "running OpenStack" really commits them to

It assumes a working knowledge of OpenStack. It is not an installation guide and does not replace the official documentation.

## Why this book exists

Deployment is the beginning of the operational journey, not the end. The hard-won lessons of Day-2 operations are rarely written down, and when they are, they are scattered across incident reports, tribal knowledge and conference talks. This book is an attempt to consolidate them into a coherent, opinionated, practical text — and to give it back to the community that made the platform possible.

**Why it is published openly.** OpenStack is open source, and most of what I know about operating it I learned from documentation, code and discussions that other people chose to share. Publishing this book freely is the most direct way I have to give something back, and to have its content discussed, corrected and improved by the people who operate these platforms every day.

## Download

| | |
|---|---|
| **Current version** | v1.1 |
| **Published** | September 2026 |
| **Format** | PDF (English), 114 pages · Markdown (this repository) |
| **Download** | **[Latest release →](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/latest)** |

The PDF is distributed exclusively through the [Releases](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases) page of this repository. Each version is tagged, dated and accompanied by release notes. Previous versions remain available. See [CHANGELOG.md](CHANGELOG.md) for the history of changes.

The PDF is **generated automatically from the Markdown sources** of this repository ([`chapters/`](chapters/), [`appendices/`](appendices/), [`assets/figures/`](assets/figures/)) by a GitHub Actions workflow that rebuilds and verifies it on every change; a version tag publishes it as a release. See [`tools/pdf/README.md`](tools/pdf/README.md) for the toolchain (pandoc + XeLaTeX) and for building it locally.

## Reporting errors and suggesting improvements

Corrections, technical objections and suggestions are welcome and are the main way readers can contribute.

- **Found a mistake?** (technical error, typo, unclear passage, broken reference) → [open an *Errata* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=errata.yml)
- **Have a suggestion or a question about the content?** → [open a *Suggestion* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=suggestion.yml)

Please mention the book version and the page (PDF) or the chapter file and section (Markdown) concerned. Confirmed corrections are listed in the [changelog](CHANGELOG.md) and integrated into the next version. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

Copyright © 2026 Soufian Zaouam.

The book is released under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](https://creativecommons.org/licenses/by-nc-nd/4.0/) licence (CC BY-NC-ND 4.0). You are free to read it, download it, share it and redistribute it, in any medium, as long as you credit the author, do not use it commercially and do not distribute modified versions. See [LICENSE](LICENSE).

For uses not covered by the licence — translations, excerpts for training material, inclusion in a commercial offering — please open an issue or contact the author. Reasonable requests are usually welcome.

## Citing this book

> Zaouam, S. (2026). *OpenStack, the Day After Tomorrow: Operating Mission-Critical OpenStack Platforms* (v1.1). https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow

A machine-readable citation is provided in [CITATION.cff](CITATION.cff).

## About the author

Soufian Zaouam is a platform engineer focused on Day-2 operations, reliability and governance of mission-critical OpenStack platforms. This book is the first of a planned series of works on operating OpenStack in production.

[LinkedIn](https://www.linkedin.com/in/soufian-zaouam) · [GitHub](https://github.com/soufian-zaouam)


---

*OpenStack is a registered trademark of the OpenInfra Foundation. This book and this repository are independent of, and not endorsed by, the OpenInfra Foundation.*
