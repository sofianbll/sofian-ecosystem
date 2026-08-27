---
status: provisional
date: 2026-08-25
scope: Définition et responsabilité de Jarvis
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Jarvis

Jarvis est la couche agentique envisagée pour relier les sources canoniques, proposer des actions et vérifier les résultats. Il ne devient pas une base métier universelle.

## Responsabilités visées

- lire la source pertinente ;
- clarifier une entrée et exposer l’incertitude ;
- proposer une mutation exacte ;
- attendre l’accord humain ;
- exécuter puis relire la cible autoritaire ;
- aider Sofian à choisir et avancer avec peu de surcharge.

## État

Un repo autonome `SRC-JARVIS-REPO` contient documentation, fixture Mail, CLI et deux tests. Aucun parcours réel complet n’est livré.

## Dépendances

[Sofian OS](../sofian-os/README.md), [TaskNotes](../tasknotes/README.md), [Hermes](../hermes/README.md) et adaptateurs externes bornés.

Voir [l’audit](AUDIT.md), [l’architecture](ARCHITECTURE.md) et [l’état](STATUS.md).
