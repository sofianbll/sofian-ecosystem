---
status: active
date: 2026-08-25
scope: Décision sur l’autorisation et la vérification des mutations
sources:
  - ../indexes/SOURCE-MAP.md
---

# 0003 — Mutations approuvées et vérifiées

## Contexte

Les systèmes contiennent des tâches, mails, faits administratifs et données sensibles. Une mutation silencieuse peut créer une divergence ou une conséquence externe.

## Décision

Avant toute mutation, Jarvis annonce la cible, le changement et l’effet attendu, puis attend un accord exact. Après exécution, il relit la source canonique et vérifie le résultat.

## Justification

Sofian conserve la décision finale et les erreurs restent détectables.

## Conséquences

- lecture seule par défaut ;
- idempotence pour les mutations répétables ;
- aucune permission implicite d’archivage, d’envoi ou de suppression ;
- les actions sensibles exigent une preuve vérifiable.

## Statut

**Active.** Règle confirmée dans les instructions et le projet Jarvis.
