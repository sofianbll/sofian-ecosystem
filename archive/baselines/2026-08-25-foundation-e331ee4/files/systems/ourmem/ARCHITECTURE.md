---
status: provisional
date: 2026-08-25
scope: Architecture et frontières de ourmem
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Architecture de ourmem

## Flux

```text
Conversation ou fait sélectionné → extraction → mémoire sémantique
                                           ↓
                              recherche → contexte secondaire
```

## Interfaces

- service ourmem auto-hébergé ;
- stockage persistant propre ;
- MCP utilisé par Hermes ;
- opérations explicites de recherche, ajout, mise à jour ou oubli.

## Frontière Jarvis

Jarvis peut consulter ourmem pour retrouver une piste. Il doit ensuite vérifier toute information actionnable dans Sofian OS, TaskNotes, l’historique exact ou la source externe. L’architecture complète de Jarvis Memory reste différée.
