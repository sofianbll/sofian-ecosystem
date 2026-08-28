---
id: AUD-005
title: Systèmes et implémentations live — rapport d’audit
status: integrated
date: 2026-08-28
canonical_synthesis_task: t_420c7653
canonical_synthesis_run: 72
accepted_claims: 132
integration_authorized: true
---

# AUD-005 — Systèmes et implémentations live

> **État : `integrated`, contre-audité.** Ce rapport et son ledger sont intégrés au dépôt après validation explicite de Sofian.

## Verdict

AUD-005 est synthétisé au statut `reported` avec 7/7 dossiers couverts : Sofian OS V4 + TaskNotes, Jarvis, Hermes, OpenCode, ourmem, Homelab-OS et Finance OS. Le contrôle mécanique retient 132/141 claims canoniques et en rejette 9 ; aucune preuve ne permet un niveau global `user_accepted` ou `operational`, et les runtimes distants, corrections métier et restaurations restent les limites majeures.

## Ledger exhaustif

Les **132 claims acceptés** et leurs locators sont séparés : [ouvrir le ledger](claims.md).

## Couverture

- **expected :** 7
- **inspected :** 7
- **excluded :** 0
- **blocked :** 0
- **canonical_claim_candidates :** 141
- **claims_accepted :** 132
- **claims_rejected :** 9
- **systems :**
- **SYS-001 :**
- **candidate :** 30
- **accepted :** 30
- **rejected :** 0
- **SYS-002 :**
- **candidate :** 26
- **accepted :** 24
- **rejected :** 2
- **SYS-003 :**
- **candidate :** 24
- **accepted :** 20
- **rejected :** 4
- **SYS-004 :**
- **candidate :** 13
- **accepted :** 12
- **rejected :** 1
- **SYS-005 :**
- **candidate :** 12
- **accepted :** 12
- **rejected :** 0
- **SYS-006 :**
- **candidate :** 14
- **accepted :** 13
- **rejected :** 1
- **SYS-007 :**
- **candidate :** 22
- **accepted :** 21
- **rejected :** 1

## Systèmes

### Élément 1

- **id :** SYS-001

- **name :** Sofian OS V4 + TaskNotes

- **status :** current

- **audit_state :** reported

- **source_card :** t_ae316e9a

- **accepted_claim_count :** 30

- **verdict :** Système personnel documenté avec Obsidian comme implémentation actuelle et TaskNotes comme autorité déclarée des tâches ; aucune exécution récente, acceptation ou utilisation maintenue n’est prouvée.

- **boundaries :**

- **owns :**
- règles documentaires V4
- état des tâches dans les notes TaskNotes
- routines et commandes documentées
- **does_not_own :**
- preuve d’usage
- runtime Obsidian/TaskNotes/Bases
- tokens ou données sensibles de tasknotes/data.json

- **authorities :**

### Élément 1

- **fact :** état des tâches

- **authority :** TaskNotes / notes Markdown sous 98-Backend/Tasks

- **correction :** commandes TaskNotes Create, Schedule, Start, Complete, Drop, Reschedule

### Élément 2

- **fact :** règles V4

- **authority :** Architecture Référence et Workflows

- **correction :** source documentaire après décision

### Élément 3

- **fact :** vues

- **authority :** Queries/Bases/Dashboards comme projections

- **correction :** corriger la note/commande autoritaire, pas la vue

- **contracts :**

- Capture → Clarify → Task/Project/Resource/Aspiration
- Commands modifient ; Queries/Dashboards lisent
- Operating routines → commandes TaskNotes

- **permissions_risks :**

- tasknotes/data.json exclu car sensible
- mapping réel, divergence de projections et récupération non vérifiés

- **delivery :**

- **verified :**
- documentation V4, schéma, workflows et routines lisibles
- **not_proven :**
- prototyped
- technically_tested
- integrated
- exercised_real_case
- user_accepted
- operational

- **contradictions :**

- scheduled_date optionnel versus défaut today
- finished_date versus completed_date

- **unknowns :**

- conformité du runtime aux règles
- usage des routines
- procédure de correction d’une projection

### Élément 2

- **id :** SYS-002

- **name :** Jarvis

- **status :** current

- **audit_state :** reported

- **source_card :** t_01bad240

- **accepted_claim_count :** 24

- **verdict :** Couche agentique documentée ; le code observé est un prototype Python déterministe et read-only qui produit des propositions JSON sans writer externe.

- **boundaries :**

- **owns :**
- code, règles déterministes, contrats et propositions Jarvis
- **does_not_own :**
- mail autoritaire
- état TaskNotes
- projets et engagements
- runtime externe

- **authorities :**

### Élément 1

- **fact :** code et contrats

- **authority :** dépôt Jarvis

- **correction :** dépôt après accord

### Élément 2

- **fact :** message

- **authority :** Mail

- **correction :** Mail

### Élément 3

- **fact :** tâche

- **authority :** Sofian OS / TaskNotes

- **correction :** TaskNotes après autorisation

### Élément 4

- **fact :** proposition/orchestration

- **authority :** Jarvis

- **correction :** code et contrat Jarvis

- **contracts :**

- fixture/export mail → proposition
- Inbox Item → clarify-next
- proposition → futur adaptateur TaskNotes
- propositions → Daily Review documentée

- **permissions_risks :**

- prototype lu comme read-only
- absence de packaging/CI et dépôt sans commit vérifiable
- heuristiques mail et connecteurs non exercés

- **delivery :**

- **verified :**
- documented
- prototyped pour mail-to-task et clarify-next
- **not_proven :**
- technically_tested courant
- integrated
- exercised_real_case
- user_accepted
- operational

- **contradictions :**

- cinq dispositions mail documentées versus deux sorties implémentées

- **unknowns :**

- owner explicite
- tests courants
- connexion mail réelle
- déduplication et écriture TaskNotes
- intégration Daily Review/iOS

### Élément 3

- **id :** SYS-003

- **name :** Hermes Agent

- **status :** current

- **audit_state :** reported

- **source_card :** t_39ebd5e9

- **accepted_claim_count :** 20

- **verdict :** Runtime/interface agentique techniquement présent ; il possède les surfaces techniques de conversation, sessions, outils, profils et jobs, mais pas l’état métier des projets et tâches.

- **boundaries :**

- **owns :**
- sessions et historique Hermes
- définitions/tentatives Cron
- configuration et profils
- orchestration technique
- **does_not_own :**
- état métier Sofian OS/TaskNotes
- validation de la cible
- sources métier externes

- **authorities :**

### Élément 1

- **fact :** historique conversationnel

- **authority :** SessionDB / state.db

- **correction :** session_search, resume, export documenté

### Élément 2

- **fact :** définition Cron

- **authority :** jobs.json via cronjob/CLI

- **correction :** cronjob ou hermes cron

### Élément 3

- **fact :** tentative Cron

- **authority :** executions.db

- **correction :** réconciliation ; unknown non relancé automatiquement

### Élément 4

- **fact :** paramètres

- **authority :** interfaces config/profil

- **correction :** hermes config set et commandes profile

### Élément 5

- **fact :** projets/tâches métier

- **authority :** Sofian-OS / TaskNotes

- **correction :** hors Hermes

- **contracts :**

- SessionDB et session_search
- Cron séparé avec historique d’exécution
- ACP/TUI/API documentés mais non exercés
- toolsets/backends et profils isolés

- **permissions_risks :**

- redaction par défaut et secrets séparés de la configuration
- backend local et sudo désactivé au snapshot
- gateway running mais supervision launchd non alignée
- écart possible docs officielles/runtime local

- **delivery :**

- **verified :**
- installation locale et CLI observées
- sessions documentées
- Cron configuré observé
- profil default observé
- **not_proven :**
- niveau produit global
- API/ACP/TUI exercés
- user_accepted
- operational pour chaque surface

- **contradictions :**

- gateway actif versus gestion launchd
- documentation possiblement plus récente que v0.20.6

- **unknowns :**

- memory.provider et relation ourmem
- disponibilité exacte API/ACP/TUI dans v0.20.6
- résilience du gateway
- parcours réel complet

- **normalization_limits :**

- CLM-AUD-005-210,217,223,224 rejetés par R3

### Élément 4

- **id :** SYS-004

- **name :** OpenCode

- **status :** current

- **audit_state :** reported

- **source_card :** t_c4648be3

- **accepted_claim_count :** 12

- **verdict :** Source canonique d’un historique OpenCode multi-agents et multi-projets ; le service OpenCode/OpenChamber actuel, son writer runtime et son contrat courant restent inconnus.

- **boundaries :**

- **owns :**
- sessions, messages, parts et métadonnées OpenCode
- **does_not_own :**
- état actuel des processus
- projets/tâches personnels
- validation utilisateur

- **authorities :**

### Élément 1

- **fact :** sessions/messages/parts

- **authority :** /Users/sofian/.local/share/opencode/opencode.db

- **correction :** relecture read-only par helper et ID

### Élément 2

- **fact :** index de recherche

- **authority :** index dérivé

- **correction :** ne jamais le traiter comme source canonique

### Élément 3

- **fact :** runtime OpenCode/OpenChamber

- **authority :** inconnue dans ce dossier

- **correction :** contrôle live séparé

### Élément 4

- **fact :** tâches personnelles

- **authority :** Sofian-OS / TaskNotes

- **correction :** hors OpenCode

- **contracts :**

- base → opencode_history.py
- session → message → part
- OpenChamber → OpenCode historique
- traces OpenCode → systèmes personnels sans transfert d’autorité

- **permissions_risks :**

- base lue en mode read-only
- messages privés minimisés
- index stale et extraits potentiellement incomplets

- **delivery :**

- **verified :**
- base et schéma réellement interrogés
- historique architectural documenté
- **not_proven :**
- service actuel intégré
- user_accepted
- operational

- **contradictions :**

- index dérivé 1601 versus source canonique 1609
- architecture historique versus configuration actuelle inconnue

- **unknowns :**

- runtime actuel
- writer exact
- contrat OpenCode–OpenChamber–Jarvis/Hermes

### Élément 5

- **id :** SYS-005

- **name :** ourmem

- **status :** current

- **audit_state :** reported

- **source_card :** t_16f7c740

- **accepted_claim_count :** 12

- **verdict :** Mémoire persistante self-hosted documentée et partiellement lisible via MCP ; la recherche sémantique a échoué et le déploiement/runtime maintenu n’est pas prouvé.

- **boundaries :**

- **owns :**
- mémoires, profil et statistiques selon le contrat ourmem
- **does_not_own :**
- projets/tâches TaskNotes
- décision finale
- sources métier canoniques

- **authorities :**

### Élément 1

- **fact :** définition de service

- **authority :** compose Homelab-OS courant

- **correction :** compose et secret externe après accord

### Élément 2

- **fact :** mémoires servies

- **authority :** API ourmem derrière MCP

- **correction :** memory_update/memory_forget documentés, non exercés

### Élément 3

- **fact :** préférences et décisions personnelles

- **authority :** source canonique ou décision explicite

- **correction :** source propriétaire, pas projection ourmem

### Élément 4

- **fact :** intégration OpenCode

- **authority :** configuration effective non résolue

- **correction :** client effectif

- **contracts :**

- MCP stats/profile/list accessibles
- MCP search dépend du fournisseur d’embeddings
- build d’image déclaré vers GHCR
- montage runtime hors dépôt
- plugin OpenCode historique non confirmé

- **permissions_risks :**

- modèle API key/Spaces documenté mais ACL effectives non relues
- identifiants sensibles observés dans un compose sans reproduire les valeurs
- backup, rotation et rollback non vérifiés

- **delivery :**

- **verified :**
- configuration documentée
- lectures MCP réelles bornées
- recherche réelle échouée
- **not_proven :**
- intégration OpenCode
- service maintenu operational
- user_accepted

- **contradictions :**

- lectures MCP réussies versus recherche bloquée
- note Void planifiée versus compose Nova courant
- politique secrets externes versus valeurs concrètes dans le compose

- **unknowns :**

- conteneur/version/digest réellement déployés
- writer runtime
- backup/restore
- résolution du quota embeddings

### Élément 6

- **id :** SYS-006

- **name :** Homelab-OS

- **status :** current

- **audit_state :** reported

- **source_card :** t_03983e70

- **accepted_claim_count :** 13

- **verdict :** Control repo courant de configuration et documentation ; les contrats et artefacts déclaratifs sont présents, mais aucun runtime distant ni usage maintenu n’a été vérifié.

- **boundaries :**

- **owns :**
- layout, bootstrap, déclarations Compose, documentation et politiques versionnées
- **does_not_own :**
- volumes Data
- secrets
- état/logs des conteneurs
- backups réels

- **authorities :**

### Élément 1

- **fact :** layout et bootstrap

- **authority :** AGENTS/README/66/67 et bootstrap-linux.sh

- **correction :** source Git après décision

### Élément 2

- **fact :** stacks

- **authority :** `docker/stacks/<machine>/<service>/compose`

- **correction :** source Compose puis déploiement contrôlé

### Élément 3

- **fact :** dotfiles

- **authority :** yadm selon canon courant

- **correction :** source dotfiles

### Élément 4

- **fact :** runtime

- **authority :** Docker/Dockhand sur la machine

- **correction :** réconciliation runtime ↔ Git

### Élément 5

- **fact :** données/secrets

- **authority :** ~/Data sur les machines

- **correction :** service/opérateur, jamais Git

- **contracts :**

- Git → bootstrap Linux
- Git → Docker/Dockhand
- services → Caddy/Tailscale/Cloudflare
- runtime → Restic/backup documenté

- **permissions_risks :**

- working tree non propre et stacks non suivies
- Dockhand peut potentiellement écrire les stacks et contrôler Docker
- sockets Docker root-equivalent
- restauration/RPO/RTO non prouvés

- **delivery :**

- **verified :**
- documentation et artefacts déclaratifs présents
- bootstrap et Compose comme implémentation statique
- **not_proven :**
- déploiement
- restauration exercée
- operational

- **contradictions :**

- zéro port hôte versus bindings déclarés
- yadm/bootstrap courant versus chezmoi/Ansible historique
- politique secrets externes versus compose ourmem

- **unknowns :**

- writer exact des stacks
- état Docker/services
- backup/restauration
- politique réseau acceptée

### Élément 7

- **id :** SYS-007

- **name :** Finance OS

- **status :** current

- **audit_state :** reported

- **source_card :** t_b928e7fd

- **accepted_claim_count :** 21

- **verdict :** Stack PocketBase privé documenté avec importeurs Python/Bash et contrat de données statique ; runtime, données financières, ACL, tests exécutés et correction métier n’ont pas été inspectés.

- **boundaries :**

- **owns :**
- schéma/imports/transactions/documents persistés selon le code
- **does_not_own :**
- source bancaire primaire
- runtime prouvé
- Athena Dashboard
- acceptation utilisateur

- **authorities :**

### Élément 1

- **fact :** schéma

- **authority :** scripts/import_finance.py

- **correction :** contrat source après décision

### Élément 2

- **fact :** fichier bancaire

- **authority :** CSV source sélectionné

- **correction :** corriger/remplacer la source puis réimporter selon workflow à confirmer

### Élément 3

- **fact :** transaction normalisée

- **authority :** PocketBase après import avec CSV comme preuve d’entrée

- **correction :** workflow de rapprochement inconnu

### Élément 4

- **fact :** cashflow prévu

- **authority :** inconnue

- **correction :** aucun writer observé

### Élément 5

- **fact :** document

- **authority :** manifest et fichier local

- **correction :** source/manifest ; procédure opérationnelle inconnue

- **contracts :**

- CSV Revolut/Sumeria → normalisation
- source_uid/id déterministes et unicité
- importeur authentifié → PocketBase
- manifest → documents
- Tailscale déclaré privé

- **permissions_risks :**

- superuser temporaire dans run_import.sh
- ACL PocketBase effectives non relues
- ligne Sumeria invalide potentiellement ignorée
- sémantique de fuseau non spécifiée
- aucune sauvegarde/restauration prouvée

- **delivery :**

- **verified :**
- documentation et implémentation statique présentes
- tests lisibles mais non exécutés
- **not_proven :**
- technically_tested
- integrated
- exercised_real_case
- user_accepted
- operational

- **contradictions :**

- instruction Homelab « pas de suite de tests » versus suite Finance OS
- confidentialité déclarée versus ACL runtime non vérifiées

- **unknowns :**

- runtime Pulsar
- règles PocketBase
- workflow de correction/rapprochement
- writer cashflow_items
- hôte d’exécution de l’import

## Contradictions

- SYS-001 : scheduled_date optionnel versus défaut today ; finished_date versus completed_date.
- SYS-002 : cinq dispositions mail documentées versus deux sorties implémentées.
- SYS-003 : gateway running versus supervision launchd ; documentation et runtime local doivent rester séparés.
- SYS-004 : index dérivé 1601 versus base canonique 1609 ; runtime actuel distinct de l’historique.
- SYS-005/SYS-006 : politique secrets externes versus identifiants présents dans le compose ourmem ; les valeurs ne sont pas reproduites et le doublon CLM-AUD-005-511 est rejeté.
- SYS-006 : zéro port hôte versus bindings déclarés ; yadm actuel versus chezmoi/Ansible historique.
- SYS-007 : règle Homelab « pas de suite de tests » versus suite Finance OS ; confidentialité déclarée versus ACL non relues.
- Aucun désaccord n’est résolu silencieusement et aucun système n’est qualifié d’obsolète.

## Inconnues

- Usage opérationnel maintenu et acceptation explicite de Sofian pour chacun des sept systèmes.
- Writer runtime exact et procédure de correction pour projections TaskNotes, Dockhand/stacks, ourmem, OpenCode/OpenChamber et Finance OS.
- Rôle futur des anciens mécanismes et systèmes ; aucune cible n’est définie ici.
- Backups, restores, RPO/RTO et propriétaires de récupération pour Homelab-OS, ourmem et Finance OS.
- État effectif des ACL PocketBase, du plugin OpenCode ourmem et des runtimes distants exclus.
- Parcours réel complet pour Sofian OS, Jarvis et Hermes.
- Quatre claims SYS-003 doivent être renormalisés avant toute réutilisation future de leur contenu.

## Niveaux de livraison

### Élément 1

- **system :** SYS-001

- **verified :**

- documented

- **not_proven :**

- prototyped
- technically_tested
- integrated
- exercised_real_case
- user_accepted
- operational

### Élément 2

- **system :** SYS-002

- **verified :**

- documented
- prototyped pour deux commandes locales

- **not_proven :**

- technically_tested courant
- integrated
- exercised_real_case
- user_accepted
- operational

### Élément 3

- **system :** SYS-003

- **verified :**

- installation/CLI live
- contrats sessions/Cron/profils documentés
- configuration bornée observée

- **not_proven :**

- niveau produit global
- API/ACP/TUI exercés
- user_accepted
- operational pour chaque surface

### Élément 4

- **system :** SYS-004

- **verified :**

- base et historique interrogés
- architectures historiques documentées

- **not_proven :**

- service actuel intégré
- user_accepted
- operational

### Élément 5

- **system :** SYS-005

- **verified :**

- configuration documentée
- lectures MCP réelles bornées
- recherche réelle échouée

- **not_proven :**

- intégration OpenCode
- service maintenu operational
- user_accepted

### Élément 6

- **system :** SYS-006

- **verified :**

- documentation
- artefacts déclaratifs présents

- **not_proven :**

- déploiement
- restauration exercée
- operational

### Élément 7

- **system :** SYS-007

- **verified :**

- documentation
- implémentation statique
- tests lisibles non exécutés

- **not_proven :**

- technically_tested
- integrated
- exercised_real_case
- user_accepted
- operational

## Santé des sources

### Élément 1

- **source_id :** SRC-OBS-ACTIVE

- **status :** readable_for_bounded_corpus

- **limit :** 5/5 fichiers SYS-001 lus ; runtime, tâches réelles et fichier sensible exclus.

### Élément 2

- **source_id :** SRC-LIVE

- **status :** available_with_scope_limits

- **limit :** Dépôts et configurations ciblés lisibles ; working-tree drift sur Homelab-OS/Jarvis/Finance OS ; aucun runtime distant ni healthcheck.

### Élément 3

- **source_id :** SRC-HERMES

- **status :** available_with_dynamic_limits

- **limit :** session, documentation et CLI ciblés accessibles ; snapshots dynamiques rejetés lorsqu’ils n’étaient pas horodatés précisément.

### Élément 4

- **source_id :** SRC-OPENCODE

- **status :** canonical_db_readable_index_stale

- **limit :** base 1609 sessions lisible en read-only ; index dérivé 1601, aucun rebuild.

### Élément 5

- **source_id :** SRC-OURMEM

- **status :** partially_available

- **limit :** stats/profile/list/resources accessibles ; recherche sémantique bloquée par le fournisseur d’embeddings.

## Vérifications directes

- Carte S1, onze parents et trois enfants aval inspectés avec kanban_show ; la provenance SYS-001 a été corrigée vers t_ae316e9a et t_8a4461cc exclue.
- README, AGENTS, scope, evidence-model, source-registry, subagent-protocol, audit-orchestration, brief AUD-005, template system-dossier et skill-routing lus.
- Références Guide 2026 01, 04, 05, 06, 07 et carte 08 chargées ; frontières, autorités, données, permissions, risques et niveaux traités sans définir de cible.
- R1 et R2 portent deux listes identiques de 112 claims acceptés pour six dossiers ; R3 accepte 20/24 claims SYS-003 et ne contient aucun finding bloquant.
- Agrégation SQLite read-only + jq : 141 IDs canoniques uniques, 132 acceptés, 9 rejetés ; répartition 30+24+20+12+12+13+21 ; aucun ID accepté absent.
- Contrôle du contrat : tous les records acceptés possèdent les 13 champs requis, contradicts est toujours un tableau et les source_id se limitent à SRC-HERMES, SRC-LIVE, SRC-OBS-ACTIVE, SRC-OPENCODE et SRC-OURMEM.
- Aucun secret, valeur sensible ou donnée financière runtime n’a été affiché ; aucun fichier, service, configuration, mémoire, dépôt, test ou appareil n’a été modifié.

## Provenance Kanban

- Synthèse : `t_420c7653` / run `72`.
- Mutations des sources : `0`.
- Intégration au dépôt : oui, après validation explicite de Sofian.
- Aucune cible d’architecture n’est acceptée par ce rapport.
