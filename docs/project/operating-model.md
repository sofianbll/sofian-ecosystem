---
title: Mode opératoire
status: active
date: 2026-08-27
---

# Mode opératoire

## Boucle principale

```text
1. Déclarer une question d’audit
2. Résoudre les sources et identités
3. Produire un brief borné
4. Déléguer en lecture seule
5. Recevoir faits, preuves et inconnues
6. Contre-vérifier depuis le parent
7. Intégrer le rapport accepté
8. Mettre à jour couverture et contradictions
9. Extraire les besoins sans décider de la cible
10. Comparer les options et demander la décision de Sofian
```

## Objets documentaires

| Objet | Rôle | Ne possède pas |
|---|---|---|
| Brief d’audit | question, sources, limites, format | résultat ou statut de tâche |
| Rapport | faits et preuves du worker | validation finale |
| Review | contre-audit et verdict d’intégration | source externe |
| Source registry | accès, autorité et santé | contenu de la source |
| Evidence ledger | claims et provenance | vérité indépendante |
| Need catalog | besoins et idées qualifiés | tâches d’implémentation |
| Candidate architecture | options comparées | décision de Sofian |
| Accepted target | décisions explicitement acceptées | futur certain |
| Roadmap | séquence de résultats | statut opérationnel TaskNotes |

## Rôles

- **Sofian** — arbitre les besoins, frontières, priorités et mutations.
- **Jarvis** — orchestre, vérifie, intègre et expose les décisions.
- **Worker** — répond à une question bornée avec preuves.
- **Source canonique** — arbitre le fait dans son périmètre.
- **TaskNotes** — possède l’exécution opérationnelle.

## Parallélisme

Les branches parallèles doivent être indépendantes par source ou question. Plusieurs agents peuvent couvrir un corpus, mais chaque lot possède un identifiant stable, des bornes non chevauchantes, un format commun, une règle de déduplication, un parent responsable de la synthèse et un contrôle du nombre attendu avant clôture.

## Intégration

Aucun résultat n’est intégré depuis une simple affirmation `completed`. Le parent vérifie les chemins, identifiants, citations et conclusions décisives. Les désaccords restent visibles dans `docs/audits/contradictions.md`.

## Escalade

Arrêter et demander une décision si l’identité est ambiguë, deux sources revendiquent la même autorité, une donnée sensible serait nécessaire, une mutation est requise, une source décisive est inaccessible ou la cible est interprétée comme déjà décidée.
