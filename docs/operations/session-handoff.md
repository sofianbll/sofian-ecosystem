---
title: Handoff de session
status: active
date: 2026-08-27
---

# Reprendre ce chantier

## Checkpoint courant — 2026-08-28

```text
Objectif actif : valider l’architecture actuelle par scénarios réels avant les besoins et la cible
Workstreams : AUD-001 à AUD-006 intégrés
Couverture : 531 claims acceptés uniques ; limites et rejets conservés
État live : sept dossiers reportés, rafraîchis le 2026-08-28
Publication : dépôt et Pages publics par décision explicite de Sofian
Consentement actif pour une nouvelle session : none
Actions interdites : mutations des sources externes, cible inventée, TaskNotes dupliquées
Prochaine décision unique : choisir le premier scénario traversant de Phase 3
```

## Lecture obligatoire

1. `README.md`
2. `AGENTS.md`
3. `docs/project/scope.md`
4. `docs/audits/catalog.md`
5. `docs/audits/coverage.md`
6. `docs/audits/evidence-model.md`
7. `docs/audits/source-registry.md`
8. `docs/operations/subagent-protocol.md`
9. le brief du workstream concerné
10. le dernier rapport et sa review, s’ils existent
11. `git status --short --branch`

## Charger la méthode

1. Charger `software-engineering-lifecycle`, `opencode-history`, `ourmem`, `obsidian`, `i-have-adhd` et `tdah-visual-responses`.
2. Lire le passage du Guide 2026 demandé par le brief. Source : `/Users/sofian/Documents/00-Inbox/Guide-ultime-ingenierie-logicielle.pdf` ; les références opérationnelles sont dans la skill `software-engineering-lifecycle`.
3. Charger les skills spécialistes indiqués par le brief et `docs/reference/skill-routing.md`.

## Résoudre les sources

Pour chaque `source_id` du frontmatter du brief :

1. chercher l’ID dans `docs/audits/source-registry.md` ;
2. récupérer le chemin, ID, API, période et limite ;
3. vérifier l’existence et la santé sans lire de secret ;
4. arrêter avec `blocked` si la source ne correspond pas.

## État à transmettre lors d’une reprise

```text
Objectif actif :
Workstream :
Question exacte :
Sources lues :
Couverture : attendu / inspecté / bloqué
Claims acceptés :
Contradictions ouvertes :
Dernière preuve vérifiée :
Fichiers modifiés :
Consentement actif : none | description exacte
Action interdite :
Prochaine décision unique :
```

Pour une **nouvelle collecte** : `Consentement actif: none`. Les 531 claims déjà intégrés restent consultables ; aucun nouveau claim n’est accepté sans brief, preuve et review.

## Prompt de reprise générique

```text
Tu travailles dans :
/Users/sofian/Developer/10-Personal/sofian-ecosystem

Lis dans cet ordre : README.md, AGENTS.md, docs/project/scope.md,
docs/audits/catalog.md, docs/audits/coverage.md,
docs/audits/evidence-model.md, docs/audits/source-registry.md,
docs/operations/subagent-protocol.md, puis [CHEMIN DU BRIEF].

Charge les skills obligatoires et les skills spécialistes du brief.
Lis les références pertinentes du Guide ultime 2026 via
software-engineering-lifecycle.

Résous chaque source_id depuis source-registry.md avant toute collecte.
Mission unique : exécuter le brief sans élargir son corpus.
Travail en lecture seule sur les sources externes.
Consentement actif : none.
Ne modifie aucun fichier ; retourne le rapport dans la session.
Niveau de détail : claims atomiques complets, citations exactes,
verdict de premier niveau concis, couverture chiffrée ou unknown justifié.
Préserve les identités littérales et arrête-toi à la DoD du brief.
```

## Règle de reprise

Le transcript historique explique ce qui a été tenté. Les fichiers et sources live prouvent ce qui existe maintenant. Si les deux divergent, conserver les deux états et demander le prochain arbitrage.
