---
title: Registre des sources
status: seeded
date: 2026-08-27
---

# Registre des sources

Ce registre décrit où lire. Il ne copie pas les sources et ne décide pas seul de leur autorité.

| ID | Source | Rôle | Période confirmée | Santé / limite |
|---|---|---|---|---|
| `SRC-NOTION-LIVE` | API Notion, page `Sofian OS` | source historique directe | page créée le 2026-01-08 | accessible en lecture ; corpus complet non audité |
| `SRC-NOTION-EXPORT` | `/Users/sofian/Developer/90-Archives/_DELETE-REVIEW/2026-06-14/notion-to-obsidian/Vault/` | conversion dérivée | fichiers datés 2026-02-10 ; contenu interne plus ancien | 8 442 fichiers, 765 177 009 octets ; `source_data` vide |
| `SRC-DOCX-V2` | `/Users/sofian/Documents/00-Inbox/SOFIAN OS V2 Document Reference.docx` | document historique | document daté 2026-01-08 | lisible ; données sensibles à minimiser |
| `SRC-OBS-OLD` | `/Users/sofian/Documents/Obsidian/Sofian's Vault/` | ancien vault, historique | Git 2026-05-04 → 2026-07-17 | lecture seule explicite |
| `SRC-OBS-ACTIVE` | `/Users/sofian/Documents/Obsidian/Sofian-OS/` | vault canonique actuel | Git depuis 2026-05-16 | actif ; commits automatiques fréquents |
| `SRC-OPENCODE` | `/Users/sofian/.local/share/opencode/opencode.db` | historique OpenCode canonique | 2026-06-10 → 2026-08-26 vérifié | base read-only ; index dérivé stale 1601/1609 sessions |
| `SRC-HERMES` | historique Hermes via `session_search` | sessions et décisions Hermes | au moins depuis 2026-08-19 pour ce chantier | lire les sessions exactes |
| `SRC-OURMEM` | MCP `ourmem` | mémoire sémantique secondaire | données récentes visibles | listing accessible ; recherche bloquée par quota embeddings au 2026-08-27 |
| `SRC-LIVE` | dépôts, configurations, APIs et runtimes spécialisés | état actuel vérifiable | selon chaque système | audit séparé requis |
| `SRC-GUIDE` | `/Users/sofian/Documents/00-Inbox/Guide-ultime-ingenierie-logicielle.pdf` | méthode d’ingénierie | édition 2026 | méthode, pas décision personnelle |
| `SRC-BASELINE` | `archive/baselines/2026-08-25-foundation-e331ee4/` | première consolidation du dépôt | commit `e331ee4…` | 73/73 blobs et 255 869 octets vérifiés |
| `SRC-STUDIOFLOW` | `/Users/sofian/Developer/10-Personal/studioflow/` | modèle VitePress / CI | déploiement vérifié le 2026-08-26 | public ; ne pas copier sa politique de publication |

## Priorité de preuve

```text
état live / configuration exécutable
→ source canonique actuelle
→ document ou session historique exacte
→ export ou index dérivé
→ mémoire sémantique
→ hypothèse
```

## Règles de lecture

- Utiliser l’outil spécialisé de la source.
- Ne jamais afficher un secret.
- Enregistrer instant, version, commit ou identifiant.
- Une date de fichier n’est pas automatiquement la date de l’événement décrit.
- Une source historique fait autorité sur ce qu’elle disait alors, pas sur l’état actuel.
- Toute indisponibilité devient une limite de couverture visible.
