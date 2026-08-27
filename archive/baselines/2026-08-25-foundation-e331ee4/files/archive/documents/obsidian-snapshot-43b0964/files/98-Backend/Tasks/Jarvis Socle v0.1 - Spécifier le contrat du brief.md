---
type: "✏️ Task"
title: "Jarvis Socle v0.1 - Spécifier le contrat du brief"
area: "[[🏠 Perso]]"
projects:
  - "[[Jarvis — Socle v0.1]]"
contexts:
  - computer
status: in_progress
priority: high
scheduled_date: 2026-08-20
due_date:
is_template: false
---

# Jarvis Socle v0.1 - Spécifier le contrat du brief

## Outcome

Un contrat de sortie court, déterministe et testable définit ce qu’est un brief Jarvis fiable avant toute implémentation.

## Le Brief Doit Contenir

Pour chaque priorité :

- action visible ;
- raison du classement ;
- projet ou contexte ;
- source canonique et chemin ;
- niveau de certitude : `confirmé`, `non établi`, `indisponible` ou `conflit` ;
- prochaine action proposée.

## Contraintes

- trois priorités maximum ;
- lecture seule ;
- Sofian OS et TaskNotes comme seules sources obligatoires ;
- aucune source indisponible interprétée comme vide ;
- aucune mutation déclenchée depuis le brief ;
- aucune projection présentée comme preuve.

## Definition Of Done

- [ ] Le schéma de sortie est documenté.
- [ ] Les règles de classement sont explicites.
- [ ] Les quatre niveaux de certitude sont définis.
- [ ] Trois exemples attendus couvrent normal, conflit et indisponible.
- [ ] Le contrat peut être testé sans dépendre d’un modèle précis.
