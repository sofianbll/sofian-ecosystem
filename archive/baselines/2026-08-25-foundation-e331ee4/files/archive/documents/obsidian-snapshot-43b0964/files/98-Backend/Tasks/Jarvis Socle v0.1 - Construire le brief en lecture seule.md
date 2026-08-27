---
type: "✏️ Task"
title: "Jarvis Socle v0.1 - Construire le brief en lecture seule"
area: "[[🏠 Perso]]"
projects:
  - "[[Jarvis — Socle v0.1]]"
contexts:
  - computer
status: todo
priority: high
scheduled_date:
due_date:
is_template: false
---

# Jarvis Socle v0.1 - Construire le brief en lecture seule

## Outcome

Une commande Jarvis à la demande lit Sofian OS et TaskNotes, applique le contrat validé et retourne un brief vérifiable de trois priorités maximum.

## Dépendance

Commencer seulement après [[Jarvis Socle v0.1 - Spécifier le contrat du brief]].

## Contraintes

- aucune écriture dans le vault pendant la génération ;
- aucune dépendance obligatoire à Gmail, Calendar, Finance OS ou ourmem ;
- provenance lisible pour chaque priorité ;
- erreurs et indisponibilités visibles ;
- résultat réellement exercé depuis l’interface Jarvis/Hermes.

## Definition Of Done

- [ ] La commande s’exécute à la demande.
- [ ] Elle lit uniquement les sources autorisées.
- [ ] Elle renvoie au maximum trois priorités.
- [ ] Chaque priorité affiche provenance et certitude.
- [ ] Une erreur de lecture reste visible.
- [ ] Aucune mutation du vault n’est observée.
