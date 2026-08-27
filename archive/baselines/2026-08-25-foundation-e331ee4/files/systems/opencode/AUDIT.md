---
status: active
date: 2026-08-25
scope: Audit factuel d’OpenCode et de son historique
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Audit d’OpenCode

## Faits vérifiés

- la base canonique des conversations est `SRC-OPENCODE` ;
- OpenChamber est principalement une interface et des métadonnées de session ;
- un index FTS local dérivé permet la recherche sans écrire dans la base canonique ;
- l’ancien moteur Daily Brief réside encore dans une skill OpenCode et passe 81 tests ;
- plusieurs architectures Jarvis historiques proviennent de ce contexte ;
- Sofian a explicitement demandé de ne pas classer OpenCode comme obsolète.

## Limites

- l’existence d’une ancienne session ne prouve pas qu’une décision reste active ;
- la base peut contenir du raisonnement ou des données sensibles ;
- aucune migration brute dans ce projet n’est autorisée.

## Source principale

`SRC-OPENCODE` en lecture seule et `SRC-DAILY`.
