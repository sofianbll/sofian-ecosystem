---
title: Handoff de session
status: active
date: 2026-08-27
---

# Reprendre ce chantier

## Lecture rapide

1. `README.md`
2. `docs/project/scope.md`
3. `docs/audits/catalog.md`
4. `docs/audits/coverage.md`
5. le brief du workstream concerné
6. le dernier rapport et sa review, s’ils existent
7. `git status --short --branch`

## État à transmettre

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
Consentement actif :
Action interdite :
Prochaine décision unique :
```

## Prompt de reprise générique

```text
Tu reprends Sofian Ecosystem dans :
/Users/sofian/Developer/10-Personal/sofian-ecosystem

Lis AGENTS.md, docs/project/scope.md, docs/audits/evidence-model.md,
docs/operations/subagent-protocol.md puis le brief [CHEMIN].

Mission unique : [QUESTION].
Travail en lecture seule sur les sources externes.
Ne modifie aucun fichier sauf [CHEMIN EXACT AUTORISÉ], si présent.
Préserve les identités littérales, cite chaque claim et déclare la couverture.
Arrête-toi à la Definition of Done du brief.
```

## Règle de reprise

Le transcript historique explique ce qui a été tenté. Les fichiers et sources live prouvent ce qui existe maintenant. Si les deux divergent, conserver les deux états et demander le prochain arbitrage.
