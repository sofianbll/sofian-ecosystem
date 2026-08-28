---
id: AUD-005-CLAIMS
title: AUD-005 — Ledger des claims
status: integrated
date: 2026-08-28
coverage: 132
---

# AUD-005 — Ledger exhaustif des claims

> Annexe intégrée du [rapport AUD-005](report.md). Ces 132 claims ont été retenus après collecte, contre-reviews et normalisations explicites.

### CLM-AUD-005-001

- **Statement :** Sofian OS V4 est présenté comme un système personnel indépendant des outils.
- **État :** current_canon
- **Sujet littéral :** Sofian OS V4
- **Temps du fait :** non datée ; note présentée comme référence V4 actuelle
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Architecture Référence.md:24-34
- **Citation / observation :** Sofian OS V4 est un système personnel indépendant des outils.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Énoncé documentaire ; ne prouve pas une validation utilisateur.

### CLM-AUD-005-002

- **Statement :** Obsidian est décrit comme l’outil actuel d’implémentation, sans définir les règles métier du système.
- **État :** current_canon
- **Sujet littéral :** Obsidian
- **Temps du fait :** non datée ; implémentation actuelle déclarée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Architecture Référence.md:24-34
- **Citation / observation :** Obsidian est l’outil actuel d’implémentation, mais il ne définit pas les règles métier du système.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Pas de vérification du runtime Obsidian.

### CLM-AUD-005-003

- **Statement :** L’architecture documentaire sépare Governance / Intent, Domain Core, Application Core, Operating Layer, Interface Adapter, Infrastructure et Automation / Agents.
- **État :** current_canon
- **Sujet littéral :** Sofian OS V4 layers
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Architecture Référence.md:38-65
- **Citation / observation :** Le diagramme Mermaid relie G, D, A, O, I, N et X dans cet ordre.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Un diagramme et non une preuve d’implémentation de chaque layer.

### CLM-AUD-005-004

- **Statement :** La note Architecture Référence est déclarée point d’entrée canonique de Sofian OS V4 et relie les notes de référence.
- **État :** current_canon
- **Sujet littéral :** Sofian OS V4 - Architecture Référence
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Architecture Référence.md:17-20,70-85
- **Citation / observation :** Cette note est le point d'entrée canonique de Sofian OS V4.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Canon documentaire local ; aucune acceptation externe prouvée.

### CLM-AUD-005-005

- **Statement :** Les Commands modifient l’état, les Queries et Dashboards le lisent, et l’Operating Layer décrit les routines d’utilisation.
- **État :** current_canon
- **Sujet littéral :** séparation Command/Query/Dashboard/Operating Routine
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Architecture Référence.md:89-97; Operating Layer.md:22-29
- **Citation / observation :** Command ... Oui ; Query ... Non ; Dashboard ... Non ; Operating Routine ... Indirectement.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Contrat documentaire non exercé.

### CLM-AUD-005-006

- **Statement :** Les workflows sont décrits comme indépendants d’Obsidian ; le mapping frontmatter, Bases et TaskNotes appartient à l’Interface Adapter.
- **État :** current_canon
- **Sujet littéral :** Workflows / Interface Adapter
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Workflows.md:18-21
- **Citation / observation :** Les workflows ... restent indépendants d’Obsidian ; le mapping ... appartient à l’Interface Adapter.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ne vérifie pas qu’un adaptateur exécutable existe.

### CLM-AUD-005-007

- **Statement :** L’ordre recommandé des workflows commence par Capture, Clarify, Create Task, Create Project, puis Create / Qualify Resource.
- **État :** current_canon
- **Sujet littéral :** workflow order
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Workflows.md:39-55
- **Citation / observation :** 1. Capture ; 2. Clarify ; 3. Create Task ; 4. Create Project ; 5. Create / Qualify Resource.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ordre recommandé, pas preuve de parcours réel.

### CLM-AUD-005-008

- **Statement :** Capture doit minimiser la friction et ne pas décider Area, Project ou Status.
- **État :** current_canon
- **Sujet littéral :** Capture
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Workflows.md:58-83
- **Citation / observation :** Aucune question métier ; le but est de capturer sans décider ; ne pas choisir Area/Project/Status.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le corpus ne contient pas de mesure de friction.

### CLM-AUD-005-009

- **Statement :** Clarify décide une destination unique pour un Inbox Item : Trash, Do it now, Resource, Aspiration, Task ou Project.
- **État :** current_canon
- **Sujet littéral :** Clarify
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Workflows.md:94-141
- **Citation / observation :** Outputs: Trash, Do it now, Create Resource, Create Aspiration, Create Task, Create Project.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune série d’items réels inspectée.

### CLM-AUD-005-010

- **Statement :** Une Task doit être une prochaine action physique et visible ; elle doit avoir une Area et peut avoir un Project.
- **État :** current_canon
- **Sujet littéral :** Task
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Workflows.md:145-193
- **Citation / observation :** Une Task doit être une prochaine action visible ; une Task doit avoir une Area ; une Task peut avoir un Project.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Règle métier déclarée, non testée sur une note.

### CLM-AUD-005-011

- **Statement :** due_date représente une vraie deadline et scheduled_date une date prévue de commencer, revoir ou faire apparaître ; elles ne doivent pas être confondues.
- **État :** current_canon
- **Sujet littéral :** due_date / scheduled_date
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Workflows.md:167-179
- **Citation / observation :** due_date = vraie deadline ; scheduled_date = date prévue pour commencer / revoir / faire apparaître.
- **Confiance :** high
- **Contradictions :** ["CONTR-AUD-005-001"]
- **Review :** accepted
- **Limite :** La règle est contredite ou rendue ambiguë par le défaut TaskNotes déclaré today.

### CLM-AUD-005-012

- **Statement :** Create Task documente status par défaut Todo, priority par défaut Low et context par défaut Anywhere.
- **État :** current_canon
- **Sujet littéral :** Create Task defaults
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Workflows.md:167-193
- **Citation / observation :** context = Anywhere ; priority = Low ; status = Todo.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les valeurs sont documentées, non vérifiées par création réelle.

### CLM-AUD-005-013

- **Statement :** Create Project exige un résultat ou titre, une Area et un statut par défaut Todo ; il crée une première Task ou une Setup Task si nécessaire.
- **État :** current_canon
- **Sujet littéral :** Create Project
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Workflows.md:224-270
- **Citation / observation :** area est obligatoire ; status default = Todo ; si aucune première action claire existe : créer Setup project - {title}.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucun projet réel inspecté.

### CLM-AUD-005-014

- **Statement :** Une Resource est une information utile à consulter et ne devient pas directement une action.
- **État :** current_canon
- **Sujet littéral :** Resource
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Workflows.md:294-345
- **Citation / observation :** Une Resource = information utile à consulter ; une Resource ne devient pas directement une action.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Règle documentaire seulement.

### CLM-AUD-005-015

- **Statement :** Operating Layer fixe la règle Queries lisent, Dashboards composent, Operating décide, Commands modifient.
- **État :** current_canon
- **Sujet littéral :** Operating Layer
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Operating Layer.md:22-29
- **Citation / observation :** Queries lisent. Dashboards composent. Operating décide. Commands modifient.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Pas de preuve d’exécution.

### CLM-AUD-005-016

- **Statement :** Daily Review traite Overdue en premier, regarde Today/Calendar/This Week, décide au maximum trois MIT et utilise TaskNotes pour les changements.
- **État :** current_canon
- **Sujet littéral :** Daily Review
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Operating Layer.md:92-108
- **Citation / observation :** Décider max 3 MIT ; utiliser TaskNotes pour Schedule / Unschedule / Complete / Drop.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune Daily réelle ni sortie de query lue.

### CLM-AUD-005-017

- **Statement :** Engage demande de choisir une seule action et propose Start Task, Complete ou Reschedule via TaskNotes.
- **État :** current_canon
- **Sujet littéral :** Engage
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Operating Layer.md:112-126
- **Citation / observation :** Commencer une seule action ; utiliser TaskNotes Start Task / Complete / Reschedule.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Usage réel inconnu.

### CLM-AUD-005-018

- **Statement :** Le système documente des routines Inbox Processing, Daily Review, Engage, Weekly Review, Project Review et Aspirations Review avec dashboards et commandes associés.
- **État :** current_canon
- **Sujet littéral :** Operating routines
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 98-Backend/Resources/Sofian OS V4 - Operating Layer.md:58-67
- **Citation / observation :** Tableau Routines Canon listant six routines, leurs buts, dashboards, vues utilisées et commandes possibles.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence de la documentation ne prouve pas que les routines sont utilisées.

### CLM-AUD-005-019

- **Statement :** TaskNotes est déclaré source de vérité des tâches, chaque tâche étant une note Markdown dans 98-Backend/Tasks.
- **État :** current_canon
- **Sujet littéral :** TaskNotes
- **Temps du fait :** configuration déclarée active ; date interne absente
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/TaskNotes Schema.md:9-13
- **Citation / observation :** TaskNotes est la source de vérité pour les tâches dans Sofian-OS ; une tâche = une note Markdown dans 98-Backend/Tasks.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Autorité documentaire ; aucun fichier de tâche n’a été lu dans ce corpus.

### CLM-AUD-005-020

- **Statement :** L’identification d’une tâche repose sur type: "✏️ Task" dans 98-Backend/Tasks, avec is_template: true exclu.
- **État :** current_canon
- **Sujet littéral :** TaskNotes task identification
- **Temps du fait :** configuration déclarée active ; date interne absente
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/TaskNotes Schema.md:18-23
- **Citation / observation :** Propriété type ; valeur "✏️ Task" ; dossier 98-Backend/Tasks ; templates exclus via is_template: true.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le mapping réel n’a pas été comparé à un fichier de tâche.

### CLM-AUD-005-021

- **Statement :** Les valeurs de status autorisées sont todo, in_progress, paused, done et dropped ; les priorités sont low, medium et high.
- **État :** current_canon
- **Sujet littéral :** TaskNotes status/priority
- **Temps du fait :** configuration déclarée active ; date interne absente
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/TaskNotes Schema.md:41-52
- **Citation / observation :** Status : todo, in_progress, paused, done, dropped ; Priority : low, medium, high.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune validation de schéma sur données réelles.

### CLM-AUD-005-022

- **Statement :** Le schéma distingue area, projects et contexts ; due_date est une deadline et scheduled_date une planification.
- **État :** current_canon
- **Sujet littéral :** TaskNotes properties
- **Temps du fait :** configuration déclarée active ; date interne absente
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/TaskNotes Schema.md:54-65,114-117
- **Citation / observation :** area = domaine de vie ; projects = conteneur de travail ; contexts = condition / environnement / mode d’exécution.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le sens est documenté ; la conformité des fichiers n’est pas auditée.

### CLM-AUD-005-023

- **Statement :** La configuration TaskNotes déclare task folder 98-Backend/Tasks, default status todo, default priority low, default scheduled date today et Bases integration activé.
- **État :** current_canon
- **Sujet littéral :** TaskNotes configuration
- **Temps du fait :** configuration déclarée active ; date interne absente
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/TaskNotes Schema.md:84-99
- **Citation / observation :** Task folder 98-Backend/Tasks ; Default status todo ; Default priority low ; Default scheduled date today ; Bases integration activé.
- **Confiance :** high
- **Contradictions :** ["CONTR-AUD-005-001"]
- **Review :** accepted
- **Limite :** La note décrit la configuration ; tasknotes/data.json a été exclu et non lu.

### CLM-AUD-005-024

- **Statement :** La documentation Workflow emploie finished_date pour Complete ou Drop, tandis que la note TaskNotes désigne completed_date comme champ réel de fin TaskNotes et réserve finished_date aux autres entités V4.
- **État :** contradicted
- **Sujet littéral :** finished_date / completed_date
- **Temps du fait :** non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** Workflows.md:167-179; TaskNotes Schema.md:97-99
- **Citation / observation :** Workflows : finished_date est rempli par Complete ou Drop ; Schema : TaskNotes utilise completed_date pour la date de fin et finished_date pour les autres entités.
- **Confiance :** high
- **Contradictions :** ["CONTR-AUD-005-002"]
- **Review :** accepted
- **Limite :** Le sens exact dépend du mapping non lu ; parent doit trancher la portée.

### CLM-AUD-005-025

- **Statement :** La configuration déclare Archive folder 99-System/Archives/Tasks et précise que les tâches archivées ne sont pas déplacées automatiquement.
- **État :** current_canon
- **Sujet littéral :** TaskNotes archive
- **Temps du fait :** configuration déclarée active ; date interne absente
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/TaskNotes Schema.md:84-99,104-112
- **Citation / observation :** Archive folder 99-System/Archives/Tasks ; les tâches archivées ne sont pas déplacées automatiquement.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucun état d’archive réel inspecté.

### CLM-AUD-005-026

- **Statement :** La note TaskNotes avertit que tasknotes/data.json contient des champs OAuth et tokens ; ce fichier est une donnée sensible à ne pas imprimer, copier ou committer.
- **État :** current_canon
- **Sujet littéral :** tasknotes/data.json
- **Temps du fait :** configuration déclarée active ; date interne absente
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** 99-System/Config/TaskNotes Schema.md:101-102
- **Citation / observation :** tasknotes/data.json contient des champs OAuth et tokens ... Ne pas imprimer, copier ou committer ces valeurs.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le fichier n’a pas été lu conformément à l’exclusion du brief.

### CLM-AUD-005-027

- **Statement :** Le vault n’a pas de package.json, script de build, test runner ou workflow CI racine selon ses instructions locales.
- **État :** current_canon
- **Sujet littéral :** Sofian-OS repository shape
- **Temps du fait :** guidance locale non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** AGENTS.md:3-8
- **Citation / observation :** There is no root package.json, build script, test runner, or CI workflow to discover.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Constat des instructions locales, pas une recherche supplémentaire hors corpus.

### CLM-AUD-005-028

- **Statement :** Les Bases sont des surfaces de requête/vue et ne doivent pas créer directement des tâches TaskNotes.
- **État :** current_canon
- **Sujet littéral :** Bases / TaskNotes
- **Temps du fait :** guidance locale non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** AGENTS.md:26-31
- **Citation / observation :** Do not create full TaskNotes tasks through Base Board. Bases are query/view surfaces.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune vérification d’interface.

### CLM-AUD-005-029

- **Statement :** La documentation locale interdit de traiter un fichier, un test vert ou une documentation persistée comme preuve d’usage opérationnel ou d’acceptation utilisateur.
- **État :** current_canon
- **Sujet littéral :** preuve de livraison
- **Temps du fait :** guidance locale non datée
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** AGENTS.md:32-50
- **Citation / observation :** Une documentation persistée ou un test vert ne prouve ni validation utilisateur ni fonctionnement opérationnel.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ce claim borne l’audit ; il ne constitue pas une preuve positive d’absence.

### CLM-AUD-005-030

- **Statement :** Le corpus inspecté ne contient aucune sortie de test, parcours de cas réel, observation runtime datée ou validation explicite de Sofian.
- **État :** unknown
- **Sujet littéral :** Sofian OS V4 + TaskNotes livraison
- **Temps du fait :** corpus des cinq fichiers inspectés au 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OBS-ACTIVE
- **Locator :** corpus exact SYS-001 : cinq fichiers
- **Citation / observation :** Les cinq fichiers inspectés sont des instructions, ressources d’architecture, workflows, operating layer et schéma ; aucune sortie d’exécution ou validation utilisateur n’y figure.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Absence bornée à ce corpus ; ne prouve pas qu’aucune preuve n’existe ailleurs.

### CLM-AUD-005-101

- **Statement :** Jarvis est décrit comme la couche agentique qui relie les systèmes canoniques de Sofian et non comme un remplacement de Sofian OS, TaskNotes ou des sources externes.
- **État :** current_canon
- **Sujet littéral :** Jarvis
- **Temps du fait :** 2026-08-22 à 2026-08-27, selon les documents de dépôt
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/README.md:1-3,19-25
- **Citation / observation :** Jarvis est la couche agentique qui relie les systèmes déjà canoniques de Sofian ; il ne remplace ni Sofian OS, ni TaskNotes, ni les sources externes.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Énoncé documentaire ; ne prouve ni usage opérationnel ni acceptation utilisateur.

### CLM-AUD-005-102

- **Statement :** Les autorités déclarées sont Sofian OS pour projets/décisions/engagements, TaskNotes pour l’état des tâches, Mail pour contenu/état des messages et Jarvis pour orchestration/propositions/traces/vérifications.
- **État :** current_canon
- **Sujet littéral :** autorités par fait
- **Temps du fait :** 2026-08-22 à 2026-08-27
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/AGENTS.md:7-12; README.md:19-25
- **Citation / observation :** Sofian OS possède les projets et engagements ; TaskNotes possède l’état des tâches ; les mails possèdent le contenu et l’état ; Jarvis propose, orchestre et vérifie.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Carte d’autorité documentaire ; les systèmes externes n’ont pas été relus dans ce dossier.

### CLM-AUD-005-103

- **Statement :** Le code applicatif observé est écrit en Python et porte des règles déterministes dans le package `jarvis`.
- **État :** live_implementation
- **Sujet littéral :** code applicatif Jarvis
- **Temps du fait :** snapshot des fichiers lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/jarvis/__main__.py:1-12; jarvis/clarify_next.py:1-7; jarvis/mail_to_task.py:1-7
- **Citation / observation :** Les modules contiennent du Python avec `argparse`, `json`, `pathlib`, `re`, `datetime` et `typing`, plus les imports internes `jarvis.*`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Inspection statique ; aucune compilation ou exécution n’a été relancée.

### CLM-AUD-005-104

- **Statement :** Le CLI expose deux sous-commandes : `mail-to-task` et `clarify-next`.
- **État :** live_implementation
- **Sujet littéral :** interface CLI Jarvis
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/jarvis/__main__.py:14-34,37-52
- **Citation / observation :** Le parser crée les sous-commandes `mail-to-task` et `clarify-next`, puis imprime une sortie JSON triée.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence du branchement CLI ne prouve pas qu’il s’exécute dans l’environnement actuel.

### CLM-AUD-005-105

- **Statement :** Les dépendances directes visibles du code sont la bibliothèque standard Python et les deux modules internes `jarvis.clarify_next` et `jarvis.mail_to_task`; aucune dépendance tierce déclarée n’a été trouvée dans le périmètre inspecté.
- **État :** live_implementation
- **Sujet littéral :** dépendances directes
- **Temps du fait :** snapshot des fichiers lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/jarvis/*.py ; recherche de `pyproject.toml`, `setup.cfg`, `requirements*.txt`, `Dockerfile*`, `Makefile` et `.github` : aucun résultat
- **Citation / observation :** Les imports visibles sont `argparse`, `json`, `pathlib`, `typing`, `re`, `datetime`, plus les imports internes ; les fichiers de packaging/CI recherchés sont absents.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Absence dans le périmètre et les motifs recherchés ; ne prouve pas l’absence de dépendance implicite dans un environnement externe.

### CLM-AUD-005-106

- **Statement :** Les implémentations observées sont read-only : elles lisent des fichiers/objets d’entrée et produisent une proposition sans écrire Mail, vault ou TaskNotes.
- **État :** live_implementation
- **Sujet littéral :** permissions d’exécution du prototype
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/jarvis/clarify_next.py:19-31,39-62,65-115; mail_to_task.py:38-76
- **Citation / observation :** Les accès visibles sont ouverture/lecture, `iterdir`, `read_text`, `stat` et retour d’un dictionnaire ; `mutation_performed` vaut `False`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Conclusion statique sur les modules inspectés ; elle ne couvre pas des exécutables ou services hors dépôt.

### CLM-AUD-005-107

- **Statement :** Aucun writer vers Mail, Sofian-OS ou TaskNotes n’est présent dans les fichiers Jarvis inspectés.
- **État :** live_implementation
- **Sujet littéral :** writers externes
- **Temps du fait :** snapshot du dépôt lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/jarvis/*.py ; README.md:40-47
- **Citation / observation :** Le dépôt décrit les mutations comme futures et les modules retournent uniquement des propositions JSON avec `mutation_performed: false`.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Inventaire borné au dépôt nommé ; aucun runtime ou connecteur externe n’a été audité.

### CLM-AUD-005-108

- **Statement :** Les consommateurs directs observables sont le CLI, les tests et les appelants humains/adaptateurs futurs ; aucune consommation réelle par TaskNotes ou Daily Review n’est implémentée dans le code inspecté.
- **État :** live_implementation
- **Sujet littéral :** consumers Jarvis
- **Temps du fait :** snapshot du code et des tests lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/jarvis/__main__.py:10-49; tests/*.py; workflows/*/README.md
- **Citation / observation :** Le CLI appelle les fonctions et imprime JSON ; les tests importent les fonctions ; les workflows décrivent les intégrations comme futures ou documentées.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les consommateurs hors dépôt n’ont pas été recherchés.

### CLM-AUD-005-109

- **Statement :** La documentation du workflow Mail vers TaskNote définit cinq dispositions : `action_required`, `waiting`, `reference`, `noise` et `uncertain`.
- **État :** current_canon
- **Sujet littéral :** dispositions Mail vers TaskNote
- **Temps du fait :** 2026-08-22 selon la documentation du workflow
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/workflows/mail-to-task/README.md:15-21
- **Citation / observation :** La section `Dispositions` énumère `action_required`, `waiting`, `reference`, `noise` et `uncertain`.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-110", "CLM-AUD-005-111"]
- **Review :** accepted
- **Limite :** Contrat documentaire ; ne prouve pas l’implémentation de chaque branche.

### CLM-AUD-005-110

- **Statement :** Le code `clarify_thread` ne retourne actuellement que `action_required` pour une requête explicite ou `uncertain` dans le cas contraire.
- **État :** live_implementation
- **Sujet littéral :** clarify_thread
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/jarvis/mail_to_task.py:38-76
- **Citation / observation :** Le branchement retourne `disposition: uncertain` si la regex échoue, sinon `disposition: action_required`; aucune branche `waiting`, `reference` ou `noise` n’est visible.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-109", "CLM-AUD-005-111"]
- **Review :** accepted
- **Limite :** Le résultat est limité au module inspecté ; une autre implémentation externe n’a pas été recherchée.

### CLM-AUD-005-111

- **Statement :** Il existe une contradiction non résolue entre le contrat documentaire à cinq dispositions et l’implémentation live à deux dispositions pour le workflow mail.
- **État :** contradicted
- **Sujet littéral :** contrat Mail vers TaskNote
- **Temps du fait :** snapshot comparé le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** Comparaison /Users/sofian/Developer/10-Personal/jarvis/workflows/mail-to-task/README.md:15-21 avec jarvis/mail_to_task.py:44-60
- **Citation / observation :** La documentation annonce cinq valeurs ; le code ne produit que `uncertain` ou `action_required`.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-109", "CLM-AUD-005-110"]
- **Review :** accepted
- **Limite :** Ce dossier signale la contradiction sans choisir quelle source doit être modifiée.

### CLM-AUD-005-112

- **Statement :** Le prototype mail produit une proposition fixe avec titre `Transmettre le document demandé`, date extraite si une date française valide est trouvée, statut `todo` et priorité `medium`.
- **État :** live_implementation
- **Sujet littéral :** task_proposal mail
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/jarvis/mail_to_task.py:26-35,59-76
- **Citation / observation :** Le dictionnaire `task_proposal` contient ces quatre champs et `_extract_due_date` transforme une date française en ISO.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ne prouve pas que le titre ou les champs conviennent à un cas réel ni au schéma TaskNotes.

### CLM-AUD-005-113

- **Statement :** `clarify-next` sélectionne seulement les fichiers Markdown réguliers directement contenus dans `00-Inbox`, exclut ceux dont le frontmatter contient exactement `is_template: true`, puis choisit le plus récent selon mtime, création et nom.
- **État :** live_implementation
- **Sujet littéral :** select_next_inbox_item
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/jarvis/clarify_next.py:19-52
- **Citation / observation :** La liste utilise `inbox.iterdir()`, `suffix == .md`, `_is_template`, puis `max` avec `(st_mtime, _creation_time, name)`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La sélection n’est pas récursive et le schéma réel des Inbox Items n’est pas vérifié ici.

### CLM-AUD-005-114

- **Statement :** `clarify-next` rend visibles les contrôles incomplets : `blocked` si aucun Inbox Item lisible et `needs_input` si le premier contenu est vide ou ambigu ; dans ces deux cas la sortie canonique est `null` et aucune mutation n’est faite.
- **État :** live_implementation
- **Sujet littéral :** clarify_next contrôle de source
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/jarvis/clarify_next.py:71-103
- **Citation / observation :** Les retours portent `decision_state` `blocked` ou `needs_input`, `canonical_output: None`, `mutation_preview: None` et `mutation_performed: False`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le code dépend d’une proposition préexistante et ne réalise pas l’arbre métier complet Clarify.

### CLM-AUD-005-115

- **Statement :** Le parcours Capture iOS est documenté comme prévu mais aucun Shortcut Jarvis correspondant n’est déclaré installé dans le corpus Jarvis inspecté.
- **État :** current_canon
- **Sujet littéral :** Capture iOS
- **Temps du fait :** 2026-08-22 selon le workflow documenté
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/workflows/ios-capture/README.md:7-24
- **Citation / observation :** Le document décrit le MVP et le contrat JSON puis indique qu’aucun `Quick Task`, `Voice Journal` ou `Energy Check` correspondant n’est actuellement installé.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’absence est bornée au corpus et à la déclaration documentaire ; aucun inventaire d’appareil n’a été exécuté.

### CLM-AUD-005-116

- **Statement :** Le workflow Daily Review réutilisable est décrit comme un ancien helper externe avec 81 tests de caractérisation historiques ; aucun brief réel ni mutation mail/vault n’est déclaré exécuté pendant la réconciliation.
- **État :** current_canon
- **Sujet littéral :** Daily Review
- **Temps du fait :** 2026-08-22 selon le workflow documenté
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/workflows/daily-review/README.md:7-14
- **Citation / observation :** Le document cite l’ancien helper `~/.config/opencode/skills/productivity/jarvis-daily-brief/`, `status: ok` structurel, 81 tests historiques et l’absence de brief réel/mutation pendant la réconciliation.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ces tests ne sont ni ceux du dépôt Jarvis ni une preuve d’intégration actuelle.

### CLM-AUD-005-117

- **Statement :** Le dépôt contient deux fichiers de tests avec sept méthodes de test visibles au total, mais cette collecte ne les a pas relancées.
- **État :** live_implementation
- **Sujet littéral :** preuves de test Jarvis
- **Temps du fait :** snapshot des fichiers lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/tests/test_clarify_next.py:12-175; tests/test_mail_to_task.py:13-46
- **Citation / observation :** `test_clarify_next.py` contient cinq méthodes `test_...` et `test_mail_to_task.py` en contient deux ; la mission interdit de relancer les tests.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence des tests prouve une intention de preuve, pas un résultat vert actuel.

### CLM-AUD-005-118

- **Statement :** Aucun fichier de packaging, dépendances déclarées, CI ou conteneur n’a été trouvé par les recherches bornées effectuées dans le dépôt Jarvis.
- **État :** live_implementation
- **Sujet littéral :** build et déploiement
- **Temps du fait :** snapshot du dépôt vérifié le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** Recherches de `pyproject.toml`, `setup.cfg`, `requirements*.txt`, `Dockerfile*`, `Makefile` et `.github` sous /Users/sofian/Developer/10-Personal/jarvis : 0 résultat
- **Citation / observation :** Les recherches de fichiers ciblées retournent zéro résultat pour chaque motif.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Une configuration externe ou implicite hors dépôt n’est pas couverte.

### CLM-AUD-005-119

- **Statement :** Le dépôt Jarvis est un dépôt Git initialisé sur `main` sans commit vérifiable ; tous les chemins inspectés apparaissent non suivis et aucun remote n’est affiché.
- **État :** live_implementation
- **Sujet littéral :** état Git Jarvis
- **Temps du fait :** état observé le 2026-08-28 à 14:44 CEST
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** Commande read-only `git status --short --branch; git rev-parse --is-inside-work-tree; git rev-parse --verify HEAD; git remote -v` depuis /Users/sofian/Developer/10-Personal/jarvis
- **Citation / observation :** Sortie : `## No commits yet on main`, arborescences `??`, `true`, puis `fatal: Needed a single revision`; aucune ligne de remote.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** État du dépôt local uniquement ; ne prouve pas l’absence d’une copie ou d’un historique ailleurs.

### CLM-AUD-005-120

- **Statement :** Les preuves live directement datées disponibles pour SYS-002 sont statiques : lecture des fichiers, métadonnées mtime et état Git ; aucune sortie d’exécution, connexion externe ou observation de runtime n’a été obtenue dans ce dossier.
- **État :** unknown
- **Sujet littéral :** niveau de preuve live
- **Temps du fait :** snapshot du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** Lectures directes et `date -Iseconds` retournant `2026-08-28T14:44:04+02:00`; aucune commande de test/build/healthcheck exécutée
- **Citation / observation :** Le protocole interdit tests, build, healthcheck distant et mutation ; les preuves réunies restent documentaires/statistiques/Git.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ne permet pas de classer le système `technically_tested`, `integrated`, `exercised_real_case` ou `operational`.

### CLM-AUD-005-121

- **Statement :** L’owner humain ou organisationnel de Jarvis n’est pas explicitement établi dans les fichiers Jarvis inspectés.
- **État :** unknown
- **Sujet littéral :** owner Jarvis
- **Temps du fait :** corpus inspecté le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/AGENTS.md, README.md, docs/*.md
- **Citation / observation :** Les sources décrivent le but, les autorités et la décision de build, mais aucune propriété `owner` ou formulation explicite d’ownership n’a été trouvée.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’absence de champ dans le corpus n’exclut pas une décision externe.

### CLM-AUD-005-122

- **Statement :** La correction des faits est répartie par autorité : Mail corrige les messages, Sofian OS/TaskNotes corrige l’état des tâches, et le dépôt Jarvis corrige ses règles et contrats.
- **État :** current_canon
- **Sujet littéral :** mécanismes de correction
- **Temps du fait :** 2026-08-22 à 2026-08-27
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/AGENTS.md:7-12,22-27; README.md:19-25
- **Citation / observation :** Les règles déclarent les propriétaires respectifs et exigent que les futures mutations soient idempotentes et relues.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les mécanismes concrets de correction externe et de relecture ne sont pas implémentés.

### CLM-AUD-005-123

- **Statement :** Les contrats documentés couvrent Mail vers TaskNote, Clarify, Capture iOS et Daily Review, mais seule une partie des deux premiers possède un code local ; les intégrations externes sont futures ou optionnelles.
- **État :** current_canon
- **Sujet littéral :** contrats et dépendances Jarvis
- **Temps du fait :** 2026-08-22 à 2026-08-27
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/workflows/*/README.md; docs/clarify/contract.md; docs/build-roadmap.md:13-37
- **Citation / observation :** La roadmap réserve les lots futurs à la TaskNote approuvée, Capture iOS et Daily Review ; Mail réel, doublons et écriture approuvée restent à construire.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La qualification porte sur le corpus Jarvis, sans audit des systèmes partenaires.

### CLM-AUD-005-124

- **Statement :** Les propositions JSON et la documentation de workflow sont des vues/projections susceptibles de diverger de l’autorité TaskNotes ; le dépôt ne montre pas de contrôle de conformité automatisé entre code, contrat et schéma réel.
- **État :** hypothesis
- **Sujet littéral :** copies et projections
- **Temps du fait :** snapshot du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Developer/10-Personal/jarvis/README.md:19-25,40-47; workflows/mail-to-task/README.md:23-41; jarvis/mail_to_task.py:59-76
- **Citation / observation :** Le JSON de proposition contient `status`, `priority`, `due_date` et `title`, tandis que les autorités résident dans Mail/TaskNotes ; aucun schéma TaskNotes importé ni vérificateur de contrat n’est présent.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Risque de divergence identifié ; divergence effective avec TaskNotes réelle non mesurée.

### CLM-AUD-005-201

- **Statement :** L’intention historique de Sofian était de disposer d’une base système pour auditer les systèmes et réutiliser le travail via plusieurs sessions et groupes de subagents.
- **État :** historical_intent
- **Sujet littéral :** Hermes dans l’écosystème documentaire
- **Temps du fait :** 2026-08-27
- **Temps d’enregistrement :** 2026-08-27
- **Source :** SRC-HERMES
- **Locator :** default/20260827_154335_c51ad8:52676,52972
- **Citation / observation :** La session demande une base de structure pour l’audit puis décrit l’usage de sessions et de subagents pour poursuivre le travail.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Intention historique, pas preuve d’un workflow Hermes opérationnel sur un cas réel.

### CLM-AUD-005-202

- **Statement :** La cible de l’écosystème n’était pas prédéfinie ; elle devait être déduite du passé prouvé, de l’état actuel et des besoins avant validation de Sofian.
- **État :** historical_intent
- **Sujet littéral :** Hermes comme composant d’audit/orchestration
- **Temps du fait :** 2026-08-27
- **Temps d’enregistrement :** 2026-08-27
- **Source :** SRC-HERMES
- **Locator :** default/20260827_154335_c51ad8:52961-52972
- **Citation / observation :** La conversation corrige explicitement l’hypothèse d’une cible déjà connue et impose la séquence audit → besoins → capacités → options → cible proposée → validation.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ne constitue pas une décision d’architecture cible pour Hermes.

### CLM-AUD-005-203

- **Statement :** Hermes est le runtime/interface agentique qui relie conversation, outils, mémoire, sessions, profils, surfaces de programmation et exécutions en arrière-plan.
- **État :** current_canon
- **Sujet littéral :** Hermes Agent
- **Temps du fait :** snapshot documentation consulté le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** ~/.hermes/skills/autonomous-ai-agents/hermes-agent/SKILL.md; sections Quick Start, Surfaces, Hard Invariants
- **Citation / observation :** La skill locale décrit les surfaces CLI, desktop, dashboard, TUI, proxy, profils, mémoire, plugins, MCP, cron et délégation.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Décrit la responsabilité du runtime ; ne donne pas à Hermes l’autorité sur les projets/tâches métier.

### CLM-AUD-005-204

- **Statement :** L’implémentation locale observée est Hermes Agent v0.20.6, installée dans ~/.hermes/hermes-agent, avec Python 3.11.15 et le modèle gpt-5.6-sol-900k via ChatGPT or Codex Subscription.
- **État :** live_implementation
- **Sujet littéral :** Installation Hermes locale
- **Temps du fait :** 2026-08-28
- **Temps d’enregistrement :** 2026-08-28T12:49:34Z
- **Source :** SRC-LIVE
- **Locator :** hermes --version; hermes status --all
- **Citation / observation :** Diagnostics CLI locaux terminés avec exit code 0 ; la sortie indique Hermes Agent v0.20.6 (2026.8.27), Python 3.11.15, installation ~/.hermes/hermes-agent et modèle actif gpt-5.6-sol-900k.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Snapshot local ; ne prouve pas que tous les composants documentés sont disponibles dans cette version.

### CLM-AUD-005-205

- **Statement :** Les sessions Hermes sont persistées dans une base SQLite locale avec historique, métadonnées, compteurs et parent_session_id ; la recherche FTS5 permet de retrouver les messages sans appel LLM.
- **État :** current_canon
- **Sujet littéral :** SessionDB / session_search
- **Temps du fait :** documentation consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-HERMES
- **Locator :** https://hermes-agent.nousresearch.com/docs/user-guide/sessions#how-sessions-work
- **Citation / observation :** La documentation Sessions décrit state.db, les métadonnées de session, la persistance de l’historique, la lignée parent/enfant et les tables de recherche FTS5.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le schéma SQLite n’a pas été inspecté dans cette unité ; le chemin exact dépend du profil/HERMES_HOME.

### CLM-AUD-005-206

- **Statement :** Une session active utilise une fenêtre de contexte ; la base persistée contient l’historique mais celui-ci n’est pas automatiquement injecté en entier dans chaque tour.
- **État :** current_canon
- **Sujet littéral :** Contexte versus historique
- **Temps du fait :** documentation consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-HERMES
- **Locator :** https://hermes-agent.nousresearch.com/docs/user-guide/sessions#context-window
- **Citation / observation :** La documentation sépare reprise de session, historique persistant et fenêtre de contexte ; elle décrit également la compression et la croissance du contexte.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les seuils exacts de compression et de tokens ne sont pas intégrés au dossier.

### CLM-AUD-005-207

- **Statement :** Les sessions peuvent être reprises et recherchées par identifiant ou titre ; les sources de session incluent notamment CLI, desktop, API, ACP, cron, webhook et batch.
- **État :** current_canon
- **Sujet littéral :** Entrées et rappel historique
- **Temps du fait :** documentation consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-HERMES
- **Locator :** https://hermes-agent.nousresearch.com/docs/user-guide/sessions#resuming-sessions; #session-sources
- **Citation / observation :** Sections de reprise et de sources de sessions consultées ; la session historique de référence est retrouvable dans Hermes sous default/20260827_154335_c51ad8.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La session historique complète comporte 389 messages mais la vue globale retournée était tronquée ; seuls les locators pertinents ont été relus.

### CLM-AUD-005-208

- **Statement :** Cron Hermes est un ordonnanceur séparé qui permet des jobs ponctuels ou récurrents, pause/reprise/modification/exécution/suppression, scripts sans agent, compétences ciblées, toolsets et livraisons multi-canaux.
- **État :** current_canon
- **Sujet littéral :** Cron Hermes
- **Temps du fait :** documentation consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-HERMES
- **Locator :** https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
- **Citation / observation :** La documentation officielle décrit le tool cronjob et ses actions, schedules, scripts, no_agent, skills, enabled_toolsets, workdir, context_from et delivery.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Une capacité documentée n’est pas une preuve de bon fonctionnement d’un job précis.

### CLM-AUD-005-209

- **Statement :** L’autorité du planning Cron est jobs.json ; les sorties sont sous cron/output et les tentatives sont enregistrées dans executions.db avec les états claimed, running, completed, failed ou unknown.
- **État :** current_canon
- **Sujet littéral :** Autorité des jobs et traces d’exécution
- **Temps du fait :** documentation consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-HERMES
- **Locator :** https://hermes-agent.nousresearch.com/docs/user-guide/features/cron#storage-and-execution-history
- **Citation / observation :** La documentation distingue définition de job, sortie produite et historique d’exécution ; les tentatives unknown ne sont pas relancées automatiquement.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le contenu des jobs actuels et executions.db n’a pas été lu pour éviter d’élargir le périmètre.

### CLM-AUD-005-211

- **Statement :** Hermes expose trois familles d’intégration documentées : ACP en JSON-RPC sur stdio, TUI gateway en JSON-RPC stdio/WebSocket, et API HTTP avec Server-Sent Events ; l’API prévoit runs, événements, approval, steer et stop.
- **État :** current_canon
- **Sujet littéral :** Contrats d’intégration
- **Temps du fait :** documentation consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-HERMES
- **Locator :** https://hermes-agent.nousresearch.com/docs/developer-guide/programmatic-integration
- **Citation / observation :** La documentation Programmatic Integration décrit les transports, endpoints /v1/runs, événements et contrôles d’exécution.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les endpoints n’ont pas été appelés ; leur disponibilité dans la version 0.20.6 reste à vérifier.

### CLM-AUD-005-212

- **Statement :** Les outils sont regroupés par toolsets et peuvent inclure terminal, fichiers, web, browser, vision, mémoire, recherche de sessions, cron, délégation, code execution, Home Assistant et MCP ; le terminal possède plusieurs backends documentés, dont local et SSH.
- **État :** current_canon
- **Sujet littéral :** Outils et environnement d’exécution
- **Temps du fait :** documentation consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-HERMES
- **Locator :** https://hermes-agent.nousresearch.com/docs/user-guide/features/tools; SRC-LIVE: SKILL.md
- **Citation / observation :** La documentation Tools et la skill locale décrivent les toolsets, le registre d’outils, les backends terminal et MCP.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le registre exact et les toolsets effectivement chargés dans chaque profil n’ont pas été exportés.

### CLM-AUD-005-213

- **Statement :** Les profils isolent configuration, sessions, compétences et mémoire ; les commandes de profil couvrent list, use, create, describe, delete, export, import, install et update.
- **État :** current_canon
- **Sujet littéral :** Profils Hermes
- **Temps du fait :** documentation consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-HERMES
- **Locator :** https://hermes-agent.nousresearch.com/docs/reference/profile-commands
- **Citation / observation :** La référence officielle des commandes de profils décrit l’isolation et les opérations de cycle de vie.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’isolation logique est documentée ; aucune comparaison de deux profils actifs n’a été exercée.

### CLM-AUD-005-214

- **Statement :** La redaction des secrets est activée par défaut dans Hermes ; les permissions/approbations et les opérations sudo doivent rester configurées explicitement, et les secrets sont séparés de la configuration générale.
- **État :** current_canon
- **Sujet littéral :** Sécurité et permissions
- **Temps du fait :** documentation/skill consultées le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** ~/.hermes/skills/autonomous-ai-agents/hermes-agent/references/security-privacy.md; SKILL.md Hard Invariants
- **Citation / observation :** La référence sécurité décrit redaction et modes d’approbation ; la skill impose secrets dans .env et paramètres dans config.yaml.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les valeurs de configuration et credentials ne sont pas reproduites ; l’existence d’une permission ne prouve pas son utilisation.

### CLM-AUD-005-215

- **Statement :** Dans le snapshot live, le backend terminal sélectionné est local et sudo est désactivé.
- **État :** live_implementation
- **Sujet littéral :** Permissions et exécution locale
- **Temps du fait :** 2026-08-28
- **Temps d’enregistrement :** 2026-08-28T12:49:34Z
- **Source :** SRC-LIVE
- **Locator :** hermes status --all
- **Citation / observation :** La sortie du diagnostic local indique Backend terminal: local et Sudo: disabled.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Cela décrit le profil/runtime observé, pas tous les profils ni les sessions distantes.

### CLM-AUD-005-216

- **Statement :** Le gateway local est signalé running, mais le diagnostic indique que launchd n’est pas le gestionnaire du gateway actuellement actif.
- **État :** contradicted
- **Sujet littéral :** Gateway et supervision
- **Temps du fait :** 2026-08-28
- **Temps d’enregistrement :** 2026-08-28T12:49:34Z
- **Source :** SRC-LIVE
- **Locator :** hermes status --all
- **Citation / observation :** Le même diagnostic rapporte gateway running et, séparément, service installé sans gestion du processus actuellement actif.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Il faut distinguer disponibilité actuelle du processus et supervision/persistance après redémarrage.

### CLM-AUD-005-218

- **Statement :** Le runtime local observé indique 2 jobs actifs sur 2 jobs au total, avec une prochaine échéance rapportée au 2026-08-29T08:00:00+02:00.
- **État :** live_implementation
- **Sujet littéral :** État Cron local
- **Temps du fait :** 2026-08-28
- **Temps d’enregistrement :** 2026-08-28T12:49:34Z
- **Source :** SRC-LIVE
- **Locator :** hermes cron status
- **Citation / observation :** Diagnostic local terminé avec exit code 0 ; contenu des jobs volontairement non lu.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le statut configuré ne prouve pas qu’une exécution future réussira ni que le fuseau système est correct.

### CLM-AUD-005-219

- **Statement :** Le runtime local observé utilise un profil default ; la liste de profils n’a pas révélé de second profil actif dans ce contrôle.
- **État :** live_implementation
- **Sujet littéral :** Profil actif
- **Temps du fait :** 2026-08-28
- **Temps d’enregistrement :** 2026-08-28T12:49:34Z
- **Source :** SRC-LIVE
- **Locator :** hermes profile list
- **Citation / observation :** La commande profile list a terminé avec exit code 0 et le contrôle rapportait le profil default.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Une liste de profils n’est pas une preuve de multiplexage gateway ni d’usage multi-profil.

### CLM-AUD-005-220

- **Statement :** L’autorité des faits doit rester séparée par type : SessionDB pour conversations/historique, jobs.json pour définitions Cron, executions.db pour tentatives, configuration/profil pour paramètres et TaskNotes/Sofian-OS pour l’état métier des tâches.
- **État :** current_canon
- **Sujet littéral :** Frontière d’autorité Hermes–Sofian OS
- **Temps du fait :** snapshot documentaire
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-HERMES
- **Locator :** documentation Sessions/Cron/Profiles; session historique: 52961-52972
- **Citation / observation :** Les documents Hermes séparent les stockages techniques ; la session d’écosystème sépare l’agent qui lit/propose de TaskNotes qui possède l’état de tâche.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La relation complète avec le vault Sofian-OS doit être contre-vérifiée dans SYS-001 ; ce dossier ne crée aucune nouvelle autorité.

### CLM-AUD-005-221

- **Statement :** Les corrections supportées passent par les interfaces de contrôle documentées : session_search/resume pour l’historique, cronjob ou hermes cron pour les jobs, hermes config set pour la configuration, et profile commands pour l’isolation ; l’édition directe des fichiers internes est déconseillée.
- **État :** current_canon
- **Sujet littéral :** Correction et récupération
- **Temps du fait :** documentation consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** SKILL.md Hard Invariants; references/background-systems.md; references/cli-reference.md
- **Citation / observation :** La skill impose config.yaml via hermes config set et les références Cron recommandent les interfaces de gestion plutôt que l’édition directe de jobs.json.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ce dossier n’autorise ni n’exécute aucune mutation.

### CLM-AUD-005-222

- **Statement :** Les traces et exports de session sont des projections utiles pour rappel/audit mais ne remplacent pas la base de session ni la source métier ; une vue de session tronquée ne doit pas être traitée comme un transcript complet.
- **État :** current_canon
- **Sujet littéral :** Auditabilité et projections
- **Temps du fait :** documentation et contrôle session consultés le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-HERMES
- **Locator :** https://hermes-agent.nousresearch.com/docs/user-guide/sessions; session_search default/20260827_154335_c51ad8
- **Citation / observation :** La documentation distingue persistance, reprise et exports ; le contrôle réel a signalé une vue globale tronquée et a nécessité des lectures ciblées.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le format exact des traces produit par la version locale n’a pas été exporté.

### CLM-AUD-005-301

- **Statement :** La base OpenCode canonique contient 1 609 sessions, 40 619 messages et 186 048 parts sur la période du 2026-06-10 au 2026-08-26.
- **État :** live_implementation
- **Sujet littéral :** historique OpenCode
- **Temps du fait :** 2026-06-10T13:56:27Z..2026-08-26T18:35:44Z
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** opencode_history.py stats ; source /Users/sofian/.local/share/opencode/opencode.db
- **Citation / observation :** stats direct : sessions 1609, messages 40619, parts 186048, oldest 2026-06-10T13:56:27.193000+00:00, newest 2026-08-26T18:35:44.329000+00:00
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence de données ne prouve pas qu’un processus OpenCode ou OpenChamber soit actuellement en fonctionnement.

### CLM-AUD-005-302

- **Statement :** L’index dérivé OpenCode est stale : il annonce 1 601 sessions contre 1 609 dans la base source.
- **État :** contradicted
- **Sujet littéral :** index OpenCode versus source canonique
- **Temps du fait :** snapshot au 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** opencode_history.py stats ; index /Users/sofian/Data/imports/hermes/opencode-history/opencode-index.db
- **Citation / observation :** index_status stale ; source sessions 1609 ; index metadata session_count 1601
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La différence ne permet pas d’identifier les sessions manquantes ; aucun rebuild n’a été effectué.

### CLM-AUD-005-303

- **Statement :** La base enregistre un usage sous plusieurs agents nommés et plusieurs répertoires de projet.
- **État :** live_implementation
- **Sujet littéral :** usage multi-agents et multi-projets
- **Temps du fait :** 2026-06-10..2026-08-26
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** requêtes SQLite read-only sur session : group by agent et directory
- **Citation / observation :** Agents : general 651, explore 250, build 116, jarvis 124 ; répertoires : Sofian-OS 798 sessions, open-job 304 sessions, Homelab-OS 87 sessions
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Des enregistrements de sessions ne prouvent ni utilisation actuelle continue ni qualité des résultats.

### CLM-AUD-005-304

- **Statement :** Le schéma source relie les messages à une session et les parts à un message, avec des clés étrangères et des timestamps distincts.
- **État :** live_implementation
- **Sujet littéral :** contrat interne session-message-part
- **Temps du fait :** snapshot du schéma lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** sqlite3 -readonly .schema message ; .schema part ; .schema session
- **Citation / observation :** message.session_id references session(id) ; part.message_id references message(id) ; part.session_id et les tables portent time_created/time_updated
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le schéma décrit la persistance ; il ne prouve pas quel processus écrivait chaque ligne.

### CLM-AUD-005-305

- **Statement :** Une architecture historique séparait OpenCode Docker sur Nova et OpenChamber comme service UI/proxy, avec des ports distincts et des volumes runtime partagés.
- **État :** historical_execution
- **Sujet littéral :** OpenCode/OpenChamber Homelab
- **Temps du fait :** 2026-06-10
- **Temps d’enregistrement :** 2026-06-10
- **Source :** SRC-OPENCODE
- **Locator :** ses_14e2df203ffekuUz1bqls0KMu7 — réponse finale, section OpenCode Docker Stack et OpenChamber Docker Stack
- **Citation / observation :** OpenCode Docker Stack (nova) ; port 9090 -> 3000 ; OpenChamber Docker Stack (nova) ; port 9091 -> 3000 ; volumes runtime OpenCode partagés
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Architecture historique rapportée ; aucun service ou fichier de déploiement n’a été relu dans SYS-004.

### CLM-AUD-005-306

- **Statement :** Une autre session historique décrit OpenChamber avec OPENCODE_SKIP_START=true comme client d’une instance OpenCode externe, et non comme preuve qu’il lance lui-même OpenCode.
- **État :** historical_execution
- **Sujet littéral :** relation OpenChamber → OpenCode
- **Temps du fait :** 2026-07-02
- **Temps d’enregistrement :** 2026-07-02
- **Source :** SRC-OPENCODE
- **Locator :** ses_0db576410ffekoLvvVM5NDab1y — réponse finale sur les logs OpenChamber/OpenCode
- **Citation / observation :** dans ta config OPENCODE_SKIP_START=true, donc OpenChamber ne lance pas opencode — il se connecte juste à une instance externe
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Configuration historique d’un contexte donné ; ne tranche pas la configuration actuelle.

### CLM-AUD-005-307

- **Statement :** Une proposition historique décrit Jarvis comme master steward avec routage intent→workflow et permissions défensives autour des surfaces Obsidian/TaskNotes.
- **État :** historical_intent
- **Sujet littéral :** Jarvis dans l’écosystème OpenCode
- **Temps du fait :** 2026-06-27
- **Temps d’enregistrement :** 2026-06-27
- **Source :** SRC-OPENCODE
- **Locator :** ses_0f552e33effeaMT8HM8bMavnQ2 — réponse finale, sections capabilities et intent→workflow
- **Citation / observation :** Jarvis serves as the Master Steward ; Intent Table ; permission model highly defensive
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Proposition historique ; le parent AUD-003 distingue ce rôle des identités actuelles Jarvis Agent, Jarvis OS et Hermes.

### CLM-AUD-005-308

- **Statement :** Une session historique a proposé Obsidian comme adaptateur, TaskNotes comme source des tâches et Jarvis comme routeur/intendant des routines.
- **État :** historical_intent
- **Sujet littéral :** Jarvis / Sofian OS
- **Temps du fait :** 2026-08-06
- **Temps d’enregistrement :** 2026-08-06
- **Source :** SRC-OPENCODE
- **Locator :** ses_027208599ffe4z7qrsGkVcziTe — réponse finale, modèle d’architecture
- **Citation / observation :** Obsidian joue l’adaptateur, TaskNotes la source des tâches, et Jarvis le routeur/intendant
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Proposition non acceptée ; ne constitue pas le contrat actuel et ne donne aucune autorité métier à OpenCode.

### CLM-AUD-005-309

- **Statement :** Une session historique a rapporté la présence du package @ourmem/opencode v0.3.2 et a séparé cette présence de l’activation effective dans la configuration OpenCode.
- **État :** historical_execution
- **Sujet littéral :** @ourmem/opencode
- **Temps du fait :** 2026-07-22
- **Temps d’enregistrement :** 2026-07-22
- **Source :** SRC-OPENCODE
- **Locator :** ses_07591aad6ffeVMGBQmfWtfLuI3 — sections composants et lacunes prouvées
- **Citation / observation :** Plugin npm @ourmem/opencode v0.3.2 — INSTALLÉ ; Mais le plugin n'est PAS activé dans opencode.jsonc actif
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Rapport historique ; aucune relecture de configuration ou activation n’a été faite dans SYS-004.

### CLM-AUD-005-310

- **Statement :** Une revue historique a signalé une correction de configuration MCP OpenCode : le remplacement d’un package indisponible par mcp-3d-printer-server, puis une correction ultérieure vers un runtime local et des permissions de lecture ciblées.
- **État :** historical_execution
- **Sujet littéral :** corrections de configuration OpenCode
- **Temps du fait :** 2026-08-02
- **Temps d’enregistrement :** 2026-08-02
- **Source :** SRC-OPENCODE
- **Locator :** ses_03b6620a3ffebGqQpAsVVuYDbb et ses_03b518addffe85x1BXjW8Z82ox — réponses finales
- **Citation / observation :** 550dfd4 replaced the command with mcp-3d-printer-server ; All other requested config changes are semantically correct ; Permission precedence correctly denies moonraker_* then permits exactly the five specified read tools
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les sessions sont des audits historiques et non une preuve de l’état actuel de la configuration ou du runtime.

### CLM-AUD-005-311

- **Statement :** Une tentative historique de rappel OpenCode pour la revue quotidienne a rapporté des erreurs 401 Unauthorized sur le consommateur d’exploration externe et des éléments restés en attente.
- **État :** historical_execution
- **Sujet littéral :** opencode-session-recall et revue quotidienne
- **Temps du fait :** 2026-08-18
- **Temps d’enregistrement :** 2026-08-18
- **Source :** SRC-OPENCODE
- **Locator :** ses_fe949f465ffeSQioRcjCXibPEF — réponse finale, synthèse du contexte
- **Citation / observation :** Toutes les tentatives d'exploration des bases (explore) ont échoué avec une erreur 401 Unauthorized ; les requêtes étaient en attente d’exécution
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Échec à cette date ; ne prouve ni la cause actuelle ni l’échec de toutes les fonctions OpenCode.

### CLM-AUD-005-312

- **Statement :** Le statut actuel du service OpenCode/OpenChamber est inconnu dans ce dossier : la base de sessions prouve des enregistrements récents mais aucun processus, conteneur ou API live n’a été interrogé.
- **État :** unknown
- **Sujet littéral :** runtime OpenCode/OpenChamber
- **Temps du fait :** snapshot au 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** opencode_history.py stats et schémas SQLite ; périmètre SYS-004 sans healthcheck/service
- **Citation / observation :** Observation directe : la source expose des tables de persistance et des timestamps, pas un état de processus ou de connexion ; aucun runtime n’a été interrogé
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le statut unknown est une limite de couverture, pas une preuve d’absence.

### CLM-AUD-005-401

- **Statement :** ourmem est décrit comme une mémoire persistante et partagée entre sessions, appareils, agents et équipes, disponible en mode self-hosted ou hosted.
- **État :** current_canon
- **Sujet littéral :** ourmem
- **Temps du fait :** snapshot de la skill locale consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/dotfiles/.ai-agents/skills/ourmem/SKILL.md:54-73
- **Citation / observation :** La skill décrit ourmem comme une mémoire persistante partagée et distingue hosted et self-hosted.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La description documentaire ne prouve ni un besoin utilisateur validé ni un usage opérationnel maintenu.

### CLM-AUD-005-402

- **Statement :** La surface MCP ourmem accessible pendant l’audit contient 698 mémoires actives, toutes de type insight, dans l’espace default et au tier peripheral.
- **État :** live_implementation
- **Sujet littéral :** ourmem MCP / espace default
- **Temps du fait :** 2026-08-28T16:13:16+02:00
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OURMEM
- **Locator :** MCP mcp__ourmem__memory_stats, réponse reçue le 2026-08-28T16:13:16+02:00
- **Citation / observation :** total=698 ; by_type insight=698 ; by_space default=698 ; by_state active=698 ; by_tier peripheral=698.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La statistique ne prouve ni la qualité, ni la fraîcheur métier, ni la sauvegarde, ni la persistance future.

### CLM-AUD-005-403

- **Statement :** Les lectures MCP `memory_profile`, `memory_list` et `list_resources` ont répondu pendant l’audit, avec la ressource déclarée `omem://profile`.
- **État :** live_implementation
- **Sujet littéral :** ourmem MCP read surface
- **Temps du fait :** 2026-08-28T16:13:16+02:00
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OURMEM
- **Locator :** MCP mcp__ourmem__memory_profile, mcp__ourmem__memory_list(limit=20), mcp__ourmem__list_resources
- **Citation / observation :** Les trois appels ont renvoyé un résultat ; `list_resources` expose `omem://profile`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Cela prouve une lecture bornée via le MCP utilisé ici, pas la disponibilité de toutes les fonctions ni la configuration de chaque client.

### CLM-AUD-005-404

- **Statement :** Les deux recherches sémantiques MCP tentées pendant l’audit ont échoué avec une erreur HTTP 500 enveloppant une réponse 403 du fournisseur d’embeddings pour quota gratuit épuisé.
- **État :** live_implementation
- **Sujet littéral :** ourmem MCP semantic search
- **Temps du fait :** 2026-08-28T16:13:16+02:00
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OURMEM
- **Locator :** MCP mcp__ourmem__memory_search, deux appels bornés pendant l’audit
- **Citation / observation :** `Search failed: 500 Internal Server Error` ; cause imbriquée : embedding API `403 Forbidden`, quota gratuit épuisé.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-403"]
- **Review :** accepted
- **Limite :** L’échec concerne la recherche sémantique dans cette fenêtre ; il ne prouve pas que les mémoires sont absentes ni que les lectures list/profile sont indisponibles.

### CLM-AUD-005-405

- **Statement :** Le compose courant dans Homelab-OS définit un service `omem-server` nommé `omem`, construit depuis `ourmem/omem` et exposé par une liaison localhost `127.0.0.1:3608:8080`, avec redémarrage automatique et limites mémoire.
- **État :** live_implementation
- **Sujet littéral :** omem-server / Homelab-OS Nova compose
- **Temps du fait :** snapshot du fichier lu le 2026-08-28 ; fichier modifié dans le worktree
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/nova/omem/compose.yml:11-26
- **Citation / observation :** Service `omem-server`, `container_name: omem`, build depuis le dépôt upstream, `restart: unless-stopped`, `mem_limit: 256m`, `memswap_limit: 512m`, port localhost 3608 vers 8080 et montage de données runtime hors dépôt.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-410"]
- **Review :** accepted
- **Limite :** Un compose présent et lisible ne prouve ni qu’il est déployé, ni que le conteneur tourne, ni que l’image construite correspond à la définition.

### CLM-AUD-005-406

- **Statement :** Le compose courant contient trois variables d’environnement `*_API_KEY` avec des valeurs non placeholders pour l’embedding, le LLM et le reranking.
- **État :** live_implementation
- **Sujet littéral :** omem-server credentials configuration
- **Temps du fait :** snapshot du fichier lu le 2026-08-28 ; fichier modifié dans le worktree
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/nova/omem/compose.yml:28-43
- **Citation / observation :** Les blocs embedding, LLM et reranking contiennent chacun une variable de clé avec une valeur concrète ; aucune valeur n’est reproduite ici.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-407"]
- **Review :** accepted
- **Limite :** Le fichier est actuellement modifié dans le worktree ; la présence dans le worktree ne prouve pas que ces valeurs sont commitées ou déployées.

### CLM-AUD-005-407

- **Statement :** La présence de clés concrètes dans le compose courant contredit la politique Homelab-OS qui interdit les clés API en dépôt et prescrit des secrets externes.
- **État :** contradicted
- **Sujet littéral :** Homelab-OS secrets policy versus omem compose
- **Temps du fait :** snapshot du compose et de la politique lus le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/nova/omem/compose.yml:28-43 ; /Users/sofian/Homelab-OS/SECRETS.md:1-35
- **Citation / observation :** `SECRETS.md` interdit les API keys/tokens/passwords et recommande `env_file` depuis `~/Data/secrets`; le compose contient des valeurs concrètes dans `environment`.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-406"]
- **Review :** accepted
- **Limite :** Aucun diagnostic de rotation ou de compromission n’a été effectué, conformément à la frontière de lecture seule.

### CLM-AUD-005-408

- **Statement :** Homelab-OS définit une workflow GitHub Actions `Build Omem` déclenchable manuellement et planifiée chaque dimanche, qui construit puis pousse `ghcr.io/sofian-bll/omem-server:latest`.
- **État :** current_canon
- **Sujet littéral :** omem image build workflow
- **Temps du fait :** configuration lue le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/.github/workflows/build-omem.yml:1-33
- **Citation / observation :** `workflow_dispatch`, cron hebdomadaire, checkout `ourmem/omem` et `docker/build-push-action` avec le tag GHCR latest.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucun run CI, digest d’image, déploiement ou rollback n’a été vérifié ; le workflow est une définition, pas une preuve d’exécution.

### CLM-AUD-005-409

- **Statement :** La configuration OpenCode versionnée dans dotfiles autorise un répertoire local de skill `ourmem`, mais la recherche bornée n’y a retrouvé ni entrée `@ourmem/opencode`, ni `plugin_config`, ni variables `OMEM_API_URL` ou `OMEM_API_KEY`.
- **État :** live_implementation
- **Sujet littéral :** OpenCode dotfiles integration
- **Temps du fait :** snapshot du fichier et des recherches lus le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/dotfiles/.config/opencode/opencode.jsonc:207-222 ; recherche bornée dans /Users/sofian/dotfiles
- **Citation / observation :** Le bloc de permissions contient `/Users/sofian/.config/opencode/skills/ourmem/*`; la recherche ciblée des marqueurs de plugin/configuration a renvoyé zéro résultat dans les fichiers visibles.
- **Confiance :** medium
- **Contradictions :** ["CLM-AUD-005-410"]
- **Review :** accepted
- **Limite :** Une absence dans cette recherche ne prouve pas l’absence du plugin dans un autre fichier ou dans l’état runtime non inspecté.

### CLM-AUD-005-410

- **Statement :** Un document Homelab-OS daté du 2026-06-03 décrivait Omem comme planifié sur Void, avec domaine Tailscale, volume Docker nommé, réseaux `proxy` et `ai`, dépendance future à Ollama et plugin OpenCode côté Nova.
- **État :** historical_intent
- **Sujet littéral :** Omem deployment documentation
- **Temps du fait :** 2026-06-03
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/vault-os/20-29 Services/22 AI/22.01 Omem.md:1-18,29-113
- **Citation / observation :** Frontmatter `status: planned`, hôte Void et exposition tailscale ; compose documentaire avec volume `omem_data`, réseaux `proxy` + `ai`, puis notes sur OpenCode et le patch `isSystemNoise`.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-405"]
- **Review :** accepted
- **Limite :** Ce document est historique et explicitement planifié ; il ne prouve pas l’état actuel ni ne permet de qualifier la solution d’obsolète.

### CLM-AUD-005-411

- **Statement :** La skill locale documente un contrat MCP comprenant notamment `memory_store`, `memory_search`, `memory_list`, `memory_get`, `memory_update`, `memory_forget`, `memory_ingest`, `memory_stats` et `memory_profile`.
- **État :** current_canon
- **Sujet littéral :** ourmem API/MCP contract
- **Temps du fait :** snapshot de la skill consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/dotfiles/.ai-agents/skills/ourmem/SKILL.md:106-128
- **Citation / observation :** La table locale associe ces outils à la persistance, recherche, listing, lecture, correction, suppression, ingestion et statistiques.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le contrat local n’a pas été comparé au code upstream ni exercé pour les opérations d’écriture, interdites par ce workstream.

### CLM-AUD-005-412

- **Statement :** La documentation locale décrit les permissions ourmem par API key et Spaces, avec des rôles `admin`, `member` et `reader`, et une visibilité limitée aux espaces propres ou partagés.
- **État :** current_canon
- **Sujet littéral :** ourmem permissions model
- **Temps du fait :** snapshot de la skill consultée le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/dotfiles/.ai-agents/skills/ourmem/SKILL.md:60-73,188-200
- **Citation / observation :** La skill décrit l’API key comme identité, les Spaces personal/team/organization, les trois rôles et l’interdiction de voir l’espace privé d’un autre agent.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucun rôle effectif, partage concret, politique de moindre privilège ou ACL runtime n’a été relu via une API dédiée.

### CLM-AUD-005-501

- **Statement :** Homelab-OS est décrit comme un control repo de configuration et de documentation utilisé pour reconstruire l’environnement de Sofian sur Nova, Void et Pulsar ; ce n’est pas présenté comme un projet applicatif normal.
- **État :** current_canon
- **Sujet littéral :** Homelab-OS
- **Temps du fait :** snapshot documentaire courant
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/AGENTS.md:3-7; /Users/sofian/Homelab-OS/README.md:1-5
- **Citation / observation :** Les sources nomment Homelab-OS control/configuration repo et source of truth pour reconstruire l’environnement.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La documentation ne prouve ni reconstruction réussie ni usage opérationnel maintenu.

### CLM-AUD-005-502

- **Statement :** La canon actuelle déclarée par AGENTS, README, 66 et 67 utilise `~/Homelab-OS`, `~/Developer`, `~/Data`, des dossiers natifs et des dotfiles gérés via yadm ; `bootstrap-linux.sh` est l’entrée Linux.
- **État :** current_canon
- **Sujet littéral :** layout et bootstrap Homelab-OS
- **Temps du fait :** à partir du 2026-07-07 selon les sources courantes
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/AGENTS.md:35-50; /Users/sofian/Homelab-OS/README.md:7-21,55-78; /Users/sofian/Homelab-OS/vault-os/60-69 Architecture/67 Unified Home Architecture.md:22-53; /Users/sofian/Homelab-OS/vault-os/60-69 Architecture/66 Deployment Guide.md:41-82
- **Citation / observation :** Les documents courants convergent vers `~/Data`, `~/Developer`, yadm et `./scripts/bootstrap-linux.sh`.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-509"]
- **Review :** accepted
- **Limite :** La présence des contrats dans les fichiers ne prouve pas qu’ils sont appliqués sur chaque machine.

### CLM-AUD-005-503

- **Statement :** Le snapshot courant contient 20 fichiers Compose sous `docker/stacks` : 11 suivis par Git et 9 répertoires de stacks non suivis dans le working tree.
- **État :** live_implementation
- **Sujet littéral :** inventaire déclaratif des stacks
- **Temps du fait :** snapshot du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** Inventaire read-only de `/Users/sofian/Homelab-OS/docker/stacks`; `git ls-files` et `git status --short`
- **Citation / observation :** La recherche de fichiers Compose retourne 20 résultats ; Git retourne 11 chemins suivis et 9 répertoires `??` de stacks.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Un fichier Compose présent, suivi ou non, ne prouve pas qu’une stack est déployée ou active.

### CLM-AUD-005-504

- **Statement :** `scripts/bootstrap-linux.sh` définit un bootstrap Linux non-root avec modes apply, `--check` et `--dry-run`, création du layout, paquets apt/Homebrew, outils CLI, yadm conditionnel et permissions 700 pour `~/Data/secrets`; les dotfiles ne sont pas clonés automatiquement.
- **État :** live_implementation
- **Sujet littéral :** bootstrap-linux.sh
- **Temps du fait :** code présent dans le snapshot du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/scripts/bootstrap-linux.sh:1-25,85-114,133-169,187-203,236-320
- **Citation / observation :** Le script contient les modes, les listes de paquets, le layout, la garde Linux/non-root, le chmod secrets et le bootstrap yadm conditionnel.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune exécution n’a été relancée ; compatibilité réelle avec une machine et résultat final inconnus.

### CLM-AUD-005-505

- **Statement :** Les contrats déclarés séparent le dépôt des données runtime : volumes sous `~/Data/appdata`, secrets sous `~/Data/secrets`, backups/imports/tmp hors Git, avec chemins absolus adaptés à Linux ou Nova.
- **État :** current_canon
- **Sujet littéral :** séparation dépôt/runtime
- **Temps du fait :** snapshot documentaire courant
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/AGENTS.md:10-12,35-40; /Users/sofian/Homelab-OS/SECRETS.md:1-43; /Users/sofian/Homelab-OS/vault-os/60-69 Architecture/67 Unified Home Architecture.md:126-148; /Users/sofian/Homelab-OS/vault-os/10-19 Infrastructure/12 Storage.md:17-48
- **Citation / observation :** Les sources placent appdata, secrets, backups, imports et tmp sous `Data` hors Git et imposent des chemins absolus.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-511"]
- **Review :** accepted
- **Limite :** La séparation documentaire ne prouve ni permissions réelles ni absence de secrets dans tout l’historique.

### CLM-AUD-005-506

- **Statement :** Le Compose courant de Dockhand monte `docker/stacks` dans le conteneur sans suffixe read-only et monte le socket Docker en accès rw ; la configuration autorise donc potentiellement Dockhand à écrire les déclarations et à contrôler Docker, sans prouver que ces écritures ont eu lieu.
- **État :** live_implementation
- **Sujet littéral :** Dockhand comme writer potentiel
- **Temps du fait :** snapshot du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/void/dockhand/compose.yml:4-23; /Users/sofian/Homelab-OS/vault-os/20-29 Services/21 Core/21.00 Dockhand.md:44-68,87-106
- **Citation / observation :** Le Compose déclare `/home/sofian/Homelab-OS/docker/stacks:/app/data/stacks` et `/var/run/docker.sock:/var/run/docker.sock`, sans `:ro`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le mode d’utilisation effectif de Dockhand et son writer exact restent inconnus ; le risque est de configuration, pas une preuve d’écriture.

### CLM-AUD-005-507

- **Statement :** Les Compose et le Port Registry déclarent des bindings hôte sur IP Tailscale pour Caddy, AdGuard et Dockhand, ainsi qu’une exception LAN pour MediaMTX ; Caddy utilise actuellement un réseau Docker `proxy` et des mappings de ports dans le Compose lu.
- **État :** live_implementation
- **Sujet littéral :** bindings réseau déclarés
- **Temps du fait :** snapshot du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/void/caddy/compose.yaml:11-27,49-52; /Users/sofian/Homelab-OS/docker/stacks/void/adguard/compose.yaml:3-25; /Users/sofian/Homelab-OS/docker/stacks/void/dockhand/compose.yml:3-27; /Users/sofian/Homelab-OS/vault-os/60-69 Architecture/61 Port Registry.md:14-54
- **Citation / observation :** Les déclarations contiennent notamment des mappings pour 80/443, 53 et 9000 sur `100.115.31.73`, et des exceptions LAN documentées pour MediaMTX.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-508"]
- **Review :** accepted
- **Limite :** Les bindings déclarés ne prouvent pas l’écoute effective ni l’exposition réelle.

### CLM-AUD-005-508

- **Statement :** `62 Network Architecture.md` affirme un principe de zéro port exposé sur l’OS hôte hors MediaMTX, alors que le Port Registry et les Compose actuels déclarent des bindings hôte pour plusieurs services.
- **État :** contradicted
- **Sujet littéral :** contrat réseau zéro-port
- **Temps du fait :** snapshot documentaire du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/vault-os/60-69 Architecture/62 Network Architecture.md:17-20,162-166,191-197; `/Users/sofian/Homelab-OS/vault-os/60-69 Architecture/61 Port Registry.md:18-54`
- **Citation / observation :** La note réseau écrit « Zéro port exposé sur l’OS hôte, hors exception LAN MediaMTX », tandis que le registre et les Compose déclarent Caddy/AdGuard/Dockhand sur IP Tailscale.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-507"]
- **Review :** accepted
- **Limite :** Aucune décision utilisateur ou vérification runtime ne permet de choisir silencieusement entre ces formulations.

### CLM-AUD-005-509

- **Statement :** Les documents historiques `65 Homelab-OS Architecture Decision.md` et le plan Unified Home Deployment décrivent chezmoi et Ansible comme mécanismes de dotfiles/bootstrap, en conflit avec la canon yadm + `bootstrap-linux.sh` des documents courants.
- **État :** contradicted
- **Sujet littéral :** historique dotfiles/bootstrap
- **Temps du fait :** 2026-06-06..2026-06-07
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/vault-os/60-69 Architecture/65 Homelab-OS Architecture Decision.md:18-27,36-51,136-143; /Users/sofian/Homelab-OS/vault-os/40-49 Operations/Plans/2026-06-07 Unified Home Deployment.md:16-19,39-50,83-142
- **Citation / observation :** Les sources historiques mentionnent chezmoi/Ansible et Vela ; la note 65 indique elle-même que son filesystem layout est remplacé par 63/66/67.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-502"]
- **Review :** accepted
- **Limite :** Conflit documentaire daté ; il ne permet pas d’inférer l’état actuel de `~/dotfiles` ou des machines.

### CLM-AUD-005-510

- **Statement :** La stratégie backup est documentée comme Restic hebdomadaire avec rétention de quatre semaines, secrets manuels et restauration via Restic, mais les tâches d’installation, cron, restauration complète et off-site restent non cochées.
- **État :** current_canon
- **Sujet littéral :** backup/recovery
- **Temps du fait :** snapshot documentaire du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/vault-os/40-49 Operations/42 Backups.md:10-37; /Users/sofian/Homelab-OS/vault-os/10-19 Infrastructure/12 Storage.md:36-48; /Users/sofian/Homelab-OS/vault-os/50-59 Knowledge/51 Workflows.md:31-45
- **Citation / observation :** La procédure Restic et la restauration sont écrites ; `Installer Restic`, `Configurer cron`, `Tester une restauration complète` et `Backup off-site` sont non cochés.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Documentation de procédure uniquement : outil, exécution, snapshots, RPO/RTO et restauration réelle inconnus.

### CLM-AUD-005-512

- **Statement :** La CI déclarée valide les fichiers Compose avec `docker compose config --quiet --no-interpolate` et possède un workflow séparé de validation Chezmoi ; aucune exécution CI ou commande de validation n’a été relancée dans ce sous-audit.
- **État :** current_canon
- **Sujet littéral :** CI de validation
- **Temps du fait :** snapshot des workflows du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/.github/workflows/validate-compose.yml:1-37; /Users/sofian/Homelab-OS/.github/workflows/validate-chezmoi.yml:1-34; /Users/sofian/Homelab-OS/Makefile:18-47
- **Citation / observation :** Les workflows déclarent la validation Compose et Chezmoi ; le Makefile expose `validate-compose` et `validate`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence d’un contrôle ou un ancien résultat vert ne prouve ni déploiement ni bon fonctionnement runtime.

### CLM-AUD-005-513

- **Statement :** L’état live de Nova, Void, Pulsar, Docker, Dockhand, Caddy, stacks et backups reste inconnu dans ce dossier, car la mission interdisait healthcheck distant, restart, build, test et lecture des données runtime.
- **État :** unknown
- **Sujet littéral :** runtime Homelab-OS
- **Temps du fait :** au moment du snapshot du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** Frontière de la carte SYS-006 ; Git read-only et fichiers locaux seulement
- **Citation / observation :** Les sources locales déclarent des statuts, ports et services ; aucune observation distante autorisée n’a été obtenue.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Unknown ne signifie ni absent ni arrêté ; une vérification future devra rester read-only et datée.

### CLM-AUD-005-514

- **Statement :** Le besoin de reconstruction cohérente et de séparation déclaratif/runtime est documenté, mais sa validation utilisateur, son outcome mesuré et son usage opérationnel maintenu ne sont pas établis par les sources de SYS-006.
- **État :** hypothesis
- **Sujet littéral :** valeur Homelab-OS
- **Temps du fait :** snapshot documentaire du 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/README.md:1-5,24-53; /Users/sofian/Homelab-OS/AGENTS.md:3-7,41-50
- **Citation / observation :** Les sources décrivent une source de vérité pour rebuild et des règles de séparation ; aucune validation utilisateur ni métrique d’outcome n’est incluse dans le corpus.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Il s’agit d’une limite de preuve, pas d’un rejet du besoin.

### CLM-AUD-005-601

- **Statement :** Finance OS est décrit comme un PocketBase privé dédié aux finances personnelles de Sofian et indépendant d’Athena Dashboard.
- **État :** current_canon
- **Sujet littéral :** Finance OS
- **Temps du fait :** snapshot documentaire lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/README.md:1-3
- **Citation / observation :** Le README nomme Finance OS, PocketBase privé, finances personnelles et indépendance d’Athena Dashboard.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Déclaration documentaire; ne prouve ni besoin validé, ni usage maintenu, ni séparation runtime effectivement appliquée.

### CLM-AUD-005-602

- **Statement :** Le périmètre déclaré comprend les collections accounts, imports, transactions, cashflow_items et documents, ainsi que des exports bancaires, des flux de trésorerie prévus et des justificatifs.
- **État :** current_canon
- **Sujet littéral :** périmètre Finance OS
- **Temps du fait :** snapshot documentaire et code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/README.md:11-27; scripts/import_finance.py:25-124
- **Citation / observation :** Les cinq collections sont nommées dans le README et spécifiées dans COLLECTIONS.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les collections futures ou vides ne prouvent pas qu’elles sont alimentées.

### CLM-AUD-005-603

- **Statement :** L’implémentation de contrat de données est écrite en Python; le déploiement est déclaré en Compose YAML et l’orchestration d’import en Bash.
- **État :** live_implementation
- **Sujet littéral :** langages et artefacts
- **Temps du fait :** snapshot des fichiers lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/import_finance.py:1-24,613-648; compose.yml:1-46; scripts/run_import.sh:1-23
- **Citation / observation :** Les extensions et shebangs montrent Python, YAML Compose et Bash.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Présence statique; aucune exécution n’a été relancée.

### CLM-AUD-005-604

- **Statement :** Le compose définit un conteneur PocketBase avec image épinglée par digest, limites mémoire/processus, no-new-privileges, healthcheck HTTP local, volume pb_data hors Git et réseau externe pulsar.
- **État :** live_implementation
- **Sujet littéral :** déploiement déclaratif Finance OS
- **Temps du fait :** création déclarée le 2026-08-18; contenu du snapshot lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/compose.yml:1-46
- **Citation / observation :** Le service contient image digest, mem_limit, pids_limit, security_opt, healthcheck, volume et réseau externe.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le fichier ne prouve pas que l’image, le réseau ou le conteneur existent sur Pulsar.

### CLM-AUD-005-605

- **Statement :** La persistance déclarée de PocketBase est placée sous Data/appdata/finance-os/pb_data et non dans le dépôt Homelab-OS.
- **État :** current_canon
- **Sujet littéral :** persistance Finance OS
- **Temps du fait :** snapshot documentaire lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/README.md:11-17; compose.yml:37-38
- **Citation / observation :** README et compose convergent vers un volume pb_data hors Git.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune existence, permission, sauvegarde ou restauration du volume n’a été vérifiée.

### CLM-AUD-005-606

- **Statement :** Le collecteur ne découvre que les CSV récursifs dont le nom commence par revolut ou bank_statement; les autres fichiers sont exclus du scan.
- **État :** live_implementation
- **Sujet littéral :** découverte des imports
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/import_finance.py:421-427
- **Citation / observation :** discover_source_files parcourt *.csv et conserve uniquement les deux préfixes supportés.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La couverture réelle des exports présents dans les dossiers source est inconnue; aucune donnée runtime n’a été lue.

### CLM-AUD-005-607

- **Statement :** Les relevés Revolut sont normalisés depuis Amount et dates complètes; les relevés Sumeria prennent en charge deux variantes d’en-têtes, reconstruisent l’année depuis la période du relevé et calculent amount comme credit moins debit.
- **État :** live_implementation
- **Sujet littéral :** normalisation bancaire
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/import_finance.py:287-308,319-408,411-468
- **Citation / observation :** Les fonctions normalize_revolut_row, normalize_sumeria_row et _period_from_metadata portent ces règles.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les règles métier ne sont pas comparées à des exports réels ni à une validation financière; la correction des erreurs est inconnue.

### CLM-AUD-005-608

- **Statement :** Les transactions possèdent un source_uid SHA-256 et un id déterministe; une unicité est imposée en mémoire pendant le scan puis par index PocketBase sur source_uid.
- **État :** live_implementation
- **Sujet littéral :** identité et déduplication des transactions
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/import_finance.py:53-84,311-316,476-491
- **Citation / observation :** _record_identity dérive id/source_uid et scan_source_root lève une erreur en cas de doublon normalisé.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Deux lignes économiquement distinctes mais identiques selon identity_payload peuvent être rejetées; aucune preuve sur exports réels.

### CLM-AUD-005-609

- **Statement :** Le writer observé est l’importeur authentifié: il crée ou vérifie les collections, upsert les comptes, les imports et les transactions, puis marque l’import imported; les transactions sont envoyées en parallèle.
- **État :** live_implementation
- **Sujet littéral :** writers et workflow d’import
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/import_finance.py:173-194,272-284,511-543,581-600
- **Citation / observation :** import_all appelle ensure_collections, _account_records et _import_one_source; ce dernier utilise ThreadPoolExecutor puis update_record.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucun writer runtime ou résultat d’appel n’a été vérifié.

### CLM-AUD-005-610

- **Statement :** Les documents sont importés seulement lorsqu’un manifest JSON est fourni; chaque entrée lit un chemin local, calcule son hash et crée ou met à jour un enregistrement documents avec fichier protégé.
- **État :** live_implementation
- **Sujet littéral :** imports de documents
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/import_finance.py:105-123,546-578
- **Citation / observation :** import_documents retourne vide sans manifest et utilise upsert_file_record pour le fichier document.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le manifest et les documents réels étaient explicitement hors lecture; existence et intégrité opérationnelle inconnues.

### CLM-AUD-005-611

- **Statement :** La collection cashflow_items est spécifiée avec dettes, créances, revenus/dépenses attendus et statuts, mais aucun writer de cashflow_items n’est visible dans les fichiers inspectés.
- **État :** unknown
- **Sujet littéral :** cashflow_items
- **Temps du fait :** snapshot des fichiers inspectés le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/import_finance.py:86-103,581-600; tests/test_import_finance.py:102-108
- **Citation / observation :** La collection est définie et testée comme contrat, mais import_all ne l’alimente pas.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Un writer externe ou une saisie PocketBase hors corpus reste possible; non vérifié.

### CLM-AUD-005-612

- **Statement :** L’accès réseau est déclaré privé: l’interface et l’API sont exposées par une adresse Tailscale fixe sans domaine public, et le compose lie le port à cette adresse.
- **État :** current_canon
- **Sujet littéral :** frontière d’accès
- **Temps du fait :** snapshot documentaire et compose lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/README.md:5-9; compose.yml:26-29
- **Citation / observation :** README dit Tailscale uniquement; compose bind le port à l’adresse privée déclarée.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La règle réseau réelle, le routage Tailscale, les ACL et les règles PocketBase n’ont pas été lus.

### CLM-AUD-005-613

- **Statement :** Le workflow Bash provisionne temporairement un compte superuser sur Pulsar, exécute l’import puis la vérification et tente de supprimer ce compte à la sortie.
- **État :** live_implementation
- **Sujet littéral :** permission et orchestration d’import
- **Temps du fait :** snapshot du script lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/run_import.sh:1-23
- **Citation / observation :** Le script génère un secret de session, l’exporte, utilise ssh/docker exec pour upsert/delete le superuser et appelle import puis verify.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le workflow n’a pas été exécuté; l’exposition de la valeur via argument de commande et la politique d’audit/rotation n’ont pas été éprouvées.

### CLM-AUD-005-614

- **Statement :** Une erreur ValueError sur une ligne Sumeria est silencieusement ignorée pendant load_source_file, puis le fichier peut être marqué imported avec un row_count réduit.
- **État :** live_implementation
- **Sujet littéral :** gestion des erreurs d’import
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/import_finance.py:440-468,511-543
- **Citation / observation :** La boucle Sumeria fait except ValueError: continue; _import_one_source marque ensuite l’import imported après les transactions acceptées.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Impact réel non mesuré sans export; risque de perte silencieuse d’une ligne financière.

### CLM-AUD-005-615

- **Statement :** Les dates parsées sans fuseau sont formatées avec le suffixe Z, tandis que le compose déclare Europe/Paris; la sémantique exacte de l’instant stocké est donc non spécifiée.
- **État :** hypothesis
- **Sujet littéral :** temps des transactions
- **Temps du fait :** snapshot du code et compose lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/import_finance.py:292-308; compose.yml:21-24
- **Citation / observation :** _pb_datetime strftime retourne une valeur finissant par Z sans conversion de fuseau; TZ est Europe/Paris.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Il faut vérifier le contrat PocketBase et l’intention métier avant de conclure à une erreur.

### CLM-AUD-005-616

- **Statement :** Le dépôt fournit une validation locale déclarée par docker compose config et unittest, mais aucune de ces commandes n’a été exécutée dans cet audit read-only.
- **État :** current_canon
- **Sujet littéral :** preuves de validation
- **Temps du fait :** snapshot documentaire lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/README.md:29-34; tests/test_import_finance.py:1-187
- **Citation / observation :** Le README documente les commandes; le fichier de tests contient des cas de normalisation, découverte et client PocketBase.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La présence des tests ne prouve ni leur succès actuel, ni une couverture complète, ni un cas financier réel.

### CLM-AUD-005-617

- **Statement :** Les cinq fichiers Finance OS sont présents mais non suivis par Git dans le snapshot Homelab-OS; aucun historique Git propre à ce chemin n’a été trouvé par git log.
- **État :** live_implementation
- **Sujet littéral :** provenance du snapshot
- **Temps du fait :** état Git vérifié le 2026-08-28 à 16:25:03 +0200
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** git status --short --branch et git log -5 -- docker/stacks/pulsar/finance-os; /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/*
- **Citation / observation :** Le chemin Finance OS apparaît comme répertoire non suivi et ses cinq fichiers lisibles sont dans ce répertoire.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le statut peut changer après le snapshot; non-suivi ne prouve ni absence d’usage ni absence de déploiement antérieur.

### CLM-AUD-005-618

- **Statement :** Une contradiction de périmètre existe entre l’instruction parente Homelab-OS, qui affirme qu’il n’y a pas de suites de tests, et Finance OS, qui contient tests/test_import_finance.py et documente une commande unittest.
- **État :** contradicted
- **Sujet littéral :** contrat de validation Homelab-OS versus Finance OS
- **Temps du fait :** snapshot des instructions et fichiers lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/AGENTS.md:7-10; docker/stacks/pulsar/finance-os/README.md:29-34; tests/test_import_finance.py:1-187
- **Citation / observation :** AGENTS.md dit no test suites; le sous-répertoire Finance OS contient une suite unittest explicitement documentée.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-005-616"]
- **Review :** accepted
- **Limite :** Le sens de l’instruction parente pour les stacks applicatives n’est pas clarifié; ne pas choisir silencieusement une règle.

### CLM-AUD-005-620

- **Statement :** L’autorité et la correction sont seulement partielles: les fichiers d’export/manifest fournissent les entrées d’import, PocketBase reçoit les enregistrements normalisés, mais aucun workflow de correction financière, de rapprochement ou de rollback métier n’est documenté dans le corpus inspecté.
- **État :** unknown
- **Sujet littéral :** autorité et correction par fait
- **Temps du fait :** snapshot des sources inspectées le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/README.md:11-27; scripts/import_finance.py:319-408,511-600
- **Citation / observation :** Le code conserve raw_data, hashes et source_file, mais expose seulement les opérations d’upsert/import/verify observées.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les règles PocketBase ou procédures externes non nommées restent inconnues.

### CLM-AUD-005-621

- **Statement :** Plusieurs copies ou vues peuvent diverger: raw_data recopie la ligne source, imports conserve le fichier source protégé, documents conserve une copie de fichier et original_path, tandis que les champs normalisés et comptes sont dérivés.
- **État :** live_implementation
- **Sujet littéral :** copies et projections Finance OS
- **Temps du fait :** snapshot du code lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/import_finance.py:38-123,335-359,384-408,494-508,552-578
- **Citation / observation :** Les schémas et normaliseurs définissent raw_data, source_file, original_path et les champs dérivés.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La politique de divergence, fraîcheur, reconstruction et correction de chaque copie n’est pas définie.

### CLM-AUD-005-622

- **Statement :** Le script run_import.sh a par défaut un répertoire source sous le préfixe macOS, alors que le compose et le déploiement ciblent Pulsar Linux; l’hôte prévu pour exécuter l’import n’est pas explicité.
- **État :** unknown
- **Sujet littéral :** hôte d’exécution de l’import
- **Temps du fait :** snapshot du code et README lu le 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/Homelab-OS/docker/stacks/pulsar/finance-os/scripts/run_import.sh:4-6,18-23; README.md:36-45; compose.yml:37-38
- **Citation / observation :** Le défaut SOURCE_ROOT utilise /Users/... tandis que le déploiement et le volume utilisent /home/... sur Pulsar.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le script peut être intentionnellement lancé depuis Nova avec accès réseau; aucun runbook ne tranche ce scénario.

## Claims rejetés ou hors intégration

### Élément 1

- **id :** CLM-AUD-005-125

### Élément 2

- **id :** CLM-AUD-005-126

### Élément 3

- **id :** CLM-AUD-005-210

### Élément 4

- **id :** CLM-AUD-005-217

### Élément 5

- **id :** CLM-AUD-005-223

### Élément 6

- **id :** CLM-AUD-005-224

### Élément 7

- **id :** CLM-AUD-005-313

### Élément 8

- **id :** CLM-AUD-005-511

### Élément 9

- **id :** CLM-AUD-005-619

### Élément 10

- **ids :**

- CLM-AUD-005-125
- CLM-AUD-005-126

- **reason :** Claims méta non atomiques mêlant niveau positif, absences de preuve et listes d’inconnues.

### Élément 11

- **ids :**

- CLM-AUD-005-210

- **reason :** La réémission SYS-003 perd le sous-fait « le prompt doit être autonome » ; parité sémantique incomplète.

### Élément 12

- **ids :**

- CLM-AUD-005-217
- CLM-AUD-005-223

- **reason :** Snapshots dynamiques sans `valid_time` horodaté ; les valeurs ont dérivé lors de la relecture.

### Élément 13

- **ids :**

- CLM-AUD-005-224

- **reason :** Locator non direct et temps d’enregistrement non réconcilié.

### Élément 14

- **ids :**

- CLM-AUD-005-313

- **reason :** Agrège état de preuve et niveau de livraison, et nie trop largement un cas réel ; la classification reste par composant.

### Élément 15

- **ids :**

- CLM-AUD-005-511

- **reason :** Doublon inter-dossiers du constat SYS-005 sur le même compose et la même politique de secrets ; conserver CLM-AUD-005-406/407 et CLM-AUD-005-505.

### Élément 16

- **ids :**

- CLM-AUD-005-619

- **reason :** Claim méta non atomique ; preuves statiques, tests non exécutés et niveaux inconnus doivent rester séparés.

## Provenance

- Synthèse Kanban : `t_420c7653`.
- `review_status: accepted` signifie accepté pour ce rapport documentaire, pas `user_accepted` ni `operational`.
- Mutations des sources : `0`.
