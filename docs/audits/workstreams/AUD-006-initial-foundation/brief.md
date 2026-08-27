---
id: AUD-006
title: Fondation initiale sofian-ecosystem
status: brief_ready
date: 2026-08-27
owner: Jarvis
role: worker
period: snapshot_2026-08-25
expected_count: 73
output_path: none
source_ids:
  - SRC-BASELINE
  - SRC-HERMES
---

# AUD-006 — Fondation initiale

## Mission unique

Auditer la première fondation documentaire de `sofian-ecosystem`, identifier les claims solides, contestés ou stale, puis proposer ce qui mérite une réintégration dans le nouvel arbre actif.

## Sources exactes

- payloads : `archive/baselines/2026-08-25-foundation-e331ee4/files/` ;
- manifeste : `archive/baselines/2026-08-25-foundation-e331ee4/MANIFEST.sha256` ;
- métadonnées : `archive/baselines/2026-08-25-foundation-e331ee4/BASELINE.md` ;
- commit source : `e331ee4e0a1006f813cf89f3a5c6f6bb262d2d29` ;
- sessions de création/correction : `20260819_191819_626eec` et `20260825_175948_c37c83`.

Le dénominateur est 73 payloads. `BASELINE.md` et `MANIFEST.sha256` sont des sidecars, pas des payloads.

## Vérification préalable

Depuis `archive/baselines/2026-08-25-foundation-e331ee4/` :

```bash
shasum -a 256 -c MANIFEST.sha256
```

Depuis la racine du dépôt, comparer le commit aux payloads sans modifier Git. Un échec arrête l’audit.

## Questions

1. Quelles sources externes la fondation déclarait-elle ?
2. Quels systèmes et responsabilités étaient présentés comme actuels ?
3. Quelles décisions étaient acceptées, provisoires ou contestées ?
4. Quels workflows et composants avaient une preuve technique ?
5. Quels niveaux de livraison étaient gonflés ou agrégés ?
6. Quelles affirmations étaient déjà stale ?
7. Quels contenus doivent être réintégrés, rester archivés ou être remplacés ?

## Méthode et skills

Socle obligatoire + `personal-system-reconciliation`, `personal-filesystem-governance`, `cross-agent-session-handoff` et `grounded-citations`.

## Groupes de fichiers

1. quatre registres racine ;
2. cinq index ;
3. sept décisions ;
4. trente-deux documents des huit systèmes ;
5. cinq workflows ;
6. cartes HTML et README d’artefacts ;
7. snapshot Obsidian et métadonnées d’archive.

Compter chaque groupe et vérifier que le total dédupliqué reste 73.

## Exclusions

- sidecars hors dénominateur ;
- sources externes non nécessaires à la vérification d’un claim actuel ;
- toute modification de payload ;
- réintégration automatique.

## Sortie

Classer chaque artefact : `reintegrate_after_review`, `historical_only`, `disputed`, `superseded` avec remplacement, ou `unknown`. Retourner le rapport dans la session. Aucune écriture dans le dépôt par défaut.

## Niveau de détail

Inventaire exhaustif 73/73 en annexe de rapport ; chat limité au verdict et aux claims structurants.

## Definition of Done

- [ ] manifeste vérifié depuis le bon répertoire ;
- [ ] 73 payloads couverts par inventaire et groupes ;
- [ ] claims structurants vérifiés ou marqués ;
- [ ] décisions reliées aux messages utilisateur ;
- [ ] artefacts et tests classés ;
- [ ] plan de réintégration sans mutation automatique ;
- [ ] baseline inchangée.
