---
name: "Finance OS"
system_id: SYS-007
status: current_or_historical_as_reported
audit_state: reported
date: 2026-08-28
source_ids: [SRC-LIVE]
---

# Finance OS

> **État : dossier `reported`, non accepté comme cible.** Il décrit uniquement ce qu’AUD-005 a pu prouver.

## Verdict

Stack PocketBase privé documenté avec importeurs Python/Bash et contrat de données statique. Le healthcheck Tailscale répond HTTP 200 ; les données financières, ACL, tests courants et correction métier n’ont pas été inspectés.

## Autorité des faits

### Élément 1

- **fact :** schéma

- **authority :** scripts/import_finance.py

- **correction :** contrat source après décision

### Élément 2

- **fact :** fichier bancaire

- **authority :** CSV source sélectionné

- **correction :** corriger/remplacer la source puis réimporter selon workflow à confirmer

### Élément 3

- **fact :** transaction normalisée

- **authority :** PocketBase après import avec CSV comme preuve d’entrée

- **correction :** workflow de rapprochement inconnu

### Élément 4

- **fact :** cashflow prévu

- **authority :** inconnue

- **correction :** aucun writer observé

### Élément 5

- **fact :** document

- **authority :** manifest et fichier local

- **correction :** source/manifest ; procédure opérationnelle inconnue

## Frontières

- **owns :**
- schéma/imports/transactions/documents persistés selon le code
- **does_not_own :**
- source bancaire primaire
- runtime prouvé
- Athena Dashboard
- acceptation utilisateur

## Contrats et dépendances

- CSV Revolut/Sumeria → normalisation
- source_uid/id déterministes et unicité
- importeur authentifié → PocketBase
- manifest → documents
- Tailscale déclaré privé

## Permissions et risques

- superuser temporaire dans run_import.sh
- ACL PocketBase effectives non relues
- ligne Sumeria invalide potentiellement ignorée
- sémantique de fuseau non spécifiée
- aucune sauvegarde/restauration prouvée

## État live et livraison

- **verified :**
- documentation et implémentation statique présentes
- tests lisibles mais non exécutés
- healthcheck runtime HTTP 200 vérifié le 2026-08-28
- **not_proven :**
- technically_tested
- integrated
- exercised_real_case
- user_accepted
- operational

## Contradictions

- instruction Homelab « pas de suite de tests » versus suite Finance OS
- confidentialité déclarée versus ACL runtime non vérifiées

## Inconnues

- fraîcheur et intégrité métier du runtime Pulsar
- règles PocketBase
- workflow de correction/rapprochement
- writer cashflow_items
- hôte d’exécution de l’import

## Provenance

- Source : `AUD-005`, dossier `SYS-007`, carte `t_b928e7fd`.
- Claims acceptés : `21`.
- Niveau maximal : aucune promotion globale vers `user_accepted` ou `operational`.
