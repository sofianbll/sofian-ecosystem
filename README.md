---
title: Sofian Ecosystem
status: audit_corpus_integrated_current_state_refreshed
date: 2026-08-27
visibility: public_temporarily_accepted
---

# Sofian Ecosystem

## Conclusion

Ce dépôt est la base commune permettant à plusieurs sessions et groupes d’agents de **reconstruire le passé, auditer l’état actuel, découvrir les besoins puis définir avec Sofian l’écosystème cible**.

Les **six audits `AUD-001` à `AUD-006` sont intégrés et mécaniquement vérifiés**. Cela valide leurs corpus documentaires et leurs limites ; les sept dossiers système restent au niveau `reported`, sans acceptation de l’architecture actuelle ni preuve opérationnelle globale.

## Trois portes d’entrée

1. **Comprendre le chantier** — [`docs/project/scope.md`](docs/project/scope.md)
2. **Lancer ou reprendre un audit** — [`docs/audits/catalog.md`](docs/audits/catalog.md)
3. **Voir comment la cible sera construite** — [`docs/architecture/README.md`](docs/architecture/README.md)

## État actuel

- baseline initiale archivée et vérifiée sous [`archive/baselines/2026-08-25-foundation-e331ee4/`](archive/baselines/2026-08-25-foundation-e331ee4/BASELINE.md) ;
- méthode, scope, sources, preuves et protocoles installés ;
- six workstreams bornés et intégrés ;
- audits intégrés : **[`AUD-001`](docs/audits/workstreams/AUD-001-notion-docx-genesis/report.md) à [`AUD-006`](docs/audits/catalog.md)** ;
- dossiers système reportés : **7** ; dossiers système acceptés : **aucun** ;
- besoins validés : **aucun** ;
- cible acceptée : **aucune** ;
- état live rafraîchi : Finance OS répond à son healthcheck, Hermes utilise Honcho et un gateway supervisé, OpenCode reste indexé partiellement et la recherche ourmem reste bloquée ;
- prochaine gate : **tester les frontières, corrections et restaurations par des scénarios réels avant toute acceptation de l’architecture actuelle** ;
- publication : **dépôt et GitHub Pages publics, acceptés pour l’instant par Sofian (`CUR-007`, locator `63985`) ; gate CI anti-secrets/PII active**.

## Autorités

| Information | Autorité |
|---|---|
| Méthode, audits intégrés, architecture et décisions de ce chantier | ce dépôt |
| Projets, tâches, statuts, dates et priorités | Sofian-OS / TaskNotes |
| Faits métier ou techniques externes | leur système ou document propriétaire |
| Décision finale | Sofian |

## Fonctionnement

```text
Sources réelles
   ↓
Audits isolés
   ↓
Contre-vérification Jarvis
   ↓
État historique et actuel réconcilié
   ↓
Besoins et capacités
   ↓
Options d’architecture
   ↓
Cible proposée → validation Sofian
   ↓
Roadmap liée à TaskNotes
```

## Règles rapides

- lecture seule par défaut ;
- aucune cible inventée avant les besoins ;
- aucun raw dump dans la documentation ;
- aucune tâche opérationnelle dupliquée ici ;
- aucune publication publique sans revue de confidentialité ;
- aucune conclusion sans provenance.
