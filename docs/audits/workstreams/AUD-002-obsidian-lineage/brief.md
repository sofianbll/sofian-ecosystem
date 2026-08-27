---
id: AUD-002
title: Filiation des vaults Obsidian
status: brief_ready
date: 2026-08-27
owner: Jarvis
role: coordinator
period: 2026-05-04..2026-08-27
expected_count: 33_documents_plus_2_git_histories
output_path: none
source_ids:
  - SRC-OBS-OLD
  - SRC-OBS-ACTIVE
---

# AUD-002 — Filiation des vaults Obsidian

## Mission unique

Reconstituer comment `Sofian's Vault` et `Sofian-OS` ont été créés, utilisés et reliés, puis distinguer migration, copie sélective, refonte de schéma, décisions V1–V4 et état canonique actuel.

## Lots fermés

| Lot | Corpus | Attendu |
|---|---|---:|
| A | `/Users/sofian/Documents/Obsidian/Sofian's Vault/Backend/Resources/Sofian OS V*.md` | 19 fichiers |
| B | ancien vault : `Backend/Resources/PLAN - Nouvelle Organisation Vault.md` et `Backend/Projects/Sofian OS.md` | 2 fichiers |
| C | `/Users/sofian/Documents/Obsidian/Sofian-OS/98-Backend/Tasks/Sofian OS RCU - Phase *.md` | 7 fichiers |
| D | vault actif : `AGENTS.md`, `98-Backend/Resources/Sofian OS V4 - Architecture Référence.md`, `98-Backend/Resources/Sofian OS V4 - Journal De Décisions.md`, `99-System/Config/V4 Obsidian Adapter Mapping.md`, `99-System/AI Handoffs/Sofian Ecosystem Architecture.md` | 5 fichiers |
| E | historique Git read-only des deux racines | 2 historiques |

Le coordinateur énumère les chemins exacts de A et C, vérifie respectivement `19` et `7`, puis donne un lot non chevauchant à chaque worker. Tout écart arrête la collecte.

Dans B, les chemins sont relatifs à `/Users/sofian/Documents/Obsidian/Sofian's Vault/`. Dans D, ils sont relatifs à `/Users/sofian/Documents/Obsidian/Sofian-OS/`.

## Questions

1. Pourquoi un nouveau vault a-t-il été créé ?
2. Qu’est-ce qui a été migré, reconstruit, laissé historique ou jamais transféré ?
3. Quelles différences de schéma et vocabulaire existent entre les vaults ?
4. Quelles notes sont canoniques aujourd’hui, et dans quel périmètre ?
5. Quels workflows V4 sont documentés, testés ou réellement exercés ?
6. Comment les noms V1–V4 ont-ils évolué ?
7. Quelles décisions historiques ont été remplacées ou restent ouvertes ?

## Méthode et skills

Socle obligatoire + `obsidian`, `personal-system-reconciliation`, `personal-knowledge-migration`, `cross-agent-session-handoff` et `grounded-citations`. Lire les chapitres 12–15, 20, 42, 46, 57 et 65 du Guide selon la branche.

## Exclusions

- notes sans préfixe `Sofian OS` hors des sept tâches RCU et cinq fichiers actifs nommés ;
- Daily Notes, pièces jointes, caches, plugins et secrets ;
- contenu Epitech ou personnel sans relation explicite ;
- checkout, restauration ou modification Git.

## Règles

- Les deux vaults restent strictement en lecture seule.
- Une date frontmatter n’est pas une date d’exécution sans Git ou autre preuve.
- Un commit automatique n’est pas une validation.
- Ne pas réintroduire les champs legacy dans le canon actuel.

## Sortie

Chaque worker retourne son rapport dans la session. Le coordinateur produit une synthèse suivant `templates/audit-report.md`. Aucune écriture dans le dépôt par défaut.

## Niveau de détail

Rapports claim-level par lot ; synthèse limitée aux décisions, migrations, noms et divergences. Couverture : `33/33 documents + 2/2 historiques` ou blocages nommés.

## Definition of Done

- [ ] lots A–E énumérés et complets ;
- [ ] racines Git et décisions de création établies ;
- [ ] correspondances sans fusion spéculative ;
- [ ] schémas actuels distingués des historiques ;
- [ ] migrations prouvées séparées des intentions ;
- [ ] workflows et niveaux de livraison classés ;
- [ ] timeline et noms cités ;
- [ ] aucun vault modifié.
