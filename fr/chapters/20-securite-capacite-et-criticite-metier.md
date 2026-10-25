*Partie VI — Décisions du terrain*

# Chapitre 20 — Sécurité, capacité et criticité métier

Les exigences de sécurité sont réelles. Mais l’exécution d’une mesure de sécurité peut elle-même introduire un risque opérationnel, et la décision sur la *manière* de satisfaire une exigence est souvent une décision métier que l’équipe d’infrastructure ne peut pas prendre seule.

## Contexte

Une plateforme de production comptant entre cent et plusieurs centaines d’hôtes de calcul, soumise à une obligation d’application des correctifs de système d’exploitation sur ces hôtes. Appliquer les correctifs sur un hôte de calcul exige en général de le redémarrer, et le redémarrer sans perturber les instances qu’il exécute exige de les déplacer ailleurs au préalable.

## Signal

La plateforme ne disposait pas d’assez de capacité de calcul de réserve pour migrer à chaud toutes les charges de travail hors de chaque hôte avant de le corriger. La contrainte était la capacité nécessaire pour appliquer le correctif en sécurité, pas le correctif lui-même.

> **Note technique — ce qu’implique la maintenance d’un hôte.** Retirer un hôte de calcul du service pour maintenance consiste normalement à désactiver son service `nova-compute`, de sorte que le scheduler n’y place plus de nouvelles instances, puis à déplacer les instances qu’il exécute. La migration à chaud garde l’instance en fonctionnement pendant son déplacement ; elle exige une destination disposant d’assez de CPU, de mémoire et de disque, et soit un stockage partagé pour les disques de l’instance, soit une migration par blocs qui les copie à travers le réseau, ce qui ajoute de la charge au réseau comme au système de stockage. Elle a aussi des contraintes de compatibilité qu’une campagne de correctifs rencontre de plein fouet : le modèle de CPU de la destination doit être compatible avec celui de la source, et la migration d’un libvirt/QEMU plus récent vers un plus ancien n’est pas prise en charge ; dès lors que certains hôtes sont corrigés, les instances peuvent se déplacer vers eux mais pas revenir, et l’ordre d’application des correctifs décide des destinations possibles. Certaines instances ne peuvent pas du tout être migrées à chaud, ou ne devraient pas l’être : celles qui ont du PCI passthrough, y compris les ports SR-IOV de type `direct-physical`, celles qui utilisent un vGPU sur les versions qui ne prennent pas en charge la migration des mediated devices, et les charges de travail intensives en mémoire dont les pages changent plus vite qu’elles ne peuvent être copiées, sauf si auto-converge ou post-copy est activé ; pour celles-là, un redémarrage est une nécessité technique et non un choix métier. Les instances dotées de ports SR-IOV `direct` sont un cas différent : avec le pilote libvirt, elles peuvent être migrées à chaud depuis la version Train (Nova 20.0.0), mais le port est débranché avant le déplacement puis rebranché sur la destination, de sorte que l’invité perd brièvement cette interface, ce que son propriétaire doit accepter. La migration à froid (`openstack server migrate`), qui arrête l’instance et la déplace, est l’option intermédiaire. L’évacuation est une opération différente, destinée à un hôte qui a déjà défailli, et elle ne doit jamais être utilisée sur un hôte qui exécute peut-être encore ses instances (chapitre 10). Enfin, un correctif de l’hyperviseur ou de QEMU ne protège que les instances migrées ou redémarrées depuis ; une instance qui continue de tourner sur l’ancien binaire n’est pas corrigée. Voir la documentation Nova sur la configuration et l’utilisation de la migration à chaud, sur la migration à froid et sur l’évacuation des instances ; voir aussi les notes de version Nova de Train.

![Figure 20.1](../../assets/figures/fr/figure-20-1.svg)

*Figure 20.1 : Déplacer des instances hors d’un hôte : quelle opération s’applique, et ce qui doit être vrai au préalable.*

## Incertitude

L’incertitude portait sur les charges de travail capables de tolérer un redémarrage plutôt qu’une migration. Nova ne peut pas le dire, parce qu’il voit des instances, pas des processus métier.

## Risque métier

Retarder l’application des correctifs prolongeait l’exposition de la plateforme. Faire passer chaque charge de travail par une migration à chaud n’était pas réalisable avec la capacité disponible. Redémarrer des charges de travail sans connaître leur criticité risquait de perturber un processus métier dont personne dans l’équipe d’infrastructure n’avait connaissance.

## Options

Tout migrer, ce que la capacité ne permettait pas. Tout redémarrer et accepter un impact métier inconnu. Ou obtenir l’information manquante auprès des personnes qui la détenaient, les équipes consommatrices, et exécuter une stratégie différenciée.

## Décision

Les équipes consommatrices ont fourni ce que l’infrastructure ne pouvait pas déduire : la criticité métier, le temps d’indisponibilité acceptable, les attentes de reprise et les échéances, rassemblés dans un tableau partagé que chaque équipe a rempli pour ses propres charges de travail. Les charges de travail critiques ont été migrées à chaud dans la limite de la capacité disponible ; des redémarrages ont été coordonnés pour celles qui pouvaient les tolérer. L’objectif de sécurité n’a pas changé. La stratégie d’exécution reflétait l’environnement d’exploitation réel.

## Compromis

Une stratégie différenciée est plus longue à planifier qu’une stratégie uniforme, et elle dépend d’informations qu’il faut collecter en dehors de l’équipe plateforme. En échange, elle rend l’application des correctifs réalisable avec la capacité qui existe réellement, et elle confie la décision sur chaque charge de travail aux personnes qui savent à quoi elle sert.

## Résultat

Les hôtes ont été corrigés sans forcer chaque charge de travail à passer par une migration que la plateforme ne pouvait pas absorber. Le tableau de criticité constitué pour la campagne est le type d’information qui devrait exister avant un événement de maintenance plutôt que d’être collecté pour la première fois quand l’application des correctifs commence ; tenu à jour, que ce soit sous la forme d’un document partagé ou de métadonnées portées par les instances et les projets eux-mêmes, il devient une entrée de la planification de capacité plutôt qu’un effort ponctuel.

## Leçon

Le travail de sécurité est un travail de plateforme. L’application des correctifs modifie le placement des charges de travail, la capacité et la disponibilité ; les exigences de sécurité doivent donc être intégrées à la planification de capacité de la plateforme plutôt qu’imposées de l’extérieur à l’exploitation. Si la capacité de calcul est insuffisante pour migrer chaque charge de travail, c’est une contrainte sur l’aptitude de l’organisation à satisfaire les exigences de sécurité sans perturbation, et la planification de capacité doit donc inclure explicitement les scénarios de maintenance : combien d’hôtes peuvent être indisponibles en même temps, combien de charges de travail peuvent être en cours de déplacement, quelle capacité de réserve une application sûre des correctifs exige. La réponse dépend du domaine de défaillance : une plateforme qui peut se permettre un hôte arrêté par rack, ou par zone de disponibilité, a besoin de la capacité de réserve d’un hôte dans chacun de ces domaines, pas d’un hôte au total.

La criticité a besoin de l’apport des consommateurs, et elle en a besoin avant l’événement de maintenance. Le risque de sécurité et le risque de disponibilité sont tous deux des risques métier, et les présenter comme un conflit entre deux équipes techniques passe à côté de l’essentiel : la décision consiste à trouver l’équilibre le plus sûr qui soit atteignable compte tenu de l’état réel de la plateforme. Une difficulté récurrente à corriger les hôtes, à migrer les charges de travail ou à mettre à niveau les dépendances est aussi le signe de quelque chose de plus profond. La tâche immédiate doit tout de même être menée à bien, mais une opération de sécurité qui consomme chaque fois une capacité disproportionnée est un problème de cycle de vie, et elle a sa place sur la feuille de route de la plateforme. C’est aussi là que la sécurité rejoint l’alignement upstream : une organisation très en retard sur les versions maintenues finit par devoir choisir entre des backports locaux répétés et une mise à niveau majeure, et si un backport à court terme peut être rationnel, un schéma durable de divergence est une dette de cycle de vie (chapitres 14 et 17).

> **Principe.** Les exigences de sécurité définissent ce qui doit être atteint. La capacité de la plateforme et la criticité métier déterminent avec quelle sûreté cela peut l’être.

---

[← Chapitre 19 — Quand la décision sûre est de s’arrêter](19-quand-la-decision-sure-est-de-s-arreter.md) · [Sommaire](../README.md) · [Conclusion : garder OpenStack sous contrôle →](21-conclusion-garder-openstack-sous-controle.md)
