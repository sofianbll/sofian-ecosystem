---
name: "OpenCode"
system_id: SYS-004
status: current_or_historical_as_reported
audit_state: reported
date: 2026-08-28
source_ids: [SRC-OPENCODE]
---

# OpenCode

> **État : dossier `reported`, non accepté comme cible.** Il décrit uniquement ce qu’AUD-005 a pu prouver.

## Verdict

Source canonique d’un historique OpenCode multi-agents et multi-projets. La base contient toujours 1 609 sessions ; l’index dérivé reste stale à 1 601. Le service OpenCode/OpenChamber actuel, son writer runtime et son contrat courant restent inconnus.

## Autorité des faits

### Élément 1

- **fact :** sessions/messages/parts

- **authority :** /Users/sofian/.local/share/opencode/opencode.db

- **correction :** relecture read-only par helper et ID

### Élément 2

- **fact :** index de recherche

- **authority :** index dérivé

- **correction :** ne jamais le traiter comme source canonique

### Élément 3

- **fact :** runtime OpenCode/OpenChamber

- **authority :** inconnue dans ce dossier

- **correction :** contrôle live séparé

### Élément 4

- **fact :** tâches personnelles

- **authority :** Sofian-OS / TaskNotes

- **correction :** hors OpenCode

## Frontières

- **owns :**
- sessions, messages, parts et métadonnées OpenCode
- **does_not_own :**
- état actuel des processus
- projets/tâches personnels
- validation utilisateur

## Contrats et dépendances

- base → opencode_history.py
- session → message → part
- OpenChamber → OpenCode historique
- traces OpenCode → systèmes personnels sans transfert d’autorité

## Permissions et risques

- base lue en mode read-only
- messages privés minimisés
- index stale et extraits potentiellement incomplets

## État live et livraison

- **verified :**
- base et schéma réellement interrogés
- historique architectural documenté
- 1 609 sessions, 40 619 messages et 186 048 parts confirmés le 2026-08-28
- **not_proven :**
- service actuel intégré
- user_accepted
- operational

## Contradictions

- index dérivé 1601 versus source canonique 1609
- architecture historique versus configuration actuelle inconnue

## Inconnues

- runtime actuel
- writer exact
- contrat OpenCode–OpenChamber–Jarvis/Hermes

## Provenance

- Source : `AUD-005`, dossier `SYS-004`, carte `t_c4648be3`.
- Claims acceptés : `12`.
- Niveau maximal : aucune promotion globale vers `user_accepted` ou `operational`.
