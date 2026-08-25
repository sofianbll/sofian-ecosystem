---
status: active
date: 2026-08-25
scope: Décision de différer l’infrastructure non démontrée
sources:
  - ../indexes/SOURCE-MAP.md
  - ../systems/jarvis/ARCHITECTURE.md
---

# 0006 — Différer l’infrastructure spéculative

## Contexte

Des architectures historiques proposaient Gateway, NATS, PostgreSQL central, microservices, plusieurs agents spécialisés et mémoire complète avant un parcours utile.

## Décision

Ne pas ajouter ces composants tant qu’une contrainte observée dans un parcours actif ne les exige pas.

## Justification

Les systèmes existants et du Python déterministe suffisent pour tester les premiers parcours. Une infrastructure anticipée augmente la coordination et le risque de divergence.

## Conséquences

- n8n reste un adaptateur optionnel ;
- aucune nouvelle base métier ;
- aucun event bus ou service séparé par défaut ;
- chaque ajout futur doit répondre à un besoin et à une preuve.

## Statut

**Active.** Aucun composant différé n’a été déployé pour Jarvis pendant cette conversation.
