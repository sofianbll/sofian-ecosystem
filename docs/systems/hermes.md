---
name: "Hermes Agent"
system_id: SYS-003
status: current_or_historical_as_reported
audit_state: reported
date: 2026-08-28
source_ids: [SRC-HERMES, SRC-LIVE]
---

# Hermes Agent

> **État : dossier `reported`, non accepté comme cible.** Il décrit uniquement ce qu’AUD-005 a pu prouver.

## Verdict

Runtime/interface agentique actif en v0.20.6 ; il possède les surfaces techniques de conversation, sessions, outils, profils et jobs, mais pas l’état métier des projets et tâches. Le provider mémoire courant est Honcho ; ourmem reste un MCP séparé.

## Autorité des faits

### Élément 1

- **fact :** historique conversationnel

- **authority :** SessionDB / state.db

- **correction :** session_search, resume, export documenté

### Élément 2

- **fact :** définition Cron

- **authority :** jobs.json via cronjob/CLI

- **correction :** cronjob ou hermes cron

### Élément 3

- **fact :** tentative Cron

- **authority :** executions.db

- **correction :** réconciliation ; unknown non relancé automatiquement

### Élément 4

- **fact :** paramètres

- **authority :** interfaces config/profil

- **correction :** hermes config set et commandes profile

### Élément 5

- **fact :** projets/tâches métier

- **authority :** Sofian-OS / TaskNotes

- **correction :** hors Hermes

### Élément 6

- **fact :** provider mémoire Hermes

- **authority :** configuration live et `hermes doctor`

- **correction :** `hermes config set` après décision ; aucune fusion implicite avec ourmem

## Frontières

- **owns :**
- sessions et historique Hermes
- définitions/tentatives Cron
- configuration et profils
- orchestration technique
- **does_not_own :**
- état métier Sofian OS/TaskNotes
- validation de la cible
- sources métier externes

## Contrats et dépendances

- SessionDB et session_search
- Cron séparé avec historique d’exécution
- ACP/TUI/API documentés mais non exercés
- toolsets/backends et profils isolés

## Permissions et risques

- redaction par défaut et secrets séparés de la configuration
- backend local et sudo désactivé au snapshot
- gateway actif sous supervision externe/launchd vérifiée
- runtime en retard de 225 commits sur l’amont au contrôle
- `state.db` volumineuse, signalée par `hermes doctor`

## État live et livraison

- **verified :**
- installation locale et CLI observées
- sessions documentées
- Cron configuré observé
- profil default observé
- gateway supervisé actif et `hermes doctor` sans avis de sécurité actif
- provider mémoire `honcho` confirmé ; MCP ourmem distinct
- **not_proven :**
- niveau produit global
- API/ACP/TUI exercés
- user_accepted
- operational pour chaque surface

## Contradictions

- l’écart gateway/launchd historique est résolu au contrôle live
- documentation et amont peuvent être plus récents que v0.20.6

## Inconnues

- relation éventuelle Honcho ↔ ourmem ; aucune intégration prouvée
- disponibilité exacte API/ACP/TUI dans v0.20.6
- résilience du gateway
- parcours réel complet

## Limites de normalisation

- CLM-AUD-005-210,217,223,224 rejetés par R3

## Provenance

- Source : `AUD-005`, dossier `SYS-003`, carte `t_39ebd5e9`.
- Claims acceptés : `20`.
- Niveau maximal : aucune promotion globale vers `user_accepted` ou `operational`.
