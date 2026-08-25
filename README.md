---
status: provisional
date: 2026-08-25
scope: Navigation générale de Sofian Ecosystem — Architecture & Build
sources:
  - indexes/SOURCE-MAP.md
---

# Sofian Ecosystem — Architecture & Build

## Finalité

Ce projet documente comment les systèmes numériques de Sofian coopèrent au service de sa vie. Il conserve les audits, architectures, décisions, états et artefacts issus du chantier **Ultimate Sofian OS — Architect & Build Sofian Life Space** sans remplacer les sources canoniques.

## Périmètre

- registre des systèmes et de leurs responsabilités ;
- parcours quotidiens envisagés ou livrés ;
- décisions confirmées, provisoires, contestées ou remplacées ;
- provenance des documents et artefacts historiques ;
- état vérifié des implémentations.

Ce projet n’est ni une nouvelle base métier, ni un gestionnaire de tâches, ni une copie d’Obsidian, de Git ou des historiques agents.

## État global

**Provisoire.** Le registre documentaire est en construction. Sofian OS et TaskNotes sont opérationnels ; Jarvis ne possède encore aucun parcours quotidien complet livré. La priorité entre Brief, Mail et Daily Start reste non réconciliée.

## Navigation

1. [Registre des systèmes](SYSTEMS.md)
2. [Index des décisions](DECISIONS.md)
3. [Évolution du projet](CHANGELOG.md)
4. [Manifeste des fichiers](indexes/MANIFEST.md)
5. [Carte des sources](indexes/SOURCE-MAP.md)
6. [Contradictions ouvertes](indexes/CONTRADICTIONS.md)
7. [Artefacts accessibles](indexes/ARTIFACTS.md)

## Principes

- une source canonique par fait précis ;
- lecture seule par défaut ;
- aucune mutation sans accord exact et vérification ;
- besoins quotidiens avant outils et infrastructure ;
- petit parcours vertical observable avant automatisation ;
- toute information non vérifiable porte `[À CONFIRMER]`.

## Convention

Les fichiers ordinaires utilisent `kebab-case`. Les index racine utilisent des noms stables en majuscules. Chaque document déclare son statut, sa date, sa portée et ses sources ; toute navigation interne utilise des chemins relatifs.

## Statuts

| Statut | Sens |
|---|---|
| `active` | Référence actuelle confirmée |
| `provisional` | Base de travail à valider ou compléter |
| `disputed` | Affirmation ou orientation explicitement contestée |
| `superseded` | Remplacé par une version identifiée |
| `archived` | Conservé pour provenance, hors usage actif |

OpenCode est **conservé pour un usage futur**. Il n’est pas classé comme obsolète ; sa responsabilité future reste `[À CONFIRMER]`.

## Limites

Les sources externes restent à leur emplacement. Aucun artefact ni document historique n’est copié dans ce projet à cette étape. Aucun dépôt Git n’a été initialisé.
