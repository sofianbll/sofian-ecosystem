---
title: Dossiers système
status: not_started
date: 2026-08-27
---

# Systèmes

## État

Aucun dossier système actif n’est encore accepté dans le nouvel arbre. Les documents précédents restent dans la baseline et seront réintégrés uniquement après audit.

## Sujets d’audit semés

| Nom littéral | Nature à tester | État documentaire | Source de découverte |
|---|---|---|---|
| `Sofian OS V4` | système humain portable / modèle métier | `seeded_subject` | `SRC-OBS-ACTIVE` — Architecture Référence et Journal V4 |
| `Sofian-OS` | vault Obsidian actif / adapter | `tool_identity_observed` | `SRC-OBS-ACTIVE` — `AGENTS.md:3-8` |
| `TaskNotes` | gestionnaire d’état des tâches | `authority_claim_sourced` | `SRC-OBS-ACTIVE` — `AGENTS.md:26-31`, Journal V4 `:104-110` |
| `Jarvis` / `Jarvis Agent` / `Jarvis OS` | agent, projet et architecture selon l’époque | `identity_unresolved` | `SRC-LIVE` — `/Users/sofian/Developer/10-Personal/jarvis/AGENTS.md`, lignes `3–18`, plus sources historiques |
| `Hermes` | runtime et interface de la session actuelle | `live_subject_to_audit` | `SRC-HERMES` — session `20260827_154335_c51ad8` |
| `OpenCode` | runtime et historique agentique | `future_role_unresolved` | `SRC-OPENCODE` |
| `ourmem` | mémoire sémantique secondaire candidate | `live_subject_to_audit` | `SRC-OURMEM` |
| `Homelab-OS` | configuration et reconstruction du homelab | `authority_claim_sourced` | `SRC-LIVE` — `/Users/sofian/Homelab-OS/AGENTS.md`, lignes `3–23` |
| `Finance OS` | système spécialisé financier candidat | `historical_subject_to_audit` | `SRC-BASELINE` ; état live à vérifier |

Cette table est une file de sujets avec provenance, pas une carte de frontières ni d’autorités acceptées.

## Contrat d’un dossier

Chaque dossier doit répondre :

1. quel besoin durable sert-il et pour qui ?
2. quel langage, état et cycle de vie possède-t-il ?
3. quels faits possède-t-il et quels faits ne possède-t-il pas ?
4. comment corrige-t-on une divergence ?
5. quels sont ses contrats, consommateurs et dépendances ?
6. quels risques et permissions le distinguent ?
7. quel est son historique et son niveau de livraison réel ?
8. quels besoins restent non couverts ?

Utiliser `templates/system-dossier.md`. Un grand projet ne devient pas un système sans preuve de frontière durable.
