---
name: "ourmem"
system_id: SYS-005
status: current_or_historical_as_reported
audit_state: reported
date: 2026-08-28
source_ids: [SRC-OURMEM, SRC-LIVE]
---

# ourmem

> **État : dossier `reported`, non accepté comme cible.** Il décrit uniquement ce qu’AUD-005 a pu prouver.

## Verdict

Mémoire persistante self-hosted joignable via MCP : statistiques, liste et profil sont lisibles. La recherche sémantique échoue toujours avec un quota d’embeddings 403 ; la résilience, les backups et le déploiement maintenu restent non prouvés.

## Autorité des faits

### Élément 1

- **fact :** définition de service

- **authority :** compose Homelab-OS courant

- **correction :** compose et secret externe après accord

### Élément 2

- **fact :** mémoires servies

- **authority :** API ourmem derrière MCP

- **correction :** memory_update/memory_forget documentés, non exercés

### Élément 3

- **fact :** préférences et décisions personnelles

- **authority :** source canonique ou décision explicite

- **correction :** source propriétaire, pas projection ourmem

### Élément 4

- **fact :** intégration OpenCode

- **authority :** configuration effective non résolue

- **correction :** client effectif

## Frontières

- **owns :**
- mémoires, profil et statistiques selon le contrat ourmem
- **does_not_own :**
- projets/tâches TaskNotes
- décision finale
- sources métier canoniques

## Contrats et dépendances

- MCP stats/profile/list accessibles
- MCP search dépend du fournisseur d’embeddings
- build d’image déclaré vers GHCR
- montage runtime hors dépôt
- plugin OpenCode historique non confirmé

## Permissions et risques

- modèle API key/Spaces documenté mais ACL effectives non relues
- identifiants sensibles observés dans un compose sans reproduire les valeurs
- backup, rotation et rollback non vérifiés

## État live et livraison

- **verified :**
- configuration documentée
- lectures MCP réelles : 698 mémoires actives observées, statistiques/liste/profil disponibles
- recherche réelle toujours bloquée par le quota d’embeddings
- **not_proven :**
- intégration OpenCode
- service maintenu operational
- user_accepted

## Contradictions

- statistiques/liste/profil MCP réussis versus recherche sémantique bloquée
- note Void planifiée versus compose Nova courant
- politique secrets externes versus valeurs concrètes dans le compose

## Inconnues

- conteneur/version/digest réellement déployés
- writer runtime
- backup/restore
- résolution du quota embeddings 403

## Provenance

- Source : `AUD-005`, dossier `SYS-005`, carte `t_16f7c740`.
- Claims acceptés : `12`.
- Niveau maximal : aucune promotion globale vers `user_accepted` ou `operational`.
