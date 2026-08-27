---
id: AUD-003
title: OpenCode et OpenChamber
status: brief_ready
date: 2026-08-27
owner: Jarvis
role: worker
period: 2026-06-10..2026-08-26
expected_count: relevant_sessions_discovered_from_1609
candidate_cap: 30
output_path: none
source_ids:
  - SRC-OPENCODE
---

# AUD-003 — OpenCode / OpenChamber

## Mission unique

Retrouver les sessions OpenCode/OpenChamber qui ont conçu, modifié, testé ou contesté Sofian OS, Jarvis et Sofian Ecosystem, puis produire une chronologie des décisions, réalisations, échecs et boucles ouvertes.

## Source et helper exacts

- base canonique : `/Users/sofian/.local/share/opencode/opencode.db` ;
- helper : `/Users/sofian/.hermes/skills/migration/opencode-history/scripts/opencode_history.py` ;
- index dérivé : `/Users/sofian/Data/imports/hermes/opencode-history/opencode-index.db`.

La base source est ouverte uniquement en lecture. L’index était stale : 1 601 sessions indexées contre 1 609 dans la source. Ne pas le reconstruire dans ce workstream.

## Périmètre

- période : première session source du 2026-06-10 jusqu’au 2026-08-26 inclus ;
- discovery : six requêtes initiales, maximum dix candidats chacune ;
- déduplication par `session_id` ;
- maximum trente sessions ouvertes profondément ;
- priorité aux directories `Sofian-OS`, `jarvis`, `Homelab-OS` et aux noms exacts découverts par AUD-001/AUD-002.

## Requêtes initiales

`Sofian OS`, `Notion Obsidian`, `Jarvis`, `Sofian Ecosystem`, `vault migration`, `TaskNotes`.

## Questions

1. Quelles décisions ont été explicitement demandées ou confirmées par Sofian ?
2. Quels fichiers, skills, prototypes et tests ont réellement été produits ?
3. Quels composants ont été seulement proposés ?
4. Quelles corrections ont invalidé des conclusions antérieures ?
5. Comment les noms et responsabilités de Jarvis/OpenCode ont-ils évolué ?
6. Quelles boucles sont encore ouvertes aujourd’hui ?

## Méthode et skills

Socle obligatoire + `opencode-history`, `cross-agent-session-handoff`, `personal-system-reconciliation` et `grounded-citations`.

1. exécuter `stats` ;
2. rechercher les six termes ;
3. dédupliquer et classer les candidats ;
4. ouvrir les sessions pertinentes sans tools par défaut ;
5. vérifier les fichiers ou états live cités ;
6. citer ID, titre, date et directory ;
7. ne jamais exporter le raisonnement caché.

## Exclusions

- sessions hors période ;
- résultats thématiques sans lien direct au chantier ;
- tool payloads, sauf preuve manquante explicitement nécessaire ;
- reconstruction de l’index ;
- import dans Hermes.

## Sortie

Utiliser `templates/audit-report.md` et retourner le rapport dans la session. Aucune écriture dans le dépôt par défaut.

## Niveau de détail

Un claim par décision/réalisation/correction ; liste exhaustive des sessions retenues et rejetées avec raison courte ; verdict synthétique.

## Definition of Done

- [ ] stats et statut d’index enregistrés ;
- [ ] six requêtes exécutées ;
- [ ] candidats dédupliqués et dénominateur déclaré ;
- [ ] sessions pertinentes ordonnées et citées ;
- [ ] décisions, réalisations et échecs séparés ;
- [ ] claims live revérifiés ;
- [ ] corrections utilisateur propagées ;
- [ ] base source inchangée.
