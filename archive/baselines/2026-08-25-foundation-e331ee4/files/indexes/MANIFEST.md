---
status: active
date: 2026-08-25
scope: Manifeste exhaustif des fichiers du projet documentaire
sources:
  - ../README.md
  - MIGRATION-LOG.md
---

# Manifeste

## Résumé

- **73 fichiers** présents dans le projet ;
- **12 payloads copiés byte-for-byte** : trois HTML et neuf blobs Markdown historiques ;
- **0 fichier source déplacé, renommé ou supprimé** ;
- **0 dépôt Git initialisé** ;
- les sources externes restent décrites dans [SOURCE-MAP.md](SOURCE-MAP.md).

## Fichiers présents

### Registres racine

- `CHANGELOG.md`
- `DECISIONS.md`
- `README.md`
- `SYSTEMS.md`

### Index

- `indexes/ARTIFACTS.md`
- `indexes/CONTRADICTIONS.md`
- `indexes/MANIFEST.md`
- `indexes/MIGRATION-LOG.md`
- `indexes/SOURCE-MAP.md`

### Systèmes

- `systems/finance-os/ARCHITECTURE.md`
- `systems/finance-os/AUDIT.md`
- `systems/finance-os/README.md`
- `systems/finance-os/STATUS.md`
- `systems/hermes/ARCHITECTURE.md`
- `systems/hermes/AUDIT.md`
- `systems/hermes/README.md`
- `systems/hermes/STATUS.md`
- `systems/homelab-os/ARCHITECTURE.md`
- `systems/homelab-os/AUDIT.md`
- `systems/homelab-os/README.md`
- `systems/homelab-os/STATUS.md`
- `systems/jarvis/ARCHITECTURE.md`
- `systems/jarvis/AUDIT.md`
- `systems/jarvis/README.md`
- `systems/jarvis/STATUS.md`
- `systems/opencode/ARCHITECTURE.md`
- `systems/opencode/AUDIT.md`
- `systems/opencode/README.md`
- `systems/opencode/STATUS.md`
- `systems/ourmem/ARCHITECTURE.md`
- `systems/ourmem/AUDIT.md`
- `systems/ourmem/README.md`
- `systems/ourmem/STATUS.md`
- `systems/sofian-os/ARCHITECTURE.md`
- `systems/sofian-os/AUDIT.md`
- `systems/sofian-os/README.md`
- `systems/sofian-os/STATUS.md`
- `systems/tasknotes/ARCHITECTURE.md`
- `systems/tasknotes/AUDIT.md`
- `systems/tasknotes/README.md`
- `systems/tasknotes/STATUS.md`

### Workflows

- `workflows/daily-review.md`
- `workflows/daily-start.md`
- `workflows/inbox-processing.md`
- `workflows/ios-capture.md`
- `workflows/mail-to-task.md`

### Décisions

- `decisions/0001-canonical-authorities.md`
- `decisions/0002-jarvis-orchestration-layer.md`
- `decisions/0003-human-approved-mutations.md`
- `decisions/0004-needs-first-vertical-slices.md`
- `decisions/0005-hermes-current-runtime.md`
- `decisions/0006-defer-speculative-infrastructure.md`
- `decisions/0007-first-functional-increment.md`

### Artefacts actifs

- `artifacts/README.md`
- `artifacts/maps/README.md`
- `artifacts/maps/architecture-level-0.html`
- `artifacts/maps/capabilities.html`

### Archive

- `archive/README.md`
- `archive/artifacts/README.md`
- `archive/artifacts/disputed/README.md`
- `archive/artifacts/disputed/systems-and-authorities.html`
- `archive/decisions/README.md`
- `archive/documents/README.md`
- `archive/documents/obsidian-snapshot-43b0964/README.md`
- `archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis Agent.md`
- `archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis — Socle v0.1.md`
- `archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Architecture Niveau 0.md`
- `archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Capacités Transverses.md`
- `archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Systèmes et Autorité des Faits.md`
- `archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Tasks/Jarvis Socle v0.1 - Construire le brief en lecture seule.md`
- `archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Tasks/Jarvis Socle v0.1 - Spécifier le contrat du brief.md`
- `archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Tasks/Jarvis Socle v0.1 - Tester trois scénarios réels.md`
- `archive/documents/obsidian-snapshot-43b0964/files/99-System/AI Handoffs/Sofian Ecosystem Architecture.md`

## Éléments non migrés

- prototype de code `SRC-JARVIS-REPO` : référencé comme workspace autonome ;
- historique et base OpenCode : jamais copiés ;
- moteur Daily Brief : référencé à son emplacement ;
- harness JSDOM temporaire : absent, `[À CONFIRMER]`.

## Règle de mise à jour

Toute création, copie ou opération d’archivage future doit mettre à jour ce manifeste et [MIGRATION-LOG.md](MIGRATION-LOG.md) dans le même lot.
