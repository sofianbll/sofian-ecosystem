---
status: provisional
date: 2026-08-25
scope: Parcours de clôture et réalignement quotidien
sources:
  - ../indexes/SOURCE-MAP.md
  - ../systems/jarvis/AUDIT.md
  - ../systems/sofian-os/AUDIT.md
---

# Daily Review

## Besoin

Clôturer la journée, rendre les boucles visibles et préparer demain sans relire tout le système.

## Parcours cible

```text
Faits de la journée → tâches et attentes → écarts / preuves manquantes
                   → clôture / replanification → 3 priorités maximum
```

## Existant réutilisable

- routines documentées dans Sofian OS ;
- ancien moteur `SRC-DAILY` avec 81 tests passants ;
- lecture bornée de TaskNotes et certaines sources locales.

## État

**Composant partiel testé, parcours intégré non livré.** Aucun brief réel complet n’a été exécuté et accepté pendant la réconciliation. Le préflight le plus récent était partiel car ActivityWatch était indisponible.

## Garde-fous

- couverture des sources affichée ;
- indisponibilité jamais interprétée comme vide ;
- propositions séparées des mutations ;
- aucune opération Mail ou vault implicite.

## Manques

Orchestration Hermes, sortie validée par Sofian et trois scénarios réels rejouables.
