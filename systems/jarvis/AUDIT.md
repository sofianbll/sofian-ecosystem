---
status: disputed
date: 2026-08-25
scope: Audit factuel et contradictions de Jarvis
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Audit de Jarvis

## Faits vérifiés

- `SRC-JARVIS-NOTE` rassemble une vision historique hétérogène ;
- `SRC-JARVIS-SOCLE` définit un Brief à la demande mais a été créé trop vite ;
- `SRC-JARVIS-REPO` contient 15 fichiers non suivis, sans commit ni remote lors de l’audit ;
- sa CLI Mail sur fixture passe deux tests et ne mute rien ;
- l’ancien moteur `SRC-DAILY` passe 81 tests séparés ;
- aucun vrai Mail, Shortcut iOS ou Daily Start n’est connecté.

## Contradictions

- premier incrément : Brief, Mail ou Daily Start ;
- architecture historique OpenCode/NATS face à Hermes actuel ;
- statut « validé » de documents ensuite contestés ;
- somme de 83 tests présentée trop largement.

Voir [les contradictions](../../indexes/CONTRADICTIONS.md).
