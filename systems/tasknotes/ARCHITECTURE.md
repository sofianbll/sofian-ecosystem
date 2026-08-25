---
status: active
date: 2026-08-25
scope: Architecture et interfaces de TaskNotes
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Architecture de TaskNotes

## Modèle utile

Une TaskNote contient au minimum un titre, un statut, une priorité et `is_template: false`. Elle peut porter projet, contexte, date planifiée, échéance, preuve ou lien externe selon le schéma canonique.

## Flux

```text
Entrée clarifiée → proposition → accord humain → TaskNote
                                              ↓
                                dashboard / revue / exécution
```

## Interfaces

- écriture : fichier Markdown conforme au template canonique ;
- lecture : frontmatter et contenu de la note ;
- vues : Bases et dashboards reconstruisibles ;
- correction : modifier la TaskNote, puis vérifier les vues.

Toute mutation future par Jarvis doit être idempotente, ciblée et relue après écriture.
