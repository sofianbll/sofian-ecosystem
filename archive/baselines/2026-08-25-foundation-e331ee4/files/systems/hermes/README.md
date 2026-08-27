---
status: active
date: 2026-08-25
scope: Définition et responsabilité de Hermes
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Hermes

Hermes est le runtime et l’interface agentique actuels utilisés par Sofian. Il fournit les sessions, projets, outils, skills, jobs, mémoire agentique et connexions configurées.

## Responsabilités

- exécuter les conversations et appels d’outils ;
- conserver son historique et ses métadonnées ;
- orchestrer des sous-agents et jobs ;
- exposer Jarvis dans l’interface actuelle.

## Hors périmètre

Hermes ne possède pas l’état des tâches, projets, paiements ou obligations externes. Ses résumés et mémoires sont secondaires face aux sources directes.

## Dépendances

Sources locales, outils autorisés, [Jarvis](../jarvis/README.md), skills et services configurés.

Voir [l’audit](AUDIT.md), [l’architecture](ARCHITECTURE.md) et [l’état](STATUS.md).
