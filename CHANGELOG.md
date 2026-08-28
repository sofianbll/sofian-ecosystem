---
title: Journal du système documentaire
status: active
date: 2026-08-27
---

# Changelog

## 2026-08-28 — Réconciliation après intégration complète

### Corrigé

- séparation explicite entre synthèse source `reported`, rapport `integrated` et dossier système toujours `reported` ;
- décisions de publication, roadmap, définitions de fin, confidentialité, timeline et handoff alignés sur l’état réel ;
- sept dossiers système rafraîchis depuis les sources live sans promotion d’architecture.

### Ajouté

- gate CI testée qui bloque les motifs évidents de secrets et PII avant la publication ;
- décision actuelle de conserver temporairement le dépôt et GitHub Pages publics ;
- preuves live : Finance OS joignable, Hermes sur Honcho avec gateway supervisé, OpenCode stale et recherche ourmem toujours bloquée.

### Non effectué

- aucune mutation des vaults, TaskNotes, mémoires, bases, services ou dépôts voisins ;
- aucune architecture cible, besoin ou opérationnalité accepté par narration.

## 2026-08-28 — Intégration des audits AUD-002 à AUD-006

### Ajouté

- cinq rapports humains et cinq ledgers séparés : `AUD-002` à `AUD-006` ;
- sept dossiers système au statut `reported` ;
- couverture vérifiée des deux vaults, de 30 sessions OpenCode retenues, de six sessions Hermes, de sept systèmes et de 73 payloads de baseline.

### Vérifié

- claims acceptés : `94`, `83`, `56`, `132` et `94` selon les cinq workstreams ;
- réparations et normalisations explicites, notamment SYS-003 Hermes : 20 claims retenus sur 24 réémis ;
- manifeste baseline `73/73`, sources externes inchangées et absence de secret/PII détectée dans les artefacts intégrés.

### Limites

- index OpenCode dérivé stale et 24 IDs hors cap non individualisés ;
- trois recherches ourmem bloquées avant résultat ;
- aucun payload historique recopié, aucun workflow promu automatiquement et aucune cible, acceptation utilisateur ou opérationnalité déduite.

## 2026-08-28 — Intégration du pilote AUD-001

### Ajouté

- rapport humain `AUD-001` et ledger séparé de 72 claims acceptés ;
- couverture vérifiée de 10 objets sur 10, sans exclusion ni blocage ;
- chronologie, filiation des noms, décisions historiques et contradictions issues du corpus fermé.

### Vérifié

- reviews `R1` et `R2`, réparation de 17 claims, contre-audit `R3` sans finding et contre-vérification Jarvis ;
- séparation entre artefacts `documented`, solutions `proposed` et niveaux non prouvés ;
- aucune mutation de Notion, des vaults Obsidian, de TaskNotes, d’ourmem ou d’un autre système externe.

### Limites

- aucune migration opérationnelle ni filiation continue de bout en bout n’est prouvée ;
- aucune architecture cible, aucun besoin actuel et aucun dossier système ne sont acceptés par cette intégration ;
- la méthode pilote doit encore être revue par Sofian avant généralisation.

## 2026-08-27 — Système d’audit et de conception

### Ajouté

- constitution du dépôt pour les agents ;
- scope consolidé de la conversation ;
- méthode de preuve et registre des sources ;
- catalogue de workstreams et briefs délégables ;
- espaces dédiés aux besoins, architectures, systèmes, workflows et décisions ;
- protocoles de délégation, contre-audit, handoff et confidentialité ;
- templates réutilisables pour chaque type de livrable.

### Décidé

- l’écosystème cible sera dérivé des besoins, jamais supposé à l’avance ;
- le futur VitePress reste privé pendant la construction et la validation ;
- TaskNotes conserve l’autorité des tâches et projets opérationnels ;
- les sources externes restent canoniques et en lecture seule pendant l’audit.

### Archivé

- snapshot byte-for-byte des 73 fichiers du commit initial `e331ee4e0a1006f813cf89f3a5c6f6bb262d2d29` ;
- premier commit d’archive local : `e090180e06ee2f102e4251dbe555a842b9d2eedf`.

### Non effectué

- aucun remote ou push ;
- aucun déploiement ;
- aucune mutation de Notion, Obsidian, TaskNotes, OpenCode, ourmem ou d’un service ;
- aucune installation VitePress ou Node.
