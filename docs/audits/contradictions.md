---
title: Contradictions
status: seeded
date: 2026-08-27
---

# Contradictions et corrections

## Ouvertes

| ID | Contradiction | Impact | Résolution attendue |
|---|---|---|---|
| `CON-001` | priorité historique successivement décrite comme Brief, Mail, Daily Start puis Clarify | risque de reprendre le mauvais build | reconstruire les décisions et demander un besoin actuel |
| `CON-002` | documents déclarant une validation alors que Sofian a ensuite contesté le rythme ou la direction | faux canon | retrouver les messages exacts et séparer persistance / acceptation |
| `CON-003` | noms `Jarvis`, `Jarvis Agent` et `Jarvis OS` employés à plusieurs niveaux | frontières fausses | audit d’identité et de responsabilités |
| `CON-004` | annonces agrégées de tests ou de livraison provenant de suites différentes | niveau de livraison gonflé | conserver chaque suite et chaque oracle séparément |
| `CON-005` | responsabilité future d’OpenCode | risque de le déclarer obsolète | garder `unresolved` jusqu’à décision de Sofian |

## Corrections déjà vérifiées

| ID | Affirmation erronée | Correction |
|---|---|---|
| `FIX-001` | StudioFlow n’aurait jamais été déployé | GitHub Action réussie et Pages public vérifiés le 2026-08-27 |
| `FIX-002` | aucun export Notion explicite retrouvé | conversion locale retrouvée avec 8 442 fichiers ; live Notion accessible |
| `FIX-003` | le dépôt initial n’aurait pas été initialisé en Git | commit `e331ee4…` existant ; affirmation archivée comme historique stale |

## Discipline

- conserver les deux lectures et leurs sources ;
- ne pas choisir par récence seule ;
- corriger les conclusions dépendantes ;
- enregistrer le verdict et la décision de Sofian ;
- ne jamais supprimer une contradiction pour embellir la documentation.
