# Contribuer

Merci de prendre le temps d’améliorer ce livre. Cette page résume en français le guide de contribution du dépôt ; la version de référence, plus complète, est [`CONTRIBUTING.md`](../CONTRIBUTING.md) (en anglais), et un résumé en arabe se trouve dans [`ar/CONTRIBUTING.md`](../ar/CONTRIBUTING.md).

*OpenStack, the Day After Tomorrow* est un livre d’un seul auteur, publié librement et **traduit et corrigé comme un projet communautaire**. Le texte anglais est celui de l’auteur et fait référence ; l’édition française est sa propre traduction ; l’édition arabe est traduite par des volontaires de la communauté OpenStack, sous la supervision éditoriale de l’auteur. Toutes les éditions vivent dans ce dépôt, chapitre par chapitre, et sont publiées ensemble.

## Ce que vous pouvez faire

| Vous voulez… | Faites ceci | Git nécessaire ? |
| --- | --- | --- |
| Signaler une erreur technique, une coquille, un passage peu clair, dans n’importe quelle édition | Ouvrir une [issue *Errata*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=errata.yml) | Non |
| Suggérer un sujet, une nuance, un contre-exemple, poser une question | Ouvrir une [issue *Suggestion*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=suggestion.yml) | Non |
| Traduire un chapitre en arabe (ou le mettre à jour) | Le réserver avec une [issue *Translate a chapter*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=translate-chapter.yml), puis ouvrir une pull request | Oui (ou l’éditeur web) |
| Relire une traduction (langue ou exactitude technique) | Commenter une [pull request de traduction ouverte](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/pulls?q=is%3Apr+is%3Aopen+label%3Atranslation) | Non |
| Signaler un problème de traduction | Ouvrir une [issue *Translation feedback*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=translation-feedback.yml) | Non |
| Proposer ou discuter un terme | Ouvrir une [issue *Terminology*](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues/new?template=terminology.yml) | Non |
| Corriger une coquille, un lien cassé, un défaut de mise en forme | Ouvrir directement une petite pull request | Oui (ou l’éditeur web) |

L’état de chaque chapitre dans chaque langue est dans [TRANSLATIONS.md](../TRANSLATIONS.md).

## La licence, en clair

Le livre est publié sous [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.fr) ([LICENSE](../LICENSE)) :

- **Chacun** peut lire, télécharger, copier et partager le livre, dans n’importe quelle édition, à condition de créditer l’auteur, de ne pas en faire un usage commercial et de le partager sans modification.
- **Une traduction est une version modifiée** (« matériel adapté » au sens de la licence). La licence n’autorise personne à publier de son côté une traduction ou une édition modifiée. Les traductions du livre n’existent qu’ici, dans le dépôt de l’auteur, et sont publiées avec chaque version, sous la même licence.
- **Contribuer n’est donc pas redistribuer.** En proposant une traduction, une relecture ou une correction, vous ne publiez pas une œuvre dérivée : vous proposez un texte que l’auteur intègre aux éditions officielles.

En soumettant une contribution, vous acceptez qu’elle fasse partie du livre et soit publiée sous sa licence (CC BY-NC-ND 4.0, l’auteur étant le concédant), que l’auteur puisse la modifier ou la refuser pour garder les éditions cohérentes, que vous en êtes l’auteur (ou avez le droit de la proposer), et que vous soyez crédité dans [CONTRIBUTORS.md](../CONTRIBUTORS.md) et dans les notes de version, sauf si vous préférez ne pas l’être. La licence du livre lui-même n’est pas modifiée par ce processus.

## Traduire un chapitre, en six étapes

1. **Choisir** un chapitre *not started* et non réservé dans [TRANSLATIONS.md](../TRANSLATIONS.md) et dans les [issues de traduction ouvertes](https://github.com/soufian-zaouam/openstack-the-day-after-tomorrow/issues?q=is%3Aissue+is%3Aopen+label%3Atranslation).
2. **Le réserver** en ouvrant une issue *Translate a chapter* : l’issue ouverte est la réservation, c’est ce qui évite que deux personnes traduisent le même chapitre. Un chapitre à la fois ; une réservation sans nouvelles depuis 30 jours peut être libérée.
3. **Traduire** en suivant le guide de la langue ([`ar/STYLE.md`](../ar/STYLE.md) pour l’arabe) : même fichier, même structure, paragraphe par paragraphe, sans rien fusionner, scinder, résumer ni ajouter ; code, URL, figures et tableaux inchangés ; termes du glossaire ; en cas de doute, traduire fidèlement et laisser un commentaire `<!-- للمراجعة : … -->` plutôt qu’inventer.
4. **Vérifier** avec `python3 tools/check_editions.py ar` (Python 3 seulement). Le workflow GitHub fait la même vérification sur la pull request.
5. **Relire** le chapitre dans la langue cible seule, pour la fluidité.
6. **Ouvrir une pull request** (un chapitre par pull request) qui référence l’issue, ajoute votre nom à CONTRIBUTORS.md et met la ligne du chapitre dans TRANSLATIONS.md à *in review* ; puis **participer à la relecture** et intégrer les retours. Une pull request est fusionnée quand au moins une autre personne l’a relue, que la vérification passe et qu’aucun commentaire ne reste sans réponse.

## Relire une traduction

Aucun outil n’est nécessaire : ouvrir la pull request, lire le fichier rendu (*Files changed* → *View file*), commenter les lignes à changer. Deux relectures sont utiles : **linguistique** (fluidité, grammaire, cohérence avec le glossaire, affichage de droite à gauche), accessible à tout bon lecteur de la langue ; **technique** (notes techniques, noms de services, commandes, raisonnement), qui demande de connaître l’exploitation d’OpenStack. Citer la phrase, dire ce qui ne va pas, proposer une formulation.

## Corriger

- Coquille, lien cassé, défaut de forme, formulation maladroite dans une traduction : petite pull request directe, un sujet par pull request.
- Tout ce qui change le sens d’un passage, dans n’importe quelle édition : d’abord une issue *Errata*. Le texte anglais fait référence : une correction de fond est faite dans le fichier anglais puis reportée dans les fichiers français et arabe de même numéro, pour que les éditions ne divergent jamais. Une correction propre à une traduction ne touche que cette traduction.

## Les règles éditoriales

1. Le sens d’abord : la traduction dit ce que dit l’original, nuances et ton compris. Reformuler librement, ne pas réinterpréter.
2. Rien d’ajouté, rien d’omis : aucun paragraphe, encadré, figure, tableau ou élément de liste n’est fusionné, scindé, résumé ou omis.
3. La voix de l’auteur : première personne, opinions et passages *Sur le terrain* gardent leur personne et leur degré de certitude.
4. Exactitude technique : noms de services, commandes, options, statuts et URL ne sont jamais traduits. Une erreur technique présumée se signale par une issue *Errata* sur le texte anglais, pas par une correction dans la traduction.
5. Terminologie cohérente : un concept, un terme, pris dans le glossaire de la langue. Un terme nouveau se propose avant de s’utiliser.
6. Signaler plutôt que deviner : un passage ambigu reçoit un commentaire de relecture dans le fichier et une note dans la pull request.
7. Passages validés par l’auteur : le titre du livre et des chapitres, le glossaire, les passages *Sur le terrain*, et toute phrase sur laquelle les relecteurs ne s’accordent pas.
8. Garder une trace : décisions terminologiques dans le glossaire (avec l’issue), corrections de fond dans CHANGELOG.md, décisions de traduction dans la pull request.

## Terminologie et désaccords

Le glossaire de chaque langue fait référence ([`ar/STYLE.md`](../ar/STYLE.md), [`fr/STYLE.md`](STYLE.md)). Un terme se propose ou se conteste dans une issue *Terminology* ; il est adopté par accord des participants ou, après deux semaines sans consensus, par décision de l’auteur, puis ajouté au glossaire et appliqué aux chapitres déjà traduits. Un désaccord sur une phrase se règle dans la relecture de la pull request ; à défaut, le mainteneur de la langue tranche, et l’auteur a le dernier mot.

## Qui décide

L’**auteur** est titulaire des droits et éditeur : dernier mot sur toute édition, seul auteur des textes anglais et français, validation des titres, du glossaire et des passages listés ci-dessus. Des **mainteneurs de langue** volontaires peuvent coordonner une édition (tri des issues, libération des réservations inactives, arbitrage des relectures, mise à jour de TRANSLATIONS.md) ; tant qu’il n’y en a pas pour l’arabe, l’auteur tient ce rôle. Les **traducteurs et relecteurs** sont crédités dans CONTRIBUTORS.md.

## Portée et ton

Le livre reflète l’expérience et le point de vue de l’auteur. Le désaccord est bienvenu, factuel et respectueux ; les discussions sur des produits, éditeurs ou organisations particuliers sont hors sujet. Patience avec les nouveaux venus et avec ceux dont la langue relue n’est pas la langue maternelle : l’objectif est un livre qui se lit bien, pas un premier jet parfait.
