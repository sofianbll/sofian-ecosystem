---
id: AUD-006
title: Fondation initiale sofian-ecosystem
status: brief_ready
date: 2026-08-27
owner: Jarvis
output_path: none
source_ids:
  - SRC-BASELINE
  - SRC-HERMES
---

# AUD-006 — Fondation initiale

## Mission unique

Auditer la première fondation documentaire de `sofian-ecosystem`, comprendre quelles sources et décisions elle résumait, identifier les claims solides, contestés ou stale, puis proposer ce qui mérite une réintégration dans le nouvel arbre actif.

## Source immuable

`archive/baselines/2026-08-25-foundation-e331ee4/files/`

Provenance : commit `e331ee4e0a1006f813cf89f3a5c6f6bb262d2d29`, 73 fichiers vérifiés par `MANIFEST.sha256`.

## Méthode et skills

Charger le socle obligatoire du dépôt, puis `personal-system-reconciliation`, `personal-filesystem-governance`, `cross-agent-session-handoff` et `grounded-citations`.

## Questions

1. Quelles sources externes la fondation déclarait-elle ?
2. Quels systèmes et responsabilités étaient présentés comme actuels ?
3. Quelles décisions étaient réellement acceptées, provisoires ou contestées ?
4. Quels workflows et composants avaient une preuve technique ?
5. Quels niveaux de livraison étaient gonflés ou agrégés ?
6. Quelles affirmations sont devenues stale entre le document et l’état Git/live ?
7. Quels contenus doivent être réintégrés, rester archivés ou être remplacés ?

## Contrôles prioritaires

- README, SYSTEMS, DECISIONS et CHANGELOG ;
- source map, contradictions, manifeste et migration log ;
- sept décisions ;
- dossiers des huit systèmes ;
- cinq workflows ;
- cartes HTML et snapshot Obsidian ;
- sessions Hermes ayant créé, corrigé puis committé cette fondation.

## Règles

- Ne jamais modifier la baseline.
- Persistance et hash ne valident pas le contenu.
- Vérifier les claims actuels dans les sources live.
- Conserver séparément les cartes contestées.
- Ne pas agréger les suites de tests.
- Ne pas promouvoir un ancien premier incrément.

## Sortie

Classer chaque artefact :

- `reintegrate_after_review` ;
- `historical_only` ;
- `disputed` ;
- `superseded` avec remplacement ;
- `unknown`.

Retourner le rapport dans la session. Aucune écriture dans le dépôt par défaut.

## Definition of Done

- [ ] 73 fichiers couverts par inventaire et groupes ;
- [ ] claims structurants vérifiés ou marqués ;
- [ ] décisions reliées aux messages utilisateur ;
- [ ] artefacts et tests classés ;
- [ ] contradictions mises à jour ;
- [ ] plan de réintégration sans mutation automatique ;
- [ ] baseline inchangée et manifeste toujours valide.
