---
status: active
date: 2026-08-25
scope: Décision sur Hermes comme runtime actuel
sources:
  - ../indexes/SOURCE-MAP.md
  - ../systems/hermes/README.md
  - ../systems/opencode/STATUS.md
---

# 0005 — Hermes comme runtime actuel

## Contexte

Jarvis doit être accessible depuis l’interface utilisée au quotidien. Hermes fournit les sessions, outils, skills et projets actuels, tandis qu’OpenCode reste disponible pour d’autres usages.

## Décision

Utiliser Hermes comme runtime et interface actuels de Jarvis.

## Justification

Hermes est déjà l’interface centrale de Sofian et peut consulter les sources sans créer un nouveau cockpit.

## Conséquences

- les parcours Jarvis seront exercés d’abord dans Hermes ;
- OpenCode reste conservé pour un usage futur ;
- la répartition future Hermes/OpenCode est `[À CONFIRMER]` ;
- aucun système n’est qualifié d’obsolète par cette décision.

## Statut

**Active** pour l’interface actuelle. Le rôle futur d’OpenCode reste ouvert.
