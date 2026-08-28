---
id: AUD-004
title: Hermes et ourmem — rapport d’audit
status: integrated
date: 2026-08-28
canonical_synthesis_task: t_1e313379
canonical_synthesis_run: 63
accepted_claims: 56
integration_authorized: true
---

# AUD-004 — Hermes et ourmem

> **État : `integrated`, contre-audité.** Ce rapport et son ledger sont intégrés au dépôt après validation explicite de Sofian.

## Verdict

La synthèse source d’AUD-004 a été produite au statut `reported` ; ce rapport est désormais `integrated`. En lecture seule, 6/6 sessions Hermes sont couvertes, 59 claims uniques ont été contrôlés, 56 sont retenus et 3 rejetés ; les 3/3 recherches ourmem ont été tentées mais bloquées avant tout résultat. Les décisions ponctuelles et mutations historiques sont séparées des recommandations et des claims produit actuels ; aucune cible Jarvis/Hermes/Bot/skills/mémoire/orchestration, aucun parcours partagé Honcho et aucun niveau opérationnel ne sont prouvés.

## Ledger exhaustif

Les **56 claims acceptés** et leurs locators sont séparés : [ouvrir le ledger](claims.md).

## Couverture

- **expected :** 6 sessions Hermes + statut ourmem
- **inspected :** 6
- **excluded :** 0
- **blocked :** 3
- **sessions :**
- 20260819_191819_626eec
- 20260825_175948_c37c83
- 20260825_194053_5f380f
- 20260826_192853_171fd3
- 20260827_130813_2c311f
- 20260827_154335_c51ad8
- **claims_inspected :** 59
- **claims_unique :** 59
- **claims_accepted :** 56
- **claims_rejected :** 3
- **ourmem :**
- **queries_expected :** 3
- **queries_inspected :** 3
- **queries_blocked :** 3
- **results_returned :** 0
- **limit :** Le blocage daté ne prouve ni absence de souvenirs ni état permanent du quota.

## Contradictions

### Élément 1

- **ids :**

- CLM-AUD-004-001
- CLM-AUD-004-002

- **meaning :** La première assimilation des Bots au gateway est corrigée par Bot Mode et les docs actuelles.

### Élément 2

- **ids :**

- CLM-AUD-004-200
- CLM-AUD-004-201

- **meaning :** La proposition skill+noyau sans Bot est recadrée par la demande utilisateur de reprendre besoins et conditions de réussite.

### Élément 3

- **ids :**

- CLM-AUD-004-205
- CLM-AUD-004-206

- **meaning :** L’ordre historique Bot puis Cron est rouvert ; aucun ordre de remplacement n’est accepté.

### Élément 4

- **ids :**

- CLM-AUD-004-401
- CLM-AUD-004-402

- **meaning :** La recommandation Hindsight est remplacée par la préférence utilisateur Honcho ; CLM-AUD-004-401 reste rejeté.

### Élément 5

- **ids :**

- CLM-AUD-004-414
- direct-live-check

- **meaning :** `Privé d’abord` est une décision historique ; le README live rapporte GitHub Pages public actif et une politique à réconcilier.

### Élément 6

- **ids :**

- CLM-AUD-004-415
- CLM-AUD-004-419
- CLM-AUD-004-421

- **meaning :** Checkpoint historique sans remote et sans audit intégré versus dépôt live avec origin/main, AUD-001 et commits CI/Pages.

### Élément 7

- **ids :**

- CLM-AUD-004-405
- official-docs-memory-exception

- **meaning :** Memory Providers décrit l’externe comme additif ; Persistent Memory documente aussi la désactivation complète possible de MEMORY.md/USER.md.

## Inconnues

- Cible acceptée pour Jarvis, Hermes, Bot Mode, skills, mémoire et orchestration.
- Déploiement Honcho réellement actif et parcours partagé Hermes→OpenCode→ChatGPT Web.
- Fonctionnalités Hermes documentées réellement activées et exercées sur l’installation locale.
- Bot Hermes, Bot Chat et Cron Clarify exercés sur un cas réel borné.
- Contenu ourmem pertinent : les trois recherches ont échoué avant résultat ; aucune absence de souvenirs n’est déduite.
- État opérationnel réel de Pages et réconciliation de la politique de confidentialité ; aucun healthcheck distant n’était autorisé.
- Tests Clarify et Daily Brief historiquement rapportés non relancés dans cet audit.

## Niveaux de livraison

- **product_documentation :** `current_canon` seulement ; activation locale non prouvée
- **historical_mutations :** `historical_execution` datée
- **technically_tested :** historique seulement lorsque rapporté ; aucun test relancé
- **integrated :** AUD-001 intégré dans le dépôt live uniquement ; cela ne prouve pas l’écosystème opérationnel
- **exercised_real_case :** non démontré pour Bot/Cron/Clarify
- **user_accepted :** décisions ponctuelles seulement ; cible globale non acceptée
- **operational :** non démontré

## Santé des sources

### Élément 1

- **source_id :** SRC-HERMES

- **status :** healthy_for_closed_corpus

- **coverage :** 6/6 sessions ; fins réelles 47853, 48231, 52675, 51173, 52970 et 53429 contrôlées

### Élément 2

- **source_id :** SRC-HERMES-OFFICIAL-DOCS

- **status :** checked_current

- **coverage :** 13 claims produit contrôlés, 12 retenus, 1 rejeté

### Élément 3

- **source_id :** SRC-OURMEM

- **status :** blocked

- **attempts :** 3

- **reason :** échec de recherche 500 avec embedding sous-jacent HTTP 403 ; aucune mémoire brute lue

### Élément 4

- **source_id :** SRC-LIVE

- **status :** checked_read_only

- **observation :** sofian-ecosystem : main suit origin/main ; AUD-001 et commits CI/Pages observés dans l’historique

## Vérifications directes

- Socle projet, modèle de preuve, registre, protocoles, brief AUD-004 et références Guide 01/07/08 lus.
- 59 claims parents inventoriés en SQLite read-only ; 56 IDs retenus uniques, 3 rejetés, 13 champs canoniques par claim et 0 mauvais compte de champs.
- 6/6 sessions relues aux locators structurants et fins réelles contrôlées par les reviews parents.
- 13/13 claims produit confrontés aux docs Hermes actuelles ; 12 acceptés et CLM-AUD-004-405 rejeté.
- Contrat Clarify et TaskNote relus en live par R1 ; Git du dépôt contrôlé en lecture seule par R1/R2.
- Trois recherches ourmem bornées exécutées ; aucune lecture brute, aucun contournement et aucun résultat mémoire affiché.
- Aucun test, build, déploiement, healthcheck distant, commit, push, fichier, mémoire ou configuration modifié par cette synthèse.

## Provenance Kanban

- Synthèse : `t_1e313379` / run `63`.
- Mutations des sources : `0`.
- Intégration au dépôt : oui, après validation explicite de Sofian.
- Aucune cible d’architecture n’est acceptée par ce rapport.
