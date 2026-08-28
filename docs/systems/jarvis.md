---
name: "Jarvis"
system_id: SYS-002
status: current_or_historical_as_reported
audit_state: reported
date: 2026-08-28
source_ids: []
---

# Jarvis

> **État : dossier `reported`, non accepté comme cible.** Il décrit uniquement ce qu’AUD-005 a pu prouver.

## Verdict

Couche agentique documentée ; le code observé est un prototype Python déterministe et read-only qui produit des propositions JSON sans writer externe.

## Autorité des faits

### Élément 1

- **fact :** code et contrats

- **authority :** dépôt Jarvis

- **correction :** dépôt après accord

### Élément 2

- **fact :** message

- **authority :** Mail

- **correction :** Mail

### Élément 3

- **fact :** tâche

- **authority :** Sofian OS / TaskNotes

- **correction :** TaskNotes après autorisation

### Élément 4

- **fact :** proposition/orchestration

- **authority :** Jarvis

- **correction :** code et contrat Jarvis

## Frontières

- **owns :**
- code, règles déterministes, contrats et propositions Jarvis
- **does_not_own :**
- mail autoritaire
- état TaskNotes
- projets et engagements
- runtime externe

## Contrats et dépendances

- fixture/export mail → proposition
- Inbox Item → clarify-next
- proposition → futur adaptateur TaskNotes
- propositions → Daily Review documentée

## Permissions et risques

- prototype lu comme read-only
- absence de packaging/CI et dépôt sans commit vérifiable
- heuristiques mail et connecteurs non exercés

## État live et livraison

- **verified :**
- documented
- prototyped pour mail-to-task et clarify-next
- **not_proven :**
- technically_tested courant
- integrated
- exercised_real_case
- user_accepted
- operational

## Contradictions

- cinq dispositions mail documentées versus deux sorties implémentées

## Inconnues

- owner explicite
- tests courants
- connexion mail réelle
- déduplication et écriture TaskNotes
- intégration Daily Review/iOS

## Provenance

- Source : `AUD-005`, dossier `SYS-002`, carte `t_01bad240`.
- Claims acceptés : `24`.
- Niveau maximal : aucune promotion globale vers `user_accepted` ou `operational`.
