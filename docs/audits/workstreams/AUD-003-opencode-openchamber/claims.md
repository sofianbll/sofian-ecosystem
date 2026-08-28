---
id: AUD-003-CLAIMS
title: AUD-003 — Ledger des claims
status: integrated
date: 2026-08-28
coverage: 83
---

# AUD-003 — Ledger exhaustif des claims

> Annexe intégrée du [rapport AUD-003](report.md). Ces 83 claims ont été retenus après collecte, contre-reviews et normalisations explicites.

### CLM-AUD-003-001

- **Statement :** Sofian a demandé un audit strictement en lecture seule du vault et des notes Jarvis, avec sources de vérité, flux, permissions, contradictions et boucles ouvertes.
- **État :** historical_intent
- **Sujet littéral :** Audit architecture Jarvis OS
- **Temps du fait :** 2026-08-06
- **Temps d’enregistrement :** 2026-08-06T20:59:12.454000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_027208599ffe4z7qrsGkVcziTe — message user initial
- **Citation / observation :** AUDIT STRICTEMENT EN LECTURE SEULE... Produis en français un modèle d’architecture... Ne modifie rien.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Instruction utilisateur d’audit ; ne prouve ni état ni acceptation d’architecture.

### CLM-AUD-003-002

- **Statement :** La session 1 a proposé un modèle où Obsidian joue l’adaptateur, TaskNotes la source des tâches, et Jarvis le routeur/intendant des routines Daily/Inbox/Engage.
- **État :** proposed
- **Sujet littéral :** Jarvis / Sofian OS
- **Temps du fait :** 2026-08-06
- **Temps d’enregistrement :** 2026-08-06T21:02:00.392000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_027208599ffe4z7qrsGkVcziTe — réponse finale
- **Citation / observation :** Règle d’or : System first, Tool second, Automation later ; TaskNotes = source de vérité des tâches ; flux Inbox → Tasks/Projects/Ressources → Dashboards.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Proposition assistant historique, non décision utilisateur et non canon actuel.

### CLM-AUD-003-003

- **Statement :** La session 2 a rencontré des échecs unauthorized_client sur les recherches web demandées, puis a poursuivi avec des fetches ; ses recommandations ne prouvent donc pas une recherche conforme au protocole initial.
- **État :** historical_execution
- **Sujet littéral :** Web research agent ecosystem
- **Temps du fait :** 2026-06-27
- **Temps d’enregistrement :** 2026-06-27T20:11:31.569000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0f54aa593ffeVDSYqTJL8YZjBR — messages assistant
- **Citation / observation :** WebSearch is failing with unauthorized errors... All websearch_cited calls are failing with unauthorized_client.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Échec visible du canal websearch ; ne qualifie pas toutes les sources de remplacement.

### CLM-AUD-003-004

- **Statement :** La session 2 a formulé des recommandations d’installation/configuration de mémoire, MCP et commandes OpenCode, mais elles restent des propositions historiques non acceptées dans cette session.
- **État :** proposed
- **Sujet littéral :** Personal AI Assistant Ecosystem
- **Temps du fait :** 2026-06-27
- **Temps d’enregistrement :** 2026-06-27T20:13:17.412000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0f54aa593ffeVDSYqTJL8YZjBR — réponse finale
- **Citation / observation :** MASTER RECOMMENDATIONS ; Phase 1 — Install THIS WEEK ; Total tools to install now.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Recommandations historiques sans acceptation ni exécution prouvée.

### CLM-AUD-003-005

- **Statement :** La session 3 ne contient dans la sortie visible que la demande d’audit des skills ; aucune conclusion, artefact, test ou boucle ouverte produite par l’assistant n’est disponible.
- **État :** unknown
- **Sujet littéral :** Audit Jarvis skills gaps
- **Temps du fait :** 2026-06-27
- **Temps d’enregistrement :** 2026-06-27T19:39:57.332000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0f56773f1ffe5NTSQpZKvtawdN — fin de show sans réponse finale
- **Citation / observation :** Dernier contenu visible : demande utilisateur ; aucun rapport assistant visible.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Absence de réponse visible ; ne pas inférer un résultat caché.

### CLM-AUD-003-006

- **Statement :** La session 4 a décrit Jarvis comme master steward avec routage intent→workflow, permissions défensives et couplage aux surfaces Obsidian/TaskNotes.
- **État :** historical_intent
- **Sujet littéral :** Analyze Jarvis current state
- **Temps du fait :** 2026-06-27
- **Temps d’enregistrement :** 2026-06-27T20:02:45.677000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0f552e33effeaMT8HM8bMavnQ2 — réponse finale
- **Citation / observation :** Jarvis serves as the Master Steward... Intent Table... permission model highly defensive.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le rapport n’est pas une relecture live actuelle des configs.

### CLM-AUD-003-007

- **Statement :** La session 5 a reçu une demande de continuation de l’implémentation Task 3 avec correction d’encodage, RED attendu puis GREEN/py_compile, mais sa sortie visible s’arrête sur le message utilisateur et ne prouve pas une clôture.
- **État :** unknown
- **Sujet littéral :** Implement local collectors TDD
- **Temps du fait :** 2026-07-20
- **Temps d’enregistrement :** 2026-07-20T03:03:09.024000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0828893e7ffeF5ped44jHp7Fhi — dernier message visible
- **Citation / observation :** Continue the same implementation task... Return only when DONE or DONE_WITH_CONCERNS...
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Demande de continuation visible, clôture non prouvée.

### CLM-AUD-003-008

- **Statement :** La première revue de la session 6 a identifié des contournements par constantes synthétiques et des défauts de filtrage/découverte, puis la re-revue a déclaré ces écarts corrigés.
- **État :** historical_execution
- **Sujet littéral :** Review collectors spec
- **Temps du fait :** 2026-07-20
- **Temps d’enregistrement :** 2026-07-20T03:23:15.122000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0827362e6ffe7X9va724pA72vP — deux messages user et réponse
- **Citation / observation :** Initial review : Requirement Gaps ; re-review : APPROVED ; all 17 tests now pass.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Verdict de reviewer historique ; tests non rejoués dans R2.

### CLM-AUD-003-009

- **Statement :** La session 6 affirme que collect_activitywatch, scan_tasknotes, collect_spotlight, collect_git_activity et le CLI utilisent finalement les entrées arbitraires/injectées, avec confidentialité et tri déterministe.
- **État :** historical_execution
- **Sujet littéral :** Jarvis daily collectors
- **Temps du fait :** 2026-07-20
- **Temps d’enregistrement :** 2026-07-20T03:27:33.335000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0827362e6ffe7X9va724pA72vP — re-review response
- **Citation / observation :** APPROVED ; dynamically aggregates fetched events; parses arbitrary frontmatter/runner output; invokes all four collectors.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Claim historique du reviewer, non rejoué ici.

### CLM-AUD-003-010

- **Statement :** La session 7 a déclaré 14 tests verts, compilation réussie et une implémentation standard-library-only dans scripts/jarvis_daily.py, sans commit.
- **État :** historical_execution
- **Sujet littéral :** Make collectors tests green
- **Temps du fait :** 2026-07-20
- **Temps d’enregistrement :** 2026-07-20T03:22:52.403000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_082830bdeffe76EL0yB5nhVNqV — réponse finale
- **Citation / observation :** All 14 tests pass, the code compiles... Changed path: .../scripts/jarvis_daily.py.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Résultat historique ; aucun test n’a été relancé selon la frontière de cette carte.

### CLM-AUD-003-011

- **Statement :** Le fichier live jarvis_daily.py contient actuellement les agrégateurs ActivityWatch, le scan TaskNotes, la découverte Git, les collecteurs Git/Spotlight et les enveloppes source_result correspondantes.
- **État :** live_implementation
- **Sujet littéral :** jarvis_daily.py
- **Temps du fait :** 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/.config/opencode/skills/productivity/jarvis-daily-brief/scripts/jarvis_daily.py — lignes 237–642 relues
- **Citation / observation :** Fonctions aggregate_window_events, aggregate_web_events, collect_activitywatch, scan_tasknotes, discover_git_repositories, collect_git_activity et collect_spotlight présentes.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Présence du code ≠ tests actuels, intégration ou usage opérationnel.

### CLM-AUD-003-012

- **Statement :** Le fichier live de tests contient les cas collectors et CLI historiques, ainsi que des tests de comportement mail ajoutés ultérieurement ; le périmètre actuel dépasse le Task 3 historique.
- **État :** live_implementation
- **Sujet littéral :** test_jarvis_daily.py
- **Temps du fait :** 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/.config/opencode/skills/productivity/jarvis-daily-brief/tests/test_jarvis_daily.py — lignes 126–545 relues et taille statée
- **Citation / observation :** Les tests ActivityWatch/TaskNotes/Git/Spotlight/CLI sont présents ; le fichier compte 1 881 lignes et contient ensuite JarvisDailyMailTests.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune exécution de tests autorisée ou réalisée.

### CLM-AUD-003-013

- **Statement :** Un SKILL.md existe actuellement dans le dossier jarvis-daily-brief, contrairement à l’exclusion « ne pas créer SKILL.md » formulée dans les sessions d’implémentation historiques ; cela indique une évolution temporelle, pas une contradiction automatique.
- **État :** live_implementation
- **Sujet littéral :** jarvis-daily-brief SKILL.md
- **Temps du fait :** 2026-08-28
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-LIVE
- **Locator :** /Users/sofian/.config/opencode/skills/productivity/jarvis-daily-brief/SKILL.md — search_files
- **Citation / observation :** Fichier trouvé par recherche read-only.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Évolution temporelle ultérieure ; aucune violation historique automatique.

### CLM-AUD-003-014

- **Statement :** Les audits TaskNotes des sessions 8 et 9 rapportent une recherche initialement vide/inaccessible puis l’existence de 18 tâches canoniques et 20 tâches au total, avec un dénominateur interne incohérent : rubrique « Unscheduled Active (4) » suivie de six lignes.
- **État :** contradicted
- **Sujet littéral :** TaskNotes audit counts
- **Temps du fait :** 2026-07-12
- **Temps d’enregistrement :** 2026-07-12T11:37:09.543000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0a9e2a168ffeX9UcLu9cTvw7TM et ses_0a9e073abffe2QYXV0dejj2xwU — réponses finales
- **Citation / observation :** Le rapport passe de « no .md files » à « 20 task notes / 18 tasks », puis affiche « Unscheduled Active (4) » avec six entrées.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ne pas utiliser ces comptes comme état actuel sans relecture de la source.

### CLM-AUD-003-015

- **Statement :** La session 10 a rapporté un inventaire des Bases, des propriétés/statuses TaskNotes et plusieurs écarts V4, notamment les filtres dropped, les champs techniques et la définition d’orphan resources.
- **État :** historical_intent
- **Sujet littéral :** Bases config audit
- **Temps du fait :** 2026-06-26
- **Temps d’enregistrement :** 2026-06-26T12:46:43.668000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0fc0fbeb3ffeIGGk8fkT7ken0 — réponse finale
- **Citation / observation :** Base Inventory ; Canon Used ; Gaps Versus V4 Canon ; Target Files / Sections To Formalize.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les valeurs sensibles de la configuration n’ont pas été imprimées ; les écarts restent à contre-vérifier live.

### CLM-AUD-003-017

- **Statement :** Le manifeste parent indique 1 609 sessions dans la base canonique contre 1 601 dans l’index dérivé stale ; les huit sessions absentes de l’index peuvent manquer à la discovery.
- **État :** unknown
- **Sujet littéral :** OpenCode source/index health
- **Temps du fait :** 2026-06-10..2026-08-26
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-OPENCODE
- **Locator :** parent task t_91c7ddc5 — metadata source_health
- **Citation / observation :** source_sessions: 1609 ; index_sessions: 1601 ; index_status: stale.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Limite de discovery : huit sessions source absentes de l’index, pas preuve qu’elles sont pertinentes.

### CLM-AUD-003-300

- **Statement :** La session a audité les templates, commandes et workflows de mutation de Sofian OS en lecture seule.
- **État :** historical_execution
- **Sujet littéral :** Templates, commandes et workflows Sofian OS
- **Temps du fait :** 2026-06-26
- **Temps d’enregistrement :** 2026-06-26T12:48:38.863000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0fc0fbe8bffeaQqBAROa2rXTTr — 2026-06-26 — visible user/assistant exchange
- **Citation / observation :** Demande `READ-ONLY ONLY` puis rapport final d’audit des templates, commandes et workflows.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** audit historique, pas état actuel

### CLM-AUD-003-301

- **Statement :** La session a identifié neuf templates suivis, principalement pour projets et tâches Epitech.
- **État :** historical_execution
- **Sujet littéral :** Templates Sofian OS
- **Temps du fait :** 2026-06-26
- **Temps d’enregistrement :** 2026-06-26T12:48:38.863000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0fc0fbe8bffeaQqBAROa2rXTTr — 2026-06-26 — rapport final
- **Citation / observation :** Le rapport direct indique `Found 9 tracked templates`.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Rapport historique ; état actuel seulement lorsqu’une source actuelle séparée le confirme.

### CLM-AUD-003-302

- **Statement :** Le rapport historique déclare l’absence de template générique Task, Resource et Aspiration dans 98-Backend/Templates.
- **État :** historical_execution
- **Sujet littéral :** Templates Task / Resource / Aspiration
- **Temps du fait :** 2026-06-26
- **Temps d’enregistrement :** 2026-06-26T12:48:38.863000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0fc0fbe8bffeaQqBAROa2rXTTr — 2026-06-26 — rapport final
- **Citation / observation :** Le rapport direct indique l’absence de template générique Task, Resource et Aspiration.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** non revérifié dans le contenu live

### CLM-AUD-003-303

- **Statement :** Le rapport historique décrit TaskNotes comme propriétaire de la création et des champs de tâche, avec Note Toolbar comme surface de lancement Task.
- **État :** historical_intent
- **Sujet littéral :** TaskNotes / Note Toolbar
- **Temps du fait :** 2026-06-26
- **Temps d’enregistrement :** 2026-06-26T12:48:38.863000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0fc0fbe8bffeaQqBAROa2rXTTr — 2026-06-26 — rapport final
- **Citation / observation :** Le tableau final classe TaskNotes canonique pour les tâches et Note Toolbar actif pour Task/Project/Resource.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Rapport historique ; état actuel seulement lorsqu’une source actuelle séparée le confirme.

### CLM-AUD-003-304

- **Statement :** Le rapport historique décrit Resource comme créé par un script inline Note Toolbar et les Aspirations comme notes réelles à création apparemment manuelle.
- **État :** historical_execution
- **Sujet littéral :** Resource / Aspiration
- **Temps du fait :** 2026-06-26
- **Temps d’enregistrement :** 2026-06-26T12:48:38.863000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0fc0fbe8bffeaQqBAROa2rXTTr — 2026-06-26 — rapport final
- **Citation / observation :** Le tableau final décrit Resource via JavaScript Note Toolbar et Aspiration comme création manuelle.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Rapport historique ; état actuel seulement lorsqu’une source actuelle séparée le confirme.

### CLM-AUD-003-306

- **Statement :** La session a audité les plugins Obsidian, les configurations d’agents et les surfaces d’outillage en lecture seule.
- **État :** historical_execution
- **Sujet littéral :** Plugins et outillage Sofian-OS
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-06-21T17:16:37.567000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_114d2d382ffeOpFlTZ6CD1bTeL — 2026-06-21 — user request et rapport final
- **Citation / observation :** Demande et rapport direct d’audit read-only des plugins, configurations agents et outillage.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Audit historique ; aucune activation live ni valeur sensible n’est déduite.

### CLM-AUD-003-307

- **Statement :** Le rapport historique liste TaskNotes, QuickAdd, Templater, Base Board, Homepage, Omnisearch, Note Toolbar et plusieurs plugins d’interface comme présents dans le vault.
- **État :** historical_execution
- **Sujet littéral :** Plugins Obsidian
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-06-21T17:16:37.567000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_114d2d382ffeOpFlTZ6CD1bTeL — 2026-06-21 — section Installed / active Obsidian plugins
- **Citation / observation :** Le rapport direct liste TaskNotes, QuickAdd, Templater, Base Board, Homepage, Omnisearch et Note Toolbar.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** présence historique, pas activation live affirmée

### CLM-AUD-003-308

- **Statement :** Le rapport historique signale des champs potentiellement sensibles dans la configuration TaskNotes et un auto-backup/auto-commit Obsidian Git; aucune valeur secrète n’est reprise ici.
- **État :** historical_execution
- **Sujet littéral :** Configuration TaskNotes / Obsidian Git
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-06-21T17:16:37.567000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_114d2d382ffeOpFlTZ6CD1bTeL — 2026-06-21 — section Sensitive / risky config
- **Citation / observation :** Le rapport direct signale des champs sensibles TaskNotes et l’auto-backup/auto-commit, sans reproduire de valeur.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Audit historique ; aucune activation live ni valeur sensible n’est déduite.

### CLM-AUD-003-309

- **Statement :** Le rapport historique considère l’absence de runtime .opencode dans le vault comme intentionnelle et les références d’agents comme externes au vault.
- **État :** historical_intent
- **Sujet littéral :** Runtime agentique externe au vault
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-06-21T17:16:37.567000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_114d2d382ffeOpFlTZ6CD1bTeL — 2026-06-21 — section Agent / skill organization
- **Citation / observation :** Le rapport direct dit que le runtime agentique est externe au vault et que l’absence de `.opencode` suivie est intentionnelle.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Audit historique ; aucune activation live ni valeur sensible n’est déduite.

### CLM-AUD-003-310

- **Statement :** La session a conclu historiquement à une architecture V4 largement implémentée mais encore à stabiliser.
- **État :** hypothesis
- **Sujet littéral :** Architecture V4 Sofian OS
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-06-21T17:16:40.798000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_114d2d3daffei3JTKIRptzIKgr — 2026-06-21 — Verdict
- **Citation / observation :** Verdict direct : V4 `mostly implemented / ready to stabilize`.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Rapport historique supersédable par le canon actuel ; aucune preuve d’usage réel.

### CLM-AUD-003-311

- **Statement :** Le rapport historique indique que cinq Bases avancées étaient encore manquantes: By Context, High Priority, Projects Without Next Action, Orphan Resources et Aspirations.
- **État :** historical_execution
- **Sujet littéral :** Bases avancées Sofian OS
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-06-21T17:16:40.798000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_114d2d3daffei3JTKIRptzIKgr — 2026-06-21 — Gaps
- **Citation / observation :** Le rapport direct énumère cinq Bases alors manquantes.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** non revérifié dans le contenu live

### CLM-AUD-003-312

- **Statement :** Le rapport historique indique que le mapping Aspiration↔Obsidian restait une décision ouverte.
- **État :** unknown
- **Sujet littéral :** Mapping Aspiration
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-06-21T17:16:40.798000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_114d2d3daffei3JTKIRptzIKgr — 2026-06-21 — Gaps / Journal de décisions
- **Citation / observation :** Le rapport direct cite `Mapping exact de Aspiration dans Obsidian` comme décision ouverte.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Décision ouverte au 2026-06-21 ; le mapping actif actuel la supersède pour le canon courant.

### CLM-AUD-003-313

- **Statement :** Le rapport historique indique que les routines Inbox Processing, Daily, Weekly et Engage n’étaient pas encore exercées ou finalisées.
- **État :** historical_execution
- **Sujet littéral :** Operating Layer
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-06-21T17:16:40.798000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_114d2d3daffei3JTKIRptzIKgr — 2026-06-21 — Operating Layer gaps
- **Citation / observation :** Le rapport direct dit que Daily/Inbox/Weekly/Engage restaient à finaliser ou tester.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Rapport historique supersédable par le canon actuel ; aucune preuve d’usage réel.

### CLM-AUD-003-314

- **Statement :** Le rapport historique signale un décalage entre la checklist Home / Command Center et l’absence d’un fichier Home dédié.
- **État :** historical_execution
- **Sujet littéral :** Home / Command Center
- **Temps du fait :** 2026-06-21
- **Temps d’enregistrement :** 2026-06-21T17:16:40.798000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_114d2d3daffei3JTKIRptzIKgr — 2026-06-21 — Minor surface mismatch
- **Citation / observation :** Le rapport direct signale l’absence historique d’un Home dédié sous `01-Dashboards`.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Écart historique ; la source actuelle possède un Home racine et ne permet pas de conclure à un manque courant.

### CLM-AUD-003-327

- **Statement :** Sofian décide de ne pas créer de nouveau repo SAS: SAS Posture Pro est lié à l’association Z-code et Tokn Project/Epitalk sont déjà poussés.
- **État :** user_decision
- **Sujet littéral :** SAS Posture Pro / Z-code / Tokn Project / Epitalk
- **Temps du fait :** 2026-06-16
- **Temps d’enregistrement :** 2026-06-16T20:04:43.971000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_12e033645ffeUqYCM55fctrfC1 — 2026-06-16 — user correction
- **Citation / observation :** Correction utilisateur : SAS Posture Pro appartient à Z-code et Tokn Project/Epitalk étaient déjà poussés ; pas de nouveau repo SAS.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Décision historique limitée au lot discuté ; aucune autorisation actuelle de mutation.

### CLM-AUD-003-328

- **Statement :** Sofian décide de ne pas déplacer les bootcamps pour l’instant, de ne pas toucher aux forks et de ne pas pousser Design, Gemini, Icons, Misc ou Scripts.
- **État :** user_decision
- **Sujet littéral :** Bootcamps / forks / experiments
- **Temps du fait :** 2026-06-16
- **Temps d’enregistrement :** 2026-06-16T20:04:43.971000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_12e033645ffeUqYCM55fctrfC1 — 2026-06-16 — user correction
- **Citation / observation :** Correction utilisateur : ne pas déplacer les bootcamps, ne pas toucher aux forks et ne pas pousser les expériences citées.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Décision historique limitée au lot discuté ; aucune autorisation actuelle de mutation.

### CLM-AUD-003-329

- **Statement :** Sofian décide de conserver les éléments de Dead-Personal et Dead-Forks, avec review plutôt que suppression pour Soundcloud_Wav_Playlist, AI-THREEJS-Seahorse-Animation, SidecarPatcher et AppStore_PriceScraper.
- **État :** user_decision
- **Sujet littéral :** Dead-Personal / Dead-Forks
- **Temps du fait :** 2026-06-16
- **Temps d’enregistrement :** 2026-06-16T20:04:43.971000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_12e033645ffeUqYCM55fctrfC1 — 2026-06-16 — user correction
- **Citation / observation :** Correction utilisateur : conserver les archives et revoir les projets nommés plutôt que les supprimer.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Décision historique limitée au lot discuté ; aucune autorisation actuelle de mutation.

### CLM-AUD-003-330

- **Statement :** Sofian valide la suppression des fichiers .bak du vault, mais demande de ne pas supprimer les archives sans revue.
- **État :** user_decision
- **Sujet littéral :** Fichiers .bak / archives
- **Temps du fait :** 2026-06-16
- **Temps d’enregistrement :** 2026-06-16T20:04:43.971000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_12e033645ffeUqYCM55fctrfC1 — 2026-06-16 — user correction
- **Citation / observation :** Correction utilisateur : suppression des `.bak` acceptée, archives à ne pas supprimer sans revue.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Consentement historique au lot d’alors, pas autorisation réutilisable.

### CLM-AUD-003-331

- **Statement :** Sofian demande de cloner formrelay localement puis d’archiver le repo GitHub, et d’archiver AionUi-CopilotCLI-support et allure3-demo.
- **État :** user_decision
- **Sujet littéral :** formrelay / AionUi-CopilotCLI-support / allure3-demo
- **Temps du fait :** 2026-06-16
- **Temps d’enregistrement :** 2026-06-16T20:04:43.971000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_12e033645ffeUqYCM55fctrfC1 — 2026-06-16 — user correction
- **Citation / observation :** Correction utilisateur : cloner formrelay puis archiver le repo, et archiver les deux forks nommés.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Décision historique limitée au lot discuté ; aucune autorisation actuelle de mutation.

### CLM-AUD-003-332

- **Statement :** Sofian décide d’utiliser le préfixe ept- pour les repos Epitech.
- **État :** user_decision
- **Sujet littéral :** Préfixe ept-
- **Temps du fait :** 2026-06-16
- **Temps d’enregistrement :** 2026-06-16T20:13:27.621000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_12e033645ffeUqYCM55fctrfC1 — 2026-06-16 — user correction
- **Citation / observation :** Correction utilisateur : préférence littérale `ept-corelab`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Correction historique ; préserver les noms littéralement et ne pas inférer l’état courant.

### CLM-AUD-003-333

- **Statement :** Sofian corrige les statuts historiques: Corelab est fini et Codename est en cours.
- **État :** user_decision
- **Sujet littéral :** Corelab / Codename
- **Temps du fait :** 2026-06-16
- **Temps d’enregistrement :** 2026-06-16T20:13:27.621000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_12e033645ffeUqYCM55fctrfC1 — 2026-06-16 — user correction
- **Citation / observation :** Correction utilisateur : `Corelab c’est fini. Code name c’est en cours.`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le journal courant du projet Sofian OS indique ensuite `Codename done` au 2026-06-25 ; garder la correction du 16 juin comme état historique seulement.

### CLM-AUD-003-334

- **Statement :** Sofian remplace le nom Perplexity-Headless par PPLX - Web Query et le nom de skill par pplx-web-query.
- **État :** user_decision
- **Sujet littéral :** PPLX - Web Query / pplx-web-query
- **Temps du fait :** 2026-06-16
- **Temps d’enregistrement :** 2026-06-16T20:13:27.621000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_12e033645ffeUqYCM55fctrfC1 — 2026-06-16 — user correction
- **Citation / observation :** Correction utilisateur : titre `PPLX - Web Query`, skill `pplx-web-query`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Correction historique ; préserver les noms littéralement et ne pas inférer l’état courant.

### CLM-AUD-003-337

- **Statement :** La recherche ADHD historique conclut que les patterns proposés sont capture-first, next-action unique, progressive disclosure, limite de trois options, prise en compte énergie/temps et transparence des actions.
- **État :** hypothesis
- **Sujet littéral :** Patterns ADHD
- **Temps du fait :** 2026-06-27
- **Temps d’enregistrement :** 2026-06-27T20:07:05.236000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0f552b400ffev34OqV3nSO9zfi — 2026-06-27 — research synthesis
- **Citation / observation :** Synthèse historique : capture-first, action suivante unique, divulgation progressive et options bornées.
- **Confiance :** low
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Sources Perplexity non contre-vérifiées ; niveau `hypothesis`.

### CLM-AUD-003-338

- **Statement :** La recherche ADHD historique recommande de ne pas créer un second task manager et de conserver Sofian OS/TaskNotes comme fondation.
- **État :** proposed
- **Sujet littéral :** Sofian OS / TaskNotes
- **Temps du fait :** 2026-06-27
- **Temps d’enregistrement :** 2026-06-27T20:07:05.236000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0f552b400ffev34OqV3nSO9zfi — 2026-06-27 — Specific Recommendations
- **Citation / observation :** Recommandation directe : ne pas créer de second task manager ; conserver Sofian OS/TaskNotes comme fondation.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** recommandation historique, non décision utilisateur

### CLM-AUD-003-339

- **Statement :** La recherche OpenCode historique rapporte des plugins npm pour notifications, webhooks, mémoire et rappels, ainsi qu’une configuration MCP locale ou distante dans opencode.json.
- **État :** hypothesis
- **Sujet littéral :** Écosystème OpenCode
- **Temps du fait :** 2026-06-29
- **Temps d’enregistrement :** 2026-06-29T14:19:30.837000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0ec40559affedox5XTPSi6Ca8N — 2026-06-29 — sections 1–2
- **Citation / observation :** Synthèse web directe sur plugins npm et MCP OpenCode, conservée comme hypothèse.
- **Confiance :** low
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Sources externes non revérifiées ; niveau `hypothesis`.

### CLM-AUD-003-340

- **Statement :** La recherche OpenCode historique rapporte Build et Plan comme agents primaires et des sous-agents en sessions enfant isolées, sans établir de limite dure fiable.
- **État :** hypothesis
- **Sujet littéral :** Agents OpenCode
- **Temps du fait :** 2026-06-29
- **Temps d’enregistrement :** 2026-06-29T14:19:30.837000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0ec40559affedox5XTPSi6Ca8N — 2026-06-29 — section 3
- **Citation / observation :** Synthèse web directe sur agents primaires et sessions enfant ; aucune limite dure fiable établie.
- **Confiance :** low
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Sources externes non revérifiées ; niveau `hypothesis`.

### CLM-AUD-003-341

- **Statement :** La recherche OpenCode historique rapporte que opencode serve expose une API REST mais que des hangs de délégation ont été signalés; elle recommande de traiter les hooks comme rapides à évoluer.
- **État :** hypothesis
- **Sujet littéral :** OpenCode serve / délégation
- **Temps du fait :** 2026-06-29
- **Temps d’enregistrement :** 2026-06-29T14:19:30.837000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0ec40559affedox5XTPSi6Ca8N — 2026-06-29 — sections 5 et 7
- **Citation / observation :** Synthèse web directe sur `opencode serve` et un signalement de hang, conservée comme hypothèse.
- **Confiance :** low
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Sources externes non revérifiées ; niveau `hypothesis`.

### CLM-AUD-003-600

- **Statement :** La session a audité en lecture seule les outils et développements existants liés à ourmem/omem, à la mémoire OpenCode, au contexte injecté et à la capture/observabilité.
- **État :** historical_execution
- **Sujet littéral :** Audit outils mémoire locaux
- **Temps du fait :** 2026-07-22
- **Temps d’enregistrement :** 2026-07-22T15:28:22.055000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_07591aad6ffeVMGBQmfWtfLuI3 — message utilisateur initial et séquence visible
- **Citation / observation :** « Audit lecture seule, sans modifier aucun fichier et sans exposer de secret » ; rapport d’audit visible en fin de session.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le rapport historique ne prouve pas l’état live de tous les composants.

### CLM-AUD-003-601

- **Statement :** Le rapport historique décrit @ourmem/opencode en version 0.3.2 comme installé, avec des sources de plugin présentes dans ~/.config/opencode/node_modules/@ourmem/opencode/src/.
- **État :** historical_execution
- **Sujet littéral :** @ourmem/opencode
- **Temps du fait :** 2026-07-22
- **Temps d’enregistrement :** 2026-07-22T15:28:22.055000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_07591aad6ffeVMGBQmfWtfLuI3 — section « Plugin npm @ourmem/opencode v0.3.2 »
- **Citation / observation :** Le rapport liste le package version 0.3.2 et les fichiers index.ts, hooks.ts, tools.ts, client.ts, tags.ts, keywords.ts et privacy.ts.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le package courant a été relu séparément, mais l’activation effective du plugin reste une question distincte.

### CLM-AUD-003-602

- **Statement :** Le rapport historique affirme que la configuration OpenCode active ne mentionnait pas @ourmem/opencode et ne contenait pas de plugin_config ourmem.
- **État :** historical_execution
- **Sujet littéral :** Configuration OpenCode / ourmem
- **Temps du fait :** 2026-07-22
- **Temps d’enregistrement :** 2026-07-22T15:28:22.055000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_07591aad6ffeVMGBQmfWtfLuI3 — section « plugin npm non activé »
- **Citation / observation :** Le rapport oppose le package installé à opencode.jsonc actif « sans @ourmem/opencode » et signale l’absence de plugin_config.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La recherche live ciblée a renvoyé zéro correspondance mais cette absence n’est pas promue comme preuve exhaustive.

### CLM-AUD-003-603

- **Statement :** Le rapport décrit trois hooks ourmem historiques : auto-recall sur la transformation système initiale, détection de mots-clés à chaque message et réinjection lors de la compaction, avec un hook shell.env.
- **État :** historical_intent
- **Sujet littéral :** Hooks ourmem/OpenCode
- **Temps du fait :** 2026-07-22
- **Temps d’enregistrement :** 2026-07-22T15:28:22.055000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_07591aad6ffeVMGBQmfWtfLuI3 — section « Hooks exacts et flux de données »
- **Citation / observation :** Le rapport décrit autoRecallHook, keywordDetectionHook, compactingHook et shell.env, leurs déclencheurs et leurs sorties.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Description historique du rapport ; le comportement live n’a pas été exercé.

### CLM-AUD-003-604

- **Statement :** La session a relevé un état contradictoire du serveur omem : documentation de service planifiée, audit ancien indiquant un conteneur sain et autres traces indiquant une pause ou un échec d’embedding.
- **État :** contradicted
- **Sujet littéral :** Serveur omem
- **Temps du fait :** 2026-07-22
- **Temps d’enregistrement :** 2026-07-22T15:28:22.055000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_07591aad6ffeVMGBQmfWtfLuI3 — section « Serveur omem dans Homelab-OS »
- **Citation / observation :** Le rapport juxtapose « Up 4h (healthy) », « Paused — Vela unreliable », une tâche terminée avec conteneur down et un embedding en échec.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Contradiction historique ; aucun état runtime n’a été interrogé dans cette collecte.

### CLM-AUD-003-605

- **Statement :** Le rapport historique signale l’absence du patch isSystemNoise et l’absence du plugin local ourmem-local.ts dans l’installation alors qu’ils étaient documentés dans des ressources.
- **État :** historical_execution
- **Sujet littéral :** Patch isSystemNoise et ourmem-local.ts
- **Temps du fait :** 2026-07-22
- **Temps d’enregistrement :** 2026-07-22T15:28:22.055000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_07591aad6ffeVMGBQmfWtfLuI3 — sections « Patch isSystemNoise » et « Plugin ourmem-local.ts »
- **Citation / observation :** Le rapport indique que ~/.config/opencode/patches/ et le fichier ourmem-local.ts n’étaient pas trouvés.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Absence historique rapportée ; la présence actuelle des ressources Sofian-OS n’a pas pu être relue par le lecteur live.

### CLM-AUD-003-606

- **Statement :** Les options A à E proposées dans la session vont de zéro changement à l’activation du plugin, au serveur local, au patch puis à la recherche vectorielle.
- **État :** proposed
- **Sujet littéral :** Options ourmem/OpenCode
- **Temps du fait :** 2026-07-22
- **Temps d’enregistrement :** 2026-07-22T15:28:22.055000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_07591aad6ffeVMGBQmfWtfLuI3 — section « Options less-is-more »
- **Citation / observation :** Le rapport présente les options A — zéro changement, B — plugin, C — serveur local, D — patch, E — vectoriel.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune de ces options n’est une décision utilisateur actuelle.

### CLM-AUD-003-607

- **Statement :** Le rapport historique affirme qu’une collection Bruno Omem de 56 endpoints était présente.
- **État :** historical_execution
- **Sujet littéral :** Collection Bruno Omem
- **Temps du fait :** 2026-07-22
- **Temps d’enregistrement :** 2026-07-22T15:28:22.055000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_07591aad6ffeVMGBQmfWtfLuI3 — section « Bruno Collection Omem »
- **Citation / observation :** Le rapport mentionne ~/Developer/60-Devtools/Bruno/Omem/ et 56 endpoints testables.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Présence historique non revérifiée dans le live.

### CLM-AUD-003-608

- **Statement :** La session a constaté un écart entre une structure Developer numérotée et des documents Homelab décrivant encore des dossiers sémantiques anciens.
- **État :** historical_execution
- **Sujet littéral :** Architecture Developer/Data/Documents
- **Temps du fait :** 2026-06-25
- **Temps d’enregistrement :** 2026-06-25T19:05:15.795000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0ffd87857ffeSBR1Kg5knXMzRY — observations intermédiaires et conclusion visible
- **Citation / observation :** « Developer uses numbered folders, while Homelab docs still describe lowercase semantic folders » ; une documentation v2 est décrite comme plus récente.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le rapport ne donne pas une preuve live actuelle de toute l’arborescence.

### CLM-AUD-003-609

- **Statement :** Le rapport historique a décrit Homelab-OS comme le dépôt de contrôle et la couche canonique de reconstruction des machines/services, tandis que Sofian-OS portait davantage la conception et la planification.
- **État :** historical_intent
- **Sujet littéral :** Frontière Sofian-OS / Homelab-OS
- **Temps du fait :** 2026-06-25
- **Temps d’enregistrement :** 2026-06-25T19:05:15.795000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0ffd87857ffeSBR1Kg5knXMzRY — conclusion visible
- **Citation / observation :** Le rapport présente README/AGENTS, Unified Home Architecture, Deployment Guide, Folder Structure et Compose comme couche canonique, avec Sofian-OS comme espace de planification.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** C’est une lecture historique et non une décision acceptée de frontière.

### CLM-AUD-003-610

- **Statement :** La session a signalé des contradictions historiques de service et de réseau, notamment les noms DNS AdGuard, le binding Dockhand et la portée d’exposition Caddy.
- **État :** contradicted
- **Sujet littéral :** Services Homelab-OS
- **Temps du fait :** 2026-06-25
- **Temps d’enregistrement :** 2026-06-25T19:04:51.982000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0ffd87931ffe6OXaBV60qgqfrp — observations intermédiaires visibles
- **Citation / observation :** Le rapport signale notamment adguard.void.lab versus dns.void.lab et 127.0.0.1 versus 100.115.31.73 pour Dockhand.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les extraits sont historiques et n’ont pas été contre-vérifiés par cette collecte.

### CLM-AUD-003-611

- **Statement :** La session a déclaré ne pas avoir trouvé de politique concrète iCloud Drive ou Google Drive dans les recherches ciblées de migration.
- **État :** unknown
- **Sujet littéral :** Migration iCloud Drive / Google Drive
- **Temps du fait :** 2026-06-25
- **Temps d’enregistrement :** 2026-06-25T19:05:15.795000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0ffd87857ffeSBR1Kg5knXMzRY — observations visibles sur les recherches ciblées
- **Citation / observation :** « No exact iCloud Drive, Google Drive, or cloud migration documentation was found » dans le périmètre recherché.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Une recherche négative bornée ne prouve pas l’absence dans tout le corpus.

### CLM-AUD-003-612

- **Statement :** La session candidate 23 a une demande utilisateur et une séquence d’analyse visibles, mais aucune réponse assistant finale distincte n’est disponible dans la sortie show.
- **État :** unknown
- **Sujet littéral :** Audit Homelab OS
- **Temps du fait :** 2026-06-25
- **Temps d’enregistrement :** 2026-06-25T19:04:51.982000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0ffd87931ffe6OXaBV60qgqfrp — fin de sortie show
- **Citation / observation :** La sortie se termine après une réflexion sur l’état des commandes et n’expose pas de rapport final séparé.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les payloads outils sont exclus par le mode show par défaut ; un résultat caché ne doit pas être inféré.

### CLM-AUD-003-613

- **Statement :** La session candidate 24 ne contient dans la sortie visible que la demande utilisateur initiale ; aucune décision, réalisation, test, échec ou boucle ouverte assistant n’est disponible.
- **État :** unknown
- **Sujet littéral :** Research Homelab-OS vault
- **Temps du fait :** 2026-06-25
- **Temps d’enregistrement :** 2026-06-25T17:58:54.472000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_10010af22ffeLxzU9H8C9OYha8 — fin de sortie show
- **Citation / observation :** La sortie show contient le message utilisateur de recherche read-only et aucun message assistant visible.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les tool payloads et tout contenu non visible ne sont pas utilisés comme preuve.

### CLM-AUD-003-614

- **Statement :** Le rapport de lint a identifié Hawser avec port_host 2376 comme allocation non présente dans le registre et hors de la convention applicative 9000+.
- **État :** historical_execution
- **Sujet littéral :** Hawser / registre de ports
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T15:20:50.573000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_143963db6ffewdKquPkrM4LX3P — section « Port conflicts »
- **Citation / observation :** Le rapport final classe 2376 comme absent de 61 Port Registry.md et hors de la plage 9000+.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Finding historique, non requalifié comme état actuel.

### CLM-AUD-003-615

- **Statement :** Le rapport de lint a signalé un port 9090 encore alloué historiquement à OpenCode Daemon et un port 9091 d’OpenChamber absent du registre, alors que les services étaient rapportés retiré/supprimé.
- **État :** contradicted
- **Sujet littéral :** Port Registry / OpenCode / OpenChamber
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T15:20:50.573000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_143963db6ffewdKquPkrM4LX3P — sections « Port conflicts » et « Updated statuses »
- **Citation / observation :** Le rapport oppose l’allocation 9090 au statut retired et décrit 9091 comme absent pour un service removed.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les statuts et allocations décrits sont datés du 2026-06-12.

### CLM-AUD-003-616

- **Statement :** Le rapport de lint conclut qu’aucun conflit de port effectif entre deux services n’a été détecté dans son scan.
- **État :** historical_execution
- **Sujet littéral :** Conflits de ports Homelab-OS
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T15:20:50.573000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_143963db6ffewdKquPkrM4LX3P — résumé final
- **Citation / observation :** « No actual port conflicts (two services fighting for the same port) were detected. »
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Résultat borné au scan et aux fichiers de cette session.

### CLM-AUD-003-617

- **Statement :** Le rapport de lint a listé comme orphelines plusieurs pages de contenu et le plan AI Structure Inventory, tout en distinguant les templates volontairement orphelins.
- **État :** historical_execution
- **Sujet littéral :** Orphelins du wiki Homelab-OS
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T15:20:50.573000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_143963db6ffewdKquPkrM4LX3P — section « Orphan pages »
- **Citation / observation :** Le rapport final distingue Clippings, AI Structure Inventory et les quatre templates.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le décompte historique contient des hésitations intermédiaires ; seule la liste finale est retenue comme observation.

### CLM-AUD-003-618

- **Statement :** Le rapport de lint a identifié comme liens cassés historiques SECRETS.md, _tucas et .ai/README dans le périmètre du vault analysé.
- **État :** historical_execution
- **Sujet littéral :** Liens wiki Homelab-OS
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T15:20:50.573000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_143963db6ffewdKquPkrM4LX3P — section « Broken links »
- **Citation / observation :** Le tableau final cite [[SECRETS.md]], [[_tucas]] et [[.ai/README]].
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ne prouve pas que ces liens sont encore cassés aujourd’hui.

### CLM-AUD-003-619

- **Statement :** Le rapport de lint n’a trouvé aucun service planned avec port frontmatter dans son périmètre et a distingué Tailscale, sans Compose, comme service systemd plutôt qu’anomalie Docker.
- **État :** historical_execution
- **Sujet littéral :** Statuts et Compose Homelab-OS
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T15:20:50.573000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_143963db6ffewdKquPkrM4LX3P — sections « State contradictions »
- **Citation / observation :** Le rapport indique « No violations found » pour planned + ports et traite Tailscale comme service systemd valide sans Compose.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le rapport signale aussi une anomalie Daemon Management ; les deux points ne doivent pas être fusionnés.

### CLM-AUD-003-620

- **Statement :** Le rapport de lint a proposé de réexaminer le statut de Daemon Management et les allocations du Port Registry après des migrations ou retraits historiques.
- **État :** proposed
- **Sujet littéral :** Nettoyage statuts Homelab-OS
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T15:20:50.573000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_143963db6ffewdKquPkrM4LX3P — section « Updated statuses »
- **Citation / observation :** Le rapport propose de traiter 27.04 Daemon Management et 61 Port Registry comme points de mise à jour.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Il s’agit d’une recommandation historique, pas d’une autorisation de mutation ni d’une décision actuelle.

### CLM-AUD-003-621

- **Statement :** La session a décrit un dépôt Homelab-OS comprenant des stacks OpenCode et OpenChamber sur Nova, Hawser sur Nova/Vela et des services réseau sur Void.
- **État :** historical_execution
- **Sujet littéral :** Architecture runtime Homelab-OS
- **Temps du fait :** 2026-06-10
- **Temps d’enregistrement :** 2026-06-10T13:58:07.265000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_14e2df203ffekuUz1bqls0KMu7 — rapport final, sections Docker stacks et résumé
- **Citation / observation :** Le rapport liste nova/opencode, nova/openchamber, nova/hawser, vela/hawser, void/adguard, void/caddy et void/dockhand.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Inventaire daté ; ne prouve pas que chaque stack est encore déployée.

### CLM-AUD-003-622

- **Statement :** La session a décrit les agents, skills, commands et rules OpenCode comme une configuration tool-agnostic déployée via dotfiles et reliée par symlinks.
- **État :** historical_intent
- **Sujet littéral :** Architecture dotfiles / agents
- **Temps du fait :** 2026-06-10
- **Temps d’enregistrement :** 2026-06-10T13:58:07.265000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_14e2df203ffekuUz1bqls0KMu7 — rapport final, section dotfiles
- **Citation / observation :** Le rapport décrit dot_ai-agents et les fichiers symlink_agents, symlink_skills, symlink_commands et symlink_rules.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Architecture historique du dépôt ; l’activation live n’est pas établie par ce seul rapport.

### CLM-AUD-003-623

- **Statement :** La session a décrit .ai comme espace de mémoire projet et de sorties, avec un plan dédié à l’unification OpenChamber/OpenCode et à la migration des données runtime.
- **État :** historical_execution
- **Sujet littéral :** .ai et plan OpenChamber
- **Temps du fait :** 2026-06-10
- **Temps d’enregistrement :** 2026-06-10T13:58:07.265000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_14e2df203ffekuUz1bqls0KMu7 — sections .ai et plan-openchamber-unification.md
- **Citation / observation :** Le rapport liste .ai/memory, outputs, sessions et un plan de migration vers ~/Data/appdata/opencode/ avec risques identifiés.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le plan historique n’est pas une preuve d’exécution complète.

### CLM-AUD-003-624

- **Statement :** La session a rapporté que le fichier opencode.jsonc de dotfiles contenait snapshot false, un MCP Lucid distant et aucun plugin OpenCode actif dans l’état observé.
- **État :** historical_execution
- **Sujet littéral :** Configuration OpenCode dans Homelab-OS
- **Temps du fait :** 2026-06-10
- **Temps d’enregistrement :** 2026-06-10T13:58:07.265000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_14e2df203ffekuUz1bqls0KMu7 — section configuration JSONC
- **Citation / observation :** Le rapport cite snapshot false, plugin [] et une entrée mcp lucid.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Configuration datée ; elle peut avoir évolué ensuite.

### CLM-AUD-003-625

- **Statement :** La session a conclu qu’aucun stack Docker Claude n’avait été trouvé dans le dépôt Homelab-OS inspecté.
- **État :** historical_execution
- **Sujet littéral :** Stacks Claude dans Homelab-OS
- **Temps du fait :** 2026-06-10
- **Temps d’enregistrement :** 2026-06-10T13:58:07.265000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_14e2df203ffekuUz1bqls0KMu7 — rapport final, section Docker stacks
- **Citation / observation :** Le rapport indique « No claude-related docker stacks exist anywhere in the repo ».
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Recherche bornée au dépôt et à la date de la session.

### CLM-AUD-003-626

- **Statement :** La session a historiquement créé deux fichiers de référence pour la skill obsidian-vault : vault_structure.md et markdown_formatting.md.
- **État :** historical_execution
- **Sujet littéral :** Références skill obsidian-vault
- **Temps du fait :** 2026-06-19
- **Temps d’enregistrement :** 2026-06-19T13:58:10.763000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_11fd39c4dffeXwAmAalGMN8cWa — réponse finale visible
- **Citation / observation :** La réponse finale confirme l’écriture des deux fichiers sous ~/.config/opencode/skills/obsidian/obsidian-vault/references/.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La création historique ne prouve ni validation utilisateur ni usage opérationnel.

### CLM-AUD-003-627

- **Statement :** Les références créées historiquement décrivent une hiérarchie Sofian-OS V4, les types de notes, les propriétés lower_snake_case, les statuts TaskNotes et des dashboards composés de vues.
- **État :** historical_intent
- **Sujet littéral :** Conventions Sofian-OS V4
- **Temps du fait :** 2026-06-19
- **Temps d’enregistrement :** 2026-06-19T13:58:10.763000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_11fd39c4dffeXwAmAalGMN8cWa — contenu demandé et réponse finale
- **Citation / observation :** Le contenu visible spécifie 00-Inbox, 01-Dashboards, 98-Backend, 99-System, types canoniques et dashboards query-only.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les documents sont des conventions historiques, pas une preuve que toutes les règles sont intégrées ou utilisées.

### CLM-AUD-003-628

- **Statement :** La session de revue des tâches a constaté que l’obsidian CLI n’était pas disponible et a poursuivi par analyse directe de fichiers.
- **État :** historical_execution
- **Sujet littéral :** Revue tâches/projets Sofian-OS
- **Temps du fait :** 2026-07-14
- **Temps d’enregistrement :** 2026-07-14T10:06:55.847000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_09feadf9cffevUfmn4ifM8soev — message assistant visible
- **Citation / observation :** « The obsidian CLI is not installed or not in the PATH » puis analyse file-based.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** État de l’outil au 2026-07-14 seulement.

### CLM-AUD-003-629

- **Statement :** Le rapport de revue a présenté quatre candidats Engage non bloqués, dont une vérification de facture, un nettoyage de newsletters, un nettoyage de comptes et un audit de secrets.
- **État :** historical_execution
- **Sujet littéral :** Candidats Engage
- **Temps du fait :** 2026-07-14
- **Temps d’enregistrement :** 2026-07-14T10:06:55.847000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_09feadf9cffevUfmn4ifM8soev — section « Engage Candidates »
- **Citation / observation :** Le tableau final présente quatre tâches comme candidates, avec contexte computer et statuts todo.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le rapport ne constitue pas un plan actuel ni une sélection acceptée par Sofian.

### CLM-AUD-003-630

- **Statement :** Le rapport de revue a décrit Sofian OS comme projet sans prochaine action explicite et a proposé une validation des routines Daily/Engage/Weekly Review sur sept jours.
- **État :** proposed
- **Sujet littéral :** Projet Sofian OS et cockpit
- **Temps du fait :** 2026-07-14
- **Temps d’enregistrement :** 2026-07-14T10:06:55.847000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_09feadf9cffevUfmn4ifM8soev — sections « Projects Without Next Action » et recommandations
- **Citation / observation :** Le rapport qualifie la prochaine action de Sofian OS de partielle et propose « Validate cockpit routines over 7 days ».
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Proposition historique ; aucune TaskNote n’a été créée ou modifiée dans cette collecte.

### CLM-AUD-003-631

- **Statement :** Le rapport de revue a identifié deux tâches non planifiées et a recommandé de les traiter lors d’une Weekly Review plutôt que de les considérer urgentes.
- **État :** historical_execution
- **Sujet littéral :** Tâches non planifiées
- **Temps du fait :** 2026-07-14
- **Temps d’enregistrement :** 2026-07-14T10:06:55.847000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_09feadf9cffevUfmn4ifM8soev — section « Overdue/Unscheduled Tasks »
- **Citation / observation :** Le rapport final indique deux tâches avec due date et scheduled date absentes.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Données historiques de tâches ; aucune vérification live actuelle.

### CLM-AUD-003-632

- **Statement :** Le rapport de revue a listé comme blocages historiques un problème de secrets, un embedding Omem, une clé Mistral manquante et une validation humaine du cockpit.
- **État :** historical_execution
- **Sujet littéral :** Blocages Jarvis / Sofian-OS
- **Temps du fait :** 2026-07-14
- **Temps d’enregistrement :** 2026-07-14T10:06:55.847000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_09feadf9cffevUfmn4ifM8soev — section « Blockers »
- **Citation / observation :** Le tableau final distingue Secrets Cleanup, Jarvis/Omem, Jarvis/Mistral et Sofian OS Cockpit.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune valeur secrète n’est reprise ; les blocages sont datés et non confirmés live.

### CLM-AUD-003-633

- **Statement :** Le rapport de revue du vault a décrit une structure 00-Inbox/01-Dashboards/98-Backend/99-System, 158 pages de contenu et 81 fichiers .bak à la date de l’audit.
- **État :** historical_execution
- **Sujet littéral :** Structure du vault Sofian-OS
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T19:12:04.438000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_142c2b87dffeNfbclcJcRxNTwG — sections structure et page counts
- **Citation / observation :** Le rapport final donne la structure 00/01/98/99, 158 pages et environ 81 doublons .bak.
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Décompte historique et non vérifié dans le vault live actuel.

### CLM-AUD-003-634

- **Statement :** Le rapport de revue du vault a conclu à l’absence de liens wiki directs entre les vaults Sofian-OS et Homelab-OS dans le périmètre audité.
- **État :** historical_execution
- **Sujet littéral :** Liens inter-vaults
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T19:12:04.438000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_142c2b87dffeNfbclcJcRxNTwG — section « Wiki-Links »
- **Citation / observation :** Le rapport final indique « ZERO direct wiki-links » et « The two vaults are technically disconnected ».
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Absence historique bornée au scan et à la date de session.

### CLM-AUD-003-635

- **Statement :** Le rapport de revue a proposé une séparation de rôle où Sofian-OS conserve conception, décisions et projets, tandis que Homelab-OS conserve runbooks, machines, services, incidents et Compose.
- **État :** proposed
- **Sujet littéral :** Rôles Sofian-OS / Homelab-OS
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T19:12:04.438000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_142c2b87dffeNfbclcJcRxNTwG — sections « Relationship » et recommandations
- **Citation / observation :** Le rapport distingue « personal knowledge & project management » et « homelab infrastructure control plane ».
- **Confiance :** medium
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Recommandation historique non acceptée comme cible.

### CLM-AUD-003-636

- **Statement :** Le rapport de revue a signalé la présence historique de données sensibles en clair dans des notes Inbox et a recommandé une remédiation, sans reproduire les valeurs dans ce claim.
- **État :** historical_execution
- **Sujet littéral :** Confidentialité du vault Sofian-OS
- **Temps du fait :** 2026-06-12
- **Temps d’enregistrement :** 2026-06-12T19:12:04.438000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_142c2b87dffeNfbclcJcRxNTwG — sections « Critical Issues » et « Security »
- **Citation / observation :** Le rapport final signale des clés et identifiants en clair dans deux notes Inbox et recommande leur retrait/chiffrement.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune valeur, clé ou identifiant n’est conservé ; état actuel non revérifié.

### CLM-AUD-003-637

- **Statement :** La revue finale de jarvis_daily.py a identifié comme High l’exposition de message_id Mail et de segments d’URL potentiellement traçants dans le JSON public.
- **État :** historical_execution
- **Sujet littéral :** jarvis_daily.py — confidentialité Mail
- **Temps du fait :** 2026-07-20
- **Temps d’enregistrement :** 2026-07-20T05:08:07.601000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0821451bdffeib4pfdYFblX04K — findings High
- **Citation / observation :** Les findings High citent les lignes 989, 1209, 1225, 1248 et 1253 pour message_id, puis 696 et 712 pour URL/local-part.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Revue historique read-only ; aucun correctif ni test n’a été exécuté dans cette collecte.

### CLM-AUD-003-638

- **Statement :** La revue finale a identifié comme Medium des collections potentiellement non bornées et un risque de surcomptage d’activité quand des événements actifs sans timestamp coexistent avec des intervalles AFK.
- **État :** historical_execution
- **Sujet littéral :** jarvis_daily.py — bornes et AFK
- **Temps du fait :** 2026-07-20
- **Temps d’enregistrement :** 2026-07-20T05:08:07.601000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0821451bdffeib4pfdYFblX04K — findings Medium
- **Citation / observation :** Les findings Medium citent les lignes 205, 225, 528, 575, 987 et 179.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Finding statique historique ; il ne prouve pas un impact observé en production.

### CLM-AUD-003-639

- **Statement :** La revue finale a classé Low le risque que des messages d’exception tronqués exposent encore des chemins ou identifiants dans le JSON public.
- **État :** historical_execution
- **Sujet littéral :** jarvis_daily.py — erreurs publiques
- **Temps du fait :** 2026-07-20
- **Temps d’enregistrement :** 2026-07-20T05:08:07.601000+00:00
- **Source :** SRC-OPENCODE
- **Locator :** ses_0821451bdffeib4pfdYFblX04K — finding Low
- **Citation / observation :** Le finding Low cite la ligne 102 et recommande des codes d’erreur stables ou un filtrage plus large.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Revue statique datée ; aucun test de sortie n’a été relancé.

## Claims rejetés ou hors intégration

### Élément 1

- **id :** CLM-AUD-003-016

- **reason :** L’inaccessibilité du worker W1 est une limite d’environnement supersédée par les lectures directes réussies, pas un état actuel du vault.

### Élément 2

- **id :** CLM-AUD-003-305

- **reason :** Agrège schéma, dates, scheduling, documentation et instanciation ; non atomique et schéma V2 incomplet.

### Élément 3

- **id :** CLM-AUD-003-315

- **reason :** Instruction graphify hors question structurante ; enregistrement V2 incomplet et source non rouverte dans R2.

### Élément 4

- **id :** CLM-AUD-003-316

- **reason :** Auto-rapport d’échec puis écriture, sans observation primaire dans R2 ; schéma V2 incomplet.

### Élément 5

- **id :** CLM-AUD-003-317

- **reason :** Fusionne écriture historique et absence actuelle sous `contradicted`; ces états temporels peuvent coexister et doivent être séparés.

### Élément 6

- **id :** CLM-AUD-003-318

- **reason :** Métadonnée d’audit multi-projets hors question structurante ; schéma V2 incomplet.

### Élément 7

- **id :** CLM-AUD-003-319

- **reason :** Agrège plusieurs statuts ensuite corrigés par Sofian ; non relu directement et schéma V2 incomplet.

### Élément 8

- **id :** CLM-AUD-003-320

- **reason :** Agrège plusieurs risques sans citation minimale ni sujet unique.

### Élément 9

- **id :** CLM-AUD-003-321

- **reason :** Correction de profil hors question structurante ; schéma V2 incomplet et source non rouverte.

### Élément 10

- **id :** CLM-AUD-003-322

- **reason :** Auto-rapport de neuf écritures mémoire non relu live ; schéma V2 incomplet.

### Élément 11

- **id :** CLM-AUD-003-323

- **reason :** Réorganisation Developer hors question structurante ; schéma V2 incomplet et source non rouverte.

### Élément 12

- **id :** CLM-AUD-003-324

- **reason :** Agrège quatre réalisations distinctes ; non atomique.

### Élément 13

- **id :** CLM-AUD-003-325

- **reason :** Deux états historiques successifs sont mal étiquetés `contradicted`; source non rouverte dans R2.

### Élément 14

- **id :** CLM-AUD-003-326

- **reason :** Agrège plusieurs créations/câblages GitHub ; `show` décisif non relu pour ce claim.

### Élément 15

- **id :** CLM-AUD-003-335

- **reason :** Le `show` de la session 18 atteint sa limite globale avant le rapport final invoqué ; réalisation non directement vérifiée.

### Élément 16

- **id :** CLM-AUD-003-336

- **reason :** Le `show` de la session 18 atteint sa limite globale avant la liste finale ; dénominateur et visibilité publique non vérifiés.

### Élément 17

- **id :** CLM-AUD-003-342

- **reason :** Métadonnée d’exécution du worker, pas claim source sur l’écosystème.

### Élément 18

- **id :** CLM-AUD-003-343

- **reason :** Limite de lecture W2 supersédée par les lectures directes réussies de R2.

### Élément 19

- **id :** CLM-AUD-003-344

- **reason :** Claim live non structurant avec schéma V2 incomplet, non relu directement dans R2.

### Élément 20

- **id :** CLM-AUD-003-345

- **reason :** Preuve négative limitée à un ancien chemin, schéma V2 incomplet et aucune relocalisation prouvée.

### Élément 21

- **id :** CLM-AUD-003-346

- **reason :** Contrôle d’intégrité du worker, pas claim source ; la taille source a depuis évolué alors que les comptes restent identiques.

## Provenance

- Synthèse Kanban : `t_db22ff07`.
- `review_status: accepted` signifie accepté pour ce rapport documentaire, pas `user_accepted` ni `operational`.
- Mutations des sources : `0`.
