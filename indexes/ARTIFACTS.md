---
status: active
date: 2026-08-25
scope: Index des artefacts produits pendant le chantier
sources:
  - SOURCE-MAP.md
  - ../artifacts/maps/README.md
  - ../archive/artifacts/disputed/README.md
---

# Index des artefacts

## Artefacts importés

| Artefact | Source | Copie locale | Statut | SHA-256 |
|---|---|---|---|---|
| Carte Niveau 0 | `SRC-ARTIFACTS/Sofian Ecosystem - Carte Niveau 0.html` | [architecture-level-0.html](../artifacts/maps/architecture-level-0.html) | Actif | `3af1f2e2a281befd1d3c47f6148cbbaf58203f73a52531e4b25d0eb81b69f0e9` |
| Carte des capacités | `SRC-ARTIFACTS/Sofian Ecosystem - Carte des Capacités.html` | [capabilities.html](../artifacts/maps/capabilities.html) | Actif | `979a897e0c672707f77aae0930145435ac1bca949bd3d680ff797935327ca26c` |
| Carte des systèmes et autorités | `SRC-ARTIFACTS/Sofian Ecosystem - Carte des Systèmes et Autorité des Faits.html` | [systems-and-authorities.html](../archive/artifacts/disputed/systems-and-authorities.html) | **Disputed / archivé** | `fd3b1f37d56feb8de620e496f38961364c542c230090b687c1c13aaebc6a5486` |

Les trois copies sont byte-for-byte. Les originaux restent intacts. Les métadonnées détaillées résident dans les README voisins.

## Éléments référencés seulement

| Élément | Provenance | Statut | Remarque |
|---|---|---|---|
| Harness JSDOM Autorité | Ancien `/tmp/sofian-ownership-test/test.mjs` | Perdu / `[À CONFIRMER]` | Non archivé ; historique contradictoire entre 49 et 50 assertions |
| Prototype Mail sur fixture | `SRC-JARVIS-REPO` | Provisional | Deux tests passent ; aucun mail réel |
| Ancien moteur Daily Brief | `SRC-DAILY` | Actif comme composant réutilisable | 81 tests passent ; intégration quotidienne non livrée |

## Règle

Toute future copie physique exige un hash, une provenance, un statut, une date d’import et un contrôle de collision. Copier ne constitue ni une déduplication ni une validation du contenu.
