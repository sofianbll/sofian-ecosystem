---
id: AUD-002-CLAIMS
title: AUD-002 — Ledger des claims
status: integrated
date: 2026-08-28
coverage: 94
---

# AUD-002 — Ledger exhaustif des claims

> Annexe intégrée du [rapport AUD-002](report.md). Ces 94 claims ont été retenus après collecte, contre-reviews et normalisations explicites.

### CLM-AUD-002-001

- **Statement :** `Sofian OS V1 - Synthèse Historique` présente V1 comme une première tentative globale visant à centraliser, clarifier et réduire la charge mentale, tout en constatant une architecture trop vaste avant validation d’une routine quotidienne.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS V1
- **Temps du fait :** V1 ; date d’événement non établie par la note
- **Temps d’enregistrement :** 2026-05-08
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V1 - Synthèse Historique.md:18-25
- **Citation / observation :** « première tentative » ; « trop vaste, trop théorique et trop ambitieux avant d’avoir validé une routine simple et stable »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La synthèse ne prouve ni les artefacts originaux complets ni un usage réel.

### CLM-AUD-002-002

- **Statement :** V1 recommande de reprendre dans V3 un hub central, une capture rapide, PARA, TaskNotes, des vues sobres, une inbox et au plus trois tâches importantes par jour, tout en évitant migration totale et automatisation prématurée.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS V1 → V3
- **Temps du fait :** Transition intentionnelle V1 vers V3 ; date d’exécution non établie
- **Temps d’enregistrement :** 2026-05-08
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V1 - Synthèse Historique.md:171-203
- **Citation / observation :** Table « Ce que V3 doit réutiliser » et « Ce que V3 doit éviter »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Il s’agit d’une recommandation historique ; aucune migration ou adoption effective n’est démontrée.

### CLM-AUD-002-003

- **Statement :** V2 est décrite comme une vision long terme de Jarvis personnel et non comme l’implémentation actuelle.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS V2
- **Temps du fait :** V2 ; horizon long terme
- **Temps d’enregistrement :** 2026-05-08
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V2 - Synthèse Jarvis Personnel.md:18-24
- **Citation / observation :** « Cette V2 n’est pas l’implémentation actuelle. Elle sert de direction stratégique »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Cette note ne permet pas de dater l’origine exacte des décisions ni de vérifier leur adoption ultérieure.

### CLM-AUD-002-004

- **Statement :** La vision V2 organise les sources, collecteurs/pipelines, base centrale, agents spécialisés, assistant central et interfaces en couches.
- **État :** historical_intent
- **Sujet littéral :** Architecture V2
- **Temps du fait :** V2 ; horizon long terme
- **Temps d’enregistrement :** 2026-05-08
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V2 - Synthèse Jarvis Personnel.md:45-81
- **Citation / observation :** Diagramme « Sources quotidiennes → Collecteurs et pipelines → Base centrale → Agents spécialisés → Assistant central → Interfaces utilisateur »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le diagramme est conceptuel ; aucun composant exécuté n’est prouvé.

### CLM-AUD-002-005

- **Statement :** V2 reporte explicitement n8n généralisé, PostgreSQL, Telegram Bot, webapp, agents autonomes et synchronisations complexes jusqu’à stabilisation des usages.
- **État :** historical_intent
- **Sujet littéral :** Infrastructure et automatisation V2
- **Temps du fait :** V2 vers V3 ; report intentionnel
- **Temps d’enregistrement :** 2026-05-08
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V2 - Synthèse Jarvis Personnel.md:213-250
- **Citation / observation :** « Ces briques ne sont pas abandonnées. Elles sont simplement repoussées »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le report est déclaré dans la note ; il ne prouve pas l’état actuel.

### CLM-AUD-002-006

- **Statement :** V3 fixe un ordre de conception allant de Systems Thinking à Capability Mapping, Journey Mapping, Service Blueprint, GTD, PARA puis outils.
- **État :** historical_intent
- **Sujet littéral :** Méthode V3
- **Temps du fait :** V3 ; cadrage
- **Temps d’enregistrement :** 2026-05-08
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V3 - Cadres D'Architecture.md:52-89
- **Citation / observation :** Table des cadres et diagramme « Systems Thinking → ... → Outils »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La note documente l’ordre recommandé, pas son application complète.

### CLM-AUD-002-007

- **Statement :** Le modèle V3 distingue le rangement PARA de l’action GTD et définit des capacités telles que capturer, clarifier, décider la prochaine action, suivre les projets, retrouver une information et revoir le système.
- **État :** historical_intent
- **Sujet littéral :** Modèle V3
- **Temps du fait :** V3 ; cadrage
- **Temps d’enregistrement :** 2026-05-08
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V3 - Cadres D'Architecture.md:129-158,233-295
- **Citation / observation :** « Une capacité est stable. Un outil peut changer » ; « PARA ne remplace pas GTD »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les capacités ne sont pas reliées ici à une preuve d’usage.

### CLM-AUD-002-008

- **Statement :** Le workflow V3 `Clarify` conserve `Inbox Item` comme entité temporaire et l’oriente vers Trash, Resource, Aspiration, Task, Project ou une action immédiate selon actionnabilité, engagement et nombre d’actions.
- **État :** historical_intent
- **Sujet littéral :** Workflow Clarify V3
- **Temps du fait :** V3 ; date d’exécution non établie
- **Temps d’enregistrement :** 2026-05-09
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V3 - Clarify Inbox Et Promotion.md:39-57,83-113
- **Citation / observation :** « un Inbox Item ne doit pas être rangé directement » ; sorties du diagramme Clarify
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le diagramme ne prouve pas que des captures ont réellement traversé le workflow.

### CLM-AUD-002-009

- **Statement :** V3 ajoute `Aspiration` pour représenter une envie ou direction non engagée, et autorise promotion vers Project ou demotion depuis Project selon l’engagement et la prochaine action.
- **État :** historical_intent
- **Sujet littéral :** Aspiration et promotion/demotion V3
- **Temps du fait :** V3 ; conception
- **Temps d’enregistrement :** 2026-05-09
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V3 - Clarify Inbox Et Promotion.md:60-79,147-183
- **Citation / observation :** « Aspiration devient une vraie entité » ; règles de promotion et demotion
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le mapping concret et l’usage de cette entité ne sont pas prouvés.

### CLM-AUD-002-010

- **Statement :** Le journal V3 déclare actés le système abstrait avant les outils, Obsidian comme outil et non système, PARA comme couche de rangement, TaskNotes comme cœur des tâches et Bases comme vues simples.
- **État :** historical_intent
- **Sujet littéral :** Décisions V3
- **Temps du fait :** 2026-05-08 déclaré dans la note
- **Temps d’enregistrement :** 2026-05-08
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V3 - Journal De Décisions.md:50-66
- **Citation / observation :** Table des décisions : statut « Actée » pour ces éléments
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** « Actée » est le statut interne de cette note, pas une preuve indépendante d’acceptation par Sofian.

### CLM-AUD-002-011

- **Statement :** Le cadrage V3 décrit V1 comme à synthétiser, V2 comme à synthétiser et V3 comme « En cadrage », et signale des frictions de cohérence dans Daily Notes, Inbox, frontmatter et références `.base`.
- **État :** historical_intent
- **Sujet littéral :** État déclaré du cadrage V3
- **Temps du fait :** V3 au 2026-05-08 déclaré
- **Temps d’enregistrement :** 2026-05-08
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V3 - Mémoire De Cadrage Initial.md:41-67
- **Citation / observation :** Table V1/V2/V3 et section « Points de friction »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** C’est un diagnostic déclaré, sans contre-vérification dans le vault actif pour ce lot.

### CLM-AUD-002-012

- **Statement :** V4 définit un Domain Core indépendant d’Obsidian avec les entités `Inbox Item`, `Area`, `Aspiration`, `Project`, `Task` et `Resource`, ainsi que leurs relations principales.
- **État :** historical_intent
- **Sujet littéral :** Domain Core V4
- **Temps du fait :** V4 ; 2026-05-15 déclaré
- **Temps d’enregistrement :** 2026-05-15
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Domain Core.md:19-50
- **Citation / observation :** Table des entités et diagramme ERD
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence du modèle ne prouve pas une implémentation ou validation de données.

### CLM-AUD-002-013

- **Statement :** Dans V4, `Commands / Workflows` modifient l’état, `Queries` lisent sans modification et `Dashboards` composent des queries ; l’Operating Layer utilise les dashboards et déclenche les commands.
- **État :** historical_intent
- **Sujet littéral :** Application Core V4
- **Temps du fait :** V4 ; 2026-05-15 déclaré
- **Temps d’enregistrement :** 2026-05-15
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Application Core.md:26-45,60-81
- **Citation / observation :** Diagramme des sous-couches et tableau « Modifie l’état ? »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le contrat est documentaire ; aucun appel ou effet observé.

### CLM-AUD-002-014

- **Statement :** V4 sépare explicitement Queries et Dashboards, avec `Calendar` comme query et des dashboards Home, Daily, Engage, Weekly Review, Project, Resource Library, Aspirations et Inbox Processing.
- **État :** historical_intent
- **Sujet littéral :** Queries et Dashboards V4
- **Temps du fait :** V4 ; 2026-05-15 déclaré
- **Temps d’enregistrement :** 2026-05-15
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Dashboards.md:36-57; Backend/Resources/Sofian OS V4 - Queries.md:34-73
- **Citation / observation :** Règles de séparation et table des dashboards/queries
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les noms et compositions sont documentés, pas rendus ni vérifiés sur des données.

### CLM-AUD-002-015

- **Statement :** Le workflow V4 `Capture` interdit la décision métier au moment de la capture et produit un `Inbox Item`; `Clarify` choisit ensuite la destination et refuse les Tasks floues ou les Projects sans résultat attendu.
- **État :** historical_intent
- **Sujet littéral :** Capture et Clarify V4
- **Temps du fait :** V4 ; 2026-05-13 déclaré
- **Temps d’enregistrement :** 2026-05-13
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Workflows.md:60-143
- **Citation / observation :** Rules de Capture et Outputs/Mini-flow de Clarify
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucun cas réel n’est fourni dans le corpus.

### CLM-AUD-002-016

- **Statement :** Le workflow V4 `Create Task` exige une action visible et une Area, distingue `due_date` comme deadline réelle de `scheduled_date` comme date d’apparition/reprise, et propose `Anywhere`, `Low` et `Todo` par défaut.
- **État :** historical_intent
- **Sujet littéral :** Create Task V4
- **Temps du fait :** V4 ; 2026-05-13 déclaré
- **Temps d’enregistrement :** 2026-05-13
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Workflows.md:147-221
- **Citation / observation :** Rules et Output de `Create Task`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les valeurs sont des règles de workflow, sans preuve d’alignement live avec TaskNotes.

### CLM-AUD-002-017

- **Statement :** Le mapping `Interface Adapter Obsidian` relie Task/Project/Resource/Area/Inbox aux conventions de notes du vault et laisse `Aspiration` non finalisée.
- **État :** historical_intent
- **Sujet littéral :** Interface Adapter Obsidian V4
- **Temps du fait :** V4 ; 2026-05-15 déclaré
- **Temps d’enregistrement :** 2026-05-15
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Interface Adapter Obsidian.md:43-52
- **Citation / observation :** Table « Mapping Conceptuel Vers Vault Actuel » ; `Aspiration` « à définir »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le mapping est conceptuel ; le vault actif et l’exercice de l’adapter sont hors corpus.

### CLM-AUD-002-018

- **Statement :** Le mapping V4 laisse `start_date` et `finished_date` non standardisés et `Paused`/`Dropped` non mappés dans TaskNotes.
- **État :** historical_intent
- **Sujet littéral :** Statuts et dates V4 vers Obsidian
- **Temps du fait :** V4 ; 2026-05-15 déclaré
- **Temps d’enregistrement :** 2026-05-15
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Interface Adapter Obsidian.md:56-79
- **Citation / observation :** « pas encore standardisé » ; « à définir » ; « Décision à prendre »
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-002-319", "CLM-AUD-002-320"]
- **Review :** accepted
- **Limite :** La contradiction porte sur l’état de finalisation, pas nécessairement sur le design logique.

### CLM-AUD-002-020

- **Statement :** `Sofian OS V4 - Travail Restant` marque comme faits les entités, propriétés, relations, les notes canon V4, les commands minimum, les queries minimum et les dashboards minimum.
- **État :** historical_intent
- **Sujet littéral :** État déclaratif V4
- **Temps du fait :** V4 ; note datée 2026-05-13
- **Temps d’enregistrement :** 2026-05-13
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Travail Restant.md:42-106,119-215
- **Citation / observation :** Cases `[x]` et liste des notes V4
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Une case cochée et une note existante prouvent seulement une documentation déclarée.

### CLM-AUD-002-021

- **Statement :** Le même document laisse `Inbox Processing`, `Daily Review`, `Weekly Review` et `Engage` non cochés dans l’Operating Layer et laisse les adapters futurs non définis.
- **État :** historical_intent
- **Sujet littéral :** Operating Layer et adapters V4
- **Temps du fait :** V4 ; note datée 2026-05-13
- **Temps d’enregistrement :** 2026-05-13
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Travail Restant.md:216-300
- **Citation / observation :** Cases `[ ]` pour les routines et adapters
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’absence de case cochée ne prouve pas qu’aucune routine n’a jamais été exécutée ; elle établit seulement l’état déclaré de cette note.

### CLM-AUD-002-022

- **Statement :** La source V4 `Workflows` spécifie Capture, Clarify, Create Task, Create Project et Create/Qualify Resource avec triggers, inputs, règles, outputs et mini-flows, mais ne fournit aucune preuve de traversée réelle.
- **État :** historical_intent
- **Sujet littéral :** Workflows V4
- **Temps du fait :** V4 ; 2026-05-13 déclaré
- **Temps d’enregistrement :** 2026-05-13
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Workflows.md:20-56,60-369
- **Citation / observation :** Format standard et cinq workflows détaillés
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La spécification ne monte pas le niveau au-delà de documented.

### CLM-AUD-002-023

- **Statement :** Le corpus ne contient aucune preuve directe de migration exécutée entre `Sofian's Vault` et le vault actif, de copie sélective, de refonte de schéma effectivement déployée, d’usage quotidien ou de validation utilisateur.
- **État :** unknown
- **Sujet littéral :** Filiation et migration des vaults
- **Temps du fait :** 2026-05-04..2026-08-27 ; non établi par le lot A
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-OLD
- **Locator :** Corpus exact des 19 fichiers ; exclusions du brief AUD-002 A
- **Citation / observation :** Le lot A contient des synthèses et modèles ; le brief exclut Git, liens et vault actif
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ce claim est une limite de couverture : il ne conclut pas que la migration n’a jamais eu lieu.

### CLM-AUD-002-024

- **Statement :** Les dates frontmatter 2026-05-08, 2026-05-09, 2026-05-13 et 2026-05-15 sont des dates déclarées d’enregistrement des notes ; elles ne suffisent pas à dater l’exécution des décisions ou workflows.
- **État :** historical_intent
- **Sujet littéral :** Temps des documents historiques
- **Temps du fait :** Dates déclarées des 19 notes
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-OLD
- **Locator :** Frontmatter de chacun des 19 fichiers ; exemples Backend/Resources/Sofian OS V1 - Synthèse Historique.md:1-5 et V4 - Workflows.md:1-5
- **Citation / observation :** Champ `Date` présent dans les notes ; absence de preuve d’exécution associée
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucun historique Git n’a été consulté selon le périmètre demandé.

### CLM-AUD-002-025

- **Statement :** Dans le corpus A, le vocabulaire évolue d’un OS personnel global (V1), vers Jarvis personnel et agents (V2), puis vers capacités/workflows et entité Aspiration (V3), enfin vers layers Domain/Application/Operating/Adapter (V4).
- **État :** historical_intent
- **Sujet littéral :** Filiation des noms et vocabulaires V1–V4
- **Temps du fait :** V1→V4 ; séquence documentaire 2026-05-08..2026-05-15
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-OLD
- **Locator :** V1:47-66; V2:18-41; V3 Cadres:52-62; V3 Clarify:39-79; V4 Architecture Référence:40-87
- **Citation / observation :** Évolution des titres, entités, cadres et layers dans les documents lus
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La proximité des dates et des thèmes établit une séquence documentaire, pas l’identité certaine de tous les artefacts externes.

### CLM-AUD-002-026

- **Statement :** V4 documente une séparation de responsabilité cohérente entre Governance/Intent, Domain Core, Application Core, Operating Layer, Interface Adapter, Infrastructure et Automation/Agents.
- **État :** historical_intent
- **Sujet littéral :** Architecture en layers V4
- **Temps du fait :** V4 ; 2026-05-15 déclaré
- **Temps d’enregistrement :** 2026-05-15
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/Sofian OS V4 - Architecture Référence.md:40-68
- **Citation / observation :** Diagramme en sept layers et notes associées
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le document précise un flux conceptuel ; il ne prouve pas des dépendances de code.

### CLM-AUD-002-027

- **Statement :** Le statut concret d’`Aspiration` dans l’interface Obsidian reste indéterminé alors que l’entité est définie dans le Domain Core et le workflow Clarify.
- **État :** unknown
- **Sujet littéral :** Aspiration V3/V4
- **Temps du fait :** V3→V4 ; non résolu au 2026-05-15 déclaré
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-OLD
- **Locator :** V3 Clarify:60-79; V4 Domain Core:24-33; V4 Interface Adapter:43-52; V4 Journal:66-72
- **Citation / observation :** Entité définie en V3/V4 mais mapping « à définir » et décision reportée
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-002-319"]
- **Review :** accepted
- **Limite :** Le corpus n’inclut pas le vault actif ni une décision ultérieure.

### CLM-AUD-002-028

- **Statement :** Les niveaux de livraison démontrables pour le lot A restent au maximum `documented` pour les modèles, décisions, workflows et mappings ; aucune preuve du corpus ne justifie `technically_tested`, `integrated`, `exercised_real_case`, `user_accepted` ou `operational`.
- **État :** unknown
- **Sujet littéral :** Niveaux de livraison V1–V4
- **Temps du fait :** Corpus du lot A
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-OLD
- **Locator :** 19 fichiers lus ; evidence-model du dépôt ; locators individuels dans document_matrix
- **Citation / observation :** Les sources contiennent textes, tableaux, diagrammes et checklists, mais aucune commande, sortie, cas réel ou validation utilisateur
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le niveau réel pourrait être supérieur dans d’autres sources exclues du lot A.

### CLM-AUD-002-100

- **Statement :** Le Git de `SRC-OBS-OLD` enregistre l’ajout de `PLAN - Nouvelle Organisation Vault.md` au commit `f0c0862` le 2026-05-04.
- **État :** historical_execution
- **Sujet littéral :** PLAN - Nouvelle Organisation Vault.md
- **Temps du fait :** État d’ajout du fichier dans l’ancien vault
- **Temps d’enregistrement :** 2026-05-04 13:10:10 +0200
- **Source :** SRC-OBS-OLD
- **Locator :** commit f0c0862d54d34c8d0134e088f5ce28715eedf6bc — Backend/Resources/PLAN - Nouvelle Organisation Vault.md
- **Citation / observation :** Git indique `A` et 514 insertions pour ce chemin.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’ajout Git ne prouve ni la date de rédaction réelle ni l’exécution du plan.

### CLM-AUD-002-101

- **Statement :** La note `PLAN - Nouvelle Organisation Vault.md` porte la date frontmatter `Date: 2026-02-16`, antérieure à son ajout Git vérifiable du 2026-05-04.
- **État :** historical_intent
- **Sujet littéral :** PLAN - Nouvelle Organisation Vault.md
- **Temps du fait :** Date déclarée par la note : 2026-02-16
- **Temps d’enregistrement :** 2026-05-04 (commit d’ajout vérifié)
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/PLAN - Nouvelle Organisation Vault.md:1-10
- **Citation / observation :** Frontmatter : `Date: 2026-02-16`; commit d’ajout : `f0c0862`, 2026-05-04.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La relation entre la date frontmatter et l’événement de rédaction n’est pas établie.

### CLM-AUD-002-102

- **Statement :** Le plan formule comme objectif une réorganisation simple et fonctionnelle de l’ancien vault, adaptée au TDAH, avec une routine quotidienne de cinq minutes.
- **État :** historical_intent
- **Sujet littéral :** PLAN - Nouvelle Organisation Vault.md
- **Temps du fait :** Plan daté 2026-02-16
- **Temps d’enregistrement :** 2026-05-04 (fichier Git vérifié)
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/PLAN - Nouvelle Organisation Vault.md:12-17
- **Citation / observation :** Le résumé indique : « guide complet pour restructurer ton vault », « vault simple, fonctionnel, adapté au TDAH » et « review quotidienne de 5 min ».
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Il s’agit de l’intention déclarée du plan, pas d’un résultat observé.

### CLM-AUD-002-103

- **Statement :** Le plan propose une structure PARA avec `00 - Inbox/`, un `Backend/` structuré, des projets, tâches, ressources, archives, templates et une migration progressive depuis Notion.
- **État :** historical_intent
- **Sujet littéral :** PLAN - Nouvelle Organisation Vault.md
- **Temps du fait :** Plan daté 2026-02-16
- **Temps d’enregistrement :** 2026-05-04 (fichier Git vérifié)
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/PLAN - Nouvelle Organisation Vault.md:119-178; 375-407
- **Citation / observation :** Sections « Architecture Finale », « Règles de placement » et « Migration Notion → Obsidian » décrivent ces éléments comme structure ou étapes prévues.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le libellé « Architecture Finale » reste celui d’un document de planification ; aucune mise en œuvre correspondante n’est prouvée par ce lot.

### CLM-AUD-002-104

- **Statement :** Les phases de nettoyage, migration des archives, configuration, migration Notion et routines du plan sont présentées sous forme de cases non cochées.
- **État :** historical_intent
- **Sujet littéral :** PLAN - Nouvelle Organisation Vault.md
- **Temps du fait :** État de la checklist dans la version Git du 2026-05-04
- **Temps d’enregistrement :** 2026-05-04 (commit d’ajout vérifié)
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Resources/PLAN - Nouvelle Organisation Vault.md:322-371; 466-507
- **Citation / observation :** Les actions listées sont marquées `- [ ]`, notamment les phases 1 à 6 et les migrations proposées.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Une case non cochée dans cette version ne permet pas de conclure sur une exécution ultérieure hors du lot.

### CLM-AUD-002-105

- **Statement :** Le projet a d’abord été enregistré sous le chemin `Backend/Projects/Sofian OS V3 - Architecture Système.md` au commit `5ddc27b` du 2026-05-09.
- **État :** historical_execution
- **Sujet littéral :** Sofian OS V3 - Architecture Système.md
- **Temps du fait :** Création Git du document
- **Temps d’enregistrement :** 2026-05-09 14:07:35 +0200
- **Source :** SRC-OBS-OLD
- **Locator :** commit 5ddc27b9defa49aa9284ae9e7e7789ec621bd63d — Backend/Projects/Sofian OS V3 - Architecture Système.md
- **Citation / observation :** Le commit enregistre `A` pour le chemin V3 et contient la note de projet avec `Status: In-Progress` et `Scheduled Date: 2026-05-08`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La date planifiée n’est pas une preuve de réalisation ni de validation.

### CLM-AUD-002-106

- **Statement :** Le document a été renommé à 100 % de `Backend/Projects/Sofian OS V3 - Architecture Système.md` vers `Backend/Projects/Sofian OS.md` au commit `b73652d` le 2026-05-09.
- **État :** historical_execution
- **Sujet littéral :** Sofian OS.md
- **Temps du fait :** Renommage Git du document
- **Temps d’enregistrement :** 2026-05-09 18:22:06 +0200
- **Source :** SRC-OBS-OLD
- **Locator :** commit b73652d008c8ea7e219d614d302b5e998d51e6f6 — rename R100
- **Citation / observation :** Git indique `R100` entre les deux chemins.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le renommage établit une filiation de fichier, pas une filiation complète de système ou de vault.

### CLM-AUD-002-107

- **Statement :** La note de projet décrit comme objectif une architecture de `Sofian OS` indépendante des outils, avec Obsidian comme outil actuel et non comme système final.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS
- **Temps du fait :** Version du projet créée le 2026-05-09
- **Temps d’enregistrement :** 2026-05-09 (commit de création vérifié)
- **Source :** SRC-OBS-OLD
- **Locator :** Backend/Projects/Sofian OS.md:16-36
- **Citation / observation :** Objectif : « architecture propre de Sofian OS, indépendante des outils » ; contexte : « Obsidian est l’outil actuel, pas le système final ».
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La note est dans l’ancien vault et ne constitue pas à elle seule le canon actuel.

### CLM-AUD-002-108

- **Statement :** Entre le 2026-05-09 et le 2026-05-13, la note passe d’un cadrage V3 à un cadrage V4 : V1 à V3 sont marquées `Synthétisé`, V4 `En cours`, et des éléments d’architecture/workflows sont placés dans un encart interne `Validé`.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS V4
- **Temps du fait :** Évolution documentaire vérifiée le 2026-05-13
- **Temps d’enregistrement :** 2026-05-13 19:57:50 +0200 (commit 4196b59)
- **Source :** SRC-OBS-OLD
- **Locator :** commit 4196b59 — Backend/Projects/Sofian OS.md:22-73 dans cette version
- **Citation / observation :** Le diff remplace `Sofian OS V3` par `Sofian OS V4`, ajoute la ligne `V4 ... En cours` et la section `[!success] Validé` avec architecture en layers, Obsidian adapter et workflows.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** `Validé` est un statut écrit dans la note ; il ne prouve pas une décision utilisateur comprise ni une validation externe.

### CLM-AUD-002-109

- **Statement :** La dernière modification ciblée du projet, au commit `1cb5b6e` du 2026-05-15, ajoute la documentation V4 structurée par layer et remplace les prochaines étapes par relecture/validation des notes canon V4, nettoyage visuel et mapping Obsidian après validation du modèle.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS.md
- **Temps du fait :** État documentaire au 2026-05-15
- **Temps d’enregistrement :** 2026-05-15 14:27:03 +0200
- **Source :** SRC-OBS-OLD
- **Locator :** commit 1cb5b6e32ca881926140ab2e040bf60b4d857aa5 — Backend/Projects/Sofian OS.md:60-91
- **Citation / observation :** Le diff ajoute `Documentation canonique V4 structurée par layer` et les étapes `Relire et valider les notes canon V4` puis `Définir le mapping Obsidian concret après validation du modèle`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence de liens et de prochaines étapes ne prouve pas que les notes liées ont été validées, intégrées ou utilisées.

### CLM-AUD-002-110

- **Statement :** Dans le corpus limité aux deux notes et à leurs historiques Git ciblés, aucune preuve explicite de migration exécutée entre les vaults, d’usage opérationnel maintenu ou de validation utilisateur n’a été retrouvée.
- **État :** unknown
- **Sujet littéral :** Lot B — historique des deux objets
- **Temps du fait :** Corpus vérifié jusqu’au HEAD `fec7744` du 2026-07-17
- **Temps d’enregistrement :** 2026-08-28 (lecture directe et vérification Git)
- **Source :** SRC-OBS-OLD
- **Locator :** Les deux chemins exacts ; `git log --follow` et lecture directe des versions courante/création
- **Citation / observation :** Les documents contiennent des intentions, statuts internes, liens et checklists ; aucune signature, décision utilisateur, trace d’usage ou preuve de migration n’est fournie dans ce corpus.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Cette inconnue ne signifie pas que l’action n’a jamais eu lieu ailleurs ; les autres sources sont hors mission.

### CLM-AUD-002-201

- **Statement :** Les sept notes portent le type `✏️ Task`, le domaine `[[🏠 Perso]]`, le projet `[[Sofian OS - Revue Correction Update]]`, le contexte `computer` et `is_template: false`.
- **État :** current_canon
- **Sujet littéral :** Métadonnées communes des sept TaskNotes RCU
- **Temps du fait :** État courant des fichiers lus
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Chaque fichier TaskNote, frontmatter lignes 1-17 environ
- **Citation / observation :** Les sept frontmatters commencent par `type: ✏️ Task`, référencent le même projet et indiquent `is_template: false`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence des propriétés ne prouve pas que les liens ou le projet référencé sont encore opérationnels.

### CLM-AUD-002-202

- **Statement :** Les statuts courants enregistrés sont `done` pour les phases 0, 1, 2, 4, 5 et 6, et `in_progress` pour la phase 3.
- **État :** current_canon
- **Sujet littéral :** Statuts frontmatter des sept TaskNotes RCU
- **Temps du fait :** État courant des fichiers lus
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Frontmatter : Phase 0:9, Phase 1:9, Phase 2:9, Phase 3:9, Phase 4:9, Phase 5:9, Phase 6:9
- **Citation / observation :** Les six notes indiquent `status: done`; `Sofian OS RCU - Phase 3 Cockpit Quotidien.md` indique `status: in_progress`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Un statut TaskNotes est l'état enregistré du fichier, pas une preuve d'acceptation ou d'usage maintenu.

### CLM-AUD-002-203

- **Statement :** Les phases 0 à 5 sont planifiées le 2026-06-21 et la phase 6 le 2026-06-26 ; les champs de fin ne sont pas homogènes entre les notes.
- **État :** current_canon
- **Sujet littéral :** Planification et dates de fin des sept TaskNotes RCU
- **Temps du fait :** Dates enregistrées dans les frontmatters
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Frontmatter des sept notes, champs `scheduled_date`, `completed_date`, `finished_date` et `done_date`
- **Citation / observation :** Phases 0,1,2,3,4,5 : `scheduled_date: 2026-06-21`; phase 6 : `scheduled_date: 2026-06-26`. Les notes utilisent respectivement `completed_date`, `finished_date`, aucun champ de fin, et `done_date`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La divergence de nommage est observée, mais sa conformité au schéma complet TaskNotes n'a pas été auditée dans ce lot.

### CLM-AUD-002-204

- **Statement :** La phase 0 vise à corriger le diagnostic avant exécution et à produire une table de vérité des projets, reliant état réel, état du vault et action à prendre.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS RCU - Phase 0 Reality Recalage
- **Temps du fait :** Phase 0, documentée le 2026-06-21
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 0 Reality Recalage.md:25-39
- **Citation / observation :** `Corriger le diagnostic avant toute exécution` ; Target Outcome : `Une table vérité existe pour les projets majeurs : état réel, état vault, action à prendre.`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L'objectif et le tableau sont documentés ; la note ne fournit pas ici la preuve indépendante de l'exécution complète.

### CLM-AUD-002-205

- **Statement :** La phase 0 enregistre une validation reçue et reporte volontairement les changements de statut des anciens projets à la phase 2.
- **État :** historical_execution
- **Sujet littéral :** Checkpoint de validation de Phase 0
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 0 Reality Recalage.md:52-64
- **Citation / observation :** `Validation reçue` ; `Les changements précis de statut ... sont volontairement différés à la Phase 2`.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La TaskNote rapporte une validation mais ne constitue pas la conversation utilisateur originale ni une preuve indépendante d'acceptation.

### CLM-AUD-002-206

- **Statement :** La phase 1 vise à définir le rangement des artefacts BMAD, Superpowers, Graphify, skills, contextes IA, projets externes et synthèses durables, avec une règle de destination canonique ou externe.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS RCU - Phase 1 Architecture Chantiers
- **Temps du fait :** Phase 1, documentée le 2026-06-21
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 1 Architecture Chantiers.md:25-41
- **Citation / observation :** `Définir où vont les artefacts...` ; Target Outcome : `Une règle simple dit quoi ranger dans Sofian OS, quoi garder externe, quoi archiver et quoi ignorer.`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La règle nommée `Sofian OS - Artifact Placement Rules` n'a pas été lue dans ce corpus fermé.

### CLM-AUD-002-207

- **Statement :** La phase 1 consigne comme sorties les destinations `98-Backend/Resources`, `98-Backend/Tasks`, `98-Backend/Projects`, `graphify-out` et le maintien des runtimes `.opencode`, `.claude`, `.agent` hors du vault ou ignorés.
- **État :** historical_execution
- **Sujet littéral :** Règles de placement enregistrées par Phase 1
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 1 Architecture Chantiers.md:43-66
- **Citation / observation :** Les cinq cases DoD correspondantes sont cochées et la note indique `git diff --check OK` et `Aucun champ legacy détecté`.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les fichiers et la sortie de commande cités n'ont pas été audités dans W-C ; cette claim conserve uniquement ce que la TaskNote rapporte.

### CLM-AUD-002-208

- **Statement :** La phase 2 vise à aligner projets, tâches, ressources et aspirations sur la réalité validée ; son journal rapporte notamment le maintien de Codename en `in_progress`, le maintien de Corelab en `done`, la fusion de Homelab Lenovo dans Homelab OS, et le maintien de Project - Media Pipeline en `paused`.
- **État :** historical_execution
- **Sujet littéral :** Sofian OS RCU - Phase 2 Reconciliation Vault
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 2 Reconciliation Vault.md:25-54
- **Citation / observation :** Target Outcome : `Les projets actifs ont une prochaine action claire...` ; journal de décisions daté du 2026-06-21.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les notes et tâches touchées sont explicitement hors corpus W-C ; les changements rapportés ne sont donc pas contre-vérifiés ici.

### CLM-AUD-002-209

- **Statement :** La phase 2 rapporte comme vérifications l'existence de `Project Tasks Board.base` et `Project Resources.base`, un inventaire des projets actifs avec tâche ouverte liée, et un `git diff --check` réussi.
- **État :** historical_execution
- **Sujet littéral :** Vérification enregistrée de Phase 2
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 2 Reconciliation Vault.md:56-73
- **Citation / observation :** La section `Verification 2026-06-21` liste les deux Bases, l'inventaire et `git diff --check passed`.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ces résultats sont auto-déclarés par la TaskNote ; aucun Base, projet ou commande n'a été relu dans le corpus fermé.

### CLM-AUD-002-210

- **Statement :** La phase 3 vise un cockpit quotidien permettant de savoir quoi faire maintenant, quoi clarifier, quoi repousser et quoi revoir ; elle enregistre la création de Bases avancées, le branchement de dashboards et la préparation d'un journal de validation réelle.
- **État :** historical_execution
- **Sujet littéral :** Sofian OS RCU - Phase 3 Cockpit Quotidien
- **Temps du fait :** Depuis le 2026-06-21
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 3 Cockpit Quotidien.md:24-47
- **Citation / observation :** La note liste `By Context`, `High Priority`, `Projects Without Next Action`, `Orphan Resources`, `Aspirations`, `Aspirations Review Candidates` et les dashboards branchés.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La note indique elle-même que la routine avec de vraies notes n'est pas cochée ; aucune validation d'usage réel n'est prouvée.

### CLM-AUD-002-211

- **Statement :** La phase 4 vise un graphe Graphify utile et borné à `98-Backend`, et son DoD rapporte un detect, un scope, trois fichiers dans `graphify-out`, la lecture des insights et un rythme d'update.
- **État :** historical_execution
- **Sujet littéral :** Sofian OS RCU - Phase 4 Graphify Memoire
- **Temps du fait :** Phase 4, jusqu'au 2026-06-30 selon frontmatter
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 4 Graphify Memoire.md:25-47
- **Citation / observation :** DoD coché : `GRAPH_REPORT.md`, `graph.json` et `graph.html` existent dans `graphify-out`.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les trois outputs et le rythme ne sont pas relus dans W-C ; la claim ne monte pas au niveau opérationnel actuel.

### CLM-AUD-002-212

- **Statement :** La phase 5 rapporte que `tasknotes/data.json` contient des champs OAuth Google/Microsoft, est tracké par Git et est exposé au risque d'auto-commit chaque minute ; elle laisse le nettoyage des secrets en projet futur.
- **État :** historical_execution
- **Sujet littéral :** Sofian OS RCU - Phase 5 Ecosysteme Tooling
- **Temps du fait :** 2026-06-25
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 5 Ecosysteme Tooling.md:41-58, 68-74
- **Citation / observation :** La note décrit le risque `HIGH`, `autoSaveInterval: 1`, et l'item ouvert `tasknotes/data.json OAuth secrets` en attente.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune valeur secrète n'est affichée ; la configuration du plugin est explicitement hors corpus et n'a pas été relue.

### CLM-AUD-002-213

- **Statement :** La phase 5 contient une contradiction interne : son DoD coche que les configurations sensibles ne sont pas exposées et qu'Obsidian Git ne pousse pas de secret, tandis que ses findings et open items décrivent des secrets OAuth trackés et un nettoyage futur non réalisé.
- **État :** contradicted
- **Sujet littéral :** DoD et findings de Sofian OS RCU - Phase 5 Ecosysteme Tooling
- **Temps du fait :** 2026-06-25
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 5 Ecosysteme Tooling.md:43-58, 60-74
- **Citation / observation :** `[x] Les configs sensibles ne sont pas exposées dans un commit` suivi de `PENDING`, contre `OAuth secrets` et `auto-commit ... chaque minute` dans les sections précédentes et ouvertes.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La contradiction est textuelle et interne à la TaskNote ; sa résolution exige la lecture autorisée de la configuration et une décision, hors de W-C.

### CLM-AUD-002-214

- **Statement :** La phase 6 rapporte quatre étapes cochées : canonisation opérationnelle, vault lint, mise à jour de la note projet/du plan et commit dédié.
- **État :** historical_execution
- **Sujet littéral :** RCU Phase 6 — Canonisation Finale Vault Lint Handoff
- **Temps du fait :** 2026-06-26..2026-06-27
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** RCU Phase 6 — Canonisation Finale Vault Lint Handoff.md:17-49
- **Citation / observation :** Les sections Step 1 à Step 4 portent toutes `[x]`; Step 4 mentionne le message `feat: Phase 6 canonisation finale + vault lint + handoff`.
- **Confiance :** medium
- **Contradictions :** ["CLM-AUD-002-215"]
- **Review :** accepted
- **Limite :** Le commit et les fichiers canonisés n'ont pas été inspectés dans ce lot ; le texte ne prouve pas la validation utilisateur ni l'opérationnalité.

### CLM-AUD-002-215

- **Statement :** La même phase 6 conserve une section Verification entièrement non cochée pour le diff, le lint legacy, l'état Git, la note projet et l'alignement du plan.
- **État :** current_canon
- **Sujet littéral :** Verification courante de RCU Phase 6
- **Temps du fait :** État du fichier lu
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** RCU Phase 6 — Canonisation Finale Vault Lint Handoff.md:59-65
- **Citation / observation :** Les cinq lignes de `Verification` commencent par `[ ]`.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-002-214"]
- **Review :** accepted
- **Limite :** Cela établit un état documentaire non coché, pas l'échec réel des contrôles ; les contrôles n'ont pas été relancés par respect de la frontière.

### CLM-AUD-002-216

- **Statement :** La phase 0 présente une divergence de nom littéral entre `[[My Bentofolio]]` dans la Reality Table et `My Portfolio` dans la Definition Of Done.
- **État :** contradicted
- **Sujet littéral :** Identité de projet dans Sofian OS RCU - Phase 0 Reality Recalage
- **Temps du fait :** Phase 0, documentée le 2026-06-21
- **Temps d’enregistrement :** 2026-08-28 (note actuelle)
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Sofian OS RCU - Phase 0 Reality Recalage.md:43-50, 58-64
- **Citation / observation :** Reality Table : `[[My Bentofolio]]`; DoD : ``My Portfolio``.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Cette divergence ne permet pas d'identifier silencieusement deux projets comme identiques ; aucune autre note de projet n'a été lue dans W-C.

### CLM-AUD-002-301

- **Statement :** `Sofian-OS` est documenté comme le vault Obsidian actif et `Sofian's Vault` comme une histoire en lecture seule.
- **État :** current_canon
- **Sujet littéral :** Sofian-OS et Sofian's Vault
- **Temps du fait :** État documenté par les fichiers actuels
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** AGENTS.md:3-8; Journal De Décisions.md:94-100
- **Citation / observation :** `Sofian-OS` est décrit comme le vault actif ; l'ancien vault ne doit pas être modifié et reste une archive historique.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Cette relation documentaire ne prouve pas une migration, une copie complète ou un usage opérationnel.

### CLM-AUD-002-302

- **Statement :** Le vault actif n'est pas documenté comme une application conventionnelle : aucun `package.json`, script de build, test runner ou workflow CI racine n'est déclaré.
- **État :** current_canon
- **Sujet littéral :** Repo Shape de Sofian-OS
- **Temps du fait :** État déclaré par AGENTS.md
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** AGENTS.md:3-7
- **Citation / observation :** `not a conventional app package` ; `no root package.json, build script, test runner, or CI workflow`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** C'est une déclaration d'instructions locales ; aucun inventaire externe du vault n'a été effectué dans ce lot.

### CLM-AUD-002-303

- **Statement :** Les notes Markdown, fichiers `.base`, configuration `.obsidian` et templates sont définis comme l'implémentation du vault, avec priorité aux sources exécutables ou de configuration en cas de divergence avec la prose.
- **État :** current_canon
- **Sujet littéral :** Médiums d'implémentation Sofian-OS
- **Temps du fait :** État documenté par AGENTS.md
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** AGENTS.md:5-7
- **Citation / observation :** `Treat Markdown notes, .base files, .obsidian/ config, and templates as the implementation.`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La priorité est une règle documentaire ; son application sur des divergences concrètes n'a pas été testée.

### CLM-AUD-002-304

- **Statement :** Le périmètre structurel documenté sépare `00-Inbox/`, `01-Dashboards/`, `98-Backend/` et `99-System/` par responsabilités distinctes.
- **État :** current_canon
- **Sujet littéral :** Frontières de dossiers Sofian-OS
- **Temps du fait :** État déclaré par AGENTS.md
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** AGENTS.md:7
- **Citation / observation :** Les quatre dossiers sont associés respectivement aux captures, surfaces, données/templates/bases/ressources/tâches et schémas/décisions/handoffs/registre.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence et la cohérence de tous ces sous-contenus n'ont pas été auditées dans le lot fermé.

### CLM-AUD-002-305

- **Statement :** Les propriétés et statuts canoniques sont documentés en `lower_snake_case`, avec statuts `todo`, `in_progress`, `paused`, `done`, `dropped`, priorités `low`, `medium`, `high`, et `is_template: false` pour les notes réelles.
- **État :** current_canon
- **Sujet littéral :** Schéma de métadonnées Sofian-OS
- **Temps du fait :** État déclaré par AGENTS.md
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** AGENTS.md:18-24
- **Citation / observation :** Les champs legacy Title Case sont bannis ; les valeurs canoniques et `is_template: false` sont explicités.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le schéma complet référencé et l'ensemble des notes ne font pas partie de ce lot.

### CLM-AUD-002-306

- **Statement :** TaskNotes est documenté comme l'autorité des tâches ; les Bases et dashboards sont des surfaces de lecture et ne doivent pas créer de TaskNotes complètes.
- **État :** current_canon
- **Sujet littéral :** Autorité des tâches
- **Temps du fait :** État déclaré par AGENTS.md
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** AGENTS.md:26-31; V4 Obsidian Adapter Mapping.md:166-173
- **Citation / observation :** Les tâches vivent dans `98-Backend/Tasks` et sont gérées par TaskNotes ; Base Board sert à visualiser, pas à créer les tâches complètes.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La résolution réelle des vues et actions TaskNotes n'a pas été exercée.

### CLM-AUD-002-307

- **Statement :** Les règles de sécurité et de vérification interdisent l'exposition des secrets et indiquent qu'il n'existe pas de commande repo-wide de build/test/lint pour ce vault.
- **État :** current_canon
- **Sujet littéral :** Sécurité et vérification locale
- **Temps du fait :** État déclaré par AGENTS.md
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** AGENTS.md:47-58
- **Citation / observation :** Les chemins secrets sont explicitement protégés ; pour Markdown-only, la vérification indiquée est `git diff --check -- <paths>`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucun test n'a été relancé, conformément à la frontière stricte du brief.

### CLM-AUD-002-308

- **Statement :** `Sofian OS V4 - Architecture Référence.md` se présente comme le point d'entrée canonique de V4, tandis que les anciennes notes sont conservées comme sources historiques.
- **État :** current_canon
- **Sujet littéral :** Point d'entrée V4
- **Temps du fait :** État documenté par la note actuelle
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Architecture Référence.md:1-20
- **Citation / observation :** La note se décrit comme `point d'entrée canonique` et indique que les anciennes notes restent disponibles comme sources historiques.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le caractère canonique est documenté par la note elle-même ; aucune validation externe d'usage n'est fournie.

### CLM-AUD-002-309

- **Statement :** L'architecture V4 pose `System first / Tool second / Automation later` et présente Obsidian comme outil d'implémentation actuel, non comme définition des règles métier.
- **État :** current_canon
- **Sujet littéral :** Indépendance outil de Sofian OS V4
- **Temps du fait :** État documenté par la note actuelle
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Architecture Référence.md:24-34
- **Citation / observation :** `Sofian OS V4 est un système personnel indépendant des outils` ; Obsidian est l'outil actuel d'implémentation.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucun autre adapter ou runtime n'a été vérifié dans ce lot.

### CLM-AUD-002-310

- **Statement :** La référence V4 documente une séparation en layers allant de `Governance / Intent` à `Automation / Agents`, avec `Infrastructure` et `Automation / Agents` représentés comme futurs.
- **État :** current_canon
- **Sujet littéral :** Layers V4
- **Temps du fait :** État documenté par la note actuelle
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Architecture Référence.md:38-66
- **Citation / observation :** Le diagramme Mermaid relie Governance, Domain Core, Application Core, Operating Layer, Interface Adapter, Infrastructure et Automation / Agents ; les deux derniers ont la classe visuelle future.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le diagramme prouve une représentation documentaire, pas une topologie ou un déploiement.

### CLM-AUD-002-311

- **Statement :** V4 distingue les `Commands`, `Queries`, `Dashboards`, `Operating Routines` et `Adapters`, avec modification d'état uniquement pour les commands et exécution selon la commande appelée côté adapter.
- **État :** current_canon
- **Sujet littéral :** Séparation conceptuelle V4
- **Temps du fait :** État documenté par la note actuelle
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Architecture Référence.md:89-97
- **Citation / observation :** Le tableau associe `Command` à une modification d'état, `Query` et `Dashboard` à aucune modification, et `Adapter` à l'exécution/affichage.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La frontière n'a pas été vérifiée sur un parcours réel.

### CLM-AUD-002-312

- **Statement :** Le journal courant conserve une décision V4 de documentation par layer, ainsi que des décisions séparant strictement Queries et Dashboards et positionnant Obsidian comme Interface Adapter.
- **État :** current_canon
- **Sujet littéral :** Décisions V4 du 2026-05-15
- **Temps du fait :** 2026-05-15
- **Temps d’enregistrement :** 2026-05-15
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Journal De Décisions.md:24-50
- **Citation / observation :** Les trois entrées portent `Statut | Validé` et décrivent la documentation par layers, la séparation Query/Dashboard et Obsidian comme adapter.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le journal enregistre ces décisions, mais ne fournit pas un locator direct vers une validation utilisateur indépendante.

### CLM-AUD-002-313

- **Statement :** Le journal courant enregistre les décisions du 2026-05-16 sur `lower_snake_case` et les cinq statuts canoniques.
- **État :** current_canon
- **Sujet littéral :** Schéma V4 du 2026-05-16
- **Temps du fait :** 2026-05-16
- **Temps d’enregistrement :** 2026-05-16
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Journal De Décisions.md:64-80
- **Citation / observation :** Les décisions bannissent `Area`, `Project`, `Status` et listent `todo`, `in_progress`, `paused`, `done`, `dropped`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le journal ne prouve pas à lui seul la conformité de tout le vault.

### CLM-AUD-002-314

- **Statement :** Le journal enregistre le 2026-05-16 la décision de créer un vault propre `Sofian-OS` plutôt que de migrer `Sofian's Vault`, en conservant l'ancien vault en lecture seule historique.
- **État :** historical_intent
- **Sujet littéral :** Création de Sofian-OS
- **Temps du fait :** 2026-05-16
- **Temps d’enregistrement :** 2026-05-16
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Journal De Décisions.md:94-100
- **Citation / observation :** `Créer un vault Obsidian propre Sofian-OS plutôt que migrer l'ancien Sofian's Vault` ; l'ancien reste en lecture seule.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La décision documentée ne prouve ni quelles données ont été copiées ni qu'une migration n'a jamais eu lieu.

### CLM-AUD-002-315

- **Statement :** Le journal enregistre TaskNotes comme propriétaire unique des tâches et exclut une section manuelle `## Tâches` dans les projets.
- **État :** current_canon
- **Sujet littéral :** TaskNotes et projets V4
- **Temps du fait :** 2026-05-16
- **Temps d’enregistrement :** 2026-05-16
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Journal De Décisions.md:104-110
- **Citation / observation :** `TaskNotes est l'unique propriétaire des tâches` ; les projets n'ont pas de section manuelle `## Tâches`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence effective de ces sections dans les autres notes n'a pas été inspectée.

### CLM-AUD-002-316

- **Statement :** Le journal enregistre `Aspiration` comme entité Someday/Maybe, mais précise que son mapping exact dans Obsidian reste à définir.
- **État :** current_canon
- **Sujet littéral :** Aspiration V4
- **Temps du fait :** 2026-05-16 et état du journal courant
- **Temps d’enregistrement :** 2026-05-16
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Journal De Décisions.md:84-90; 164-170
- **Citation / observation :** `Ajouter l'entité Aspiration` ; `Le mapping Obsidian exact reste à définir` ; le point figure encore dans `Décisions À Trancher Plus Tard`.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-002-319"]
- **Review :** accepted
- **Limite :** Ce claim décrit le contenu du journal, sans décider si le mapping de configuration plus récent le remplace.

### CLM-AUD-002-317

- **Statement :** Le journal conserve comme décisions ouvertes le mapping d'`Aspiration`, la représentation de `Paused`/`Dropped`, le choix des `.base`, le niveau d'automatisation agentique et le remplacement d'Iconize.
- **État :** current_canon
- **Sujet littéral :** Décisions V4 ouvertes
- **Temps du fait :** État du journal au 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Journal De Décisions.md:164-170
- **Citation / observation :** La section `Décisions À Trancher Plus Tard` liste ces cinq sujets.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le journal ne permet pas de savoir si une décision a été prise ailleurs après cette entrée.

### CLM-AUD-002-318

- **Statement :** `V4 Obsidian Adapter Mapping.md` est une configuration active qui traduit les concepts V4 vers Obsidian tout en réaffirmant qu'Obsidian est un adapter et non le modèle métier.
- **État :** current_canon
- **Sujet littéral :** Configuration d'adaptation V4
- **Temps du fait :** État déclaré par le frontmatter et le contenu
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/V4 Obsidian Adapter Mapping.md:1-29
- **Citation / observation :** `config_status: active` ; le rôle décrit une traduction V4→Obsidian et les principes `System first`, `Tool second`, `Automation later`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le statut `active` est un état de fichier, pas une preuve d'activation runtime.

### CLM-AUD-002-319

- **Statement :** Le mapping V4 documente `Aspiration` vers `type: "🌱 Aspiration"` dans `98-Backend/Aspirations/`, avec une review via `scheduled_date`, et documente séparément Project, Task, Resource et Decision.
- **État :** current_canon
- **Sujet littéral :** Entités de l'adapter V4
- **Temps du fait :** État documenté par la configuration
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/V4 Obsidian Adapter Mapping.md:33-44
- **Citation / observation :** La ligne `Aspiration` donne le type, le dossier et la note ; les lignes suivantes donnent les mappings Project, Task, Resource et Decision.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-002-316"]
- **Review :** accepted
- **Limite :** Le mapping écrit ne prouve pas que le dossier, les notes ou l'autocomplete l'implémentent effectivement.

### CLM-AUD-002-320

- **Statement :** Le mapping V4 définit des propriétés canoniques pour titre, area, projects, contexts, status, priority et dates, et associe les cinq statuts V4 aux valeurs Obsidian/TaskNotes correspondantes.
- **État :** current_canon
- **Sujet littéral :** Propriétés et statuts de l'adapter
- **Temps du fait :** État documenté par la configuration
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/V4 Obsidian Adapter Mapping.md:47-69; 79-87
- **Citation / observation :** Le tableau décrit `lower_snake_case`, les dates `scheduled_date`/`due_date`/`start_date`/`finished_date` et le tableau `Todo`→`todo` jusqu'à `Dropped`→`dropped`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La conformité des plugins et notes réelles n'a pas été contrôlée.

### CLM-AUD-002-321

- **Statement :** La configuration exclut la création d'automatisations avant stabilisation des workflows, l'usage de Base pour définir l'architecture, la réintroduction des champs legacy et la dépendance de V4 à Obsidian comme outil unique.
- **État :** current_canon
- **Sujet littéral :** Non-goals de l'adapter V4
- **Temps du fait :** État documenté par la configuration
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/V4 Obsidian Adapter Mapping.md:166-195
- **Citation / observation :** Les `Non-Goals` interdisent ces quatre directions et excluent également un `status` pour les Aspirations.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ces garde-fous ne prouvent pas qu'aucune automation ou champ legacy n'existe ailleurs dans le vault.

### CLM-AUD-002-322

- **Statement :** `Sofian Ecosystem Architecture.md` se présente comme un handoff de reprise persistant qui pointe vers les notes canoniques au lieu de les remplacer, avec un état déclaré actif mis à jour le 20 août 2026.
- **État :** current_canon
- **Sujet littéral :** Handoff Sofian Ecosystem Architecture
- **Temps du fait :** État déclaré dans le handoff
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/AI Handoffs/Sofian Ecosystem Architecture.md:12-23
- **Citation / observation :** Le rôle est un `Point de reprise persistant` ; le texte dit `ne remplace pas les notes canoniques` et indique `Actif — mis à jour le 20 août 2026`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le handoff est une projection documentaire ; il ne prouve pas que les liens ou l'état déclaré sont encore opérés.

### CLM-AUD-002-323

- **Statement :** Le handoff impose l'altitude Domaines de vie → Capacités → Systèmes/ownership → contrats différés → modèles différés → implémentation/outils, et interdit de descendre de niveau pour résoudre une ambiguïté du niveau courant.
- **État :** current_canon
- **Sujet littéral :** Altitude de travail Sofian Ecosystem
- **Temps du fait :** État documenté du handoff
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/AI Handoffs/Sofian Ecosystem Architecture.md:38-53
- **Citation / observation :** L'ordre de travail liste les trois premières couches validées, les contrats et modèles différés, puis l'implémentation active ; `Ne pas descendre d'un niveau` est explicite.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune validation de cette méthode dans une session réelle n'est fournie par le fichier.

### CLM-AUD-002-324

- **Statement :** Le handoff documente une autorité par fait précis : TaskNotes pour l'état des tâches, Sofian OS pour projets/décisions/engagements enregistrés, et des systèmes externes pour leurs propres faits ; une autorité non démontrée reste non établie.
- **État :** current_canon
- **Sujet littéral :** Autorité des faits
- **Temps du fait :** État documenté du handoff
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/AI Handoffs/Sofian Ecosystem Architecture.md:108-124
- **Citation / observation :** La section distingue explicitement les propriétaires et dit `toute autorité non démontrée reste non établie`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les systèmes externes nommés n'ont pas été lus dans ce lot fermé.

### CLM-AUD-002-325

- **Statement :** Le handoff définit six scénarios de référence et un format de test Déclencheur → domaine → capacité → fait autoritaire → action → permission → résultat vérifié → correction.
- **État :** current_canon
- **Sujet littéral :** Scénarios de frontière
- **Temps du fait :** État documenté du handoff
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/AI Handoffs/Sofian Ecosystem Architecture.md:128-144
- **Citation / observation :** Les scénarios couvrent notamment santé, famille, alternance, URSSAF, sortie Køya et imprimante 3D ; le format de test est donné sous forme de chaîne.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence de scénarios et d'un format ne prouve pas qu'ils ont été exécutés.

### CLM-AUD-002-326

- **Statement :** Le handoff déclare un premier incrément actif `Jarvis — Socle v0.1`, en lecture seule depuis Sofian OS et TaskNotes, mais les sources et TaskNotes correspondantes sont hors du corpus W-D.
- **État :** current_canon
- **Sujet littéral :** Jarvis — Socle v0.1
- **Temps du fait :** État déclaré dans le handoff
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/AI Handoffs/Sofian Ecosystem Architecture.md:19-24; 243-258
- **Citation / observation :** Le handoff donne `Phase active` et une `Prochaine Étape Unique` de spécification du contrat du brief Jarvis.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le statut et le contrat ne sont pas vérifiables dans les cinq fichiers seuls.

### CLM-AUD-002-327

- **Statement :** Le handoff affirme qu'un artefact interactif a été vérifié par 49 assertions JSDOM et classe plusieurs couches comme terminées et vérifiées, mais il ne fournit ni commande, ni sortie, ni locator d'artefact dans le corpus W-D.
- **État :** unknown
- **Sujet littéral :** Preuve annoncée de l'artefact interactif
- **Temps du fait :** État déclaré dans le handoff
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/AI Handoffs/Sofian Ecosystem Architecture.md:231-241
- **Citation / observation :** La section `Terminé Et Vérifié` mentionne `Artefact interactif complet vérifié par 49 assertions JSDOM`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le texte prouve une affirmation documentaire, pas le niveau `technically_tested` ou `exercised_real_case`.

### CLM-AUD-002-328

- **Statement :** Le handoff encadre les propositions et mutations par lecture directe, scénarios réels, distinction fait/hypothèse/option, consentement explicite et vérification post-mutation.
- **État :** current_canon
- **Sujet littéral :** Garde-fous et protocole du handoff
- **Temps du fait :** État documenté du handoff
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/AI Handoffs/Sofian Ecosystem Architecture.md:191-227
- **Citation / observation :** Les sections `Garde-Fous`, `Avant Une Proposition`, `Avant Une Mutation` et `Après Une Mutation` explicitent ces étapes.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ces prescriptions ne prouvent pas leur respect dans toutes les sessions antérieures.

### CLM-AUD-002-329

- **Statement :** Aucun des cinq fichiers ne fournit un locator direct vers une décision utilisateur explicite et contextualisée ; les mentions `Validé` ou `validation` restent des affirmations documentées dans les fichiers.
- **État :** unknown
- **Sujet littéral :** Acceptation utilisateur des décisions V4
- **Temps du fait :** Corpus W-D lu au 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Journal De Décisions.md:24-170; Architecture Référence.md:17-20; handoff:19-24, 70-124
- **Citation / observation :** Les fichiers utilisent `Statut | Validé` ou `validée`, sans message utilisateur, session, date de consentement ou référence externe directement incluse.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L'absence dans ce corpus ne prouve pas l'absence d'une validation ailleurs.

### CLM-AUD-002-330

- **Statement :** Les cinq fichiers documentent des règles, structures, décisions, mappings et scénarios, mais ne contiennent pas de preuve complète d'un workflow V4 réellement exercé ni d'un usage opérationnel maintenu.
- **État :** unknown
- **Sujet littéral :** Niveaux de livraison des workflows V4
- **Temps du fait :** Corpus W-D lu au 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Cinq fichiers du lot D, lecture intégrale
- **Citation / observation :** Aucun parcours complet avec entrée, sortie, commande exécutée, résultat réel et observation utilisateur n'est fourni ; les fichiers décrivent surtout des règles et intentions.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L'inconnu doit être vérifié dans les sources d'implémentation et historiques hors lot, sans transformer cette absence en preuve négative.

### CLM-AUD-002-332

- **Statement :** La date interne du handoff (`mis à jour le 20 août 2026`) et son dernier commit Git observé (2026-08-25) décrivent deux temps distincts et ne doivent pas être fusionnés.
- **État :** live_implementation
- **Sujet littéral :** Temporalité du handoff
- **Temps du fait :** 20 août 2026 et commit du 25 août 2026
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** Handoff:19-23; `git log -1` sur le chemin exact
- **Citation / observation :** Le contenu indique 20 août ; Git donne le dernier commit `43b0964` au 2026-08-25.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le commit automatique prouve une écriture Git, pas une modification substantielle ou une validation.

### CLM-AUD-002-334

- **Statement :** Niveau de livraison vérifiable dans W-D : les cinq fichiers sont `documented` ; les niveaux `technically_tested`, `integrated`, `exercised_real_case`, `user_accepted` et `operational` restent non établis pour les workflows et mappings, sauf affirmation non prouvée du handoff sur les 49 assertions JSDOM.
- **État :** unknown
- **Sujet littéral :** Matrice de niveau de livraison W-D
- **Temps du fait :** État du corpus au 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Les cinq fichiers ciblés ; evidence-model.md:60-74; handoff:231-241
- **Citation / observation :** Chaque artefact est lisible et présent ; aucune preuve locale complète ne monte automatiquement au-delà de `documented`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La vérification des niveaux supérieurs appartient aux lots d'implémentation, d'historiques ou de tests qui sont hors périmètre W-D.

### CLM-AUD-002-400

- **Statement :** Le dépôt Git de `Sofian's Vault` possède une racine sans parent, créée comme snapshot de vault le 2026-05-04.
- **État :** historical_execution
- **Sujet littéral :** Racine Git de `Sofian's Vault`
- **Temps du fait :** 2026-05-04
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-OLD
- **Locator :** git rev-list --all --max-parents=0; commit f0c0862d54d34c8d0134e088f5ce28715eedf6bc
- **Citation / observation :** Racine parentless f0c0862 ; date 2026-05-04T13:10:10+02:00 ; sujet `vault backup: 2026-05-04 13:10:10`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Une racine Git et un sujet de backup ne prouvent pas la création initiale du vault dans Obsidian ni la date de rédaction de son contenu.

### CLM-AUD-002-401

- **Statement :** Le dépôt Git de `Sofian-OS` possède une racine sans parent, créée comme snapshot avant un reset TaskNotes le 2026-05-16.
- **État :** historical_execution
- **Sujet littéral :** Racine Git de `Sofian-OS`
- **Temps du fait :** 2026-05-16
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** git rev-list --all --max-parents=0; commit 306ff1a11c1fdd1f20ce1a5f60d6f3b2623b706a
- **Citation / observation :** Racine parentless 306ff1a ; date 2026-05-16T20:55:57+02:00 ; sujet `chore: snapshot vault before tasknotes reset`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La racine prouve l’origine du dépôt Git, pas la création ou l’adoption opérationnelle du vault Obsidian.

### CLM-AUD-002-404

- **Statement :** L’ancien vault enregistre l’apparition des documents V1, V2 et V3 le 2026-05-09, puis l’apparition du corpus de documents V4 par layers le 2026-05-14.
- **État :** historical_execution
- **Sujet littéral :** Évolution des générations `Sofian OS` dans `Sofian's Vault`
- **Temps du fait :** 2026-05-09..2026-05-14
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-OLD
- **Locator :** commits 5ddc27b9 et 2e63fa66 ; git log --find-renames --name-status sur `Backend/Resources/Sofian OS V*.md`
- **Citation / observation :** Le 2026-05-09, cinq fichiers V1/V2/V3 sont ajoutés ; le 2026-05-14, onze fichiers V4 par layers sont ajoutés.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les ajouts Git datent l’enregistrement dans le dépôt, pas nécessairement la conception initiale ni l’exécution des intentions décrites.

### CLM-AUD-002-405

- **Statement :** Dans `Sofian's Vault`, `Backend/Projects/Sofian OS V3 - Architecture Système.md` est renommé en `Backend/Projects/Sofian OS.md` avec une similarité Git de 100 % le 2026-05-09 ; `Sofian OS V4 - Travail Restant.md` est déplacé de l’inbox vers les ressources avec une similarité de 99 % le 2026-05-13.
- **État :** historical_execution
- **Sujet littéral :** Renommages internes de `Sofian's Vault`
- **Temps du fait :** 2026-05-09..2026-05-13
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-OLD
- **Locator :** commit 4196b59edd4cb67786c54a0913506c17da71c497 — R099 `00 - Inbox/Sofian OS V4  - Travail Restant.md` → `Backend/Resources/Sofian OS V4 - Travail Restant.md`
- **Citation / observation :** Entrées `R100` puis `R099` pour les deux transformations de chemin.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La détection de renommage Git établit une continuité de contenu selon son seuil ; elle ne prouve pas une décision utilisateur ni une continuité d’usage.

### CLM-AUD-002-406

- **Statement :** `Sofian-OS` ajoute 13 fichiers V4 sous `98-Backend/Resources/` dans le commit `feat(resources): migrate sofian os v4 canonical notes` du 2026-05-18, puis ajoute le mapping d’adaptation Obsidian dans un commit distinct.
- **État :** historical_execution
- **Sujet littéral :** Migration documentaire V4 vers `Sofian-OS`
- **Temps du fait :** 2026-05-18
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** commits 9a420989 et f1a70271 ; git show --stat --summary
- **Citation / observation :** Le premier commit crée 13 fichiers V4, dont les notes d’architecture, journal, `Travail Restant` et `Workflows`; le commit suivant crée `99-System/Config/V4 Obsidian Adapter Mapping.md`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le message de commit et les ajouts prouvent une migration documentaire déclarée et enregistrée, pas une copie exhaustive, un transfert automatisé, une adoption ou une validation.

### CLM-AUD-002-407

- **Statement :** Les 13 paires de fichiers V4 portant le même nom logique, comparées entre le snapshot ancien du 2026-05-14 et le commit de migration actif du 2026-05-18, ne sont pas identiques octet pour octet.
- **État :** historical_execution
- **Sujet littéral :** Comparaison des contenus V4 entre les deux dépôts
- **Temps du fait :** Snapshots Git 2026-05-14 et 2026-05-18
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** git rev-parse des blobs et `cmp` sur commits 2e63fa66 / 9a420989 ; chemins `Backend/Resources/Sofian OS V4 - ...md` vs `98-Backend/Resources/Sofian OS V4 - ...md`
- **Citation / observation :** Les 13 comparaisons renvoient des blob IDs différents et `cmp` renvoie `different` pour `Architecture Référence` et `Journal De Décisions`; les 13 paires ont été comparées.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La différence binaire n’identifie pas chaque transformation sémantique et n’exclut pas une copie manuelle suivie de normalisations.

### CLM-AUD-002-408

- **Statement :** Les deux dépôts n’ont pas de racine Git commune observable : chacun possède une racine parentless distincte et l’actif ne descend pas de la racine de l’ancien vault.
- **État :** live_implementation
- **Sujet littéral :** Filiation Git entre les deux vaults
- **Temps du fait :** État des graphes Git inspectés au 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** git rev-list --all --max-parents=0 sur les deux racines; racines f0c0862 et 306ff1a
- **Citation / observation :** Chaque dépôt retourne une seule racine sans parent, avec deux identifiants distincts ; les historiques sont donc séparés au niveau Git.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’absence d’ancêtre Git commun n’exclut pas une copie de fichiers hors Git ou une migration sélective.

### CLM-AUD-002-409

- **Statement :** Les auteurs techniques Git de `Sofian's Vault` sont principalement `Sofian-bll` (184 commits) avec `Sofian` (1), tandis que ceux de `Sofian-OS` sont `Sofian` (403) et `Sofian-bll` (168).
- **État :** historical_execution
- **Sujet littéral :** Auteurs techniques Git
- **Temps du fait :** Historique Git inspecté au 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** git shortlog --all --summary --numbered sur les deux racines
- **Citation / observation :** Les agrégats `shortlog` donnent respectivement 184/1 puis 403/168 pour ces noms d’auteur techniques.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Un nom Git est un identifiant technique ; il ne suffit pas à établir une identité humaine ou un nombre de personnes.

## Claims rejetés ou hors intégration

### Élément 1

- **id :** CLM-AUD-002-019

- **reason :** Le locator contient cinq décisions à trancher, pas quatre ; décompte faux.

### Élément 2

- **id :** CLM-AUD-002-029

- **reason :** Métadonnée de couverture, non claim source atomique ; état incompatible avec la source historique.

### Élément 3

- **id :** CLM-AUD-002-030

- **reason :** Fusion multi-sources et identité non prouvée entre cible V4 interne et cible globale Sofian Ecosystem.

### Élément 4

- **id :** CLM-AUD-002-200

- **reason :** Métadonnée de corpus, non claim factuel atomique.

### Élément 5

- **id :** CLM-AUD-002-217

- **reason :** Agrège quatre relations et plusieurs états temporels ; non atomique.

### Élément 6

- **id :** CLM-AUD-002-300

- **reason :** Métadonnée de corpus, non claim factuel atomique.

### Élément 7

- **id :** CLM-AUD-002-331

- **reason :** Affirme à tort l'absence de priorité alors que `AGENTS.md:5-7` donne priorité à la configuration/exécutable face à la prose.

### Élément 8

- **id :** CLM-AUD-002-333

- **reason :** Agrège statut Git courant et cinq dates/commits historiques ; non atomique.

### Élément 9

- **id :** CLM-AUD-002-402

- **reason :** Mélange période/compte historiques et état courant de branche.

### Élément 10

- **id :** CLM-AUD-002-403

- **reason :** Mélange période/compte historiques et état courant de branche.

## Provenance

- Synthèse Kanban : `t_43a8915a`.
- `review_status: accepted` signifie accepté pour ce rapport documentaire, pas `user_accepted` ni `operational`.
- Mutations des sources : `0`.
