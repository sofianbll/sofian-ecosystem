---
status: active
date: 2026-08-25
scope: Architecture opérationnelle de Hermes dans le projet
sources:
  - ../../indexes/SOURCE-MAP.md
---

# Architecture de Hermes

## Éléments utiles

- session : contexte conversationnel ;
- projet : rattachement à un workspace ;
- skills : procédures réutilisables ;
- outils : accès contrôlé aux sources et mutations ;
- sous-agents : audits bornés ;
- jobs : exécutions planifiées ;
- mémoire : profil et faits durables limités.

## Flux Jarvis envisagé

```text
Sofian → Hermes → skill / code Jarvis → source canonique
                                      → résultat vérifié → Hermes
```

## Interfaces

Hermes appelle les fichiers, CLI, MCP et services disponibles. Toute action externe reste soumise aux permissions, à l’autorisation humaine et à la vérification de la cible.
