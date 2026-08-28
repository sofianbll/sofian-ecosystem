---
title: Couverture de l’audit
status: active
date: 2026-08-27
---

# Couverture

## État actuel

| Dimension | État | Commentaire |
|---|---|---|
| Sources principales | `audited_with_limits` | les six workstreams sont intégrés ; les exclusions et blocages restent visibles |
| Notion / DOCX | `integrated` | `AUD-001` : corpus fermé de 10 objets contre-vérifié |
| Ancien et nouveau vault | `integrated` | `AUD-002` : 33/33 documents et 2/2 historiques Git |
| OpenCode / OpenChamber | `integrated_with_limit` | `AUD-003` : 30/30 sessions retenues ; index dérivé stale et 24 IDs hors cap |
| Hermes / ourmem | `integrated_with_blocker` | `AUD-004` : 6/6 sessions ; 3/3 recherches ourmem bloquées, 0 résultat |
| Systèmes live | `integrated_reported` | `AUD-005` : 7/7 dossiers au niveau `reported`, aucun niveau global opérationnel |
| Timeline | `integrated_partial` | chronologie historique étendue ; les périodes sans preuve restent explicites |
| Noms et identités | `integrated_partial` | vaults et usages agentiques distingués ; plusieurs relations restent ouvertes |
| Besoins | `not_started` | aucun besoin canonisé |
| Cible | `none_accepted` | aucune architecture cible validée |

## Lots intégrés

| Audit | Attendus | Inspectés | Exclus | Bloqués | Claims acceptés | Claims rejetés |
|---|---:|---:|---:|---:|---:|---:|
| [`AUD-001`](workstreams/AUD-001-notion-docx-genesis/report.md) | 10 | 10 | 0 | 0 | 72 | 0 |
| [`AUD-002`](workstreams/AUD-002-obsidian-lineage/report.md) | 35 | 35 | 0 | 0 | 94 | 10 |
| [`AUD-003`](workstreams/AUD-003-opencode-openchamber/report.md) | 30 sessions retenues | 30 | 24 IDs hors cap | 0 | 83 | 21 |
| [`AUD-004`](workstreams/AUD-004-hermes-ourmem/report.md) | 6 sessions + 3 recherches | 6 sessions + 3 tentatives | 0 | 3 recherches | 56 | 3 |
| [`AUD-005`](workstreams/AUD-005-live-systems/report.md) | 7 systèmes | 7 | 0 | 0 | 132 | 9 |
| [`AUD-006`](workstreams/AUD-006-initial-foundation/report.md) | 73 payloads | 73 | 0 | 0 | 94 | 45 |

Chaque ligne vaut pour son corpus fermé. Aucun pourcentage global n’est déduit de dénominateurs hétérogènes. Les blocages ourmem, l’index OpenCode stale, les claims rejetés et les niveaux non prouvés restent des limites actives.

## Une couverture est complète lorsque

- toutes les sources attendues sont comptées ;
- les lots sont non chevauchants ou dédupliqués ;
- les périodes et trous sont visibles ;
- les éléments pertinents ont été lus profondément ;
- les exclusions sont justifiées ;
- les claims majeurs ont été revus ;
- le total intégré correspond au total attendu ;
- les sources indisponibles restent signalées.

## Pas de faux pourcentage

Aucun pourcentage global ne sera affiché tant que le dénominateur n’est pas défini. Préférer :

```text
sources attendues : N
sources inventoriées : N
sources auditées : N
claims intégrés : N
claims bloqués : N
périodes sans preuve : liste
```

Tous les totaux seront calculés mécaniquement avant publication.
