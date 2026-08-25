---
status: provisional
date: 2026-08-25
scope: État, limites et prochaines décisions de Homelab-OS
sources:
  - ../../indexes/SOURCE-MAP.md
---

# État de Homelab-OS

## État actuel

Le système de configuration existe et documente plusieurs services. Aucun workflow Jarvis dédié n’est démontré.

## Risques

- confondre infrastructure documentée et service réellement sain ;
- copier des secrets ou données runtime dans la documentation ;
- choisir n8n avant d’avoir stabilisé le parcours utilisateur ;
- dupliquer des workflows spécialisés entre repos.

## Prochaines décisions

Conserver n8n comme option d’adaptation. Un audit runtime ne sera utile que si le premier parcours Jarvis exige effectivement un webhook ou une exécution durable.
