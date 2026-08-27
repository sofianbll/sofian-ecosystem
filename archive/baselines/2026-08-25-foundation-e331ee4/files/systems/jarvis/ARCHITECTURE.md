---
status: provisional
date: 2026-08-25
scope: Architecture cible minimale de Jarvis
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Architecture de Jarvis

## Boucle cible

```text
Entrée réelle → lecture de la source → clarification
             → proposition sourcée → accord humain
             → mutation canonique → relecture → revue
```

## Composants démontrés

- Hermes : interface et runtime agentique ;
- code Python déterministe dans `SRC-JARVIS-REPO` ;
- Sofian OS et TaskNotes : cibles canoniques ;
- ancien collecteur Daily Brief : composant réutilisable ;
- adaptateurs Mail, iOS, Calendar ou n8n : non livrés.

## Interfaces

- frontières CLI en JSON structuré ;
- fichiers Markdown pour Sofian OS et TaskNotes ;
- provenance, certitude et couverture dans toute sortie ;
- confirmation distincte de l’exécution.

NATS, nouvelle base, microservices et mémoire complète sont différés jusqu’à un besoin démontré.
