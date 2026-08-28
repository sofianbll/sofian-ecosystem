---
id: AUD-006-CLAIMS
title: AUD-006 — Ledger des claims
status: integrated
date: 2026-08-28
coverage: 94
---

# AUD-006 — Ledger exhaustif des claims

> Annexe intégrée du [rapport AUD-006](report.md). Ces 94 claims ont été retenus après collecte, contre-reviews et normalisations explicites.

### CLM-AUD-006-300

- **Statement :** Le payload `systems/finance-os/ARCHITECTURE.md` décrit un flux fichier ou source bancaire → import → transaction normalisée → cashflow/index documentaire et place la source bancaire comme preuve primaire.
- **État :** historical_intent
- **Sujet littéral :** Finance OS — architecture et frontières
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/finance-os/ARCHITECTURE.md:9-29
- **Citation / observation :** `source bancaire ou document original : preuve primaire` ; contrats API exacts `[À CONFIRMER]`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le payload ne prouve ni l’implémentation actuelle ni un contrat API complet.

### CLM-AUD-006-301

- **Statement :** Le payload `systems/finance-os/AUDIT.md` rapporte comme faits historiques des collections Finance OS observées, un healthcheck HTTP 200 daté et l’absence de modèle canonique prouvé pour clients, missions, devis et factures émises.
- **État :** historical_execution
- **Sujet littéral :** Finance OS — audit factuel
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/finance-os/AUDIT.md:9-25
- **Citation / observation :** `un healthcheck avait répondu HTTP 200 lors d’un audit daté` ; peuplement et fraîcheur non démontrés.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Un healthcheck et des collections observées ne prouvent ni fraîcheur ni qualité métier actuelle.

### CLM-AUD-006-302

- **Statement :** Le payload `systems/finance-os/README.md` définit Finance OS comme système spécialisé des états financiers persistés, distinct de la vérité bancaire primaire et d’un système commercial complet.
- **État :** historical_intent
- **Sujet littéral :** Finance OS — responsabilité
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/finance-os/README.md:9-29
- **Citation / observation :** `Il ne constitue ni la vérité bancaire primaire ni un système commercial complet.`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La responsabilité déclarée doit être rapprochée de la source Finance OS avant toute reprise active.

### CLM-AUD-006-303

- **Statement :** Le payload `systems/finance-os/STATUS.md` rapporte que le service et ses collections principales existent, tout en laissant la fraîcheur et la couverture métier à confirmer et en reportant toute intégration Jarvis.
- **État :** historical_intent
- **Sujet littéral :** Finance OS — état snapshot
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/finance-os/STATUS.md:9-24
- **Citation / observation :** `Le service et ses collections principales existent` ; fraîcheur et couverture `[À CONFIRMER]`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La phrase d’existence reste une déclaration de snapshot, pas une preuve live dans ce workstream.

### CLM-AUD-006-304

- **Statement :** Le payload `systems/hermes/ARCHITECTURE.md` présente session, projet, skills, outils, sous-agents, jobs et mémoire comme éléments utiles, avec une boucle Hermes → source canonique → résultat vérifié.
- **État :** historical_intent
- **Sujet littéral :** Hermes — architecture
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/hermes/ARCHITECTURE.md:9-30
- **Citation / observation :** `Sofian → Hermes → skill / code Jarvis → source canonique → résultat vérifié → Hermes`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La boucle est présentée comme envisagée et ne prouve pas l’authentification de chaque frontière.

### CLM-AUD-006-305

- **Statement :** Le payload `systems/hermes/AUDIT.md` rapporte historiquement que Hermes était l’interface de la conversation, qu’un projet Hermes Jarvis avait été créé puis n’était plus actif, qu’ourmem était distinct et qu’aucun cron Jarvis ni connexion Gmail authentifiée n’avait été établi pendant le chantier.
- **État :** historical_execution
- **Sujet littéral :** Hermes — audit factuel
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/hermes/AUDIT.md:9-29
- **Citation / observation :** `la mémoire built-in et les sessions Hermes sont distinctes d’ourmem` ; `aucun cron Jarvis n’a été créé`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ces faits sont datés et ne déterminent pas l’état live ultérieur.

### CLM-AUD-006-306

- **Statement :** Le payload `systems/hermes/README.md` définit Hermes comme runtime et interface agentique fournissant sessions, projets, outils, skills, jobs, mémoire et connexions configurées, sans posséder l’état des tâches, projets, paiements ou obligations externes.
- **État :** historical_intent
- **Sujet littéral :** Hermes — responsabilité
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/hermes/README.md:9-28
- **Citation / observation :** `Hermes ne possède pas l’état des tâches, projets, paiements ou obligations externes.`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La définition n’est pas une preuve d’usage quotidien ni d’intégration authentifiée.

### CLM-AUD-006-307

- **Statement :** Le payload `systems/hermes/STATUS.md` rapporte que Hermes était utilisable comme interface unique et orchestrateur, mais que l’expérience Jarvis quotidienne n’était pas codifiée dans un skill validé.
- **État :** historical_intent
- **Sujet littéral :** Hermes — état snapshot
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/hermes/STATUS.md:9-26
- **Citation / observation :** `Hermes est utilisable comme interface unique et orchestrateur` ; expérience quotidienne non codifiée.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** `Utilisable` est une qualification du document ; aucun parcours réel n’est exercé dans ce corpus.

### CLM-AUD-006-308

- **Statement :** Le payload `systems/homelab-os/ARCHITECTURE.md` sépare Homelab-OS comme configuration désirée et reconstruction, le runtime technique comme état observé et l’application comme propriétaire des faits métier.
- **État :** historical_intent
- **Sujet littéral :** Homelab-OS — séparation des responsabilités
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/homelab-os/ARCHITECTURE.md:9-30
- **Citation / observation :** `Homelab-OS → configuration désirée` ; `Runtime technique → état observé maintenant` ; `Application → faits métier`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La séparation documentaire ne prouve pas l’état sain des runtimes ni un workflow Jarvis.

### CLM-AUD-006-309

- **Statement :** Le payload `systems/homelab-os/AUDIT.md` rapporte que SRC-HOMELAB contient la configuration canonique, que n8n est documenté avec PostgreSQL/Caddy/webhooks bornés et qu’aucun export de workflow Jarvis Mail/iOS n’y avait été trouvé.
- **État :** historical_execution
- **Sujet littéral :** Homelab-OS — audit factuel
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/homelab-os/AUDIT.md:9-28
- **Citation / observation :** `la documentation désirée ne prouve pas l’état live` ; aucun export Jarvis Mail/iOS trouvé.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’absence dans cet audit borné ne prouve pas l’absence dans tout le corpus externe.

### CLM-AUD-006-310

- **Statement :** Le payload `systems/homelab-os/README.md` définit Homelab-OS comme description de la configuration désirée, de la reconstruction et des procédures d’exploitation, sans lui attribuer l’autorité sur les faits métier des applications hébergées.
- **État :** historical_intent
- **Sujet littéral :** Homelab-OS — responsabilité
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/homelab-os/README.md:9-28
- **Citation / observation :** `Héberger une application ne donne pas à Homelab-OS l’autorité sur ses faits métier.`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le payload ne vérifie ni les procédures ni le runtime réel.

### CLM-AUD-006-311

- **Statement :** Le payload `systems/homelab-os/STATUS.md` rapporte que le système de configuration existait et documentait plusieurs services, mais qu’aucun workflow Jarvis dédié n’était démontré et que n8n restait une option conditionnelle.
- **État :** historical_intent
- **Sujet littéral :** Homelab-OS — état snapshot
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/homelab-os/STATUS.md:9-24
- **Citation / observation :** `Aucun workflow Jarvis dédié n’est démontré` ; n8n conservé comme option d’adaptation.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’état et l’option sont datés ; aucune décision cible n’est validée par ce payload.

### CLM-AUD-006-312

- **Statement :** Le payload `systems/jarvis/ARCHITECTURE.md` formule une boucle cible avec accord humain et relecture, mais mélange cette intention avec des composants dits démontrés et des interfaces futures différées.
- **État :** contradicted
- **Sujet littéral :** Jarvis — architecture cible snapshot
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/jarvis/ARCHITECTURE.md:9-34
- **Citation / observation :** `Boucle cible` ; `Composants démontrés` ; `NATS, nouvelle base, microservices et mémoire complète sont différés`.
- **Confiance :** high
- **Contradictions :** ["C-002", "C-003"]
- **Review :** accepted
- **Limite :** Le statut cible n’est pas une décision acceptée et l’articulation historique/current n’est pas résolue.

### CLM-AUD-006-314

- **Statement :** Le payload `systems/jarvis/README.md` définit Jarvis comme couche agentique envisagée pour relier les sources canoniques, proposer des actions et vérifier les résultats, sans devenir une base métier universelle.
- **État :** historical_intent
- **Sujet littéral :** Jarvis — responsabilité
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/jarvis/README.md:9-30
- **Citation / observation :** `Il ne devient pas une base métier universelle` ; aucun parcours réel complet n’est livré.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La responsabilité est proposée et le repo/composants mentionnés ne sont pas revalidés dans ce corpus fermé.

### CLM-AUD-006-315

- **Statement :** Le payload `systems/jarvis/STATUS.md` porte le statut disputed et distingue inventaires/contrats, prototype Mail sur fixture et moteur Daily Brief testé d’une liste de parcours non livrés.
- **État :** contradicted
- **Sujet littéral :** Jarvis — état snapshot
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/jarvis/STATUS.md:1-35
- **Citation / observation :** `status: disputed` ; `Jarvis n’aide pas encore Sofian quotidiennement de bout en bout`.
- **Confiance :** high
- **Contradictions :** ["C-002", "C-003", "C-005"]
- **Review :** accepted
- **Limite :** Le choix de priorité Brief/Mail/Daily Start est explicitement non résolu.

### CLM-AUD-006-316

- **Statement :** Le payload `systems/opencode/ARCHITECTURE.md` décrit une reprise par recherche indexée puis session OpenCode exacte et vérification dans le dépôt actuel, tout en laissant l’articulation future avec Hermes/Jarvis à confirmer.
- **État :** historical_intent
- **Sujet littéral :** OpenCode — architecture de reprise
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/opencode/ARCHITECTURE.md:9-29
- **Citation / observation :** `Question sur un ancien travail → recherche indexée → session OpenCode exacte → synthèse et vérification`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le flux est une architecture d’usage proposée ; il ne prouve pas que l’index ou l’articulation sont actuellement exercés.

### CLM-AUD-006-317

- **Statement :** Le payload `systems/opencode/AUDIT.md` rapporte historiquement la base canonique des conversations, OpenChamber comme interface/métadonnées, un index FTS dérivé et l’ancien moteur Daily Brief avec 81 tests.
- **État :** historical_execution
- **Sujet littéral :** OpenCode — audit factuel
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/opencode/AUDIT.md:9-28
- **Citation / observation :** `la base canonique des conversations est SRC-OPENCODE` ; index FTS local dérivé.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Une session ou une suite de tests historique ne prouve pas qu’une décision reste active ; aucune migration brute n’est autorisée.

### CLM-AUD-006-318

- **Statement :** Le payload `systems/opencode/README.md` positionne OpenCode comme environnement agentique utilisé pour le développement et la reprise historique, explicitement conservé pour un usage futur et non classé obsolète ou remplacé par Hermes.
- **État :** historical_intent
- **Sujet littéral :** OpenCode — position
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/opencode/README.md:9-27
- **Citation / observation :** `OpenCode est conservé pour un usage futur` ; `ni obsolète, ni supprimé, ni remplacé définitivement par Hermes`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La responsabilité future reste `[À CONFIRMER]` et doit rester séparée d’une décision de cible.

### CLM-AUD-006-319

- **Statement :** Le payload `systems/opencode/STATUS.md` rapporte qu’OpenCode restait disponible et utile pour le développement et la reprise historique, sans rôle futur exclusif arrêté.
- **État :** historical_intent
- **Sujet littéral :** OpenCode — état snapshot
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/opencode/STATUS.md:9-26
- **Citation / observation :** `OpenCode reste disponible et utile` ; `Aucun rôle futur exclusif n’est arrêté`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Cette qualification est datée et ne constitue pas une preuve live ni une décision d’usage futur.

### CLM-AUD-006-320

- **Statement :** Le payload `systems/ourmem/ARCHITECTURE.md` décrit ourmem comme mémoire sémantique secondaire et exige la vérification des informations actionnables dans les sources directes, l’historique exact ou les systèmes canoniques.
- **État :** historical_intent
- **Sujet littéral :** ourmem — architecture et frontière Jarvis
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/ourmem/ARCHITECTURE.md:9-28
- **Citation / observation :** `Il doit ensuite vérifier toute information actionnable` ; architecture complète de Jarvis Memory différée.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le payload ne prouve pas le contrat complet de mémoire ni son intégration future à Jarvis.

### CLM-AUD-006-321

- **Statement :** Le payload `systems/ourmem/AUDIT.md` rapporte historiquement un service auto-hébergé local dans Docker, un stockage persistant, une configuration canonique Homelab-OS/dotfiles et un accès Hermes via MCP, avec un fournisseur mémoire Hermes actif distinct.
- **État :** historical_execution
- **Sujet littéral :** ourmem — audit factuel
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/ourmem/AUDIT.md:9-28
- **Citation / observation :** `le service est auto-hébergé localement dans Docker` ; aucun contenu de mémoire n’est copié.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le payload ne vérifie pas le contenu, la fraîcheur ni le contrat détaillé Jarvis Memory.

### CLM-AUD-006-322

- **Statement :** Le payload `systems/ourmem/README.md` définit ourmem comme mémoire sémantique secondaire pour stocker et rechercher du contexte passé, sans remplacer TaskNotes, Sofian OS, les documents probants ou l’historique exact.
- **État :** historical_intent
- **Sujet littéral :** ourmem — responsabilité
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/ourmem/README.md:9-27
- **Citation / observation :** `sans devenir la preuve des faits métier actuels` ; `ourmem ne remplace ni TaskNotes, ni Sofian OS`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La définition ne prouve ni l’usage ni la complétude de la mémoire sémantique.

### CLM-AUD-006-323

- **Statement :** Le payload `systems/ourmem/STATUS.md` rapporte que le service et l’accès MCP existaient, mais que le rôle précis dans l’expérience Jarvis future n’était pas décidé et que Jarvis Memory devait être reporté.
- **État :** historical_intent
- **Sujet littéral :** ourmem — état snapshot
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/ourmem/STATUS.md:9-24
- **Citation / observation :** `Son rôle précis dans l’expérience Jarvis future n’est pas décidé` ; `Reporter Jarvis Memory`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le statut est historique et ne confirme pas une décision actuelle.

### CLM-AUD-006-324

- **Statement :** Le payload `systems/sofian-os/ARCHITECTURE.md` présente notes Projet, TaskNotes, Inbox, Daily/Weekly Notes, Resources/System Config et dashboards comme composants, avec un flux Capture → Inbox → Clarify → Projet/TaskNote/Resource.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS — architecture documentaire
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/sofian-os/ARCHITECTURE.md:9-35
- **Citation / observation :** `Bases et dashboards : vues dérivées, sans autorité propre` ; correction dans la note canonique.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les formats détaillés sont renvoyés aux schémas du vault, non prouvés par ce payload.

### CLM-AUD-006-325

- **Statement :** Le payload `systems/sofian-os/AUDIT.md` rapporte que le vault canonique, les projets structurés, TaskNotes et les parcours Capture/Clarify/Engage/Review étaient documentés, tandis que l’usage régulier des revues et un parcours Jarvis complet n’étaient pas démontrés.
- **État :** historical_execution
- **Sujet littéral :** Sofian OS — audit factuel
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/sofian-os/AUDIT.md:9-27
- **Citation / observation :** `les Daily Notes récentes montrent une utilisation irrégulière` ; aucun parcours Jarvis complet vérifié.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ces constats sont datés et ne remplacent pas la lecture du vault canonique actuel.

### CLM-AUD-006-326

- **Statement :** Le payload `systems/sofian-os/README.md` définit Sofian OS comme cockpit humain portant l’état enregistré des projets et engagements, les vues de revue, les liens TaskNotes et les décisions/ressources qualifiées, hors vérité bancaire ou runtime technique.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS — responsabilité
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/sofian-os/README.md:9-30
- **Citation / observation :** `Sofian OS est le cockpit humain de Sofian` ; dashboards restent des projections.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le rôle déclaré ne prouve pas l’usage réel ni la régularité des routines.

### CLM-AUD-006-327

- **Statement :** Le payload `systems/sofian-os/STATUS.md` rapporte que le cockpit et les schémas projets/tâches existaient, que les routines étaient définies sans usage régulier démontré et qu’aucune migration du vault n’était décidée dans le snapshot.
- **État :** historical_intent
- **Sujet littéral :** Sofian OS — état snapshot
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/sofian-os/STATUS.md:9-28
- **Citation / observation :** `Les routines quotidiennes sont définies mais leur usage régulier n’est pas démontré` ; `Aucune migration du vault n’est décidée`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le payload ne valide pas l’état actuel du vault ni l’acceptation des documents Jarvis.

### CLM-AUD-006-328

- **Statement :** Le payload `systems/tasknotes/ARCHITECTURE.md` définit le minimum d’une TaskNote, le flux entrée clarifiée → proposition → accord humain → TaskNote et l’exigence de mutation ciblée, idempotente et relue.
- **État :** historical_intent
- **Sujet littéral :** TaskNotes — architecture et contrat
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/tasknotes/ARCHITECTURE.md:9-30
- **Citation / observation :** `Une TaskNote contient au minimum un titre, un statut, une priorité et is_template: false` ; mutation relue après écriture.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le contrat est documentaire et les vues/données réelles ne sont pas exercées dans ce workstream.

### CLM-AUD-006-329

- **Statement :** Le payload `systems/tasknotes/AUDIT.md` rapporte que les tâches sont des notes Markdown structurées, avec statuts todo/in_progress/paused/done/dropped et priorités low/medium/high, et que trois TaskNotes Jarvis avaient été créées prématurément.
- **État :** historical_execution
- **Sujet littéral :** TaskNotes — audit factuel
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/tasknotes/AUDIT.md:9-28
- **Citation / observation :** `les tâches sont des notes Markdown structurées` ; prévention de doublons non construite.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les statuts/dates et créations rapportés sont historiques ; aucune preuve externe n’est déduite d’une tâche terminée.

### CLM-AUD-006-330

- **Statement :** Le payload `systems/tasknotes/README.md` définit TaskNotes comme autorité de l’état des tâches dans Sofian OS, sans lui attribuer la preuve qu’un organisme, une banque ou un service externe a accepté l’action.
- **État :** historical_intent
- **Sujet littéral :** TaskNotes — responsabilité
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/tasknotes/README.md:9-30
- **Citation / observation :** `TaskNotes est l’autorité de l’état des tâches` ; une TaskNote ne prouve pas l’acceptation externe.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La responsabilité déclarée ne prouve pas l’intégrité actuelle des notes ni la réussite des vues.

### CLM-AUD-006-331

- **Statement :** Le payload `systems/tasknotes/STATUS.md` rapporte que TaskNotes fonctionnait comme système canonique des actions, sans connecteur Jarvis de création approuvée, et qu’aucune écriture automatique n’était autorisée dans le snapshot.
- **État :** historical_intent
- **Sujet littéral :** TaskNotes — état snapshot
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/systems/tasknotes/STATUS.md:9-28
- **Citation / observation :** `Aucun connecteur Jarvis de création approuvée n’est livré` ; `Aucune écriture automatique n’est autorisée actuellement`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le statut est daté et ne prouve pas le comportement live ultérieur.

### CLM-AUD-006-500

- **Statement :** Le payload `files/workflows/daily-review.md` définit le besoin de clôturer la journée, rendre les boucles visibles et préparer demain, avec un parcours faits → tâches/attentes → écarts/preuves → clôture/replanification → trois priorités maximum.
- **État :** historical_intent
- **Sujet littéral :** Daily Review
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/daily-review.md:11-22
- **Citation / observation :** `Clôturer la journée, rendre les boucles visibles et préparer demain` ; `Faits de la journée → tâches et attentes → écarts / preuves manquantes → clôture / replanification → 3 priorités maximum`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le payload décrit une intention et un parcours ; il ne prouve pas une acceptation utilisateur ni un usage actuel.

### CLM-AUD-006-501

- **Statement :** Le payload `Daily Review` réutilise des routines Sofian OS et certaines lectures bornées de TaskNotes, et prescrit l’affichage de la couverture, la visibilité des indisponibilités, la séparation propositions/mutations et l’absence d’opérations Mail ou vault implicites.
- **État :** historical_intent
- **Sujet littéral :** Daily Review — garde-fous et dépendances déclarées
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/daily-review.md:24-28,34-39
- **Citation / observation :** `routines documentées dans Sofian OS` ; `lecture bornée de TaskNotes` ; `indisponibilité jamais interprétée comme vide` ; `propositions séparées des mutations`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les systèmes référencés ne sont pas revalidés dans ce groupe fermé ; ces éléments restent des dépendances déclarées.

### CLM-AUD-006-503

- **Statement :** Le payload `daily-start.md` propose de réduire le coût de décision et de démarrage en partant de TaskNotes et des projets, puis en affichant des anomalies, au plus trois options, un choix humain, du contexte et un démarrage accompagné.
- **État :** historical_intent
- **Sujet littéral :** Daily Start
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/daily-start.md:11-22
- **Citation / observation :** `Réduire le coût de décision et de démarrage` ; `TaskNotes et projets → anomalies visibles → 3 options maximum → choix humain → contexte → démarrage accompagné`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le parcours est explicitement proposé ; aucun cas réel ou besoin prioritaire accepté n’est établi dans le payload.

### CLM-AUD-006-504

- **Statement :** Le payload `Daily Start` prévoit comme sortie une action principale, jusqu’à deux actions secondaires, la raison du classement, la provenance, la certitude et les données périmées, sans mutation pendant la première version.
- **État :** historical_intent
- **Sujet littéral :** Daily Start — sortie et permission
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/daily-start.md:24-30
- **Citation / observation :** `une action principale et jusqu’à deux actions secondaires` ; `aucune mutation pendant la première version`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Il s’agit d’une sortie envisagée et non d’un contrat accepté ou exercé.

### CLM-AUD-006-505

- **Statement :** Le payload `Daily Start` se classe lui-même comme proposé et non construit ; il rapporte une todo de session marquée `in_progress`, sans autorisation de build ni code Daily Start enregistré, et renvoie sa priorité à une décision non réconciliée.
- **État :** historical_execution
- **Sujet littéral :** Daily Start — statut et priorité
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/daily-start.md:32-44
- **Citation / observation :** `Proposé, non construit` ; `aucune autorisation de build ni aucun code Daily Start` ; `Sa priorité face à Mail et Daily Review reste non réconciliée`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Une todo de session ne prouve ni construction, ni priorité utilisateur, ni usage opérationnel.

### CLM-AUD-006-506

- **Statement :** Le payload `inbox-processing.md` définit une clarification d’entrée qui mène vers tâche, projet, attente, référence ou suppression proposée, sans transformer automatiquement l’entrée en tâche.
- **État :** historical_intent
- **Sujet littéral :** Inbox Processing
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/inbox-processing.md:10-20
- **Citation / observation :** `Décider rapidement ce qu’une entrée devient sans la transformer automatiquement en tâche` ; `Entrée → clarifier → tâche / projet / attente / référence / suppression proposée`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le payload ne prouve pas qu’un moteur ou un parcours réel existe.

### CLM-AUD-006-507

- **Statement :** Le payload `Inbox Processing` attribue l’autorité à l’entrée originale pour son contenu, à Sofian pour la destination, à TaskNotes pour l’état d’une action créée et à Sofian OS pour le projet ou la ressource résultante.
- **État :** historical_intent
- **Sujet littéral :** Inbox Processing — autorités déclarées
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/inbox-processing.md:22-27
- **Citation / observation :** `l’entrée originale reste la preuve de son contenu` ; `Sofian décide de sa destination` ; `TaskNotes porte l’état` ; `Sofian OS porte le projet ou la ressource`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Ces responsabilités sont déclarées par le payload historique et ne constituent pas une carte d’autorité actuelle acceptée.

### CLM-AUD-006-508

- **Statement :** Le payload `Inbox Processing` indique que le processus humain est documenté mais non livré par Jarvis, qu’aucun moteur universel de classification n’a été vérifié et que les critères d’acceptation exigent destination explicite, provenance, incertitude visible, accord avant mutation et relecture après écriture.
- **État :** historical_intent
- **Sujet littéral :** Inbox Processing — livraison et critères
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/inbox-processing.md:29-43
- **Citation / observation :** `Documenté, non livré par Jarvis` ; `Aucun moteur universel de classification n’a été vérifié` ; `Contrat d’entrée unifié ... [À CONFIRMER]`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucun cas réel d’acceptation, traitement des doublons ou moteur vérifié n’est fourni.

### CLM-AUD-006-509

- **Statement :** Le payload `ios-capture.md` décrit une capture texte ou dictée depuis l’iPhone, sans choix immédiat de projet ou de priorité, via un Shortcut unique, un payload versionné, un endpoint autorisé, l’Inbox Sofian OS et un accusé.
- **État :** historical_intent
- **Sujet littéral :** iOS Capture
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/ios-capture.md:11-22
- **Citation / observation :** `Capturer un texte ou une dictée en quelques secondes` ; `Texte ou dictée → Shortcut unique → payload versionné → endpoint autorisé → Inbox Sofian OS → accusé`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le payload ne démontre ni endpoint autorisé, ni Shortcut installé, ni accusé reçu.

### CLM-AUD-006-510

- **Statement :** Le payload `iOS Capture` propose un contrat minimal composé de `schema_version`, `capture_id`, `captured_at`, `input_type`, `content` et `source_device`, et le qualifie de provisoire.
- **État :** historical_intent
- **Sujet littéral :** iOS Capture — contrat minimal
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/ios-capture.md:28-30
- **Citation / observation :** `schema_version`, `capture_id`, `captured_at`, `input_type`, `content` et `source_device` ; `Ce contrat reste provisoire`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le contrat n’est ni validé, ni exercé, ni relié à une implémentation actuelle dans le groupe fermé.

### CLM-AUD-006-511

- **Statement :** Le payload `iOS Capture` se classe comme documenté et non construit ; il rapporte que treize Shortcuts apparaissent dans une vision historique sans qu’un Shortcut Jarvis correspondant installé ait été retrouvé, et laisse l’authentification, l’idempotence, le format canonique et la rétention des médias à décider.
- **État :** historical_execution
- **Sujet littéral :** iOS Capture — statut et décisions manquantes
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/ios-capture.md:24-26,32-40
- **Citation / observation :** `Documenté, non construit` ; `aucun Shortcut Jarvis correspondant n’a été retrouvé comme installé` ; `Décisions manquantes` ; `Commencer éventuellement par un Shortcut texte/dictée`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’absence de Shortcut retrouvé est une preuve négative bornée au travail historique ; elle ne prouve pas une absence actuelle hors de ce corpus.

### CLM-AUD-006-512

- **Statement :** Le payload `mail-to-task.md` définit un parcours où un fil Mail autorisé est lu sans mutation, clarifié et proposé, puis transformé après accord humain en TaskNote idempotente relue.
- **État :** historical_intent
- **Sujet littéral :** Mail to Task
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/mail-to-task.md:11-22
- **Citation / observation :** `Fil autorisé → lecture sans mutation → clarification → proposition → accord humain → TaskNote idempotente → relecture`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le parcours réel, la connexion au compte et la TaskNote relue ne sont pas démontrés.

### CLM-AUD-006-514

- **Statement :** Le payload `Mail to Task` ne démontre ni compte réel, ni fil complexe, ni prévention des doublons, ni création/relecture d’une TaskNote ; il interdit les mutations Mail et la création de TaskNote sans accord et classe le parcours réel comme non livré.
- **État :** historical_intent
- **Sujet littéral :** Mail to Task — limites, permissions et priorité
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/workflows/mail-to-task.md:28-42
- **Citation / observation :** `Non démontré` ; `Marquer lu, archiver, supprimer, envoyer ou créer une TaskNote sans accord sont interdits` ; `Prototype sur fixture, parcours réel non livré` ; priorité non réconciliée.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le statut et les permissions viennent du document historique ; aucune autorisation actuelle ni usage opérationnel n’est établi.

### CLM-AUD-006-600

- **Statement :** Dans la baseline, `artifacts/README.md` se déclare `active` et décrit une politique/registre des artefacts actifs.
- **État :** historical_intent
- **Sujet littéral :** artifacts/README.md — registre des artefacts
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/README.md:1-10
- **Citation / observation :** Frontmatter : `status: active`, `date: 2026-08-25`, `scope: Politique et registre des artefacts actifs du projet` ; titre `Artefacts`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le statut `active` est celui du payload historique, pas une preuve d’activité actuelle hors de la baseline.

### CLM-AUD-006-601

- **Statement :** Le registre historique affirme que deux cartes HTML sont importées sous `artifacts/maps/` et que la carte Autorité contestée est conservée dans l’archive contestée.
- **État :** historical_intent
- **Sujet littéral :** artifacts/README.md — disposition des cartes
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/README.md:12-16
- **Citation / observation :** `Deux cartes HTML actives sont importées sous [maps/]` ; `La carte Autorité contestée n’est pas active : elle réside dans l’archive contestée`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Cette disposition est déclarée par le registre ; elle ne valide pas le contenu ni l’usage des cartes.

### CLM-AUD-006-602

- **Statement :** Le contrat historique d’import exigeait provenance, nom original, date, SHA-256, statut et raison, tout en laissant les HTML bruts inchangés et les métadonnées dans le README voisin.
- **État :** historical_intent
- **Sujet littéral :** artifacts/README.md — contrat d’import
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/README.md:18-20
- **Citation / observation :** `Chaque artefact copié enregistre sa provenance, son nom original, sa date, son SHA-256, son statut et sa raison` ; `Les fichiers HTML bruts restent inchangés`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le contrat décrit une règle documentaire historique ; il ne prouve pas que les claims métier des HTML sont vrais.

### CLM-AUD-006-603

- **Statement :** Le README historique des cartes déclare que les deux fichiers sont des copies byte-for-byte des artefacts produits, dont les originaux restent sous `SRC-ARTIFACTS`, et enregistre leurs hashes et tailles.
- **État :** historical_execution
- **Sujet littéral :** artifacts/maps/README.md — provenance des cartes actives
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/maps/README.md:9-16
- **Citation / observation :** `Ces fichiers sont des copies byte-for-byte` ; originaux sous `SRC-ARTIFACTS` ; hashes `3af1f2…` et `979a89…`, tailles `37093` et `31217` octets.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La comparaison directe réalisée ici porte sur commit → payload baseline ; les originaux externes `SRC-ARTIFACTS` n’ont pas été ouverts.

### CLM-AUD-006-604

- **Statement :** Le README des cartes limite leur rôle à des supports de lecture et précise que l’import ne confirme pas toutes les affirmations qu’elles contiennent.
- **État :** historical_intent
- **Sujet littéral :** artifacts/maps/README.md — limite de validation
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/maps/README.md:18-20
- **Citation / observation :** `Ces cartes servent de supports de lecture. Leur import ne confirme pas toutes les affirmations qu’elles contiennent.`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La limite est explicitement documentaire ; elle ne tranche pas quels claims doivent être conservés après revue.

### CLM-AUD-006-605

- **Statement :** La carte Niveau 0 présente neuf responsabilités regroupées en trois familles, avec Sofian comme point de départ.
- **État :** historical_intent
- **Sujet littéral :** artifacts/maps/architecture-level-0.html — carte Niveau 0
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/maps/architecture-level-0.html:708-815
- **Citation / observation :** `Neuf responsabilités durables, regroupées` ; familles `Soi et liens`, `Développement & contribution`, `Sécurité & environnement` ; point de départ `Sofian`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le HTML est une projection visuelle historique ; sa présence ne prouve ni validation actuelle ni couverture exhaustive de la vie.

### CLM-AUD-006-606

- **Statement :** La carte Niveau 0 affiche une base déclarée validée le 20 août 2026 et indique qu’aucun OS, Area ou donnée n’est créé dans cette vue.
- **État :** historical_intent
- **Sujet littéral :** artifacts/maps/architecture-level-0.html — portée annoncée
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/maps/architecture-level-0.html:722-724
- **Citation / observation :** `Base Niveau 0 validée le 20 août 2026` ; `aucun OS, aucune Area et aucune donnée ne sont créés ici`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La mention de validation est une assertion embarquée dans le HTML ; aucune preuve utilisateur indépendante n’est dans ce groupe.

### CLM-AUD-006-607

- **Statement :** La carte Niveau 0 propose six situations de test de couverture avec un domaine pilote et des liens secondaires, puis expose des actions de correction.
- **État :** historical_intent
- **Sujet littéral :** artifacts/maps/architecture-level-0.html — scénarios et correction
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/maps/architecture-level-0.html:852-904
- **Citation / observation :** `Une situation a un pilote principal et peut conserver des liens secondaires` ; scénarios médical, familial, alternance, URSSAF, Køya et impression 3D ; boutons `Signaler un domaine manquant` et `Rouvrir une correction`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les contrôles et boutons sont observés dans le code, mais aucun parcours navigateur n’a été exécuté conformément à la frontière de lecture seule.

### CLM-AUD-006-608

- **Statement :** La carte des capacités transverses organise dix capacités en quatre familles et décrit leurs outcomes, déclencheurs, invariants, frontières et appuis canoniques annoncés.
- **État :** historical_intent
- **Sujet littéral :** artifacts/maps/capabilities.html — capacités transverses
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/maps/capabilities.html:300-325,370-457
- **Citation / observation :** `Quatre familles structurent la lecture ; dix capacités portent des outcomes distincts` ; tableau JavaScript des capacités `Capturer` à `Améliorer progressivement`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les capacités et leurs appuis sont des assertions de projection ; leur acceptation et leur couverture actuelle restent non établies.

### CLM-AUD-006-609

- **Statement :** La carte des capacités affiche une base de travail déclarée validée le 20 août 2026, tout en maintenant systèmes, sources de vérité et contrats hors champ.
- **État :** historical_intent
- **Sujet littéral :** artifacts/maps/capabilities.html — portée annoncée
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/maps/capabilities.html:294-297,343-356
- **Citation / observation :** `Base de travail validée le 20 août 2026` ; `Les systèmes, les sources de vérité et les contrats restent hors champ`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La validation n’est pas confirmée par une décision utilisateur lisible dans ce payload.

### CLM-AUD-006-610

- **Statement :** La carte des capacités propose six scénarios et présente leurs parcours comme des tests de couverture, non comme des workflows imposés.
- **État :** historical_intent
- **Sujet littéral :** artifacts/maps/capabilities.html — scénarios de couverture
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/artifacts/maps/capabilities.html:328-340,460-466
- **Citation / observation :** `Le parcours est un test de couverture, pas un workflow imposé` ; six scénarios, dont rendez-vous médical, dossier familial, alternance Epitech, URSSAF, Køya et pièce imprimée en 3D.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune exécution réelle ni acceptation de ces parcours n’est prouvée par le groupe fermé.

### CLM-AUD-006-611

- **Statement :** L’index historique des artefacts archivés conserve la carte des systèmes et autorités parce qu’une validation y est ensuite contestée, avec un remplaçant laissé à `[À CONFIRMER]`.
- **État :** historical_intent
- **Sujet littéral :** archive/artifacts/README.md — archive contestée
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/artifacts/README.md:9-15
- **Citation / observation :** `Affiche une validation ensuite contestée` ; statut `Disputed / archived` ; remplaçant ``[À CONFIRMER]`` ; `L’HTML est conservé byte-for-byte`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’index ne donne ni la décision actuelle ni la personne qui doit confirmer un remplacement.

### CLM-AUD-006-612

- **Statement :** Le README de l’artefact contesté classe sa carte comme disputed et explique que sa conservation byte-for-byte préserve la provenance de la contradiction ; le remplaçant éventuel reste `[À CONFIRMER]`.
- **État :** contradicted
- **Sujet littéral :** archive/artifacts/disputed/README.md — statut de validation
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/artifacts/disputed/README.md:9-19
- **Citation / observation :** Frontmatter `status: disputed` ; `validation ensuite contestée` ; `La formulation « validé » ne constitue pas une validation actuelle` ; remplaçant `[À CONFIRMER]`.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-006-613"]
- **Review :** accepted
- **Limite :** La contradiction porte sur la portée de la validation affichée, pas sur l’existence matérielle du HTML.

### CLM-AUD-006-613

- **Statement :** Le HTML contesté présente textuellement une base `Validé le 20 août 2026 — base v0.1` et annonce l’absence de nouveau système, contrat ou automatisation.
- **État :** contradicted
- **Sujet littéral :** archive/artifacts/disputed/systems-and-authorities.html — validation affichée
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/artifacts/disputed/systems-and-authorities.html:283-287
- **Citation / observation :** `Validé le 20 août 2026 — base v0.1` ; `Aucun nouveau système, contrat ou automatisation.`
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-006-612"]
- **Review :** accepted
- **Limite :** Le HTML prouve seulement ce qu’il affiche ; le README voisin conteste que cette formulation vaille validation actuelle.

### CLM-AUD-006-614

- **Statement :** Le HTML contesté contient un registre historique de systèmes, autorités, faits établis/partiels/non établis, projections et instantanés techniques, dont la portée reste disputée avec la carte elle-même.
- **État :** historical_intent
- **Sujet littéral :** archive/artifacts/disputed/systems-and-authorities.html — registre embarqué
- **Temps du fait :** 2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/artifacts/disputed/systems-and-authorities.html:294-375,578-586
- **Citation / observation :** Constantes `SYSTEMES`, `FAITS_HUMAINS`, `FAITS_EXTERNES`, `FINANCE`, `HOMELAB`, `JARVIS` ; avertissement `Divergence observée pendant l’audit` et `memory.provider valait none dans Hermes`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le contenu est un artefact historique contesté ; les états embarqués ne sont pas une preuve live des systèmes ou runtimes.

### CLM-AUD-006-615

- **Statement :** Les sept payloads du groupe fermé correspondent byte-for-byte aux sept blobs du commit source `e331ee4e0a1006f813cf89f3a5c6f6bb262d2d29`, et le manifeste complet de la baseline passe pour ses 73 fichiers.
- **État :** historical_execution
- **Sujet littéral :** Baseline initiale — intégrité du groupe G6
- **Temps du fait :** 2026-08-25
- **Temps d’enregistrement :** 2026-08-28
- **Source :** SRC-BASELINE
- **Locator :** MANIFEST.sha256 ; commit e331ee4e0a1006f813cf89f3a5c6f6bb262d2d29 ; comparaison git cat-file/shasum vérifiée
- **Citation / observation :** Commande `shasum -a 256 -c MANIFEST.sha256` : toutes les entrées OK ; comparaison commit→payload : 7 paires de SHA-256 identiques.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** L’intégrité matérielle ne valide ni les affirmations métier, ni l’usage opérationnel, ni l’acceptation utilisateur.

### CLM-AUD-006-616

- **Statement :** La baseline se définit comme une preuve historique et un point de retour, non comme une validation des affirmations archivées ni comme un remplacement des sources canoniques externes.
- **État :** historical_intent
- **Sujet littéral :** BASELINE.md — statut de la consolidation
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-27
- **Source :** SRC-BASELINE
- **Locator :** BASELINE.md:12-16,28-38
- **Citation / observation :** `Elle constitue une preuve historique et un point de retour` ; `Elle ne valide pas les affirmations` ; `Persisté ne signifie pas validé`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La baseline ne renseigne pas à elle seule l’état live postérieur au 2026-08-25.

### CLM-AUD-006-700

- **Statement :** Le payload `archive/README.md` définit l’archive comme conservant les versions remplacées ou contestées sans effacer leur provenance.
- **État :** historical_intent
- **Sujet littéral :** archive/README.md — politique de conservation
- **Temps du fait :** 2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/README.md:9-11
- **Citation / observation :** `L’archive conserve les versions remplacées ou contestées sans effacer leur provenance.`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Règle documentaire historique ; ne prouve ni que les contenus sont remplacés aujourd’hui ni que leur vérité a été revue.

### CLM-AUD-006-701

- **Statement :** Le payload `archive/README.md` décrit un snapshot Obsidian de neuf blobs, une carte HTML contestée et aucune décision archivée.
- **État :** historical_intent
- **Sujet littéral :** archive/README.md — contenu annoncé
- **Temps du fait :** 2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/README.md:13-17
- **Citation / observation :** `snapshot Obsidian du commit 43b0964` : `neuf blobs historiques` ; `carte Autorité contestée` ; `décisions archivées` : `aucune actuellement`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Inventaire de navigation du snapshot ; les autres groupes de la baseline ne sont pas des preuves de statut actuel.

### CLM-AUD-006-702

- **Statement :** Le contrat d’archive exige pour chaque entrée une source, une date, une empreinte, une raison, un statut et un remplaçant éventuel, tout en conservant les payloads byte-for-byte.
- **État :** historical_intent
- **Sujet littéral :** archive/README.md — contrat d’archive
- **Temps du fait :** 2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/README.md:19-21
- **Citation / observation :** `Chaque entrée indique source, date, empreinte, raison d’archivage, statut et remplaçant éventuel` ; `payloads historiques restent byte-for-byte`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le contrat décrit une règle de conservation ; il ne valide pas les claims métier des payloads.

### CLM-AUD-006-703

- **Statement :** Le payload `archive/decisions/README.md` affirme qu’aucune décision n’est archivée et que les décisions contestées restent dans l’index avec le statut `disputed` jusqu’à résolution explicite.
- **État :** historical_intent
- **Sujet littéral :** archive/decisions/README.md — décisions archivées
- **Temps du fait :** 2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/decisions/README.md:9-11
- **Citation / observation :** `Aucune décision n’est archivée` ; `Les décisions contestées restent actives dans l’index avec le statut disputed`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Affirmation de l’archive historique ; aucun registre actif n’est consulté ici.

### CLM-AUD-006-704

- **Statement :** Le payload `archive/documents/README.md` enregistre le snapshot Obsidian `43b0964` comme un lot de neuf documents aux chemins originaux, provenant de `SRC-SOS`, avec le statut `Archived`.
- **État :** historical_intent
- **Sujet littéral :** archive/documents/README.md — registre du lot
- **Temps du fait :** 2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/README.md:9-15
- **Citation / observation :** Table : `Snapshot Obsidian 43b0964` ; `Neuf documents aux chemins originaux` ; provenance `SRC-SOS` ; statut `Archived`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Métadonnée de lot ; `SRC-SOS` n’est pas ouvert dans ce workstream fermé.

### CLM-AUD-006-705

- **Statement :** Le même registre précise que les fichiers sous `files/` sont des payloads historiques immuables et que leur README porte provenance, raison, empreintes et remplaçants `[À CONFIRMER]`.
- **État :** historical_intent
- **Sujet littéral :** archive/documents/README.md — statut des payloads
- **Temps du fait :** 2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/README.md:15
- **Citation / observation :** `Les fichiers sous files/ sont des payloads historiques immuables` ; `remplaçants [À CONFIRMER]`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le statut immuable est vérifié pour la baseline, mais le remplaçant de chaque document n’est pas établi.

### CLM-AUD-006-706

- **Statement :** Le README du snapshot déclare que les neuf fichiers proviennent du dépôt `SRC-SOS`, du commit complet `43b0964d7bace22abf2cfad32baaf1b449889687`, extraits le 2026-08-25 avec `git show`, la source courante étant laissée intacte.
- **État :** historical_execution
- **Sujet littéral :** archive/documents/obsidian-snapshot-43b0964/README.md — provenance
- **Temps du fait :** 2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/README.md:9-17
- **Citation / observation :** `dépôt source : SRC-SOS` ; `commit complet : 43b0964d7bace22abf2cfad32baaf1b449889687` ; `extraction : 2026-08-25 avec git show` ; `source courante : laissée intacte`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La provenance et l’alignement des blobs sont vérifiés depuis la baseline ; le dépôt Obsidian source n’est pas ouvert.

### CLM-AUD-006-708

- **Statement :** Le README du snapshot avertit que la présence des neuf fichiers dans le commit de backup ne prouve pas leur validation par Sofian.
- **État :** historical_intent
- **Sujet littéral :** archive/documents/obsidian-snapshot-43b0964/README.md — limite de validation
- **Temps du fait :** 2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/README.md:19-21
- **Citation / observation :** `Leur présence dans le commit de backup ne prouve pas leur validation par Sofian.`
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le corpus fermé ne contient pas les messages utilisateur permettant de qualifier une éventuelle validation.

### CLM-AUD-006-709

- **Statement :** `Jarvis Agent.md` se présente comme un projet `Jarvis Agent` `in_progress`, priorité `high`, planifié le 2026-06-27, avec la mission d’en faire un master agent personnel.
- **État :** historical_intent
- **Sujet littéral :** Jarvis Agent.md — identité et mission
- **Temps du fait :** 2026-06-27
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis Agent.md:1-25
- **Citation / observation :** Frontmatter : `title: Jarvis Agent`, `status: in_progress`, `priority: high`, `scheduled_date: 2026-06-27` ; `Mission : Transformer Jarvis ... en master agent de vie`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Statut de projet historique ; ne prouve pas l’activité actuelle ni l’acceptation du résultat attendu.

### CLM-AUD-006-710

- **Statement :** Le périmètre déclaré de `Jarvis Agent.md` vise mémoire persistante, proactivité, connexion aux systèmes, patterns ADHD et documentation automatique, avec Sofian comme unique utilisateur et une configuration OpenCode comme livrable.
- **État :** historical_intent
- **Sujet littéral :** Jarvis Agent.md — périmètre déclaré
- **Temps du fait :** 2026-06-27
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis Agent.md:46-70
- **Citation / observation :** Résultats attendus : `Mémoire persistante`, `proactif`, `lire/écrire dans tous les systèmes`, patterns ADHD, documentation ; livrable `Configuration OpenCode + skills + MCP + hooks + projet Obsidian documenté`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Objectifs et solution historique déclarés ; aucune preuve de réalisation, permission ou usage opérationnel dans ce payload.

### CLM-AUD-006-711

- **Statement :** Le projet `Jarvis Agent.md` déclare `Hermes` comme runtime agentique actuel et présente les artefacts OpenCode comme des sources à réconcilier.
- **État :** historical_intent
- **Sujet littéral :** Jarvis Agent.md — runtime déclaré
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis Agent.md:39-44
- **Citation / observation :** `Runtime agentique actuel : Hermes ; les anciens artefacts OpenCode restent des sources à réconcilier, pas le workspace actif`.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-006-712"]
- **Review :** accepted
- **Limite :** La formulation est interne au snapshot ; elle n’établit pas le runtime live hors de ce workstream.

### CLM-AUD-006-712

- **Statement :** Dans le même payload, la section Stack indique `Agent runner | OpenCode v1.17.11`, ce qui contredit ou rend temporellement ambigu le runtime `Hermes` déclaré comme actuel.
- **État :** contradicted
- **Sujet littéral :** Jarvis Agent.md — divergence Hermes/OpenCode
- **Temps du fait :** snapshot_2026-08-25
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis Agent.md:103-112
- **Citation / observation :** Stack : `Agent runner | OpenCode v1.17.11` ; comparaison avec la déclaration `Runtime agentique actuel : Hermes` aux lignes 39-44.
- **Confiance :** high
- **Contradictions :** ["CLM-AUD-006-711"]
- **Review :** accepted
- **Limite :** Contradiction interne non résolue ; ne pas choisir silencieusement un runtime actuel.

### CLM-AUD-006-713

- **Statement :** Le journal du projet rapporte au 2026-08-22 un workspace applicatif unique pour Jarvis et un premier parcours vertical `Mail → Clarify → proposition de TaskNote → accord humain → création vérifiée → Daily Review`, tandis que Capture iOS et Daily Review sont indiqués comme briques suivantes.
- **État :** historical_intent
- **Sujet littéral :** Jarvis Agent.md — lot actif historique
- **Temps du fait :** 2026-08-22
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis Agent.md:119-124,145-147
- **Citation / observation :** `workspace de build canonique ... jarvis` ; `Premier parcours vertical : un compte Mail → Clarify → proposition de TaskNote → accord humain → création vérifiée → Daily Review` ; `B1 Gateway + NATS n'est plus le prochain lot`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Journal et intention datés ; aucune exécution réelle ni état actuel n’est prouvé par ce payload.

### CLM-AUD-006-714

- **Statement :** `Jarvis — Socle v0.1.md` définit comme mission un brief à la demande, en lecture seule, depuis Sofian OS et TaskNotes, limité à trois priorités avec provenance, conflits visibles et proposition d’action.
- **État :** historical_intent
- **Sujet littéral :** Jarvis — Socle v0.1.md — mission
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis — Socle v0.1.md:21-43
- **Citation / observation :** `brief ... utile, fiable et vérifiable` ; `Sofian OS + TaskNotes` en lecture ; `3 priorités maximum` ; `provenance` ; `conflits visibles` ; `proposition d’action`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Spécification historique ; ne prouve pas une commande implémentée ou exercée.

### CLM-AUD-006-715

- **Statement :** Le périmètre du socle inclut la lecture des projets et tâches canoniques, le brief à la demande, trois priorités maximum, la provenance et des états explicites pour indisponibilité ou conflit ; il exclut cron, proactivité, mémoire complète, nouvelles bases et plusieurs systèmes externes obligatoires.
- **État :** historical_intent
- **Sujet littéral :** Jarvis — Socle v0.1.md — inclusions et exclusions
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis — Socle v0.1.md:47-67
- **Citation / observation :** Inclus : `afficher non établi, indisponible ou un conflit` ; hors périmètre : `cron`, `architecture complète de Jarvis Memory`, `Gmail, Calendar, Finance OS ou ourmem`, `nouveau stockage`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Définition de portée historique ; aucune preuve que les contraintes ont été respectées par une implémentation.

### CLM-AUD-006-716

- **Statement :** La Definition Of Done du socle demande un contrat de sortie, une commande à la demande, au plus trois priorités, provenance/certitude, visibilité des conflits et trois scénarios réels, mais toutes les cases sont non cochées dans le payload.
- **État :** historical_intent
- **Sujet littéral :** Jarvis — Socle v0.1.md — DoD et scénarios
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Projects/Jarvis — Socle v0.1.md:84-101
- **Citation / observation :** DoD : cases `[ ]` pour commande, trois priorités, provenance, conflits, mutation et trois scénarios ; scénarios `Journée normale`, `État contradictoire`, `Source indisponible ou preuve absente`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les cases non cochées indiquent l’état du document, pas la preuve qu’aucun travail n’a été réalisé ailleurs.

### CLM-AUD-006-717

- **Statement :** `Sofian Ecosystem - Architecture Niveau 0.md` présente une carte de la vie de Sofian avant les systèmes numériques et affirme que sa base de travail a été validée par Sofian le 20 août 2026 sans créer d’Area, d’OS ou de déplacement de données.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem - Architecture Niveau 0.md — rôle et validation déclarée
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Architecture Niveau 0.md:18-27
- **Citation / observation :** `la vie réelle de Sofian avant les systèmes numériques` ; `Base de travail Niveau 0 validée par Sofian le 20 août 2026` ; `ne crée aucune nouvelle Area, aucun nouvel OS et ne déplace aucune donnée`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La validation est une déclaration du payload ; aucun message utilisateur direct n’est présent dans le corpus fermé.

### CLM-AUD-006-718

- **Statement :** La carte Niveau 0 organise la vie en neuf domaines répartis dans trois familles : Soi et liens ; Développement et contribution ; Sécurité et environnement.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem - Architecture Niveau 0.md — neuf domaines
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Architecture Niveau 0.md:31-79,92-104
- **Citation / observation :** Carte listant neuf domaines : Santé & équilibre ; Famille & relations ; Logement & cadre de vie ; Études & apprentissage ; Carrière, travail & entreprise ; Création & expression ; Finances personnelles ; Droits, identité & protections ; Environnement numérique & fabrication.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Structure historique ; ne prouve pas qu’elle reste acceptée ou utilisée aujourd’hui.

### CLM-AUD-006-719

- **Statement :** La carte Niveau 0 distingue domaine de vie, projet, capacité transverse et système/outil, et affirme qu’un projet peut traverser plusieurs domaines sans créer de copie par domaine.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem - Architecture Niveau 0.md — frontières
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Architecture Niveau 0.md:83-88,139-157
- **Citation / observation :** `Un domaine de vie est une responsabilité durable` ; `Un projet est temporaire et peut traverser plusieurs domaines` ; `Aucun ... déplacement de données`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Principe de modélisation historique ; ne constitue pas une décision utilisateur indépendante du document.

### CLM-AUD-006-720

- **Statement :** `Sofian Ecosystem - Capacités Transverses.md` sépare domaine, capacité, entité, routine, système et outil, et refuse qu’une capacité devienne automatiquement un workflow, un module, une application, une équipe, un Bot ou un OS.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem - Capacités Transverses.md — distinction centrale
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Capacités Transverses.md:18-42
- **Citation / observation :** Table conceptuelle `Domaine → ... Capacité → ... Système → ... Outil` ; `Une capacité ne devient pas automatiquement un workflow, un module, une application, une équipe, un Bot ou un OS`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Carte conceptuelle historique ; n’établit pas l’architecture actuelle.

### CLM-AUD-006-721

- **Statement :** La carte des capacités décrit quatre familles et dix capacités : Capturer ; Clarifier & qualifier ; Transformer en engagement ; Organiser & planifier ; Exécuter & faire avancer ; Conserver & retrouver ; Coordonner & suivre ; Revoir & réaligner ; Décider & gouverner ; Améliorer progressivement.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem - Capacités Transverses.md — quatre familles et dix capacités
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Capacités Transverses.md:46-78,84-97
- **Citation / observation :** Carte synthétique : `1. Faire entrer & qualifier`, `2. Transformer & agir`, `3. Maintenir la continuité`, `4. Piloter l’évolution` ; registre des dix capacités.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Noms et frontières sont documentés dans le snapshot ; aucun canon actuel ni décision utilisateur directe n’est consulté ici.

### CLM-AUD-006-722

- **Statement :** La carte des capacités pose cinq invariants transverses : arbitrage humain, autorité explicite, résultat vérifiable, faible friction cognitive et réversibilité proportionnée.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem - Capacités Transverses.md — invariants
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Capacités Transverses.md:192-198
- **Citation / observation :** Registre `Invariants Transverses` : `Arbitrage humain`, `Autorité explicite`, `Résultat vérifiable`, `Faible friction cognitive`, `Réversibilité proportionnée`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Invariants déclarés ; le payload ne prouve pas leur mise en œuvre ni leur exercice sur un cas réel.

### CLM-AUD-006-723

- **Statement :** La carte des capacités affirme avoir été validée par Sofian le 20 août 2026 comme base de travail, tout en différant les systèmes, les sources de vérité détaillées, les contrats et le niveau d’autonomie de Jarvis.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem - Capacités Transverses.md — validation déclarée et différés
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Capacités Transverses.md:232-259
- **Citation / observation :** `Sofian a validé cette carte comme base de travail le 20 août 2026` ; `Elle ne valide pas encore les systèmes ... contrats ni le niveau d’autonomie de Jarvis`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune preuve utilisateur directe n’est incluse ; le mot `validée` reste une assertion historique à contre-vérifier.

### CLM-AUD-006-724

- **Statement :** `Sofian Ecosystem - Systèmes et Autorité des Faits.md` pose que l’autorité appartient à un fait précis et qu’une projection doit conserver provenance et chemin de correction.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem - Systèmes et Autorité des Faits.md — règle centrale
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Systèmes et Autorité des Faits.md:19-43
- **Citation / observation :** `L’autorité appartient à un fait précis` ; `Une copie doit être identifiable comme projection, avec sa provenance et son chemin de correction`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Règle d’architecture déclarée ; les autorités réelles ne sont pas démontrées par ce document seul.

### CLM-AUD-006-725

- **Statement :** La matrice de ce document attribue historiquement à Sofian les intentions/consentements, à Sofian OS les projets et engagements enregistrés, à TaskNotes l’état des tâches, aux systèmes spécialisés leurs faits persistés et à Hermes/Jarvis ses sessions, jobs, traces et mémoires agentiques.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem - Systèmes et Autorité des Faits.md — matrice d’autorité
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Systèmes et Autorité des Faits.md:47-59
- **Citation / observation :** Table `Frontières Des Systèmes` : `Sofian`, `Sofian OS`, `TaskNotes`, `Finance OS`, `Homelab-OS`, `Runtime technique`, `Hermes / Jarvis`, `Services et documents externes`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** La matrice est explicitement une base historique ; elle ne prouve ni accès, fraîcheur, permissions ni contrat actuel.

### CLM-AUD-006-726

- **Statement :** Le document conserve comme autorités non établies les clients, missions commerciales, devis, factures émises, rapprochement facture-paiement, plusieurs preuves externes actuelles, le contrat Sofian OS ↔ Jarvis et l’architecture détaillée de Jarvis Memory.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem - Systèmes et Autorité des Faits.md — trous d’autorité
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Resources/Sofian Ecosystem - Systèmes et Autorité des Faits.md:158-172
- **Citation / observation :** Section `Autorités Non Établies` ; `Ces trous ne justifient pas la création d’un Business OS, d’un Health OS, d’une nouvelle base ou d’un bus d’événements`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Absence et non-établissement sont ceux du snapshot ; ils ne prouvent pas l’absence actuelle.

### CLM-AUD-006-728

- **Statement :** La TaskNote historique `Jarvis Socle v0.1 - Construire le brief en lecture seule` est `todo` et définit un outcome de commande à la demande lisant Sofian OS et TaskNotes et retournant trois priorités vérifiables.
- **État :** historical_intent
- **Sujet littéral :** Jarvis Socle v0.1 - Construire le brief en lecture seule.md — tâche
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Tasks/Jarvis Socle v0.1 - Construire le brief en lecture seule.md:1-24
- **Citation / observation :** Frontmatter `status: todo`, `priority: high` ; outcome `commande Jarvis ... lit Sofian OS et TaskNotes ... trois priorités maximum`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Copie secondaire d’une TaskNote ; le statut historique ne prouve pas le statut de la TaskNote canonique.

### CLM-AUD-006-730

- **Statement :** La TaskNote historique `Jarvis Socle v0.1 - Spécifier le contrat du brief` est `in_progress`, planifiée le 2026-08-20, et vise un contrat court, déterministe et testable avant implémentation.
- **État :** historical_intent
- **Sujet littéral :** Jarvis Socle v0.1 - Spécifier le contrat du brief.md — tâche
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Tasks/Jarvis Socle v0.1 - Spécifier le contrat du brief.md:1-20
- **Citation / observation :** Frontmatter `status: in_progress`, `scheduled_date: 2026-08-20` ; outcome `contrat de sortie court, déterministe et testable`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** État d’une copie historique ; aucun progrès actuel ni acceptation n’est prouvé.

### CLM-AUD-006-731

- **Statement :** Le contrat historique demande pour chaque priorité une action, une raison, un projet/contexte, la source canonique et le chemin, un niveau de certitude et une prochaine action, tout en limitant les sources obligatoires à Sofian OS et TaskNotes et en gardant la DoD non cochée.
- **État :** historical_intent
- **Sujet littéral :** Jarvis Socle v0.1 - Spécifier le contrat du brief.md — contrat déclaré
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Tasks/Jarvis Socle v0.1 - Spécifier le contrat du brief.md:22-48
- **Citation / observation :** Champs : `action visible`, `raison`, `projet ou contexte`, `source canonique et chemin`, niveaux `confirmé`, `non établi`, `indisponible`, `conflit`, `prochaine action proposée` ; DoD six cases `[ ]`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Contrat documenté et non démontré par une exécution ; aucune source canonique live n’est ouverte.

### CLM-AUD-006-732

- **Statement :** La TaskNote historique `Jarvis Socle v0.1 - Tester trois scénarios réels` est `todo` et vise l’acceptation du brief sur trois situations sans masquer conflit, preuve manquante ou indisponibilité.
- **État :** historical_intent
- **Sujet littéral :** Jarvis Socle v0.1 - Tester trois scénarios réels.md — tâche
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Tasks/Jarvis Socle v0.1 - Tester trois scénarios réels.md:1-24
- **Citation / observation :** Frontmatter `status: todo` ; outcome `Le brief est accepté sur trois situations réelles` sans masquer `conflit`, `preuve manquante` ou `indisponibilité`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Le mot `accepté` appartient à l’outcome visé ; il ne documente pas une acceptation réalisée.

### CLM-AUD-006-733

- **Statement :** La TaskNote historique définit les trois scénarios : journée normale, état contradictoire et source indisponible ou preuve absente, avec résultat attendu et exécutions rejouables ; sa DoD reste entièrement non cochée.
- **État :** historical_intent
- **Sujet littéral :** Jarvis Socle v0.1 - Tester trois scénarios réels.md — scénarios et DoD
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/98-Backend/Tasks/Jarvis Socle v0.1 - Tester trois scénarios réels.md:26-38
- **Citation / observation :** Scénarios `Journée normale`, `État contradictoire`, `Source indisponible ou preuve absente` ; cinq cases `[ ]` de DoD.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Aucune sortie d’exécution, fixture ou preuve utilisateur n’est incluse dans ce payload.

### CLM-AUD-006-734

- **Statement :** `Sofian Ecosystem Architecture.md` se présente comme un point de reprise persistant pour Sofian Ecosystem / Sofian OS / Jarvis OS, mais précise qu’il ne remplace pas les notes canoniques et doit charger les détails juste à temps.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem Architecture.md — rôle du handoff
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/99-System/AI Handoffs/Sofian Ecosystem Architecture.md:12-23
- **Citation / observation :** `Point de reprise persistant` ; `ne remplace pas les notes canoniques` ; `doit charger les détails juste à temps`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Handoff historique et secondaire ; sa présence ne prouve ni activation ni exactitude actuelle.

### CLM-AUD-006-735

- **Statement :** Le handoff historique ordonne Domaines → Capacités → Systèmes/ownership → Contrats → Modèles → Implémentation, rapporte les couches de domaines/capacités/systèmes comme validées et garde les contrats, la mémoire détaillée, les automatisations et nouveaux OS différés.
- **État :** historical_intent
- **Sujet littéral :** Sofian Ecosystem Architecture.md — ordre, validations déclarées et différés
- **Temps du fait :** 2026-08-20
- **Temps d’enregistrement :** 2026-08-25
- **Source :** SRC-BASELINE
- **Locator :** files/archive/documents/obsidian-snapshot-43b0964/files/99-System/AI Handoffs/Sofian Ecosystem Architecture.md:38-53,108-124,243-258
- **Citation / observation :** Ordre `1. Domaines ... 6. Implémentation / outils` ; `base de travail validée` ; différés `Contrats`, `Architecture de mémoire`, `Nouveaux OS ...`.
- **Confiance :** high
- **Contradictions :** []
- **Review :** accepted
- **Limite :** Les validations sont rapportées par le handoff, sans message utilisateur direct ; les claims de livraison technique restent au niveau documentaire.

## Claims rejetés ou hors intégration

### Élément 1

- **id :** CLM-AUD-006-001

### Élément 2

- **id :** CLM-AUD-006-002

### Élément 3

- **id :** CLM-AUD-006-003

### Élément 4

- **id :** CLM-AUD-006-004

### Élément 5

- **id :** CLM-AUD-006-005

### Élément 6

- **id :** CLM-AUD-006-006

### Élément 7

- **id :** CLM-AUD-006-007

### Élément 8

- **id :** CLM-AUD-006-008

### Élément 9

- **id :** CLM-AUD-006-009

### Élément 10

- **id :** CLM-AUD-006-010

### Élément 11

- **id :** CLM-AUD-006-011

### Élément 12

- **id :** CLM-AUD-006-012

### Élément 13

- **id :** CLM-AUD-006-013

### Élément 14

- **id :** CLM-AUD-006-014

### Élément 15

- **id :** CLM-AUD-006-015

### Élément 16

- **id :** CLM-AUD-006-100

### Élément 17

- **id :** CLM-AUD-006-101

### Élément 18

- **id :** CLM-AUD-006-102

### Élément 19

- **id :** CLM-AUD-006-103

### Élément 20

- **id :** CLM-AUD-006-104

### Élément 21

- **id :** CLM-AUD-006-105

### Élément 22

- **id :** CLM-AUD-006-106

### Élément 23

- **id :** CLM-AUD-006-107

### Élément 24

- **id :** CLM-AUD-006-108

### Élément 25

- **id :** CLM-AUD-006-109

### Élément 26

- **id :** CLM-AUD-006-200

### Élément 27

- **id :** CLM-AUD-006-201

### Élément 28

- **id :** CLM-AUD-006-202

### Élément 29

- **id :** CLM-AUD-006-203

### Élément 30

- **id :** CLM-AUD-006-204

### Élément 31

- **id :** CLM-AUD-006-205

### Élément 32

- **id :** CLM-AUD-006-206

### Élément 33

- **id :** CLM-AUD-006-207

### Élément 34

- **id :** CLM-AUD-006-208

### Élément 35

- **id :** CLM-AUD-006-209

### Élément 36

- **id :** CLM-AUD-006-210

### Élément 37

- **id :** CLM-AUD-006-211

### Élément 38

- **id :** CLM-AUD-006-212

### Élément 39

- **id :** CLM-AUD-006-213

### Élément 40

- **id :** CLM-AUD-006-313

### Élément 41

- **id :** CLM-AUD-006-502

### Élément 42

- **id :** CLM-AUD-006-513

### Élément 43

- **id :** CLM-AUD-006-707

### Élément 44

- **id :** CLM-AUD-006-727

### Élément 45

- **id :** CLM-AUD-006-729

### Élément 46

- **scope :** CLM-AUD-006-001..015

- **reason :** Contrat V2 incomplet : `quote_or_observation` et `contradicts` absents.

### Élément 47

- **scope :** CLM-AUD-006-100..109

- **reason :** Contrat V2 incomplet : `quote_or_observation`, `contradicts` et `review_status` absents ; CLM-AUD-006-109 a aussi un locator agrégé non atomique.

### Élément 48

- **scope :** CLM-AUD-006-200..213

- **reason :** Contrat V2 incomplet : `limit` absent ; 12/14 sans `contradicts` ; plusieurs décisions reposent sur un résumé de sous-agent au lieu d’un message utilisateur direct.

### Élément 49

- **scope :** CLM-AUD-006-313

- **reason :** Claim agrégé non atomique.

### Élément 50

- **scope :** CLM-AUD-006-502,CLM-AUD-006-513

- **reason :** Niveau `technically_tested` sans sortie de test directe qualifiante.

### Élément 51

- **scope :** CLM-AUD-006-707

- **reason :** Observation corrompue par copie ; source lisible `[À CONFIRMER]`.

### Élément 52

- **scope :** CLM-AUD-006-727

- **reason :** `historical_execution` trop fort sans sortie brute.

### Élément 53

- **scope :** CLM-AUD-006-729

- **reason :** Locator hors limites : plage 26–42 pour un fichier de 41 lignes.

## Provenance

- Synthèse Kanban : `t_3796a3fa`.
- `review_status: accepted` signifie accepté pour ce rapport documentaire, pas `user_accepted` ni `operational`.
- Mutations des sources : `0`.
