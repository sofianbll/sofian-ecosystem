---
title: Décisions actives du projet
status: active
date: 2026-08-27
decider: Sofian
source_session: 20260827_154335_c51ad8
---

# Décisions du projet

Cette section contient les décisions fondatrices du **chantier documentaire** avec leur provenance. Les décisions historiques reconstruites vivent dans `docs/audits/decisions.md`.

## Décisions fondatrices

| ID | Décision | Statut | Source / locator | Réexamen |
|---|---|---|---|---|
| `ADR-P001` | Auditer avant de définir l’écosystème cible | accepté | `SRC-HERMES` — messages `52676`, `52682`, `52961` | si une cible antérieure explicitement validée est retrouvée |
| `ADR-P002` | Dériver la cible des besoins et capacités | accepté | `SRC-HERMES` — message `52961` | après la première tranche pilote |
| `ADR-P003` | Conserver les sources externes canoniques et read-only pendant l’audit | accepté | `SRC-HERMES` — messages `52676`, `52972` ; règles projet approuvées | si une migration distincte est décidée |
| `ADR-P004` | Garder TaskNotes comme autorité opérationnelle des tâches | accepté | `SRC-OBS-ACTIVE` — `AGENTS.md:26-31`, Journal V4 `:104-110` | si Sofian change explicitement de gestionnaire |
| `ADR-P005` | Construire la documentation en privé d’abord | supersédé pour la publication actuelle | `SRC-HERMES` — réponse `clarify` `52945` | si Sofian souhaite rétablir un corpus privé ou une version publique expurgée |
| `ADR-P006` | Intégrer un rapport uniquement après contre-vérification | `proposed_guardrail` | `SRC-GUIDE`, `AGENTS.md` et `docs/operations/audit-orchestration.md` | après la tranche pilote et mesure du coût réel |
| `ADR-P007` | Garder le dépôt et Pages publics pour l’instant, avec une gate CI anti-secrets/PII | accepté | `SRC-HERMES` — session `145c806b6027`, locator `63985` | à la prochaine décision de confidentialité ou de partage |

## Format futur

Chaque ADR doit contenir contexte, forces, options dont statu quo, décision, portée, conséquences, contrôle, réversibilité et condition de réexamen.

Une décision historique n’est pas copiée ici tant que son statut actuel n’a pas été confirmé.
