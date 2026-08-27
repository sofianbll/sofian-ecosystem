---
status: provisional
date: 2026-08-25
scope: Parcours de capture iOS vers l’Inbox de Sofian OS
sources:
  - ../indexes/SOURCE-MAP.md
  - ../systems/sofian-os/ARCHITECTURE.md
  - ../systems/homelab-os/STATUS.md
---

# iOS Capture

## Besoin

Capturer un texte ou une dictée en quelques secondes depuis l’iPhone sans devoir choisir immédiatement un projet ou une priorité.

## Parcours cible

```text
Texte ou dictée → Shortcut unique → payload versionné
                → endpoint autorisé → Inbox Sofian OS → accusé
```

## État

**Documenté, non construit.** Treize Shortcuts apparaissent dans une vision historique, mais aucun Shortcut Jarvis correspondant n’a été retrouvé comme installé. Aucun Shortcut existant n’a été modifié.

## Contrat minimal proposé

`schema_version`, `capture_id`, `captured_at`, `input_type`, `content` et `source_device`. Ce contrat reste provisoire.

## Décisions manquantes

- webhook Hermes ou adaptateur n8n ;
- authentification ;
- format canonique de l’Inbox Item ;
- idempotence ;
- rétention des médias.

Commencer éventuellement par un Shortcut texte/dictée, pas par les treize idées historiques.
