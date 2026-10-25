# OpenStack, après-demain

### Exploiter des plateformes OpenStack critiques

**Auteur : Soufian Zaouam**

[![Télécharger le PDF](https://img.shields.io/badge/T%C3%A9l%C3%A9charger-PDF%20(derni%C3%A8re%20version)-2ea44f?style=for-the-badge)](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/latest)
[![Version](https://img.shields.io/github/v/release/soufian-zaouam/openstack-the-day-after-tomorrow?label=version&style=for-the-badge)](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases)
[![Licence : CC BY-NC-ND 4.0](https://img.shields.io/badge/Licence-CC%20BY--NC--ND%204.0-lightgrey?style=for-the-badge)](../LICENSE)

Ceci est l’édition française du livre *OpenStack, the Day After Tomorrow*, maintenue dans le même dépôt que l’édition anglaise originale ([README en anglais](../README.md)). Elle en suit le texte chapitre par chapitre ; les deux éditions portent le même numéro de version et sont publiées ensemble.

Le livre est publié librement, en **PDF** (voir [Télécharger](#télécharger)) et en **Markdown, un fichier par chapitre, lisible directement sur GitHub** (voir [Lire le livre sur GitHub](#lire-le-livre-sur-github)). C’est une **contribution indépendante et personnelle à la communauté OpenStack**. Ce n’est ni une publication de l’OpenStack Foundation (OpenInfra Foundation), ni celle d’un éditeur, d’un employeur ou d’un client, et il ne décrit la plateforme d’aucune organisation en particulier.

---

## À propos du livre

La plupart des ressources sur OpenStack s’arrêtent là où le vrai travail commence : la plateforme est déployée, les services répondent, les premiers tenants sont à bord. Ce livre porte sur ce qui vient ensuite — les années pendant lesquelles une plateforme doit rester stable, observable, capable d’être mise à niveau, sûre et, surtout, compréhensible par les personnes qui l’exploitent.

Sa thèse centrale est qu’exploiter OpenStack en production n’est pas seulement un problème technique. C’est aussi un problème de visibilité, de stabilité, d’organisation, de gouvernance et de gestion du risque. Une plateforme peut être parfaitement fonctionnelle et rester difficile à exploiter, difficile à faire évoluer, difficile à sécuriser et difficile à transmettre.

C’est l’expérience et le point de vue d’un opérateur, pas une norme ni un manuel de référence. Lorsque la bonne réponse dépend du déploiement ou du backend, le texte le dit.

Le livre s’appuie sur plus de cinq ans d’exploitation de plateformes OpenStack en production (exploitation Day 2, fiabilité, mises à niveau, gestion des incidents, construction d’équipe). L’expérience réelle a été généralisée en schémas et en principes ; aucun client, employeur, projet ou environnement n’est décrit ni identifiable.

**Ce que vous trouverez à l’intérieur** (20 chapitres en six parties, plus des annexes)

- *Comprendre le problème* — pourquoi OpenStack ne s’arrête pas au déploiement, pourquoi le véritable ennemi est la perte de contrôle, et la boucle de contrôle qui traverse tout le livre
- *Évaluer le contrôle* — comment évaluer et mesurer le contrôle qu’une organisation a réellement sur sa plateforme, et que faire quand il est déjà perdu
- *Exploiter sous contrôle* — la visibilité avant l’action, la stabilité et le changement, et la reprise comme fonctionnalité plutôt que comme arrière-pensée
- *L’organisation derrière la plateforme* — la documentation comme mémoire opérationnelle, la construction de l’équipe, les droits de décision
- *Évoluer sans perdre le contrôle* — mises à niveau, backports et alignement upstream ; complexité, dette technique et simplification ; automatisation ; la sécurité comme travail de plateforme
- *Décisions du terrain* — deux décisions détaillées où preuves techniques, impact métier et contraintes opérationnelles sont entrés en collision
- Annexes : un cadre de décision du contrôle, une fiche d’évaluation du contrôle, une fiche de décision de changement minimale, des questions de revue du contrôle, les principes d’exploitation en un coup d’œil, et un glossaire

Tout au long du texte, les encadrés *Note technique*, *Principe* et *Sur le terrain* séparent le comportement documenté d’OpenStack, les principes d’exploitation de l’auteur et les situations tirées d’exploitations réelles.

## Lire le livre sur GitHub

Le texte intégral du livre est publié dans ce dépôt en Markdown, **un fichier par chapitre**, pour être lu directement sur GitHub, cherché, lié et cité par section. Le texte est celui du PDF, qui est généré à partir de ces mêmes fichiers ; les cinq figures sont fournies en SVG dans [`assets/figures/fr/`](../assets/figures/fr/).

Commencez par [Comment lire ce livre](chapters/00-comment-lire-ce-livre.md), puis suivez les liens *Précédent / Sommaire / Suivant* au bas de chaque chapitre. Le PDF reste disponible pour la lecture hors ligne (voir [Télécharger](#télécharger)).

| | Chapitre |
| --- | --- |
| | [Pages liminaires](chapters/00-pages-liminaires.md) |
| | [Comment lire ce livre](chapters/00-comment-lire-ce-livre.md) |
| | [Introduction](chapters/00-introduction.md) |
| **Partie I — Comprendre le problème** | |
| 1 | [OpenStack ne s’arrête pas au déploiement](chapters/01-openstack-ne-s-arrete-pas-au-deploiement.md) |
| 2 | [L’ennemi, c’est la perte de contrôle](chapters/02-l-ennemi-c-est-la-perte-de-controle.md) |
| 3 | [Pourquoi de bonnes plateformes deviennent difficiles à exploiter](chapters/03-pourquoi-de-bonnes-plateformes-deviennent-difficiles-a-exploiter.md) |
| 4 | [La boucle de contrôle](chapters/04-la-boucle-de-controle.md) |
| **Partie II — Évaluer le contrôle** | |
| 5 | [Évaluer le contrôle de la plateforme](chapters/05-evaluer-le-controle-de-la-plateforme.md) |
| 6 | [Mesurer le contrôle](chapters/06-mesurer-le-controle.md) |
| 7 | [Quand le contrôle est déjà perdu](chapters/07-quand-le-controle-est-deja-perdu.md) |
| **Partie III — Exploiter sous contrôle** | |
| 8 | [La visibilité avant l’action](chapters/08-la-visibilite-avant-l-action.md) |
| 9 | [Stabilité et changement](chapters/09-stabilite-et-changement.md) |
| 10 | [La reprise est une fonctionnalité](chapters/10-la-reprise-est-une-fonctionnalite.md) |
| **Partie IV — L’organisation derrière la plateforme** | |
| 11 | [La documentation est la mémoire opérationnelle](chapters/11-la-documentation-est-la-memoire-operationnelle.md) |
| 12 | [Construire l’équipe derrière la plateforme](chapters/12-construire-l-equipe-derriere-la-plateforme.md) |
| 13 | [Les droits de décision](chapters/13-les-droits-de-decision.md) |
| **Partie V — Évoluer sans perdre le contrôle** | |
| 14 | [Mises à niveau, backports et alignement upstream](chapters/14-mises-a-niveau-backports-et-alignement-upstream.md) |
| 15 | [Complexité, dette technique et simplification](chapters/15-complexite-dette-technique-et-simplification.md) |
| 16 | [Automatisation et complexité opérationnelle](chapters/16-automatisation-et-complexite-operationnelle.md) |
| 17 | [La sécurité est un travail de plateforme](chapters/17-la-securite-est-un-travail-de-plateforme.md) |
| 18 | [Faire évoluer une plateforme critique](chapters/18-faire-evoluer-une-plateforme-critique.md) |
| **Partie VI — Décisions du terrain** | |
| 19 | [Quand la décision sûre est de s’arrêter](chapters/19-quand-la-decision-sure-est-de-s-arreter.md) |
| 20 | [Sécurité, capacité et criticité métier](chapters/20-securite-capacite-et-criticite-metier.md) |
| | [Conclusion : garder OpenStack sous contrôle](chapters/21-conclusion-garder-openstack-sous-controle.md) |
| **Annexes** | |
| A | [Le cadre de décision du contrôle](appendices/annexe-a-le-cadre-de-decision-du-controle.md) |
| B | [La fiche d’évaluation du contrôle](appendices/annexe-b-la-fiche-d-evaluation-du-controle.md) |
| C | [Une fiche de décision de changement minimale](appendices/annexe-c-une-fiche-de-decision-de-changement-minimale.md) |
| D | [Questions de revue du contrôle](appendices/annexe-d-questions-de-revue-du-controle.md) |
| E | [Les principes d’exploitation en un coup d’œil](appendices/annexe-e-les-principes-d-exploitation-en-un-coup-d-oeil.md) |
| F | [Glossaire](appendices/annexe-f-glossaire.md) |
| | [Références et lectures complémentaires](appendices/references-et-lectures-complementaires.md) |

**Parcours court pour les managers et les sponsors** (tel que suggéré dans *Comment lire ce livre*) : l’[Introduction](chapters/00-introduction.md), les chapitres [1](chapters/01-openstack-ne-s-arrete-pas-au-deploiement.md) à [3](chapters/03-pourquoi-de-bonnes-plateformes-deviennent-difficiles-a-exploiter.md), le chapitre [7](chapters/07-quand-le-controle-est-deja-perdu.md), la dernière section du chapitre [12](chapters/12-construire-l-equipe-derriere-la-plateforme.md), les chapitres [13](chapters/13-les-droits-de-decision.md) et [14](chapters/14-mises-a-niveau-backports-et-alignement-upstream.md) jusqu’à la première note technique, les chapitres [19](chapters/19-quand-la-decision-sure-est-de-s-arreter.md) et [20](chapters/20-securite-capacite-et-criticite-metier.md), la [Conclusion](chapters/21-conclusion-garder-openstack-sous-controle.md), et les annexes [D](appendices/annexe-d-questions-de-revue-du-controle.md) et [E](appendices/annexe-e-les-principes-d-exploitation-en-un-coup-d-oeil.md).

### Organisation de l’édition française dans le dépôt

```text
openstack-the-day-after-tomorrow/
├── README.md              présentation et sommaire de l’édition anglaise
├── chapters/, appendices/ le texte anglais, un fichier Markdown par chapitre
├── assets/figures/        les figures de l’édition anglaise (SVG)
│   └── fr/                les mêmes figures, libellés en français
├── fr/
│   ├── README.md          cette page : présentation et sommaire en français
│   ├── STYLE.md           méthode, conventions et terminologie de l’édition française
│   ├── chapters/          pages liminaires, introduction, chapitres 1–20 et conclusion
│   └── appendices/        annexes A–F et références
├── tools/pdf/             génération des PDF (pandoc + XeLaTeX), les deux éditions
├── tools/figures/         traduction des figures (tables de libellés dans tools/figures/fr/)
├── tools/check_editions.py  vérification de la parité entre les deux éditions
└── tools/fr_typography.py   application de la typographie française
```

Chaque fichier français porte le même numéro de chapitre ou la même lettre d’annexe que son original anglais (correspondance complète dans [`STYLE.md`](STYLE.md)). Tout au long du texte, trois sortes d’encadrés du PDF sont rendus en citations : **Note technique** (faits OpenStack vérifiables, avec une référence), **Principe** (une règle d’exploitation que le livre recommande) et **Sur le terrain** (une situation opérationnelle et la décision qu’elle a exigée).

## Ressources complémentaires

- **[Short Guide](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow-guide)** — les idées du livre en 18 pages illustrées, une idée et une figure par page (en anglais). La porte d’entrée la plus rapide, et une référence partagée pour les équipes et les sponsors.
- **[OpenStack Production Guide](https://github.com/soufian-zaouam/openstack-production-guide)** — le compagnon pratique (en anglais) : dépannage par symptôme, par commande et par message d’erreur, la série *One Command, One Investigation* (20 épisodes), et six cas d’incidents anonymisés au format RCA. Plusieurs passages *Sur le terrain* du livre y sont développés avec leur dossier technique.
- **[OpenStack Operator Skills](https://github.com/soufian-zaouam/openstack-operator-skills)** — la méthode du livre sous forme de sept Agent Skills pour Claude (en anglais) : analyse d’incident, revue de changement, planification de maintenance, décisions d’exploitation, évaluation du contrôle, revue d’automatisation et rédaction de runbooks. Elles amènent un assistant IA à investiguer avant d’agir, à garder un chemin de retour et à laisser les décisions perturbatrices aux personnes qui en répondent. Licence Apache-2.0, évaluées avec et sans les skills.

## À qui il s’adresse

- Aux ingénieurs et aux équipes plateforme qui exploitent, ou s’apprêtent à hériter, une plateforme OpenStack
- Aux architectes et responsables de plateforme chargés de la fiabilité et de l’évolution d’un cloud privé
- Aux CTO, DSI et directeurs de programme qui doivent comprendre à quoi « faire tourner OpenStack » les engage réellement

Il suppose une connaissance pratique d’OpenStack. Ce n’est pas un guide d’installation et il ne remplace pas la documentation officielle.

## Pourquoi ce livre existe

Le déploiement est le début du parcours opérationnel, pas sa fin. Les leçons durement acquises de l’exploitation Day 2 sont rarement écrites et, quand elles le sont, elles sont dispersées dans des rapports d’incident, des savoirs tribaux et des conférences. Ce livre est une tentative de les consolider en un texte cohérent, assumé et pratique — et de le rendre à la communauté qui a rendu la plateforme possible.

**Pourquoi il est publié librement.** OpenStack est open source, et l’essentiel de ce que je sais de son exploitation, je l’ai appris dans de la documentation, du code et des discussions que d’autres ont choisi de partager. Publier ce livre librement est la façon la plus directe que j’aie de rendre quelque chose, et de voir son contenu discuté, corrigé et amélioré par ceux qui exploitent ces plateformes chaque jour.

**Pourquoi une édition française.** Une part importante des plateformes OpenStack critiques est exploitée par des équipes francophones. L’édition française est une édition à part entière, traduite et adaptée par l’auteur, qui suit l’édition anglaise chapitre par chapitre et évolue avec elle.

## Télécharger

| | |
|---|---|
| **Version courante** | v1.3 |
| **Publication** | octobre 2026 |
| **Format** | PDF (français), 125 pages · Markdown (ce dépôt) |
| **Télécharger** | **[Dernière version →](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases/latest)** |

Les PDF sont distribués exclusivement sur la page [Releases](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/releases) de ce dépôt ; chaque version porte les deux éditions (`openstack-the-day-after-tomorrow-vX.Y.pdf` et `openstack-the-day-after-tomorrow-fr-vX.Y.pdf`). Chaque version est taguée, datée et accompagnée de notes de version. Les versions précédentes restent disponibles. Voir [CHANGELOG.md](../CHANGELOG.md) pour l’historique des changements.

Le PDF est **généré automatiquement à partir des sources Markdown** de ce dépôt ([`fr/chapters/`](chapters/), [`fr/appendices/`](appendices/), [`assets/figures/fr/`](../assets/figures/fr/)) par un workflow GitHub Actions qui le reconstruit et le vérifie à chaque changement ; un tag de version le publie en release. Voir [`tools/pdf/README.md`](../tools/pdf/README.md) pour la chaîne de génération (pandoc + XeLaTeX) et pour le construire localement (`bash tools/pdf/build.sh fr`).

## Signaler des erreurs et proposer des améliorations

Les corrections, les objections techniques et les suggestions sont les bienvenues ; c’est la principale façon pour les lecteurs de contribuer.

- **Une erreur ?** (erreur technique, coquille, passage peu clair, référence cassée, traduction inexacte) → [ouvrir une issue *Errata*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=errata.yml)
- **Une suggestion ou une question sur le contenu ?** → [ouvrir une issue *Suggestion*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=suggestion.yml)

Merci d’indiquer la version du livre, l’édition (française) et la page (PDF) ou le fichier de chapitre et la section (Markdown) concernés. Les corrections confirmées sont listées dans le [changelog](../CHANGELOG.md) et intégrées à la version suivante. Une correction de fond est d’abord faite dans l’édition anglaise, puis reportée ici. Voir [CONTRIBUTING.md](../CONTRIBUTING.md).

## Licence

Copyright © 2026 Soufian Zaouam.

Le livre est publié sous licence [Creative Commons Attribution – Pas d’utilisation commerciale – Pas de modification 4.0 International](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.fr) (CC BY-NC-ND 4.0). Vous êtes libre de le lire, de le télécharger, de le partager et de le redistribuer, sur tout support, à condition de créditer l’auteur, de ne pas en faire un usage commercial et de ne pas distribuer de version modifiée. Voir [LICENSE](../LICENSE).

Pour les usages non couverts par la licence — traductions dans d’autres langues, extraits pour des supports de formation, inclusion dans une offre commerciale — merci d’ouvrir une issue ou de contacter l’auteur. Les demandes raisonnables sont généralement les bienvenues.

## Citer ce livre

> Zaouam, S. (2026). *OpenStack, après-demain : exploiter des plateformes OpenStack critiques* (v1.3, édition française d’*OpenStack, the Day After Tomorrow*). https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow

Une citation lisible par machine est fournie dans [CITATION.cff](../CITATION.cff).

## À propos de l’auteur

Soufian Zaouam est ingénieur plateforme, spécialisé dans l’exploitation Day 2, la fiabilité et la gouvernance de plateformes OpenStack critiques. Ce livre est le premier d’une série prévue d’ouvrages sur l’exploitation d’OpenStack en production.

[LinkedIn](https://www.linkedin.com/in/soufian-zaouam) · [GitHub](https://github.com/soufian-zaouam)


---

*OpenStack est une marque déposée de l’OpenInfra Foundation. Ce livre et ce dépôt sont indépendants de l’OpenInfra Foundation et ne sont pas approuvés par elle.*
