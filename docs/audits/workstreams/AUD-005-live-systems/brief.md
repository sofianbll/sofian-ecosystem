---
id: AUD-005
title: Systèmes et implémentations live
status: brief_ready
date: 2026-08-27
owner: Jarvis
role: coordinator
period: snapshot_at_execution
expected_count: 7_subreports
output_path: none
source_ids:
  - SRC-LIVE
  - SRC-OBS-ACTIVE
  - SRC-OPENCODE
  - SRC-OURMEM
---

# AUD-005 — Systèmes live

## Mission unique

Coordonner sept sous-audits indépendants pour établir l’état réel, les responsabilités, autorités et niveaux de livraison des sujets systèmes actuellement identifiés.

**Ce brief n’est pas exécutable par un worker unique.** Le coordinateur délègue exactement un lot par worker et exige sept rapports.

## Unités de délégation

| Unité | Sujet | Racines et sources exactes | Spécialiste |
|---|---|---|---|
| `SYS-001` | Sofian OS V4 + TaskNotes | `/Users/sofian/Documents/Obsidian/Sofian-OS/AGENTS.md`, `98-Backend/Resources/Sofian OS V4 - Architecture Référence.md`, `Workflows.md`, `Operating Layer.md`, `99-System/Config/TaskNotes Schema.md` | `obsidian` |
| `SYS-002` | Jarvis | `/Users/sofian/Developer/10-Personal/jarvis/AGENTS.md`, `README.md`, `docs/`, `jarvis/`, `tests/`, Git read-only | `software-engineering-lifecycle` |
| `SYS-003` | Hermes | session `20260827_154335_c51ad8`, `https://hermes-agent.nousresearch.com/docs`, skill `hermes-agent` ; aucune lecture large de `~/.hermes` | `hermes-agent` |
| `SYS-004` | OpenCode | `/Users/sofian/.local/share/opencode/opencode.db`, helper `opencode_history.py`, résultats `AUD-003` | `opencode-history` |
| `SYS-005` | ourmem | MCP `ourmem` ; recherche structurelle bornée à `/Users/sofian/Homelab-OS` et `/Users/sofian/dotfiles` pour la config, jamais `/Users/sofian/Data/appdata/omem` | `ourmem` |
| `SYS-006` | Homelab-OS | `/Users/sofian/Homelab-OS/AGENTS.md`, `vault-os/60-69 Architecture/67 Unified Home Architecture.md`, Git read-only | `self-hosted-app-deployment` |
| `SYS-007` | Finance OS | `/Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/README.md`, `compose.yml`, `scripts/`, `tests/` ; instructions parentes Homelab-OS | `software-engineering-lifecycle` |

Avant délégation, le coordinateur résout chaque chemin relatif depuis sa racine et arrête si une unité ne correspond plus.

## Contrat commun de chaque sous-audit

1. lire les instructions locales ;
2. inventorier seulement les fichiers nommés et leurs dépendances directes ;
3. identifier besoin, langage, état, writers, consumers et correction ;
4. distinguer système, projet, adapter, runtime et source ;
5. inspecter tests et sorties historiques sans les relancer ;
6. dater l’état Git/config ;
7. classer le niveau de livraison ;
8. retourner un dossier selon `templates/system-dossier.md`.

## Questions communes

- Quel besoin durable et quel bénéficiaire ?
- Quels faits sont possédés et comment les corriger ?
- Quels workflows et contrats sont actuels ?
- Quelles copies ou projections peuvent diverger ?
- Quelles permissions et données sensibles ?
- Qu’est-ce qui fonctionne réellement aujourd’hui ?
- Qu’est-ce qui est seulement documenté ou prototypé ?

## Méthode et skills

Socle obligatoire + `personal-system-reconciliation`, `software-engineering-lifecycle`, `grounded-citations`, puis le spécialiste de chaque unité.

## Exclusions

- aucun install, test, build, restart, healthcheck distant, déploiement ou device ;
- aucun secret, environnement ou runtime data ;
- aucune requête d’écriture ;
- aucun sujet hors des sept unités ;
- aucun système déclaré obsolete/legacy.

## Sortie

Sept sous-rapports puis une synthèse coordinateur. Retourner dans la session. Aucune écriture dans le dépôt par défaut.

## Niveau de détail

Dossier complet par unité ; synthèse limitée aux frontières, autorités, contrats, risques et niveaux de livraison. Couverture attendue : `7/7`.

## Definition of Done

- [ ] sept chemins racines revalidés ;
- [ ] sept sous-rapports reçus ;
- [ ] autorités et correction par fait ;
- [ ] dépendances et contrats ;
- [ ] état live daté sans action distante ;
- [ ] niveaux de livraison avec preuves ;
- [ ] inconnues et besoins non couverts ;
- [ ] aucune mutation externe.
