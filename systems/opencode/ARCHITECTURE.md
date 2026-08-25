---
status: provisional
date: 2026-08-25
scope: Architecture d’usage d’OpenCode dans l’écosystème
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Architecture d’OpenCode

## Composants pertinents

- base SQLite canonique des sessions ;
- OpenChamber comme surface de consultation ;
- index FTS dérivé et jetable ;
- agents, skills et workspaces de développement ;
- moteur Daily Brief historique.

## Flux de reprise

```text
Question sur un ancien travail → recherche indexée
                              → session OpenCode exacte
                              → synthèse et vérification dans le repo actuel
```

## Interfaces futures

La coordination précise avec Hermes et Jarvis est `[À CONFIRMER]`. Le principe conservé est de consulter l’historique exact avant de demander à Sofian de répéter le contexte, sans dupliquer la base OpenCode.
