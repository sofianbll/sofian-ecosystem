---
status: active
date: 2026-08-25
scope: Audit factuel de Hermes
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Audit de Hermes

## Faits vérifiés

- Hermes est l’interface de cette conversation ;
- les capacités CLI et projets ont été vérifiées pendant le chantier ;
- un projet Hermes `Jarvis` a été créé et relié à `SRC-JARVIS-REPO` ;
- ce projet n’était plus actif lors de l’audit final ;
- la mémoire built-in et les sessions Hermes sont distinctes d’ourmem ;
- aucune connexion Gmail Hermes n’a été authentifiée pendant le chantier ;
- aucun cron Jarvis n’a été créé.

## Limites

- la disponibilité d’un outil ne prouve ni authentification ni permission ;
- les sorties de session compactées peuvent perdre des détails ;
- l’historique ne remplace pas l’état live d’une source externe.

## Source principale

`SRC-HERMES`, documentation officielle et historique `SRC-CONV`.
