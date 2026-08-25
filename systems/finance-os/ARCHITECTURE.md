---
status: provisional
date: 2026-08-25
scope: Architecture et frontières de Finance OS
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Architecture de Finance OS

## Flux démontré

```text
Fichier ou source bancaire → import → transaction normalisée
                           → cashflow / index documentaire
```

## Autorités

- source bancaire ou document original : preuve primaire ;
- Finance OS : état normalisé et persistant de ce qui a été importé ;
- dashboard : projection ;
- Jarvis : lecteur ou assistant, sans autorité financière propre.

## Interfaces

L’implémentation et le déploiement résident dans `SRC-FINANCE` et `SRC-HOMELAB`. Les contrats API exacts n’ont pas été intégralement documentés dans cette conversation : `[À CONFIRMER]`.

Le cycle commercial complet ne doit pas être ajouté sans besoin et source canonique démontrés.
