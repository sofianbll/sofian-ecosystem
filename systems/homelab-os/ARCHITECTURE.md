---
status: active
date: 2026-08-25
scope: Architecture de responsabilité de Homelab-OS
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Architecture de Homelab-OS

## Séparation essentielle

```text
Homelab-OS        → configuration désirée et reconstruction
Runtime technique → état observé maintenant
Application       → faits métier du service
```

## Composants pertinents

- dépôts de configuration ;
- stacks Docker ;
- reverse proxy et réseau ;
- volumes de données hors Git ;
- secrets hors Git ;
- documentation d’exploitation.

## Interface avec Jarvis

n8n peut devenir un adaptateur de webhook si un parcours manuel le justifie. Il n’est ni la fondation de Jarvis ni une source canonique de tâches ou projets.
