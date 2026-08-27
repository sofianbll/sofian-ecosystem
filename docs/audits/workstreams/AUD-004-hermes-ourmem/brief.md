---
id: AUD-004
title: Hermes et ourmem
status: brief_ready
date: 2026-08-27
owner: Jarvis
role: coordinator
period: 2026-08-19..2026-08-27
expected_count: 6_hermes_sessions_plus_ourmem_status
output_path: none
source_ids:
  - SRC-HERMES
  - SRC-OURMEM
---

# AUD-004 — Hermes et ourmem

## Mission unique

Reconstituer les décisions et travaux Hermes liés à Sofian Ecosystem, puis déterminer ce que la mémoire ourmem apporte réellement comme contexte secondaire sans la traiter comme vérité opérationnelle.

## Corpus Hermes fermé — 6 sessions

| Session | Rôle dans l’audit |
|---|---|
| `20260819_191819_626eec` | naissance du chantier Sofian Ecosystem |
| `20260825_175948_c37c83` | reprise et clarification du chantier |
| `20260825_194053_5f380f` | Clarify et corrections de canon |
| `20260826_192853_171fd3` | modèle documentaire StudioFlow / VitePress |
| `20260827_130813_2c311f` | mémoire, Hermes et architecture d’accès |
| `20260827_154335_c51ad8` | scope, cible par besoins et création du nouveau socle |

Lire les sessions via `session_search`; pour la session active non encore indexée, utiliser `/Users/sofian/.hermes/state.db` en mode read-only et seulement les messages user/assistant/tool nécessaires.

## Source officielle Hermes

- documentation : `https://hermes-agent.nousresearch.com/docs` ;
- skill : `hermes-agent` ;
- les docs officielles gagnent sur les anciennes explications produit.

## Branche ourmem bornée

1. tester au maximum trois recherches : `Sofian Ecosystem`, `Sofian OS`, `Jarvis architecture`, limite dix ;
2. si l’embedding échoue, enregistrer une seule erreur et marquer la recherche `blocked` ;
3. ne pas contourner par lecture du volume brut ou dump de mémoires ;
4. toute mémoire retenue reste `memory_lead` jusqu’à corroboration.

## Questions

1. Quelles décisions de méta-architecture Sofian a-t-il acceptées, corrigées ou rouvertes ?
2. Quels artefacts et mutations ont été effectués dans chaque session ?
3. Quels niveaux de livraison sont réellement prouvés ?
4. Comment Hermes, Jarvis, Bots, skills, mémoire et orchestration ont-ils été distingués ?
5. Quels souvenirs ourmem sont pertinents et corroborés ?
6. Quelles limites empêchent une couverture complète ?

## Méthode et skills

Socle obligatoire + `cross-agent-session-handoff`, `personal-system-reconciliation`, `hermes-agent`, `ourmem` et `grounded-citations`. Pour les claims produit, vérifier les docs officielles.

## Exclusions

- toute autre session sauf lien direct découvert et approuvé par le coordinateur ;
- données Jawed, CAF, Kobra, OpenJob ou autres sujets sans conséquence architecturale ;
- mémoire brute, imports et hooks ;
- configuration secrète Hermes/ourmem.

## Sortie

Un rapport par branche Hermes/ourmem puis une synthèse coordinateur. Retourner dans la session. Aucune écriture dans le dépôt par défaut.

## Niveau de détail

Claims atomiques avec `session_id:message_id`, décisions utilisateur séparées des recommandations et des outils. Couverture : `6/6 sessions` et statut ourmem explicite.

## Definition of Done

- [ ] six sessions inspectées et citées ;
- [ ] décisions utilisateur séparées des recommandations ;
- [ ] mutations et résultats live relus ;
- [ ] claims produit vérifiés contre les docs actuelles ;
- [ ] ourmem corroboré ou marqué secondaire/bloqué ;
- [ ] aucune mémoire ou configuration modifiée.
