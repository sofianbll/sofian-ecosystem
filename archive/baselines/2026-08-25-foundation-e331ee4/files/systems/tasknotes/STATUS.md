---
status: provisional
date: 2026-08-25
scope: État, limites et prochaines décisions de TaskNotes
sources:
  - ../../indexes/SOURCE-MAP.md
---

# État de TaskNotes

## État actuel

TaskNotes fonctionne comme système canonique des actions. Aucun connecteur Jarvis de création approuvée n’est livré.

## Risques

- création de doublons depuis Mail ou capture iOS ;
- frontmatter invalide ou incomplet ;
- tâche marquée terminée sans preuve externe ;
- priorités trop nombreuses ou périmées.

## Prochaines décisions

1. définir le contrat minimal d’une mutation Jarvis ;
2. choisir une clé d’idempotence et une stratégie de détection des doublons ;
3. tester création puis relecture sur une fixture avant une tâche réelle.

Aucune écriture automatique n’est autorisée actuellement.
