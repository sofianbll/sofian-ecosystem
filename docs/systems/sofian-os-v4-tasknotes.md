---
name: "Sofian OS V4 + TaskNotes"
system_id: SYS-001
status: current_or_historical_as_reported
audit_state: reported
date: 2026-08-28
source_ids: [SRC-OBS-ACTIVE, SRC-LIVE]
---

# Sofian OS V4 + TaskNotes

> **État : dossier `reported`, non accepté comme cible.** Il décrit uniquement ce qu’AUD-005 a pu prouver.

## Verdict

Système personnel documenté avec Obsidian comme implémentation actuelle et TaskNotes comme autorité déclarée des tâches. Le vault actif suit `origin/main` et contient des changements utilisateur courants, sans suffire à prouver l’exécution complète des routines, leur acceptation ou leur maintien opérationnel.

## Autorité des faits

### Élément 1

- **fact :** état des tâches

- **authority :** TaskNotes / notes Markdown sous 98-Backend/Tasks

- **correction :** commandes TaskNotes Create, Schedule, Start, Complete, Drop, Reschedule

### Élément 2

- **fact :** règles V4

- **authority :** Architecture Référence et Workflows

- **correction :** source documentaire après décision

### Élément 3

- **fact :** vues

- **authority :** Queries/Bases/Dashboards comme projections

- **correction :** corriger la note/commande autoritaire, pas la vue

## Frontières

- **owns :**
- règles documentaires V4
- état des tâches dans les notes TaskNotes
- routines et commandes documentées
- **does_not_own :**
- preuve d’usage
- runtime Obsidian/TaskNotes/Bases
- tokens ou données sensibles de tasknotes/data.json

## Contrats et dépendances

- Capture → Clarify → Task/Project/Resource/Aspiration
- Commands modifient ; Queries/Dashboards lisent
- Operating routines → commandes TaskNotes

## Permissions et risques

- tasknotes/data.json exclu car sensible
- mapping réel, divergence de projections et récupération non vérifiés

## État live et livraison

- **verified :**
- documentation V4, schéma, workflows et routines lisibles
- identité du vault actif et autorité TaskNotes confirmées le 2026-08-28
- **not_proven :**
- prototyped
- technically_tested
- integrated
- exercised_real_case
- user_accepted
- operational

## Contradictions

- scheduled_date optionnel versus défaut today
- finished_date versus completed_date

## Inconnues

- conformité du runtime aux règles
- usage des routines
- procédure de correction d’une projection

## Provenance

- Source : `AUD-005`, dossier `SYS-001`, carte `t_ae316e9a`.
- Claims acceptés : `30`.
- Niveau maximal : aucune promotion globale vers `user_accepted` ou `operational`.
