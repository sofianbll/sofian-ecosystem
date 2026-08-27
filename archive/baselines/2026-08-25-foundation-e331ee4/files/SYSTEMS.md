---
status: provisional
date: 2026-08-25
scope: Registre central des systèmes identifiés
sources:
  - indexes/SOURCE-MAP.md
---

# Registre des systèmes

| Système | Responsabilité actuelle | Autorité | État documentaire |
|---|---|---|---|
| [Sofian OS](systems/sofian-os/README.md) | Projets, engagements, ressources et cockpit humain | Confirmée sur les faits enregistrés dans son périmètre | Actif |
| [TaskNotes](systems/tasknotes/README.md) | État des tâches | Confirmée | Actif |
| [Jarvis](systems/jarvis/README.md) | Orchestrer, proposer et vérifier entre systèmes | Aucun fait métier canonique propre | Provisoire |
| [Hermes](systems/hermes/README.md) | Runtime et interface agentique actuels | Sessions, jobs, traces et mémoire agentique enregistrée | Actif |
| [Finance OS](systems/finance-os/README.md) | États financiers réellement persistés | Limitée aux collections démontrées | Actif, périmètre borné |
| [Homelab-OS](systems/homelab-os/README.md) | Configuration désirée et reconstruction du homelab | Confirmée sur la configuration versionnée | Actif |
| [ourmem](systems/ourmem/README.md) | Mémoire sémantique secondaire | Son propre stockage ; pas les faits métier | Actif, intégration Jarvis différée |
| [OpenCode](systems/opencode/README.md) | Travail agentique et historique OpenCode ; usage futur | Historique OpenCode pour ses propres sessions | Conservé ; responsabilité future `[À CONFIRMER]` |

## Sources externes, pas systèmes internes

Apple Mail, Gmail, Calendar, banques, URSSAF, Doctolib, MyEpitech, ActivityWatch et documents émis restent des sources ou services externes. Leur contenu et leur état font autorité selon le fait précis ; leur simple connexion à Jarvis ne transfère aucune autorité.

## Règle de frontière

Un système possède une responsabilité, un état et un cycle de vie. Un canal, un adaptateur, une vue, un dashboard ou un runtime ne devient pas automatiquement un nouveau système.
