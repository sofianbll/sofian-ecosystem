---
status: active
date: 2026-08-25
scope: Audit factuel de ourmem
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Audit de ourmem

## Faits vérifiés

- le service est auto-hébergé localement dans Docker ;
- le stockage est sous `/Users/sofian/Data/appdata/omem` ;
- la configuration canonique réside dans Homelab-OS et les dotfiles ;
- Hermes y accède via le MCP `ourmem` ;
- lors d’un audit antérieur, le fournisseur mémoire Hermes actif n’était pas ourmem.

## Limites

- les souvenirs peuvent être incomplets ou périmés ;
- la mémoire sémantique est une piste à vérifier, pas une source directe ;
- aucun contrat détaillé Jarvis Memory n’est validé ;
- aucun contenu de mémoire n’est copié dans ce projet.

## Sources

`SRC-OURMEM`, `SRC-HOMELAB` et `SRC-HERMES`.
