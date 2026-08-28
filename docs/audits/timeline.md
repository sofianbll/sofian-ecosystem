---
title: Timeline reconstruite
status: active
date: 2026-08-27
---

# Timeline

> **Attention :** cette page intègre les ancres contre-vérifiées d’`AUD-001` à `AUD-006`. Elle conserve les périodes sans preuve et ne transforme pas les statuts documentaires en usage opérationnel.

| Date | Événement prouvé | État | Source |
|---|---|---|---|
| 2026-01-08 | création de la page Notion `Sofian OS` ; DOCX V2 daté du même jour | `historical_execution` | `SRC-NOTION-LIVE`, `SRC-DOCX-V2` |
| 2026-02-10 | présence filesystem observée de l’export local Notion → Markdown ; temps de conversion inconnu | `historical_execution` | `SRC-NOTION-EXPORT`, `CLM-AUD-001-005..007` |
| 2026-02-16 | date déclarée du plan de réorganisation du vault | `historical_intent` | `SRC-OBS-OLD` ; date Git ultérieure |
| 2026-05-04 | premier commit Git de l’ancien vault | `historical_execution` | `SRC-OBS-OLD`, commit `f0c0862…` |
| 2026-05-09 | ajout Git vérifié des synthèses V1, V2 et du cadrage V3 | `historical_execution` | `SRC-OBS-OLD`, commit `5ddc27b…` |
| 2026-05-09 | renommage Git R100 de `Sofian OS V3 - Architecture Système.md` vers `Sofian OS.md` et correction des liens projet V1/V2/V3 | `historical_execution` | `SRC-OBS-OLD`, `CLM-AUD-001-212,213,321,322` |
| 2026-05-13 | reformulation de la fiche projet de V3 vers V4 ; V1/V2/V3 sont consignés `Synthétisé`, V4 `En cours` | `historical_execution` | `SRC-OBS-OLD`, `CLM-AUD-001-215,218` |
| 2026-05-14 | premier enregistrement Git du journal V4 et de quatre rubriques datées du 14 mai | `historical_execution` | `SRC-OBS-OLD`, commit `2e63fa6…`, `CLM-AUD-001-315..319,323` |
| 2026-05-15 | correction documentaire : date et quatre rubriques V4 passent au 15 mai ; ajout de la documentation V4 par layers | `historical_execution` | `SRC-OBS-OLD`, `CLM-AUD-001-218,314,318,319,323` |
| 2026-05-16 | fin de la période `AUD-001` sans événement direct distinct dans son corpus fermé | `unknown` | `AUD-001` |
| 2026-05-16 | commit racine vérifié du vault actif `Sofian-OS`, hors corpus `AUD-001` | `historical_execution` | `SRC-OBS-ACTIVE`, commit `306ff1a…` |
| 2026-05-16 | décision documentée de créer un vault propre `Sofian-OS` et de conserver `Sofian's Vault` en lecture seule | `historical_execution` | `AUD-002`, `CLM-AUD-002-314,401,408` |
| 2026-05-18 | ajout sélectif de 13 notes V4 transformées dans `Sofian-OS`, puis ajout séparé du mapping Obsidian | `historical_execution` | `AUD-002`, `CLM-AUD-002-406,407` |
| 2026-06-10 | plus ancienne session présente dans la base OpenCode auditée | `historical_execution` | `SRC-OPENCODE` |
| 2026-06-27 | travail OpenCode explicite sur Jarvis Agent et ses skills | `historical_intent` | `SRC-OPENCODE` |
| 2026-08-19 | début du chantier Hermes retrouvé sur Sofian Ecosystem | `historical_execution` | `SRC-HERMES` |
| 2026-08-25 | premier commit du dépôt `sofian-ecosystem` | `historical_execution` | `SRC-BASELINE`, commit `e331ee4…` |
| 2026-08-27 | baseline archivée et nouveau système d’audit autorisé | `user_decision` | conversation Hermes courante, commit `e090180…` |
| 2026-08-28 | intégration documentaire des audits `AUD-002` à `AUD-006` après cinq synthèses contre-auditées | `historical_execution` | rapports intégrés ; aucune mutation des sources externes |
| 2026-08-28 | dépôt, CI et GitHub Pages publics explicitement acceptés pour l’instant | `user_decision` | `SRC-HERMES`, session `145c806b6027`, locator `63985` |
| 2026-08-28 | réconciliation live : Finance OS joignable, Hermes sur Honcho avec gateway supervisé, OpenCode stale 1601/1609, ourmem lisible hors recherche | `live_implementation` | `SRC-LIVE`, `SRC-HERMES`, `SRC-OPENCODE`, `SRC-OURMEM` |

## Limites encore ouvertes

- l’index OpenCode reste stale et 24 IDs hors cap ne sont pas individualisés ;
- trois recherches ourmem n’ont retourné aucun résultat ;
- les dates documentaires, Git et de validation restent séparées ;
- aucune continuité globale Notion → vaults → runtimes n’est inférée sans locator direct.
