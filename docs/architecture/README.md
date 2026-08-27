---
title: Architecture
status: active
date: 2026-08-27
---

# Architecture

L’architecture est construite en quatre vues qui ne doivent jamais être confondues :

1. [État actuel](as-is.md) — uniquement ce qui est prouvé aujourd’hui ;
2. [Cibles candidates](target-candidates.md) — options comparées depuis les besoins ;
3. [Cible acceptée](target-accepted.md) — seulement les décisions explicites de Sofian ;
4. [Transition](transition.md) — chemin réversible entre actuel et accepté.

## Niveaux de vue

```text
L0 — domaines de vie et résultats
L1 — capacités transverses
L2 — systèmes, autorités et contrats
L3 — modules, adapters, runtimes et déploiement
```

Ne pas descendre d’un niveau pour masquer une ambiguïté du niveau courant.

## Critère d’une frontière système

Une frontière candidate doit montrer une valeur durable, un langage cohérent, des faits possédés, un cycle de vie, des invariants, des risques, des consommateurs et une raison de changer indépendamment. Sinon préférer un workflow, module ou adapter.
