---
status: active
date: 2026-08-25
scope: Identifiants et emplacements des sources utilisées
sources:
  - ../README.md
---

# Carte des sources

Les identifiants ci-dessous évitent de recopier les sources. Un chemin externe est une provenance, pas un lien interne.

| ID | Source | Rôle |
|---|---|---|
| `SRC-CONV` | Conversation Hermes courante et son historique accessible | Décisions, corrections, audits et actions de ce chantier |
| `SRC-SOS` | `/Users/sofian/Documents/Obsidian/Sofian-OS/` | Source canonique des projets, engagements, ressources et TaskNotes |
| `SRC-SOS-COMMIT` | commit `43b0964d7bace22abf2cfad32baaf1b449889687` dans `SRC-SOS` | État historique exact des neuf documents archivés |
| `SRC-SNAPSHOT-43B0964` | `../archive/documents/obsidian-snapshot-43b0964/` | Copie locale byte-for-byte des neuf blobs Git |
| `SRC-AUTH` | `SRC-SOS/98-Backend/Resources/Sofian Ecosystem - Systèmes et Autorité des Faits.md` | Carte provisoire des autorités |
| `SRC-LEVEL0` | `SRC-SOS/98-Backend/Resources/Sofian Ecosystem - Architecture Niveau 0.md` | Domaines de vie |
| `SRC-CAP` | `SRC-SOS/98-Backend/Resources/Sofian Ecosystem - Capacités Transverses.md` | Capacités transverses |
| `SRC-HANDOFF` | `SRC-SOS/99-System/AI Handoffs/Sofian Ecosystem Architecture.md` | Handoff architectural, partiellement contesté |
| `SRC-JARVIS-NOTE` | `SRC-SOS/98-Backend/Projects/Jarvis Agent.md` | Projet historique Jarvis |
| `SRC-JARVIS-SOCLE` | `SRC-SOS/98-Backend/Projects/Jarvis — Socle v0.1.md` | Lot Brief créé prématurément |
| `SRC-V4` | `SRC-SOS/98-Backend/Resources/Sofian OS V4 - Operating Layer.md` | Routines Capture, Clarify, Engage et Review |
| `SRC-JARVIS-REPO` | `/Users/sofian/Developer/10-Personal/jarvis/` | Workspace de code Jarvis, non committé et sans remote lors de l’audit |
| `SRC-DAILY` | `/Users/sofian/.config/opencode/skills/productivity/jarvis-daily-brief/` | Ancien moteur Daily Brief testé |
| `SRC-HOMELAB` | `/Users/sofian/Homelab-OS/` | Configuration du homelab et documentation n8n |
| `SRC-FINANCE` | `SRC-HOMELAB/docker/stacks/pulsar/finance-os/` | Implémentation Finance OS auditée |
| `SRC-OURMEM` | `/Users/sofian/Data/appdata/omem` et configuration Homelab-OS/dotfiles | Runtime et stockage ourmem ; contenu non copié |
| `SRC-OPENCODE` | `/Users/sofian/.local/share/opencode/opencode.db` | Historique canonique OpenCode, lecture seule |
| `SRC-HERMES` | `~/.hermes/` et documentation officielle Hermes | Runtime, projets, sessions, skills et jobs |
| `SRC-ARTIFACTS` | `/Users/sofian/.hermes/artifacts/` | Originaux des artefacts HTML importés |
| `SRC-GUIDE` | `/Users/sofian/Documents/00-Inbox/Guide-ultime-ingenierie-logicielle.pdf` | Principes d’incréments, YAGNI et responsabilités |

## Règles

- ne jamais recopier de secret ou de base de données ;
- lire les sources directes avant les résumés ;
- marquer `[À CONFIRMER]` si une source n’est plus accessible ou si les preuves divergent ;
- ne jamais modifier `SRC-OPENCODE` pendant une consultation historique ;
- traiter `SRC-SNAPSHOT-43B0964` comme une archive immuable, pas comme une source canonique actuelle.
