---
title: Architecture actuelle
status: reported_not_accepted
date: 2026-08-27
---

# État actuel — As-Is

## Verdict

**L’architecture actuelle est reportée, pas acceptée.** `AUD-005` couvre sept sujets système et borne leurs autorités, contrats, risques et niveaux. Aucun niveau global `user_accepted` ou `operational` n’est prouvé.

## Dossiers reportés

| Dossier | Claims acceptés | Niveau / limite |
|---|---:|---|
| [Sofian OS V4 + TaskNotes](../systems/sofian-os-v4-tasknotes.md) | 30 | canon et implémentation documentés ; usage maintenu non prouvé |
| [Jarvis](../systems/jarvis.md) | 24 | code et contrats observés ; parcours produit global non prouvé |
| [Hermes](../systems/hermes.md) | 20 | runtime et capacités bornées ; 4 claims rejetés |
| [OpenCode](../systems/opencode.md) | 12 | historique et outil spécialisé ; rôle futur ouvert |
| [ourmem](../systems/ourmem.md) | 12 | configuration/API documentées ; recherche sémantique non prouvée dans `AUD-004` |
| [Homelab-OS](../systems/homelab-os.md) | 13 | configuration/reconstruction documentées ; restauration non exercée |
| [Finance OS](../systems/finance-os.md) | 21 | code et contrats observés ; données runtime non lues |

## Claims de cadrage conservés

| Claim | État | Source / locator | Limite |
|---|---|---|---|
| `Sofian-OS` est le vault Obsidian actif | `current_canon` pour l’identité du vault | `SRC-OBS-ACTIVE` — `AGENTS.md:3-8` ; `Sofian OS V4 - Journal De Décisions.md:94-100` | ne prouve pas que tout son contenu est canonique |
| TaskNotes possède l’état des tâches | `current_canon` dans le vault | `SRC-OBS-ACTIVE` — `AGENTS.md:26-31` ; Journal V4 `:104-110` | les projets et autres faits demandent leur propre autorité |
| Hermes héberge la conversation actuelle du chantier | `live_implementation` | `SRC-HERMES` — session `20260827_154335_c51ad8` | ne prouve pas encore toute la responsabilité cible de Jarvis/Hermes |
| Homelab-OS est un dépôt de contrôle et reconstruction du homelab | `current_canon` pour sa configuration versionnée | `SRC-LIVE` — `/Users/sofian/Homelab-OS/AGENTS.md`, lignes `3–23` | état des services live à vérifier séparément |
| ce dépôt possède la méthode et les résultats intégrés du chantier d’audit | `user_decision` | `SRC-HERMES` — messages `52676`, `52961`, `52972` ; `AGENTS.md` actif | ne possède aucun fait métier externe |

## Claims encore à tester, pas à adopter

- rôle actuel et futur d’OpenCode ;
- frontière entre Jarvis, Jarvis Agent, Jarvis OS et Hermes ;
- rôle exact de ourmem et des autres mémoires ;
- frontière et fraîcheur de Finance OS ;
- contrats entre Sofian OS, TaskNotes, Jarvis et systèmes spécialisés ;
- systèmes supplémentaires ou frontières qui n’existent que dans les documents historiques.

## À produire avant acceptation

- carte life-first ;
- carte des capacités ;
- context map des systèmes ;
- matrice des autorités ;
- flux de correction ;
- état live et niveaux de livraison ;
- risques de double autorité ;
- scénarios réels traversants.

Aucun diagramme détaillé n’est ajouté avant cette réconciliation.
