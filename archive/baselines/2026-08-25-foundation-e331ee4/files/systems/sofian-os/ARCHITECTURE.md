---
status: active
date: 2026-08-25
scope: Architecture documentaire de Sofian OS
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Architecture de Sofian OS

## Composants observés

- notes Projet : contexte, résultat, statut et ressources ;
- TaskNotes : actions reliées aux projets ;
- Inbox : entrées à clarifier ;
- Daily et Weekly Notes : surfaces de revue ;
- Resources et System Config : connaissances et contrats ;
- Bases et dashboards : vues dérivées, sans autorité propre.

## Flux de référence

```text
Capture → Inbox → Clarify → Projet / TaskNote / Resource
                              ↓
                       Daily / Weekly Review
```

## Interfaces

- fichiers Markdown et frontmatter dans `SRC-SOS` ;
- liens Obsidian entre projets, tâches et ressources ;
- lecture future par Jarvis ;
- correction dans la note canonique, jamais uniquement dans une vue.

Les formats détaillés restent définis par les schémas du vault, pas par ce projet documentaire.
