---
status: active
date: 2026-08-25
scope: Définition et responsabilité de Sofian OS
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Sofian OS

Sofian OS est le cockpit humain de Sofian. Il organise les projets, engagements, ressources, décisions et routines de revue enregistrés dans le vault canonique `SRC-SOS`.

## Responsabilités

- porter l’état enregistré des projets et engagements humains ;
- fournir les vues Inbox, Daily, Weekly et projets ;
- relier les actions TaskNotes au contexte durable ;
- conserver les décisions et ressources qualifiées.

## Hors périmètre

Sofian OS ne possède ni la vérité bancaire primaire, ni le runtime technique, ni les états internes des services externes. Jarvis et les dashboards restent des projections.

## Dépendances

- [TaskNotes](../tasknotes/README.md) pour l’état des tâches ;
- [Jarvis](../jarvis/README.md) comme orchestration envisagée ;
- services externes pour les faits qu’ils émettent.

Voir [l’audit](AUDIT.md), [l’architecture](ARCHITECTURE.md) et [l’état](STATUS.md).
