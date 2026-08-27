---
status: active
date: 2026-08-25
scope: Audit factuel de TaskNotes
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Audit de TaskNotes

## Faits vérifiés

- les tâches sont des notes Markdown structurées dans `SRC-SOS` ;
- les statuts canoniques observés sont `todo`, `in_progress`, `paused`, `done` et `dropped` ;
- les priorités canoniques sont `low`, `medium` et `high` ;
- les TaskNotes sont utilisées par les revues et dashboards ;
- trois TaskNotes Jarvis ont été créées prématurément pendant la conversation.

## Limites

- les dates ou statuts peuvent devenir obsolètes ;
- les tâches terminées ne constituent pas seules une preuve externe ;
- la prévention de doublons pour une future création par Jarvis n’est pas construite ;
- le parseur du prototype Mail ne produit encore aucune TaskNote réelle.

## Source principale

`SRC-SOS` et les schémas TaskNotes référencés par `SRC-HANDOFF`.
