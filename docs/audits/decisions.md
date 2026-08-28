---
title: Registre de décisions reconstruites
status: active
date: 2026-08-27
source_session: 20260827_154335_c51ad8
---

# Décisions

Cette page reconstruit les décisions historiques et actuelles. Les ADR actifs du dépôt vivent sous `docs/decisions/`.

## Décisions courantes avec provenance

| ID | Décision | État | Source / locator |
|---|---|---|---|
| `CUR-001` | Auditer le passé et l’état actuel avant de définir la cible | `user_decision` | `SRC-HERMES` — session `20260827_154335_c51ad8`, messages `52676`, `52682`, `52961` |
| `CUR-002` | Dériver la cible des besoins et capacités, sans l’imposer | `user_decision` | `SRC-HERMES` — message `52961` |
| `CUR-003` | Construire VitePress en privé avant toute décision d’hébergement | `user_decision` | `SRC-HERMES` — réponse `clarify` `52945` |
| `CUR-004` | Archiver la fondation initiale puis créer un nouveau socle actif | `user_decision` | `SRC-HERMES` — message `52972`, réponse `clarify` `53020` |
| `CUR-005` | Utiliser deux commits locaux, sans remote ni push | `user_decision` | `SRC-HERMES` — réponse `clarify` `53020` |
| `CUR-006` | TaskNotes reste l’autorité des tâches opérationnelles | `current_canon` | `SRC-OBS-ACTIVE` — `AGENTS.md:26-31`, Journal V4 `:104-110` |

## Décisions historiques intégrées depuis AUD-001

Ces entrées décrivent ce que les documents affirmaient à l’époque. Elles ne deviennent pas des décisions canoniques actuelles.

| ID | Décision historique bornée | État | Source / limite |
|---|---|---|---|
| `HIS-001` | Le Plan propose une migration Notion → Obsidian par phases. | `historical_intent` | `SRC-OBS-OLD` ; réalisation non prouvée |
| `HIS-002` | La synthèse V2 conserve une vision long terme et diffère une partie de l’infrastructure. | `historical_intent` | `SRC-OBS-OLD` ; implémentation non prouvée |
| `HIS-003` | Le cadrage V3 repart du système abstrait avant le choix des outils. | `historical_intent` | `SRC-OBS-OLD` ; cadrage documenté seulement |
| `HIS-004` | Le journal V4 décrit Obsidian comme Interface Adapter et Mermaid comme canon logique. | `historical_intent` | `SRC-OBS-OLD` ; `Actée`, `Validé` et `canon` restent des statuts internes au document |
| `HIS-005` | La documentation du 2026-05-16 établit un vault propre `Sofian-OS` et conserve l’ancien vault en lecture seule. | `historical_execution` | `AUD-002`, claims `314`, `401`, `408` ; acceptation utilisateur actuelle non déduite |
| `HIS-006` | Treize notes V4 ont été ajoutées sélectivement au nouveau vault, puis le mapping a été ajouté séparément. | `historical_execution` | `AUD-002`, claims `406`, `407` ; aucune migration globale prouvée |
| `HIS-007` | Hermes est documenté comme runtime du chantier à cette période. | `historical_execution` | `AUD-003`/`AUD-004` ; partage futur avec OpenCode non décidé |
| `HIS-008` | Les mutations agentiques doivent rester liées à un lot explicitement approuvé et relu. | `user_decision` | sessions Hermes relues par `AUD-004` et trace de décision `AUD-006` ; pas d’autorisation réutilisable hors lot |

## Décisions encore ouvertes

- responsabilité future et partage exact entre Jarvis, OpenCode et Hermes ;
- cartes domaines, capacités et autorités ;
- choix Brief, Mail, Daily Start ou Clarify ;
- mémoire, Bots, automatisations et infrastructure différées ou rouvertes.

## Champs requis

```text
ID / titre / date / décideur / contexte
faits / hypothèses / options / décision / portée
conséquences / coûts acceptés / preuves
statut / décision remplacée / condition de réexamen
```

Une sélection faite sans comprendre sa conséquence reste provisoire.
