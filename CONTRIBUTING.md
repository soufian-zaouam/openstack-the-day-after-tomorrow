# Contributing

Thank you for taking the time to improve this book.

*OpenStack, the Day After Tomorrow* is a single-author book that is published openly and **translated and corrected as a community project**. The English text is the author's and is the reference edition; the French edition is the author's own translation; the Arabic edition is being translated by volunteers from the OpenStack community, under the author's editorial supervision. All editions live in this repository, chapter by chapter, and are published together.

This page explains what you can contribute, how, and the rules that keep the quality of the book while the work is shared. It is the reference version; summaries exist in [French](fr/CONTRIBUTING.md) and [Arabic](ar/CONTRIBUTING.md).

- [What you can contribute](#what-you-can-contribute)
- [Before you start: the licence](#before-you-start-the-licence)
- [Translating a chapter](#translating-a-chapter)
- [Reviewing a translation](#reviewing-a-translation)
- [Correcting a chapter](#correcting-a-chapter)
- [Reporting an error or suggesting an improvement](#reporting-an-error-or-suggesting-an-improvement)
- [Contributing without Git](#contributing-without-git)
- [Pull requests](#pull-requests)
- [Editorial rules](#editorial-rules)
- [Terminology and disagreements](#terminology-and-disagreements)
- [Who decides what](#who-decides-what)
- [Proposing a new language](#proposing-a-new-language)
- [Credit](#credit)

## What you can contribute

| You want to… | Do this | Needs Git? |
| --- | --- | --- |
| Report a technical error, a typo or an unclear passage, in any edition | Open an [*Errata* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=errata.yml) | No |
| Suggest a topic, a nuance, a counter-example, or ask a question | Open a [*Suggestion* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=suggestion.yml) | No |
| Translate a chapter into Arabic (or update one) | Claim it with a [*Translate a chapter* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=translate-chapter.yml), then open a pull request | Yes (or the web editor) |
| Review a translation for language or technical accuracy | Comment on an [open translation pull request](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/pulls?q=is%3Apr+is%3Aopen+label%3Atranslation) | No |
| Report a translation problem (meaning, terminology, style, display) | Open a [*Translation feedback* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=translation-feedback.yml) | No |
| Propose or discuss a term | Open a [*Terminology* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=terminology.yml) | No |
| Fix a typo, a broken link or a formatting glitch | Open a small pull request directly | Yes (or the web editor) |

The state of every chapter in every language is in [TRANSLATIONS.md](TRANSLATIONS.md).

## Before you start: the licence

The book is published under [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) (CC BY-NC-ND 4.0, see [LICENSE](LICENSE)). In plain words:

- **Anyone** may read, download, copy and share the book, in any edition, as long as they credit the author, do not use it commercially and share it unmodified.
- **A translation is a modified version** ("adapted material" in the licence). The licence does not allow anyone to publish a translation, an excerpt rewritten in another language, or a modified edition on their own. Translations of this book exist only here, in the author's repository, and are published with every release under the same licence and the same conditions.
- **Contributing is therefore different from redistributing.** When you contribute a translation, a review or a correction, you are not publishing a derivative work yourself: you are proposing text that the author integrates into the official editions.

By submitting a contribution to this repository (a translation, a correction, a review comment, a glossary entry), you agree that:

1. your contribution becomes part of the book and is published under the book's licence, CC BY-NC-ND 4.0, with the author as licensor, in the Markdown sources and in the generated PDFs, in this and future versions;
2. the author may edit, shorten, rephrase or decline it in order to keep the editions consistent;
3. you wrote it yourself, or have the right to contribute it, and it contains no text copied from a source that does not allow this use;
4. you are credited by name or GitHub username in [CONTRIBUTORS.md](CONTRIBUTORS.md) and in the release notes of the version that integrates your work, unless you ask not to be.

The licence of the book itself is not changed by this process. Uses that the licence does not cover (a separate edition, a commercial use, extensive excerpts for training material) still need the author's written permission: open an issue or contact the author.

## Translating a chapter

The Arabic edition follows the method of the French one: one Markdown file per chapter, the same structure as the English file, the same boxed passages, figures and tables, and a parity check that runs on every pull request. The rules of the language (terminology, typography, structural markers, right-to-left layout) are in [`ar/STYLE.md`](ar/STYLE.md); read it before translating anything.

1. **Choose a chapter.** Look at [TRANSLATIONS.md](TRANSLATIONS.md) and at the [open translation issues](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues?q=is%3Aissue+is%3Aopen+label%3Atranslation): take a chapter that is *not started* and not claimed. Short chapters (4, 13, 16, the appendices) are good first contributions; the Introduction and Chapter 1 fix the vocabulary of the whole book and are better taken after reading what is already translated.
2. **Claim it** by opening a [*Translate a chapter* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=translate-chapter.yml). The open issue is the claim: it is how two people avoid translating the same chapter. One chapter per person at a time; if you cannot finish, say so in the issue so that someone else can take over. A claim with no news for 30 days may be released by a maintainer.
3. **Translate**, on a fork or a branch, following `ar/STYLE.md`: copy the English file to the same path under `ar/`, wrap it in `<div dir="rtl">` … `</div>`, and translate paragraph by paragraph. Do not merge, split, summarise or add paragraphs. Keep every inline `code`, URL, figure and table in place. Use the glossary's terms. Where you are unsure of the meaning, translate faithfully and leave an HTML comment `<!-- للمراجعة: … -->` for the reviewers rather than inventing an interpretation.
4. **Check** with `python3 tools/check_editions.py ar` (no dependency beyond Python 3). It verifies that nothing was dropped or left in English and that the typography follows the guide. If you have pandoc and TeX Live, `bash tools/pdf/build.sh ar` builds the Arabic PDF from the chapters that exist. The GitHub workflow runs the same checks on your pull request, so you can also rely on it.
5. **Read your chapter in Arabic only**, without the original, for fluency.
6. **Open a pull request** (one chapter per pull request) that links the issue, adds your name to [CONTRIBUTORS.md](CONTRIBUTORS.md) and sets the chapter's line in [TRANSLATIONS.md](TRANSLATIONS.md) to *in review*. Use the pull request template.
7. **Take part in the review** (below) and integrate the comments. When a maintainer merges, the chapter is *translated*.

A chapter whose English text changes afterwards is marked *needs update* in TRANSLATIONS.md, with an issue describing the change; updating it follows the same steps.

## Reviewing a translation

Reviewing needs no Git: open the pull request, read the file (GitHub shows the rendered Markdown under *Files changed* → *View file*, right-to-left for Arabic), and comment on the lines you would change. Two kinds of review are useful, and both are welcome from people who are not OpenStack experts:

- **Linguistic review**: fluency, grammar, spelling, consistency with the glossary, right-to-left display. Anyone who reads Arabic well can do this.
- **Technical review**: the *Technical note* boxes, the service names, the commands and the reasoning must say exactly what the English says. This needs someone who knows OpenStack operations.

A translation pull request is merged when at least one person other than the translator has reviewed it, the parity check passes, and no comment is left unanswered. Reviewers propose; the translator decides how to integrate, and the maintainer arbitrates if they disagree (see below). Be specific and kind: quote the sentence, say what is wrong, propose a wording.

## Correcting a chapter

- **A typo, a broken link, a formatting glitch, a wording that reads badly in the translation**: open a small pull request directly, one subject per pull request. No issue needed.
- **Anything that changes the meaning of a passage**, in any edition: open an *Errata* issue first, with the version, the edition and the location. The English text is the reference: a correction of substance is made in the English file first, then carried into the French and Arabic files with the same chapter number, in the same pull request or in a follow-up, so that the editions never drift apart. A correction specific to one translation touches only that translation.
- **Confirmed corrections** are listed in [CHANGELOG.md](CHANGELOG.md) and integrated into the next version of the PDFs.

## Reporting an error or suggesting an improvement

1. Check the [open issues](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues) to avoid duplicates.
2. Open a new issue with the appropriate template.
3. Give the **book version** (printed on the title page of the PDF, listed in `CHANGELOG.md`), the **edition** (English, French, Arabic) and the **page** (PDF) or **chapter file and section** (Markdown).
4. For a technical objection, give your reasoning and, where possible, a primary source (official OpenStack documentation, specs, release notes).

Every issue is read. Context from your own production experience is especially welcome, kept generic (no organisation, client or environment identifiable).

## Contributing without Git

- **To report or suggest**: issues need only a GitHub account.
- **To review**: comment on a pull request; no Git, no local copy.
- **To translate or correct a file from the browser**: open the file on GitHub, click the pencil (*Edit this file*), edit, then *Commit changes*: GitHub creates a fork and a pull request for you. This works well for a correction or a short file; for a whole chapter, paste your translation into the new file `ar/chapters/<same name as the English file>.md` the same way (*Add file* → *Create new file* in the `ar/chapters/` folder of your fork).
- **If even that is too much**: paste your translation or correction in an issue; a maintainer will turn it into a pull request and credit you.

## Pull requests

- One subject per pull request: one chapter, or one correction. Small pull requests are reviewed quickly; large ones wait.
- Title: `ar: Chapter 4 — The Control Loop` for a translation, `fix(fr): typo in chapter 9` for a correction; anything clear will do.
- Fill in the template: edition, chapter, related issue, the checklist.
- The workflow checks every pull request: parity of the editions (`tools/check_editions.py`), figures, and the PDF builds. A red check is not a rejection; read the log, fix, push again. Ask in the pull request if the log is not clear.
- Pull requests that change the English text, the French text or the tooling are reviewed by the author.

## Editorial rules

The community character of the translations must not lower the quality of the book. These rules apply to every contribution:

1. **Meaning first.** A translation says what the original says, with its nuances, its hedges and its tone, no more and no less. Rephrase freely; do not reinterpret.
2. **Nothing added, nothing dropped.** No paragraph, box, figure, table, list item or footnote is merged, split, summarised or omitted. The parity check enforces the structure; the reviewers enforce the content.
3. **The author's voice.** First-person statements, opinions and *From the field* passages stay in the first person and keep their degree of certainty.
4. **Technical accuracy.** Service names, commands, options, statuses and URLs are never translated. A *Technical note* must remain checkable against the source it cites. If you believe a technical statement is wrong, do not fix it in the translation: open an *Errata* issue against the English text.
5. **Consistent terminology.** One concept, one term, taken from the glossary of the language (`ar/STYLE.md`, `fr/STYLE.md`). A new term is proposed before it is used.
6. **Flag, don't guess.** An ambiguous passage gets a `<!-- للمراجعة: … -->` (or `<!-- review: … -->`) comment in the file and a note in the pull request. The maintainers remove the comment when the question is settled.
7. **Passages that need the author.** The title of the book and the chapter titles, the glossary, the *From the field* passages, and any sentence whose meaning the reviewers cannot agree on are validated by the author before merge.
8. **Keep a trace.** Decisions live where they were taken: terminology decisions in the glossary (with the issue that led to them), corrections of substance in CHANGELOG.md, translation decisions in the pull request. Nothing is decided in private channels.

## Terminology and disagreements

- The glossary of each language is the reference: [`ar/STYLE.md`](ar/STYLE.md), [`fr/STYLE.md`](fr/STYLE.md). It lists the official names that stay in English and the chosen translation of every concept of the book.
- To propose a term or contest one, open a [*Terminology* issue](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=terminology.yml): the term, the current and proposed translations, why, and which chapters are affected. Discussion happens in the issue.
- A term is adopted when the participants agree, or, after two weeks without consensus, when the author decides. The adopted term goes into the glossary in the same pull request that closes the issue, and a follow-up pull request applies it to the chapters already translated.
- Disagreements about a sentence are settled in the pull request review, by the translator and the reviewers; if they cannot agree, the maintainer of the language decides, and the author has the last word. Arguments based on the original text and on the glossary carry more weight than taste.

## Who decides what

| | |
| --- | --- |
| **Author** (Soufian Zaouam) | Copyright holder and editor. Final say on every edition; sole author of the English and French texts; validates titles, the glossary and the passages listed above; merges. |
| **Language maintainers** | Volunteers who coordinate an edition: triage issues, release stale claims, arbitrate review disagreements, keep TRANSLATIONS.md current, prepare releases. Until maintainers are named for Arabic, the author plays the role. Ask in an issue if you want to help this way. |
| **Translators and reviewers** | Everyone who contributes text or reviews. Credited in CONTRIBUTORS.md. |

## Proposing a new language

A new edition is a long-term commitment: the whole book, kept in step with the English text through future versions. If you want to start one, open a *Suggestion* issue saying which language, who would coordinate it, and whether the tooling needs adapting (right-to-left scripts, fonts, hyphenation). A new edition starts with its `<lang>/STYLE.md` (method, markers, glossary), its `<lang>/README.md`, the entries in `tools/check_editions.py`, `tools/pdf/` and the workflow, following the Arabic edition as a model; the author decides when it is published.

## Scope and tone

The book reflects the author's experience and point of view. Disagreement is welcome and is often the most valuable kind of feedback; please keep it factual and respectful. Discussions about specific commercial products, vendors or organisations are out of scope. Be patient with newcomers and with non-native speakers of the language you are reviewing: the goal is a book that reads well, not a perfect first draft.

## Credit

Translators, reviewers and contributors of confirmed corrections are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md) by edition, and in the release notes of the version that integrates their work. The front matter of each translated edition names the edition as a community translation supervised by the author and points to that file.
