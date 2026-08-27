---
status: provisional
date: 2026-08-25
scope: Parcours Mail vers proposition puis TaskNote approuvée
sources:
  - ../indexes/SOURCE-MAP.md
  - ../systems/jarvis/AUDIT.md
  - ../systems/tasknotes/ARCHITECTURE.md
---

# Mail to Task

## Besoin

Repérer une demande ou obligation dans un fil Mail et la transformer en action suivie sans altérer le message original.

## Parcours cible

```text
Fil autorisé → lecture sans mutation → clarification → proposition
            → accord humain → TaskNote idempotente → relecture
```

## État démontré

`SRC-JARVIS-REPO` contient un tracer sur fixture synthétique : deux tests passent et la CLI produit une proposition JSON avec `mutation_performed: false`.

## Non démontré

- connexion à un compte réel ;
- compréhension d’un fil complexe ;
- dispositions `waiting`, `reference` et `noise` ;
- prévention des doublons ;
- création puis relecture d’une TaskNote.

## Permissions

Lire un périmètre explicitement autorisé et produire une proposition sont permis. Marquer lu, archiver, supprimer, envoyer ou créer une TaskNote sans accord sont interdits.

## Statut

**Prototype sur fixture, parcours réel non livré.** Sa priorité reste non réconciliée dans [la décision 0007](../decisions/0007-first-functional-increment.md).
