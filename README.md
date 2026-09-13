# OpenStack, the Day After Tomorrow

### Operating Mission-Critical OpenStack Platforms

**Author: Soufian Zaouam**

[![Download the PDF](https://img.shields.io/badge/Download-PDF%20(latest%20release)-2ea44f?style=for-the-badge)](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/latest)
[![Version](https://img.shields.io/github/v/release/soufian-zaouam/openstack-the-day-after-tomorrow?label=version&style=for-the-badge)](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey?style=for-the-badge)](LICENSE)

This is the author's official repository for the book *OpenStack, the Day After Tomorrow*. It is the reference place to download the current edition, follow new versions, and report errors.

The book is published as a **free PDF** and is an **independent, personal contribution to the OpenStack community**. It is not a publication of the OpenStack Foundation (OpenInfra Foundation), of a publisher, or of any employer or client, and it does not describe any specific organisation's platform.

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
| **Current version** | v1.0 |
| **Published** | September 2026 |
| **Format** | PDF (English) |
| **Download** | **[Latest release →](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/latest)** |

The PDF is distributed exclusively through the [Releases](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases) page of this repository. Each version is tagged, dated and accompanied by release notes. Previous versions remain available. See [CHANGELOG.md](CHANGELOG.md) for the history of changes.

Only the PDF is published. The manuscript sources are not part of this repository.

## Reporting errors and suggesting improvements

Corrections, technical objections and suggestions are welcome and are the main way readers can contribute.

- **Found a mistake?** (technical error, typo, unclear passage, broken reference) → [open an *Errata* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=errata.yml)
- **Have a suggestion or a question about the content?** → [open a *Suggestion* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=suggestion.yml)

Please mention the book version and the page or section concerned. Confirmed corrections are listed in the [changelog](CHANGELOG.md) and integrated into the next version. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

Copyright © 2026 Soufian Zaouam.

The book is released under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](https://creativecommons.org/licenses/by-nc-nd/4.0/) licence (CC BY-NC-ND 4.0). You are free to read it, download it, share it and redistribute it, in any medium, as long as you credit the author, do not use it commercially and do not distribute modified versions. See [LICENSE](LICENSE).

For uses not covered by the licence — translations, excerpts for training material, inclusion in a commercial offering — please open an issue or contact the author. Reasonable requests are usually welcome.

## Citing this book

> Zaouam, S. (2026). *OpenStack, the Day After Tomorrow: Operating Mission-Critical OpenStack Platforms* (v1.0). https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow

A machine-readable citation is provided in [CITATION.cff](CITATION.cff).

## About the author

Soufian Zaouam is a platform engineer focused on Day-2 operations, reliability and governance of mission-critical OpenStack platforms. This book is the first of a planned series of works on operating OpenStack in production.


---

*OpenStack is a registered trademark of the OpenInfra Foundation. This book and this repository are independent of, and not endorsed by, the OpenInfra Foundation.*
