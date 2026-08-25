---
status: active
date: 2026-08-25
scope: Audit factuel de Homelab-OS
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Audit de Homelab-OS

## Faits vérifiés

- `SRC-HOMELAB` contient la configuration et la documentation canoniques ;
- n8n y est documenté avec PostgreSQL, Caddy et exposition bornée de webhooks ;
- les données n8n et secrets sont décrits hors Git ;
- aucun export de workflow Jarvis Mail/iOS n’a été trouvé dans Homelab-OS ;
- des exports n8n spécialisés existent dans d’autres repos, sans constituer Jarvis ;
- Finance OS est déployé comme système spécialisé.

## Limites

- la documentation désirée ne prouve pas l’état live ;
- le runtime n’a pas été réaudité exhaustivement pour ce projet ;
- aucun secret ni configuration sensible n’est reproduit ici.

## Source principale

`SRC-HOMELAB`.
