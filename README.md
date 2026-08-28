---
title: Sofian Ecosystem
status: pilot_integrated_pending_review
date: 2026-08-27
visibility: private-first
---

# Sofian Ecosystem

## Conclusion

Ce dépôt est la base commune permettant à plusieurs sessions et groupes d’agents de **reconstruire le passé, auditer l’état actuel, découvrir les besoins puis définir avec Sofian l’écosystème cible**.

La **tranche pilote `AUD-001` est intégrée et contre-vérifiée**. Elle documente la genèse Notion/DOCX/V1–V4 ; le reste de l’écosystème, les dossiers système et l’architecture actuelle ne sont pas encore audités.

## Trois portes d’entrée

1. **Comprendre le chantier** — [`docs/project/scope.md`](docs/project/scope.md)
2. **Lancer ou reprendre un audit** — [`docs/audits/catalog.md`](docs/audits/catalog.md)
3. **Voir comment la cible sera construite** — [`docs/architecture/README.md`](docs/architecture/README.md)

## État actuel

- baseline initiale archivée et vérifiée sous [`archive/baselines/2026-08-25-foundation-e331ee4/`](archive/baselines/2026-08-25-foundation-e331ee4/BASELINE.md) ;
- méthode, scope, sources, preuves et protocoles installés ;
- six workstreams bornés, dont le pilote `AUD-001` intégré ;
- audits intégrés : **[`AUD-001`](docs/audits/workstreams/AUD-001-notion-docx-genesis/report.md)** ;
- dossiers système acceptés : **aucun** ;
- besoins validés : **aucun** ;
- cible acceptée : **aucune** ;
- prochaine gate : **revue de la méthode pilote par Sofian avant extension à `AUD-002`** ;
- publication : **GitHub Pages public actif ; la politique cible reste privée d’abord et doit être réconciliée**.

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
