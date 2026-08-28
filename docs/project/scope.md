---
title: Scope complet
status: active
date: 2026-08-27
owner: Sofian
sources:
  - conversation Hermes du 2026-08-27
  - ../../archive/baselines/2026-08-25-foundation-e331ee4/BASELINE.md
---

# Scope complet

## 1. Problème

Les décisions, architectures, noms, besoins, expérimentations et réalisations de Sofian sont répartis entre un ancien Notion, plusieurs générations d’Obsidian, des DOCX et médias, OpenCode/OpenChamber, Hermes, ourmem, des dépôts, Homelab-OS et des services spécialisés.

Cette dispersion empêche de voir clairement comment l’écosystème a évolué, pourquoi les choix ont changé, quels noms désignaient réellement la même chose, ce qui a été seulement discuté ou réellement livré, quelles responsabilités appartiennent à quel système, quels besoins restent à satisfaire et quelle cible choisir.

## 2. Finalité

Ce projet fournit une documentation navigable et prouvée qui relie :

```text
histoire → état actuel → besoins → capacités → options
→ cible validée → roadmap → tâches canoniques
```

La cible est un **résultat**, jamais une hypothèse cachée dans l’audit.

## 3. Définition de l’exhaustivité

Exhaustif signifie :

1. inventorier toutes les sources déclarées et retrouvées ;
2. enregistrer leur période, santé, autorité, mode de lecture et couverture ;
3. lire profondément chaque élément pertinent pour l’écosystème ;
4. documenter les exclusions et périodes sans preuve ;
5. publier un rapport de couverture permettant de savoir ce qui reste inconnu.

Exhaustif ne signifie pas recopier toutes les pages Notion, tous les messages, toutes les données personnelles ou tous les commits automatiques.

## 4. Périmètre inclus

### Archéologie

- page Notion `Sofian OS` et sources liées ;
- conversion locale `notion-to-obsidian` ;
- DOCX `SOFIAN OS V2 Document Reference.docx` ;
- anciens médias et transcriptions réellement pertinents ;
- ancien vault `Sofian's Vault` ;
- vault actif `Sofian-OS` et son historique Git ;
- OpenCode/OpenChamber ;
- sessions Hermes ;
- ourmem comme mémoire secondaire ;
- dépôts, configurations, services et artefacts réels.

### Reconstruction

- timeline ;
- filiation des noms et identités ;
- décisions, corrections et remplacements ;
- intentions historiques ;
- état actuel ;
- niveaux de livraison ;
- contradictions et périodes sans preuve.

### Audit architecture

Pour chaque domaine, capacité, système, module, projet, adapter ou runtime : besoin et bénéficiaire, responsabilité, faits possédés ou non, cycle de vie, invariants, contrats, dépendances, permissions, risques, implémentation actuelle et niveau de livraison.

### Découverte des besoins

Les besoins, irritants et idées sont capturés avant attribution à un système. Chaque entrée précise situation, résultat attendu, origine, fréquence, impact, capacité, couverture actuelle, options de responsabilité et statut `idea`, `observed`, `validated`, `deferred` ou `rejected`.

### Conception de la cible

Pour une décision structurante :

1. conserver le statu quo comme option réelle ;
2. comparer extension d’un système, workflow transversal, module/adaptateur ou nouveau système candidat ;
3. tester les frontières avec plusieurs situations réelles ;
4. expliciter coûts, risques, dépendances, réversibilité et réexamen ;
5. présenter une cible candidate ;
6. attendre la validation explicite de Sofian.

### Documentation et exécution

- VitePress public pour l’instant par décision `CUR-007`, avec gate anti-secrets/PII ;
- recherche et navigation en français ;
- diagrammes Mermaid utiles ;
- dossiers système, workflows, contrats, ADR et scénarios ;
- roadmap par chantiers et tranches verticales ;
- liens vers les projets et TaskNotes canoniques ;
- protocoles réutilisables pour sessions et subagents.

## 5. Hors périmètre sans nouvel accord

- modifier, déplacer, supprimer ou migrer une source externe ;
- importer un historique ou une mémoire ;
- créer ou changer une TaskNote ;
- modifier un skill, agent, cron ou service ;
- déployer ou publier un nouveau lot sans accord exact ;
- déclarer un système legacy, abandonné ou remplacé ;
- décider d’une cible ou d’une priorité personnelle à la place de Sofian ;
- exposer des secrets ou des données privées non nécessaires.

## 6. Livrables

1. charte et méthode d’audit ;
2. registre des sources et de leur autorité ;
3. ledger de preuves et couverture ;
4. timeline et filiation des noms ;
5. catalogue des décisions et contradictions ;
6. paysage des besoins et capacités ;
7. dossiers complets des systèmes et workflows ;
8. cartes d’autorité, responsabilités humaines/agentiques et contrats inter-systèmes ;
9. matrice de niveau de livraison ;
10. options de cible et décisions acceptées ;
11. roadmap de transition avec chantiers, sous-projets, dépendances et liens TaskNotes ;
12. documentation VitePress, actuellement publique par décision explicite ;
13. système de handoff et de délégation ;
14. procédure ou skill consolidé après preuve répétée.

## 7. Diagrammes et expérience TDAH

- conclusion visible avant le détail ;
- trois entrées principales : comprendre, auditer, construire la cible ;
- divulgation progressive ;
- une question par diagramme ;
- 3 à 9 nœuds dans une vue globale ;
- histoire, actuel et cible séparés ;
- date, statut, sources, légende et résumé textuel ;
- contraste et sens indépendants de la couleur ;
- pages courtes, liens vers les annexes plutôt que murs de texte.

## 8. Phases

### A — Reconstruire

1. cadrage et sécurité ;
2. cartographie des sources ;
3. tranche pilote Notion → DOCX → V1/V2/V3/V4 ;
4. extension chronologique jusqu’à aujourd’hui.

### B — Réconcilier

1. identités, décisions et contradictions ;
2. domaines, capacités, systèmes et autorités ;
3. portefeuille et flux ;
4. état live et niveaux de livraison.

### C — Concevoir et documenter

1. catalogue des besoins ;
2. options d’architecture ;
3. cible proposée puis acceptée ;
4. transition et roadmap ;
5. VitePress et contrôles ;
6. capitalisation de la méthode.

## 9. Gates d’approbation

| Gate | Décision attendue |
|---|---|
| 0 — Mandat | sources et limites de lecture |
| 1 — Autorités | carte des sources et conflits |
| 2 — Identités | renommages et regroupements |
| 3 — État | historique et actuel réconciliés |
| 4 — Besoins | besoins validés et différés |
| 5 — Architecture | option choisie ou statu quo |
| 6 — Roadmap | tranches et critères de fin |
| 7 — Documentation | structure et contenu à canoniser |
| 8 — Exécution | mutations exactes, séparément autorisées |

## 10. Règles du dépôt

- Le dépôt possède la documentation du chantier, pas tous les faits qu’elle décrit.
- TaskNotes possède l’état opérationnel des tâches et projets.
- Un brief d’audit n’est pas une tâche.
- Un rapport d’agent n’est pas une preuve tant que ses sources n’ont pas été vérifiées.
- Un besoin ne devient pas un système par sa taille ou son importance.
- La cible acceptée reste révisable avec un déclencheur explicite.
