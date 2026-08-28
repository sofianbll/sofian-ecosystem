---
title: Dossiers système
status: reported
date: 2026-08-27
---

# Systèmes

## État

Sept dossiers issus d’`AUD-005` sont intégrés au niveau **`reported`**. Ils ne sont ni des cibles acceptées, ni une preuve d’usage opérationnel. Les documents précédents restent dans la baseline ; `AUD-006` identifie des candidats à revue sans les recopier.

Un contrôle live du 2026-08-28 a rafraîchi les faits qui avaient dérivé : Finance OS est joignable, Hermes utilise Honcho et un gateway supervisé, ourmem répond hors recherche sémantique, OpenCode conserve un index stale, Jarvis reste sans commit et Sofian-OS reste le vault actif. Les niveaux demeurent `reported`.

## Dossiers intégrés

| Dossier | État documentaire | Claims acceptés |
|---|---|---:|
| [Sofian OS V4 + TaskNotes](sofian-os-v4-tasknotes.md) | `reported` | 30 |
| [Jarvis](jarvis.md) | `reported` | 24 |
| [Hermes](hermes.md) | `reported` | 20 |
| [OpenCode](opencode.md) | `reported` | 12 |
| [ourmem](ourmem.md) | `reported` | 12 |
| [Homelab-OS](homelab-os.md) | `reported` | 13 |
| [Finance OS](finance-os.md) | `reported` | 21 |

## Sujets et identités à préserver

| Nom littéral | Nature à tester | État documentaire | Source de découverte |
|---|---|---|---|
| `Sofian OS V4` | système humain portable / modèle métier | `reported_subject` | `AUD-002`, `AUD-005` |
| `Sofian-OS` | vault Obsidian actif / adapter | `confirmed_tool_identity` | `AUD-002` |
| `TaskNotes` | gestionnaire d’état des tâches | `reported_authority` | `AUD-005` |
| `Jarvis` / `Jarvis Agent` / `Jarvis OS` | agent, projet et architecture selon l’époque | `identity_unresolved` | `AUD-003`, `AUD-005` |
| `Hermes` | runtime et interface du chantier | `reported_subject` | `AUD-004`, `AUD-005` |
| `OpenCode` | runtime et historique agentique | `future_role_unresolved` | `AUD-003`, `AUD-005` |
| `ourmem` | mémoire sémantique secondaire | `reported_with_blocker` | `AUD-004`, `AUD-005` |
| `Homelab-OS` | configuration et reconstruction du homelab | `reported_authority` | `AUD-005` |
| `Finance OS` | système spécialisé financier | `reported_subject` | `AUD-005` |

Cette table préserve les identités et la provenance. Les dossiers restent des rapports, pas une carte cible acceptée.

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
