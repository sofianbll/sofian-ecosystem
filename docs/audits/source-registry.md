---
title: Registre des sources
status: active
date: 2026-08-27
---

# Registre des sources

Ce registre décrit où lire. Il ne copie pas les sources et ne décide pas seul de leur autorité.

| ID | Source | Rôle | Période confirmée | Santé / limite |
|---|---|---|---|---|
| `SRC-NOTION-LIVE` | API Notion, page `Sofian OS` | source historique directe | page créée le 2026-01-08 | accessible en lecture ; corpus complet non audité |
| `SRC-NOTION-EXPORT` | `/Users/sofian/Developer/90-Archives/_DELETE-REVIEW/2026-06-14/notion-to-obsidian/Vault/` | conversion dérivée | fichiers datés 2026-02-10 ; contenu interne plus ancien | 8 442 fichiers, 765 177 009 octets ; `source_data` vide |
| `SRC-DOCX-V2` | `/Users/sofian/Documents/00-Inbox/SOFIAN OS V2 Document Reference.docx` | document historique | document daté 2026-01-08 | lisible ; données sensibles à minimiser |
| `SRC-OBS-OLD` | `/Users/sofian/Documents/Obsidian/Sofian's Vault/` | ancien vault, historique | Git 2026-05-04 → 2026-07-17 | `AUD-002` intégré ; 21 documents et historique Git ciblé lus en lecture seule |
| `SRC-OBS-ACTIVE` | `/Users/sofian/Documents/Obsidian/Sofian-OS/` | vault canonique actuel | Git depuis 2026-05-16 | `AUD-002`/`AUD-005` intégrés ; 12 documents et historique Git ciblé lus ; usage maintenu non prouvé globalement |
| `SRC-OPENCODE` | `/Users/sofian/.local/share/opencode/opencode.db` | historique OpenCode canonique | 2026-06-10 → 2026-08-26 vérifié | `AUD-003` intégré ; base read-only ; index dérivé stale 1601/1609 ; 24 IDs hors cap non individualisés |
| `SRC-HERMES` | sessions Hermes via `session_search` et base locale read-only | décisions et actions de sessions | chantier depuis 2026-08-19 | `AUD-004` intégré sur 6/6 sessions ; les sessions ne prouvent pas seules un état opérationnel actuel |
| `SRC-OURMEM` | MCP `ourmem` | mémoire sémantique secondaire | statut vérifié le 2026-08-28 | 3/3 recherches tentées dans `AUD-004`, toutes bloquées avant résultat ; ni absence de souvenirs ni panne permanente prouvée |
| `SRC-LIVE` | dépôts, configurations, APIs et runtimes spécialisés | état actuel vérifiable | snapshot `AUD-005` du 2026-08-28 | 7/7 dossiers reportés ; aucun healthcheck distant, restauration ni niveau opérationnel global prouvé |
| `SRC-GUIDE` | `/Users/sofian/Documents/00-Inbox/Guide-ultime-ingenierie-logicielle.pdf` | méthode d’ingénierie | édition 2026 | méthode, pas décision personnelle |
| `SRC-BASELINE` | `archive/baselines/2026-08-25-foundation-e331ee4/` | première consolidation du dépôt | commit `e331ee4…` | `AUD-006` intégré ; manifeste 73/73 vérifié ; 24 candidats à revue, aucun payload recopié automatiquement |
| `SRC-STUDIOFLOW` | `/Users/sofian/Developer/10-Personal/studioflow/` | modèle VitePress / CI | déploiement vérifié le 2026-08-26 | public ; ne pas copier sa politique de publication |

## Locators de la session fondatrice active

Session Hermes : `20260827_154335_c51ad8`.

| Message | Type | Décision ou besoin supporté |
|---:|---|---|
| `52676` | user | demande initiale d’audit complet et de système documentaire |
| `52682` | user | extension aux origines Notion, Obsidian, oraux et DOCX ; skills obligatoires |
| `52961` | user | la cible doit être définie après l’audit depuis les besoins |
| `52945` | réponse `clarify` | publication privée d’abord |
| `52972` | user | archiver l’ancien contenu et créer le système multi-sessions/subagents |
| `53020` | réponse `clarify` | remplacer l’ancien arbre et créer deux commits locaux sans push |

Ces locators sont lisibles dans `/Users/sofian/.hermes/state.db` en mode read-only. Après clôture de la session, utiliser `@session:default/20260827_154335_c51ad8` si l’index Hermes l’expose.

## Priorité de preuve

```text
état live / configuration exécutable
→ source canonique actuelle
→ document ou session historique exacte
→ export ou index dérivé
→ mémoire sémantique
→ hypothèse
```

## Résoudre un `SRC-*`

1. chercher l’ID exact dans ce fichier ;
2. utiliser le chemin, l’ID ou l’API indiquée ;
3. charger le skill spécialiste ;
4. vérifier santé, version et période avant de lire le contenu ;
5. si la source est inaccessible ou ambiguë, arrêter et déclarer `blocked`.

## Règles de lecture

- Utiliser l’outil spécialisé de la source.
- Ne jamais afficher un secret.
- Enregistrer instant, version, commit ou identifiant.
- Une date de fichier n’est pas automatiquement la date de l’événement décrit.
- Une source historique fait autorité sur ce qu’elle disait alors, pas sur l’état actuel.
- Toute indisponibilité devient une limite de couverture visible.
