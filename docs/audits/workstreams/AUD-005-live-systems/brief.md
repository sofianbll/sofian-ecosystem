---
id: AUD-005
title: Systèmes et implémentations live
status: brief_ready
date: 2026-08-27
owner: Jarvis
output_path: none
source_ids:
  - SRC-LIVE
  - SRC-OBS-ACTIVE
---

# AUD-005 — Systèmes live

## Mission unique

Établir l’état réel, les responsabilités, autorités et niveaux de livraison des systèmes actuellement candidats dans Sofian Ecosystem, sans laisser la documentation historique remplacer le code, la configuration ou le runtime.

## Sujets initiaux

- Sofian OS V4 et adapter Obsidian ;
- TaskNotes ;
- Jarvis et son ou ses dépôts ;
- Hermes ;
- OpenCode ;
- ourmem ;
- Homelab-OS ;
- Finance OS ;
- sources externes uniquement lorsqu’un scénario les mobilise.

Cette liste n’approuve pas les frontières système.

## Méthode et skills

Charger le socle obligatoire du dépôt, `personal-system-reconciliation`, `software-engineering-lifecycle`, `grounded-citations`, puis le skill spécialiste de chaque système. Charger `hermes-agent` pour Hermes et les docs officielles comme autorité produit.

## Stratégie

Créer un sous-audit distinct par sujet ou contrat. Ne jamais envoyer un seul worker auditer tout le système live.

Pour chaque sujet :

1. lire les `AGENTS.md` et sources canoniques ;
2. vérifier Git et configuration ;
3. identifier état persistant, règles, writers et consumers ;
4. distinguer service, projet, adapter, runtime et système ;
5. exercer des lectures ou healthchecks non destructifs ;
6. retrouver les tests et leur oracle ;
7. classer le niveau de livraison ;
8. tester les frontières avec des scénarios réels.

## Questions communes

- Quel besoin durable et quel bénéficiaire ?
- Quels faits sont possédés et comment les corriger ?
- Quels workflows et contrats sont actuels ?
- Quelles copies ou projections peuvent diverger ?
- Quelles permissions et données sensibles ?
- Qu’est-ce qui fonctionne réellement aujourd’hui ?
- Qu’est-ce qui est seulement documenté ou prototypé ?
- Quel coût de maintenance et quel mode de panne ?

## Interdictions

- aucun install, build, restart, déploiement ou commande de device ;
- aucun fichier ou secret lu hors nécessité ;
- aucune requête d’écriture ;
- aucun système déclaré obsolete/legacy ;
- aucune fusion de frontières par commodité.

## Sorties

Retourner dans la session un rapport coordinateur et un dossier par sujet suivant `templates/system-dossier.md`, après contre-audit. Aucune écriture dans le dépôt par défaut.

## Definition of Done

- [ ] chaque sujet possède un sous-périmètre et une source directe ;
- [ ] autorités et correction par fait ;
- [ ] dépendances et contrats ;
- [ ] état live daté ;
- [ ] niveaux de livraison avec preuves ;
- [ ] scénarios normal, conflit et indisponibilité ;
- [ ] inconnues et besoins non couverts ;
- [ ] aucune mutation externe.
