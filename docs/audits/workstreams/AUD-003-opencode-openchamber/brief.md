---
id: AUD-003
title: OpenCode et OpenChamber
status: brief_ready
date: 2026-08-27
owner: Jarvis
output_path: none
source_ids:
  - SRC-OPENCODE
---

# AUD-003 — OpenCode / OpenChamber

## Mission unique

Retrouver les sessions OpenCode/OpenChamber qui ont conçu, modifié, testé ou contesté Sofian OS, Jarvis et Sofian Ecosystem, puis produire une chronologie des décisions, réalisations, échecs et boucles ouvertes.

## Source canonique

`/Users/sofian/.local/share/opencode/opencode.db`, ouverte uniquement en lecture via le helper du skill `opencode-history`.

L’index `/Users/sofian/Data/imports/hermes/opencode-history/opencode-index.db` est dérivé et était stale au cadrage : 1 601 sessions indexées contre 1 609 dans la source. Ne pas le reconstruire sans lot autorisé ; utiliser le snapshot pour discovery et la base read-only pour vérifier les sessions décisives.

## Questions

1. Quelles sessions concernent réellement Sofian OS, Jarvis, la migration Notion/Obsidian et l’écosystème ?
2. Quelles décisions ont été explicitement demandées ou confirmées par Sofian ?
3. Quels fichiers, skills, prototypes et tests ont réellement été produits ?
4. Quels composants ont été seulement proposés ?
5. Quelles corrections ou changements de direction ont invalidé des conclusions antérieures ?
6. Comment les noms et responsabilités de Jarvis/OpenCode ont-ils évolué ?
7. Quelles boucles sont encore ouvertes aujourd’hui ?

## Méthode et skills

Charger le socle obligatoire du dépôt, puis `opencode-history`, `cross-agent-session-handoff`, `personal-system-reconciliation` et `grounded-citations`.

1. exécuter `stats` ;
2. chercher 2–4 termes forts à la fois ;
3. limiter à dix candidats par recherche ;
4. filtrer par directory et date ;
5. ouvrir les sessions exactes sans tool payloads par défaut ;
6. vérifier les fichiers ou états live cités ;
7. citer ID, titre, date et directory ;
8. ne jamais exporter le raisonnement caché.

## Requêtes initiales

- `Sofian OS`
- `Notion Obsidian`
- `Jarvis`
- `Sofian Ecosystem`
- `vault migration`
- noms exacts découverts par AUD-001/AUD-002

## Interdictions

- aucune écriture, vacuum ou migration de la base ;
- aucun import dans le profil Hermes par défaut ;
- aucun dump de transcript ;
- aucun token ou configuration OpenChamber ;
- aucun statut actuel déduit d’une session historique.

## Sortie

Utiliser `templates/audit-report.md` et retourner le rapport dans la session. Aucune écriture dans le dépôt par défaut.

## Definition of Done

- [ ] espace de recherche et dénominateur documentés ;
- [ ] sessions pertinentes ordonnées et citées ;
- [ ] décisions, réalisations et échecs séparés ;
- [ ] claims live revérifiés dans leurs sources ;
- [ ] corrections utilisateur propagées ;
- [ ] responsabilités futures laissées ouvertes si non décidées ;
- [ ] base source inchangée.
