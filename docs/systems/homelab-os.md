---
name: "Homelab-OS"
system_id: SYS-006
status: current_or_historical_as_reported
audit_state: reported
date: 2026-08-28
source_ids: []
---

# Homelab-OS

> **État : dossier `reported`, non accepté comme cible.** Il décrit uniquement ce qu’AUD-005 a pu prouver.

## Verdict

Control repo courant de configuration et documentation ; les contrats et artefacts déclaratifs sont présents, mais aucun runtime distant ni usage maintenu n’a été vérifié.

## Autorité des faits

### Élément 1

- **fact :** layout et bootstrap

- **authority :** AGENTS/README/66/67 et bootstrap-linux.sh

- **correction :** source Git après décision

### Élément 2

- **fact :** stacks

- **authority :** `docker/stacks/<machine>/<service>/compose`

- **correction :** source Compose puis déploiement contrôlé

### Élément 3

- **fact :** dotfiles

- **authority :** yadm selon canon courant

- **correction :** source dotfiles

### Élément 4

- **fact :** runtime

- **authority :** Docker/Dockhand sur la machine

- **correction :** réconciliation runtime ↔ Git

### Élément 5

- **fact :** données/secrets

- **authority :** ~/Data sur les machines

- **correction :** service/opérateur, jamais Git

## Frontières

- **owns :**
- layout, bootstrap, déclarations Compose, documentation et politiques versionnées
- **does_not_own :**
- volumes Data
- secrets
- état/logs des conteneurs
- backups réels

## Contrats et dépendances

- Git → bootstrap Linux
- Git → Docker/Dockhand
- services → Caddy/Tailscale/Cloudflare
- runtime → Restic/backup documenté

## Permissions et risques

- working tree non propre et stacks non suivies
- Dockhand peut potentiellement écrire les stacks et contrôler Docker
- sockets Docker root-equivalent
- restauration/RPO/RTO non prouvés

## État live et livraison

- **verified :**
- documentation et artefacts déclaratifs présents
- bootstrap et Compose comme implémentation statique
- **not_proven :**
- déploiement
- restauration exercée
- operational

## Contradictions

- zéro port hôte versus bindings déclarés
- yadm/bootstrap courant versus chezmoi/Ansible historique
- politique secrets externes versus compose ourmem

## Inconnues

- writer exact des stacks
- état Docker/services
- backup/restauration
- politique réseau acceptée

## Provenance

- Source : `AUD-005`, dossier `SYS-006`, carte `t_03983e70`.
- Claims acceptés : `13`.
- Niveau maximal : aucune promotion globale vers `user_accepted` ou `operational`.
