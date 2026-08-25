---
status: active
date: 2026-08-25
scope: Journal des opérations documentaires
sources:
  - MANIFEST.md
---

# Journal de migration

## 2026-08-25 — Migration physique autorisée

### Lot exécuté

| Groupe | Fichiers | Octets | Action |
|---|---:|---:|---|
| Cartes HTML actives | 2 | 68 310 | Copie byte-for-byte vers `artifacts/maps/` |
| Carte Autorité contestée | 1 | 52 670 | Copie byte-for-byte vers `archive/artifacts/disputed/` |
| Snapshot Obsidian `43b0964` | 9 | 65 105 | Extraction Git byte-for-byte vers `archive/documents/` |
| **Total** | **12** | **186 085** | **Copie vérifiée** |

### Provenance et vérification

- commit source complet : `43b0964d7bace22abf2cfad32baaf1b449889687` ;
- les neuf documents ont été lus avec `git show <commit>:<path>` ;
- les trois HTML ont été lus depuis `SRC-ARTIFACTS` ;
- SHA-256 source et destination identiques pour les 12 copies ;
- métadonnées ajoutées dans trois README voisins.

### Effets

- **copié :** 12 fichiers, 186 085 octets ;
- **créé pour provenance :** 3 README Markdown ;
- **déplacé :** rien ;
- **renommé à la source :** rien ;
- **supprimé :** rien ;
- **espace récupéré :** 0 octet ;
- **sources externes modifiées :** aucune ;
- **Git :** aucune initialisation, configuration, création de commit ou modification d’historique.

## 2026-08-25 — Création du projet documentaire

### Créé

- quatre registres racine ;
- cinq index ;
- 32 documents obligatoires pour huit systèmes ;
- cinq workflows ;
- sept décisions structurées ;
- registres des artefacts et archives.

**Total initial : 58 fichiers Markdown.**

### Effets initiaux

- **copié, déplacé, renommé, archivé ou supprimé :** rien ;
- **sources externes modifiées :** aucune ;
- **Git :** aucune opération.

## Opérations futures

Toute autre copie ou opération d’archivage exigera une autorisation distincte et enregistrera source, destination, hash, date, raison et remplaçant éventuel.
