---
status: active
date: 2026-08-25
scope: Définition et responsabilité de Homelab-OS
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Homelab-OS

Homelab-OS décrit la configuration désirée, la reconstruction et les procédures d’exploitation du homelab de Sofian.

## Responsabilités

- stacks, réseaux, volumes et proxy attendus ;
- documentation des services ;
- procédures de déploiement et de reprise ;
- emplacements autorisés pour données et secrets hors Git.

## Hors périmètre

Héberger une application ne donne pas à Homelab-OS l’autorité sur ses faits métier. L’état réellement actif appartient au runtime observé.

## Dépendances

Hôtes et runtime Docker, applications spécialisées, stockage local et configuration réseau.

Voir [l’audit](AUDIT.md), [l’architecture](ARCHITECTURE.md) et [l’état](STATUS.md).
