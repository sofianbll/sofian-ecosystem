---
id: AUD-003
title: OpenCode et OpenChamber — rapport d’audit
status: integrated
date: 2026-08-28
canonical_synthesis_task: t_db22ff07
canonical_synthesis_run: 60
accepted_claims: 83
integration_authorized: true
---

# AUD-003 — OpenCode et OpenChamber

> **État : `integrated`, contre-audité.** Ce rapport et son ledger sont intégrés au dépôt après validation explicite de Sofian.

## Verdict

La synthèse source d’AUD-003 a été produite au statut `reported` ; ce rapport est désormais `integrated`. En lecture seule, 6/6 requêtes, 60 résultats, 54 IDs uniques et 30/30 sessions retenues ont été inspectés ; 83/104 claims sont acceptés après normalisation mécanique, 21 rejetés. Le corpus établit une évolution historique d’OpenCode/Jarvis/Sofian OS, sans autoriser la fusion de `Jarvis Agent`, `Jarvis OS`, `Sofian OS`, `Sofian-OS`, `Sofian's Vault`, OpenCode, OpenChamber et Sofian Ecosystem. Limite majeure : l’index reste stale et 24 IDs hors cap ne sont pas individualisés.

## Ledger exhaustif

Les **83 claims acceptés** et leurs locators sont séparés : [ouvrir le ledger](claims.md).

## Couverture

- **expected :** six requêtes + manifeste + sessions retenues
- **inspected :**
- **queries :** 6/6
- **raw_rows :** 60
- **unique_session_ids :** 54
- **selected_manifest :** 30/30
- **parent_claims :** 104/104 classés
- **accepted_claims :** 83
- **rejected_claims :** 21
- **excluded :**
- **sessions :** 24
- **reason :** IDs uniques hors cap pour pertinence thématique/indirecte ou moindre ; la discovery n’a pas conservé leur liste individualisée
- **blocked :** 0

## Chronologie

### Élément 1

- **valid_time :** 2026-06-10

- **event :** Les sessions décrivent historiquement deux composants distincts, OpenCode backend et OpenChamber UI/proxy, ainsi qu’une configuration agents/skills tool-agnostic liée aux dotfiles.

- **state :** historical_execution/historical_intent

- **claims :**

- CLM-AUD-003-621
- CLM-AUD-003-622
- CLM-AUD-003-623
- CLM-AUD-003-624

### Élément 2

- **valid_time :** 2026-06-12

- **event :** Audits Homelab-OS et Sofian-OS : structure, ports, liens, données sensibles et séparation de rôles sont documentés ; plusieurs écarts restent historiques ou proposés.

- **state :** historical_execution/proposed

- **claims :**

- CLM-AUD-003-614
- CLM-AUD-003-615
- CLM-AUD-003-616
- CLM-AUD-003-617
- CLM-AUD-003-618
- CLM-AUD-003-619
- CLM-AUD-003-620
- CLM-AUD-003-633
- CLM-AUD-003-634
- CLM-AUD-003-635
- CLM-AUD-003-636

### Élément 3

- **valid_time :** 2026-06-16

- **event :** Sofian corrige explicitement le lot GitHub/vault : pas de nouveau repo SAS, ne pas déplacer les bootcamps ni toucher aux forks, conserver les archives, règles d’archivage, préfixe `ept-`, statuts Corelab/Codename et renommage `PPLX - Web Query`/`pplx-web-query`.

- **state :** user_decision

- **claims :**

- CLM-AUD-003-327
- CLM-AUD-003-328
- CLM-AUD-003-329
- CLM-AUD-003-330
- CLM-AUD-003-331
- CLM-AUD-003-332
- CLM-AUD-003-333
- CLM-AUD-003-334

### Élément 4

- **valid_time :** 2026-06-19

- **event :** Deux références de skill obsidian-vault sont historiquement créées avec conventions V4.

- **state :** historical_execution/historical_intent

- **claims :**

- CLM-AUD-003-626
- CLM-AUD-003-627

### Élément 5

- **valid_time :** 2026-06-21..2026-06-29

- **event :** Les audits décrivent TaskNotes, Note Toolbar, plugins, architecture V4 et Jarvis `master steward`; les recherches externes subissent des échecs ou restent des hypothèses, et la recommandation de ne pas créer un second task manager n’est pas une décision utilisateur.

- **state :** historical_execution/historical_intent/hypothesis/proposed

- **claims :**

- CLM-AUD-003-003
- CLM-AUD-003-004
- CLM-AUD-003-006
- CLM-AUD-003-300
- CLM-AUD-003-301
- CLM-AUD-003-302
- CLM-AUD-003-303
- CLM-AUD-003-304
- CLM-AUD-003-306
- CLM-AUD-003-307
- CLM-AUD-003-308
- CLM-AUD-003-309
- CLM-AUD-003-310
- CLM-AUD-003-311
- CLM-AUD-003-312
- CLM-AUD-003-313
- CLM-AUD-003-314
- CLM-AUD-003-337
- CLM-AUD-003-338
- CLM-AUD-003-339
- CLM-AUD-003-340
- CLM-AUD-003-341

### Élément 6

- **valid_time :** 2026-07-12..2026-07-14

- **event :** Les audits TaskNotes présentent des dénominateurs contradictoires, puis une revue identifie candidats Engage, tâches non planifiées et blocages historiques, sans prouver l’état courant ni l’usage réel.

- **state :** contradicted/historical_execution/proposed

- **claims :**

- CLM-AUD-003-014
- CLM-AUD-003-628
- CLM-AUD-003-629
- CLM-AUD-003-630
- CLM-AUD-003-631
- CLM-AUD-003-632

### Élément 7

- **valid_time :** 2026-07-20

- **event :** Les collectors Jarvis sont implémentés/revus historiquement : défauts initiaux, corrections déclarées, 14 tests et compilation rapportés ; la revue finale signale encore des risques de confidentialité, de bornes, d’AFK et d’erreurs publiques.

- **state :** historical_execution

- **claims :**

- CLM-AUD-003-007
- CLM-AUD-003-008
- CLM-AUD-003-009
- CLM-AUD-003-010
- CLM-AUD-003-637
- CLM-AUD-003-638
- CLM-AUD-003-639

### Élément 8

- **valid_time :** 2026-07-22

- **event :** Un audit ourmem/OpenCode documente le package `@ourmem/opencode` 0.3.2, les hooks projetés, une activation/configuration historique non établie, des états omem contradictoires et plusieurs options de changement non acceptées.

- **state :** historical_execution/historical_intent/contradicted/proposed

- **claims :**

- CLM-AUD-003-600
- CLM-AUD-003-601
- CLM-AUD-003-602
- CLM-AUD-003-603
- CLM-AUD-003-604
- CLM-AUD-003-605
- CLM-AUD-003-606
- CLM-AUD-003-607

### Élément 9

- **valid_time :** 2026-08-06

- **event :** Sofian demande un audit d’architecture `Jarvis OS`; la réponse propose Obsidian comme adaptateur, TaskNotes comme source des tâches et Jarvis comme routeur/intendant. Cela reste une proposition historique non acceptée.

- **state :** historical_intent/proposed

- **claims :**

- CLM-AUD-003-001
- CLM-AUD-003-002

### Élément 10

- **valid_time :** 2026-08-28

- **event :** Les fichiers collectors, tests et SKILL.md sont présents. Les sources actuelles distinguent `Jarvis Agent` avec Hermes comme runtime actuel des artefacts OpenCode historiques ; `Jarvis OS` et son contrat avec Sofian OS restent non établis.

- **state :** live_implementation/current review

- **claims :**

- CLM-AUD-003-011
- CLM-AUD-003-012
- CLM-AUD-003-013

- **review_source :** t_7fad95c0

## Noms et relations

### Élément 1

- **name :** Sofian OS

- **status :** current_canon

- **relation :** système/projet cockpit décisionnel documenté dans le vault actif

- **evidence :** t_7fad95c0 direct check du projet Sofian OS et filiation AUD-002

### Élément 2

- **name :** Sofian-OS

- **status :** current_canon

- **relation :** vault/repo actif qui implémente et documente Sofian OS ; orthographe/path distincts

- **evidence :** t_7fad95c0 direct check AGENTS.md

### Élément 3

- **name :** Sofian's Vault

- **status :** historical

- **relation :** ancien vault et racine Git indépendante ; migration documentaire sélective vers Sofian-OS

- **evidence :** t_43a8915a + t_7fad95c0 filiation AUD-002

### Élément 4

- **name :** Jarvis Agent

- **status :** current_canon

- **relation :** projet agentique courant ; workspace applicatif Jarvis et runtime Hermes documenté

- **evidence :** t_7fad95c0 direct check Jarvis Agent.md

### Élément 5

- **name :** Jarvis OS

- **status :** unknown

- **relation :** nom d’architecture dans un handoff/brouillon ; alias, renommage et contrat avec Jarvis Agent non établis

- **evidence :** t_7fad95c0 direct check du handoff Sofian Ecosystem Architecture

### Élément 6

- **name :** OpenCode

- **status :** historical_and_source

- **relation :** ancien runtime/outillage Jarvis et source canonique des sessions OpenCode ; runtime Jarvis actuel non prouvé

- **evidence :** CLM-AUD-003-006 et t_7fad95c0 current cross-check

### Élément 7

- **name :** OpenChamber

- **status :** historical_component

- **relation :** UI/proxy distincte d’OpenCode dans l’architecture Homelab historique

- **evidence :** CLM-AUD-003-621..624 et session ses_14e2df203ffekuUz1bqls0KMu7

### Élément 8

- **name :** Sofian Ecosystem

- **status :** current_scope

- **relation :** ombrelle méta couvrant toute la vie ; plus large que Sofian OS ou Jarvis

- **evidence :** t_7fad95c0 direct check du handoff de frontière

## Contradictions

### Élément 1

- **subject :** runtime Jarvis

- **historical :** OpenCode/Jarvis master steward et configuration OpenCode

- **current :** Jarvis Agent.md désigne Hermes comme runtime actuel et OpenCode comme historique

- **resolution :** Préserver les deux temps ; le canon actuel prévaut pour l’actuel.

### Élément 2

- **subject :** Jarvis Agent vs Jarvis OS

- **historical :** Noms utilisés dans des architectures et handoffs

- **current :** Contrat Sofian OS ↔ Jarvis explicitement différé

- **resolution :** Unresolved ; aucune fusion.

### Élément 3

- **subject :** Sofian OS gaps

- **historical :** Bases/Aspiration/Operating manquants ou non testés en juin

- **current :** Projet actuel marque les Bases avancées créées mais conserve validation 7 jours et secrets ouverts

- **resolution :** États successifs ; ne pas présenter les gaps historiques comme actuels.

### Élément 4

- **subject :** lecture vault

- **historical :** W1/W2 rencontrent refus/inaccessibilité

- **current :** R2 relit les fichiers directement

- **resolution :** Limite des workers, pas état du vault.

### Élément 5

- **subject :** OpenCode index/source

- **historical_and_current :** 1 601 indexées contre 1 609 source

- **resolution :** Source health stale ; exhaustivité non revendiquée.

### Élément 6

- **subject :** TaskNotes counts

- **historical :** 18 tâches canoniques / 20 tâches au total et rubrique `Unscheduled Active (4)` avec six lignes

- **resolution :** Dénominateur contradictoire ; ne pas transférer à l’état courant.

### Élément 7

- **subject :** omem runtime

- **historical :** Sain, pausé, down et embedding en échec apparaissent dans des traces différentes

- **resolution :** Contradiction historique non résolue ; aucun runtime interrogé dans AUD-003.

## Inconnues

- Alias ou relation formelle entre `Jarvis Agent` et `Jarvis OS`.
- Contrat exact Sofian OS ↔ Jarvis OS ↔ systèmes spécialisés, explicitement différé.
- État live actuel des déploiements OpenCode/OpenChamber ; aucun healthcheck distant ni service interrogé.
- Usage opérationnel maintenu, cas réel traversé et acceptation utilisateur des workflows Jarvis/Sofian OS.
- Pertinence des huit sessions absentes de l’index et identité des 24 candidats hors cap non individualisés.
- Issue courante des décisions utilisateur historiques de l’inventaire GitHub ; aucun état GitHub vérifié.
- Résultats actuels des tests collectors ; fichiers présents mais aucun test relancé.
- Activation effective du plugin @ourmem/opencode et état runtime omem actuel.
- Décisions/réalisations des sessions dont la réponse finale visible est absente ou tronquée.

## Niveaux de livraison

### Élément 1

- **element :** Base OpenCode comme source d’historique

- **level :** live_implementation

- **proof :** Base canonique lue via helper read-only et stats directes

- **limit :** Ne prouve pas qu’OpenCode soit le runtime Jarvis actuel.

### Élément 2

- **element :** Architecture Jarvis master steward / Jarvis OS

- **level :** proposed/documented historical

- **proof :** CLM-AUD-003-002, CLM-AUD-003-006

- **limit :** Aucune acceptation utilisateur ni identité actuelle établie.

### Élément 3

- **element :** Collectors jarvis-daily-brief

- **level :** documented live artifact

- **proof :** CLM-AUD-003-011..013

- **limit :** Tests verts uniquement rapportés historiquement ; aucun test actuel, intégration ni cas réel exercé.

### Élément 4

- **element :** @ourmem/opencode

- **level :** documented/present package

- **proof :** CLM-AUD-003-601 et check R2

- **limit :** Activation, configuration et fonctionnement runtime inconnus.

### Élément 5

- **element :** OpenCode/OpenChamber Homelab

- **level :** documented historical

- **proof :** CLM-AUD-003-621..624

- **limit :** État live des services non interrogé.

### Élément 6

- **element :** Sofian OS / Sofian-OS

- **level :** current_canon documented

- **proof :** Filiation AUD-002 et checks actuels R2

- **limit :** Canon documentaire ≠ usage opérationnel, cas réel ou acceptation utilisateur.

## Santé des sources

### Élément 1

- **source_id :** SRC-OPENCODE

- **canonical_path :** /Users/sofian/.local/share/opencode/opencode.db

- **mode :** read_only

- **sessions :** 1609

- **messages :** 40619

- **parts :** 186048

- **period :** 2026-06-10T13:56:27.193000+00:00..2026-08-26T18:35:44.329000+00:00

- **source_bytes :** 2019348480

- **index_status :** stale

- **index_sessions :** 1601

- **index_rebuilt :** non

- **tools_payloads_exported :** non

### Élément 2

- **source_id :** SRC-OBS-ACTIVE

- **status :** readable_current_in_R2

- **scope :** Documents canoniques et handoff ciblés ; aucune configuration sensible ouverte.

### Élément 3

- **source_id :** SRC-LIVE

- **status :** partial_current_check

- **scope :** Présence code/skill/package uniquement ; aucun test, runtime ou service exercé.

## Vérifications directes

- README.md, AGENTS.md, scope, evidence model, source registry, protocoles, brief AUD-003, template et instructions locales OpenCode lus.
- Guide 2026 : références 01, 07 et carte 08 lues ; audit operating system relu.
- Les sept handoffs parents et les trois enfants ont été inspectés avant transition.
- `opencode_history.py stats` exécuté directement : 1 609 sessions, 40 619 messages, 186 048 parts, index stale 1 601.
- `show` direct sans tools pour ses_027208599ffe4z7qrsGkVcziTe, ses_07591aad6ffeVMGBQmfWtfLuI3 et ses_0821451bdffeib4pfdYFblX04K.
- Métadonnées W1/W2/W3/R2 relues depuis le board en SQLite immutable/read-only pour l’agrégation mécanique.
- Matérialisation en mémoire des 83 claims : 83 IDs uniques, égalité exacte avec l’acceptation R2, disjonction des 21 rejets, 0 champ absent et 0 champ null.
- Aucun raisonnement caché ni payload tool OpenCode exporté.

## Provenance Kanban

- Synthèse : `t_db22ff07` / run `60`.
- Mutations des sources : `0`.
- Intégration au dépôt : oui, après validation explicite de Sofian.
- Aucune cible d’architecture n’est acceptée par ce rapport.
