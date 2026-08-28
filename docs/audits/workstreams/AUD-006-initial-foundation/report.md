---
id: AUD-006
title: Fondation initiale sofian-ecosystem — rapport d’audit
status: integrated
date: 2026-08-28
canonical_synthesis_task: t_3796a3fa
canonical_synthesis_run: 75
accepted_claims: 94
integration_authorized: true
---

# AUD-006 — Fondation initiale sofian-ecosystem

> **État : `integrated`, contre-audité.** Ce rapport et son ledger sont intégrés au dépôt après validation explicite de Sofian.

## Verdict

AUD-006 est synthétisé au statut `reported` avec inventaire exhaustif 73/73 : 24 payloads `reintegrate_after_review`, 34 `historical_only`, 7 `disputed` et 8 `superseded`. Le contrôle final retient 94/139 claims parents normalisés et en rejette 45 ; aucune preuve ne permet de promouvoir la fondation au-delà d’un historique documenté, et la normalisation des décisions G1–G3 reste la limite majeure avant intégration.

## Ledger exhaustif

Les **94 claims acceptés** et leurs locators sont séparés : [ouvrir le ledger](claims.md).

## Couverture

- **expected :**
- **payloads :** 73
- **manifest_entries :** 73
- **groups :**
- **root :** 4
- **indexes :** 5
- **decisions :** 7
- **systems :** 32
- **workflows :** 5
- **artifacts :** 7
- **archive :** 13
- **parent_claims :** 139
- **creation_sessions :** 2
- **reintegration_recommendations :** 30
- **inspected :**
- **payloads :** 73
- **manifest_entries :** 73
- **unique_manifest_paths :** 73
- **groups :**
- **root :** 4
- **indexes :** 5
- **decisions :** 7
- **systems :** 32
- **workflows :** 5
- **artifacts :** 7
- **archive :** 13
- **parent_claims :** 139
- **creation_sessions :**
- 20260819_191819_626eec
- 20260825_175948_c37c83
- **reintegration_recommendations :** 30
- **excluded :** 0
- **blocked :** 0

## Classification de la baseline

- **reintegrate_after_review :** 24
- **historical_only :** 34
- **disputed :** 7
- **superseded :** 8
- **unknown :** 0
- **total :** 73

## Plan de réintégration

- **status :** reported_not_integrated
- **validated_content_only_count :** 24
- **validated_content_only :**
- files/decisions/0002-jarvis-orchestration-layer.md
- files/decisions/0003-human-approved-mutations.md
- files/decisions/0004-needs-first-vertical-slices.md
- files/decisions/0005-hermes-current-runtime.md
- files/decisions/0006-defer-speculative-infrastructure.md
- files/systems/finance-os/ARCHITECTURE.md
- files/systems/finance-os/README.md
- files/systems/hermes/ARCHITECTURE.md
- files/systems/hermes/README.md
- files/systems/homelab-os/ARCHITECTURE.md
- files/systems/homelab-os/README.md
- files/systems/jarvis/README.md
- files/systems/opencode/ARCHITECTURE.md
- files/systems/opencode/README.md
- files/systems/ourmem/ARCHITECTURE.md
- files/systems/ourmem/README.md
- files/systems/sofian-os/ARCHITECTURE.md
- files/systems/sofian-os/README.md
- files/systems/tasknotes/ARCHITECTURE.md
- files/systems/tasknotes/README.md
- files/workflows/daily-review.md
- files/workflows/inbox-processing.md
- files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Architecture Niveau 0.md
- files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Capacités Transverses.md
- **rejected_or_reclassified_count :** 6
- **rejected_or_reclassified :**
- files/artifacts/README.md
- files/artifacts/maps/README.md
- files/artifacts/maps/architecture-level-0.html
- files/artifacts/maps/capabilities.html
- files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis — Socle v0.1.md
- files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Systèmes et Autorité des Faits.md
- **steps :**
- Réémettre d’abord les claims G1, G2 et G3 au contrat canonique avec locators utilisateur directs ; ne pas corriger la baseline.
- Extraire seulement le contenu des 24 candidats après revue de leurs canons actuels ; aucun payload copié tel quel.
- Conserver les projections HTML, tâches, handoffs, audits et statuts comme historique ; ne pas les promouvoir en état live.
- Soumettre toute intégration documentaire future à une gate distincte ; aucune TaskNote, source externe ou baseline n’est modifiée ici.

## Contradictions

### Élément 1

- **subject :** Autorités

- **historical :** Principe d’autorité par fait documenté et maintien des sources sans duplication accepté.

- **current_review :** La matrice complète reste disputée ; aucune carte globale acceptée n’est prouvée.

### Élément 2

- **subject :** Premier incrément

- **historical :** Brief, Mail et Daily Start étaient non réconciliés.

- **current_review :** La session exacte sélectionne `Clarify Inbox`; le choix ne prouve pas un parcours opérationnel.

### Élément 3

- **subject :** Niveaux de livraison

- **historical :** Certains payloads annoncent composants ou prototypes testés.

- **current_review :** Aucune sortie directe acceptée ne justifie `technically_tested`; niveau workflow limité à `documented`.

### Élément 4

- **subject :** Artefact Systèmes et Autorité

- **historical :** Le HTML affiche une validation.

- **current_review :** Le README voisin classe la validation comme contestée ; aucune fusion silencieuse.

### Élément 5

- **subject :** Jarvis/Hermes/OpenCode

- **historical :** Des payloads mélangent runtime Hermes, runner OpenCode et architecture future.

- **current_review :** Le partage futur reste inconnu ; aucune déduction live depuis le snapshot.

## Inconnues

- Acceptation actuelle des cartes Architecture Niveau 0 et Capacités Transverses.
- Writer TaskNotes/Jarvis et procédure de correction d’une projection en runtime.
- Usage maintenu du parcours Clarify, des routines Sofian OS, de Daily Review et des surfaces Hermes/OpenCode.
- Rôle futur de Mail, iOS Capture, Daily Start et OpenCode au-delà des décisions bornées.
- Aucun niveau global `user_accepted` ou `operational` n’est prouvé.
- Les 45 claims rejetés ne peuvent alimenter une intégration avant normalisation et nouvelle revue.

## Niveaux de livraison

- **baseline_payloads :** documented historical snapshot
- **accepted_claims :** historical_intent | historical_execution | contradicted, bornés à la date du snapshot
- **technically_tested :** not_accepted
- **integrated :** false
- **exercised_real_case :** not_proven
- **user_accepted :** not_proven
- **operational :** not_proven
- **report :** reported

## Santé des sources

### Élément 1

- **source_id :** SRC-BASELINE

- **status :** healthy_for_closed_snapshot

- **evidence :** MANIFEST.sha256 vérifié 73/73 ; 73 entrées uniques ; baseline sans diff.

- **limit :** Intégrité des octets, pas vérité métier, acceptation, usage ni état live.

### Élément 2

- **source_id :** SRC-HERMES

- **status :** direct_read_available_via_R2

- **evidence :** Les sessions 20260819_191819_626eec et 20260825_175948_c37c83 ont été relues en mode read-only pour les locators de décision.

- **limit :** Les décisions G3 restent exclues du claimset accepté tant que leur contrat V2 n’est pas réémis.

### Élément 3

- **source_id :** PARENT_CLAIM_METADATA

- **status :** partial_requires_normalization

- **evidence :** 139 claims contrôlés ; intersection R1/R2 de 94 records valides, 45 rejetés.

- **limit :** Les corps canoniques restent dans les cartes collectrices ; aucun nouveau claim créé par la synthèse.

### Élément 4

- **source_id :** AUD-005 S1 t_420c7653

- **status :** reported_reviewed_parent

- **evidence :** 7/7 dossiers live couverts et utilisés seulement par R2 pour confronter les assertions stale.

- **limit :** `reported` ne signifie ni `integrated`, ni `user_accepted`, ni `operational`.

## Vérifications directes

- README.md, AGENTS.md, scope, evidence-model, source-registry, protocoles et brief AUD-006 lus directement.
- Les 10 cartes parents ont été inspectées ; les sorties complètes spillover de R1, R2, G4, G5, G6 et G7 ont été relues sans réinterroger le board.
- `shasum -a 256 -c MANIFEST.sha256` exécuté depuis la racine de baseline : 73/73 OK.
- Le manifeste contient 73 entrées ; l’inventaire normalisé contient 73 payloads et les comptes 24+34+7+8=73.
- `git status --short --branch` : `## main...origin/main`; diff de la baseline vide.
- Contrôle jq des 94 claims retenus : 94 records matérialisables, 94 IDs uniques, 13 champs présents, `contradicts` tableau, aucune absence.
- Aucun test, build, healthcheck distant, service, appareil, mémoire, vault, TaskNote ou source externe n’a été muté.

## Provenance Kanban

- Synthèse : `t_3796a3fa` / run `75`.
- Mutations des sources : `0`.
- Intégration au dépôt : oui, après validation explicite de Sofian.
- Aucune cible d’architecture n’est acceptée par ce rapport.
