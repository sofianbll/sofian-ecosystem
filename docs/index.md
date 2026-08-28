---
title: Accueil
description: Base auditée de reconstruction et de conception de Sofian Ecosystem.
status: active
date: 2026-08-27
---

# Sofian Ecosystem

> **État : six audits intégrés, état actuel encore non accepté.** Les sept dossiers système restent `reported` ; aucune cible n’est acceptée.

## Je veux…

### Comprendre ce projet

- [Charte](project/charter.md)
- [Scope complet](project/scope.md)
- [Mode opératoire](project/operating-model.md)
- [Roadmap](project/roadmap.md)

### Auditer une source ou un système

- [Catalogue des audits](audits/catalog.md)
- [Registre des sources](audits/source-registry.md)
- [Modèle de preuve](audits/evidence-model.md)
- [Protocole subagents](operations/subagent-protocol.md)

### Construire la cible

- [Besoins](needs/README.md)
- [Architecture actuelle](architecture/as-is.md)
- [Cibles candidates](architecture/target-candidates.md)
- [Cible acceptée](architecture/target-accepted.md)
- [Transition](architecture/transition.md)

## Progression logique

```mermaid
flowchart LR
    A[Sources] --> B[Audits]
    B --> C[État réconcilié]
    C --> D[Besoins]
    D --> E[Capacités]
    E --> F[Options]
    F --> G[Cible proposée]
    G --> H{Validation Sofian}
    H -->|corriger| D
    H -->|accepter| I[Roadmap]
```

Lecture : les sources sont auditées avant de décrire l’état ; la cible ne devient réelle qu’après validation de Sofian.
