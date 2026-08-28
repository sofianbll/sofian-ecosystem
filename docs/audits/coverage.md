---
title: Couverture de l’audit
status: active
date: 2026-08-27
---

# Couverture

## État actuel

| Dimension | État | Commentaire |
|---|---|---|
| Sources principales | `inventoried` | registre initial créé, contenu non exhaustivement audité |
| Notion / DOCX | `integrated` | `AUD-001` : corpus fermé de 10 objets contre-vérifié |
| Ancien et nouveau vault | `brief_ready` | filiation à reconstruire |
| OpenCode / OpenChamber | `brief_ready` | index stale à traiter sans modifier la base canonique |
| Hermes / ourmem | `brief_ready` | recherche ourmem partiellement bloquée |
| Systèmes live | `brief_ready` | un audit distinct par frontière sera nécessaire |
| Timeline | `seeded` | seulement des ancres déjà vérifiées |
| Noms et identités | `seeded` | relations non prouvées restent ouvertes |
| Besoins | `not_started` | aucun besoin canonisé |
| Cible | `none_accepted` | aucune architecture cible validée |

## Lots intégrés

| Audit | Attendus | Inspectés | Exclus | Bloqués | Claims acceptés | Claims rejetés |
|---|---:|---:|---:|---:|---:|---:|
| [`AUD-001`](workstreams/AUD-001-notion-docx-genesis/report.md) | 10 | 10 | 0 | 0 | 72 | 0 |

Cette couverture vaut uniquement pour le corpus fermé `AUD-001`. `AUD-002`, la filiation complète des vaults et le reste de l’écosystème restent à auditer ; aucun pourcentage global n’est déduit de ce pilote.

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
