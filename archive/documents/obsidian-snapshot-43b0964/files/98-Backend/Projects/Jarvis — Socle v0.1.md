---
type: "📂 Project"
title: "Jarvis — Socle v0.1"
area: "[[🏠 Perso]]"
projects:
  - "[[Jarvis Agent]]"
status: in_progress
priority: high
scheduled_date: 2026-08-20
due_date:
tags:
  - jarvis
  - foundation
  - read-only
  - vertical-slice
is_template: false
cssclasses:
  - max
---

# Jarvis — Socle v0.1

> [!abstract] Mission
> Livrer un premier parcours Jarvis **utile, fiable et vérifiable** : produire à la demande un brief en lecture seule depuis Sofian OS et TaskNotes, sans nouveau stockage ni mutation silencieuse.

## Résultat Attendu

```text
Sofian OS + TaskNotes
          ↓ lecture
      Jarvis / Hermes
          ↓
Brief fiable à la demande
          ↓
3 priorités maximum
+ provenance
+ conflits visibles
+ proposition d’action
```

Le socle doit aider Sofian à répondre à une question simple :

> **Quelles sont les trois choses les plus importantes à faire maintenant, et pourquoi puis-je faire confiance à cette réponse ?**

---

## Périmètre v0.1

### Inclus

- lire les projets et tâches canoniques de Sofian OS ;
- produire un brief uniquement à la demande ;
- proposer au maximum trois priorités ;
- citer la provenance de chaque élément ;
- afficher `non établi`, `indisponible` ou un conflit au lieu d’une fausse certitude ;
- proposer une mutation sans l’effectuer silencieusement ;
- vérifier trois scénarios réels de bout en bout.

### Hors Périmètre

- cron et proactivité automatique ;
- architecture complète de Jarvis Memory ;
- Gmail, Calendar, Finance OS ou ourmem comme dépendances obligatoires ;
- écritures financières, administratives ou légales ;
- nouveau stockage, nouvelle base, nouvel OS ou bus d’événements ;
- contrats complets entre tous les systèmes ;
- dashboard supplémentaire sans usage démontré.

---

## Contrat D’Autorité

Ce projet applique [[Sofian Ecosystem - Systèmes et Autorité des Faits]].

- TaskNotes possède l’état des tâches.
- Sofian OS possède les projets et engagements humains enregistrés.
- Jarvis lit, classe, explique et propose.
- Une projection n’est jamais présentée comme preuve.
- Une source indisponible ne produit jamais un faux vide.
- Toute mutation future demandera un accord explicite et une relecture de la cible.

---

## Definition Of Done

- [ ] Le contrat de sortie du brief est défini et testable.
- [ ] Une commande à la demande produit le brief en lecture seule.
- [ ] Le brief contient au maximum trois priorités.
- [ ] Chaque priorité affiche sa provenance et son niveau de certitude.
- [ ] Les conflits, preuves manquantes et sources indisponibles restent visibles.
- [ ] Aucune mutation n’arrive sans confirmation humaine.
- [ ] Trois scénarios réels passent les tests.
- [ ] Un handoff permet de reprendre le développement proprement.

---

## Scénarios D’Acceptation

1. **Journée normale** — plusieurs tâches et projets existent ; le brief retient trois priorités maximum et explique son choix.
2. **État contradictoire** — une TaskNote et une note projet divergent ; le brief affiche le conflit sans le résoudre silencieusement.
3. **Source indisponible ou preuve absente** — le brief écrit `indisponible` ou `non établi`, jamais « rien à signaler ».

---

## Risques

1. **Scope creep** — connecter trop tôt la mémoire, le calendrier, les mails ou Finance OS.
2. **Fausse autorité** — transformer un résumé Jarvis en source de vérité.
3. **Brief décoratif** — produire une jolie sortie qui n’aide pas réellement à choisir la prochaine action.

---

## Task Board

![[Project Tasks Board.base#Compact]]

## Resource Deck

![[Project Resources.base#Cards]]

---

## Décisions

| Date | Décision | Pourquoi |
|---|---|---|
| 2026-08-20 | Créer un projet de livraison enfant de [[Jarvis Agent]] | Construire un lot fini sans créer un nouvel OS |
| 2026-08-20 | Premier incrément = brief à la demande en lecture seule | Usage réel, sources connues, permission simple et résultat testable |
| 2026-08-20 | Limiter les sources obligatoires à Sofian OS et TaskNotes | Réduire les dépendances avant d’ajouter un adaptateur à la fois |

## Prochaine Action Unique

> Exécuter [[Jarvis Socle v0.1 - Spécifier le contrat du brief]].
