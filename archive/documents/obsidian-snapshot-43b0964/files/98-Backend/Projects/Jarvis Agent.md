---
type: "📂 Project"
title: Jarvis Agent
area: "[[🏠 Perso]]"
status: in_progress
priority: high
scheduled_date: 2026-06-27
due_date:
cover: "http://localhost:3042/api/og/project?title=Jarvis+Agent&area=%F0%9F%8F%A0+Perso&status=in_progress&priority=high&scheduled_date=2026-06-27"
tags:
  - ai-agent
  - jarvis
  - second-brain
  - master-agent
  - opencode
  - memory
is_template: false
cssclasses:
  - max
projects:
  - "[[Sofian OS]]"
---
# Jarvis Agent

> **Mission** : Transformer Jarvis d'un simple routeur d'intent en un véritable **master agent de vie** — second brain proactif, avec mémoire persistante, connecté à tous les systèmes de Sofian.

%% col-start:sb:1,bc:muted,b:primary %%
%% col-break:25,b:alt,sb:1,bc:gray,sep:1,sc:gray,ss:dashed %%
### Project Passport

`system-architecture` · `in_progress` · `high`

**Area**\
[[🏠 Perso]]

**Scope**\
Amélioration de l'agent Jarvis (OpenCode) pour en faire un assistant personnel complet : mémoire cross-session, proactivité, connexion à tous les systèmes (email, calendrier, Homelab, Obsidian, Graphify, Epitech).

**Repo / Lien**\
- Repo applicatif canonique : `/Users/sofian/Developer/10-Personal/jarvis`
- Documentation de build : `/Users/sofian/Developer/10-Personal/jarvis/docs/`
- Workflows : `/Users/sofian/Developer/10-Personal/jarvis/workflows/`
- Runtime agentique actuel : Hermes ; les anciens artefacts OpenCode restent des sources à réconcilier, pas le workspace actif

%% col-break:46,b:secondary,sb:1,bc:gray,sep:1,sc:accent,sw:2 %%
## Mission Control

**Résultat attendu** : Un agent Jarvis qui :
1. Se souvient de TOUT entre les sessions (mémoire persistante)
2. Est proactif — signale les problèmes avant qu'on les demande
3. Peut lire/écrire dans tous les systèmes (email, calendrier, vault, homelab, repos)
4. Respecte les patterns ADHD (max 3 options, une chose à la fois, break detection)
5. Documente chaque action automatiquement

> [!abstract] Outcome
> - [ ] Mémoire persistante activée et fonctionnelle
> - [ ] Connexion à tous les systèmes externes
> - [ ] Proactivité : check-in quotidien, alertes overdue, conflits calendrier
> - [ ] Hooks post-compression pour garder le contexte
> - [ ] Dashboard dédié dans Sofian-OS
> - [ ] Documentation complète dans le vault

### Scope

| Axe | Décision |
|---|---|
| Produit | Agent Jarvis v2 — master agent personnel |
| Utilisateurs | Sofian uniquement |
| Livrable | Configuration OpenCode + skills + MCP + hooks + projet Obsidian documenté |
| Hors scope | Nouveaux skills non liés à Jarvis, refonte du vault, nouveaux services Homelab |

%% col-break:26,b:orange-soft,sb:1,bc:orange %%
## Risk Radar

1. **Scope creep** — vouloir tout automatiser d'un coup
2. **Over-engineering** — construire une usine à gaz pour un besoin simple
3. **Maintenance** — chaque MCP/skill ajouté = maintenance future
4. **Confiance agent** — trouver le bon équilibre proactivité vs confirmation
5. **Token cost** — plus d'outils = plus de contexte = plus cher

> [!warning] Watchlist
> - [x] Omem UP sur Nova (localhost:3608) — clé API embedding à fixer
> - [ ] Trop de skills inutilisés ? Élaguer ?
> - [x] opencode.jsonc confirmé comme source canonique
%% col-end %%

## Telemetry

%% col-start:sb:1,bc:muted %%
%% col-break:50,b:blue-soft,sb:1,bc:blue,sep:1,sc:blue,ss:dashed %%
### Phases

| Phase | Nom | Statut |
|---|---|---|
| 1 | Diagnostic & Recherche | `done` |
| 2 | Mémoire (Omem/Mem0) | `in_progress` |
| 3 | Connecteurs (MCP) | `todo` |
| 4 | Hooks & Proactivité | `todo` |
| 5 | Agent Config Finale | `todo` |
| 6 | Documentation & Tests | `todo` |

%% col-break:50,b:green-soft,sb:1,bc:green,sep:1,sc:green,ss:dashed %%
### Stack

| Couche | Technologie |
|---|---|
| Agent runner | OpenCode v1.17.11 |
| LLM | deepseek-v4-pro (opencode-go) + Mistral (codestral, pixtral) via openai-compatible |
| Mémoire | Omem (Rust, self-hosted) |
| Skills | 13 catégories (~30 skills) |
| MCP | email-mcp (actif), + à ajouter |
| Hooks | 18 hooks GSD, 0 hooks Jarvis |
%% col-end %%

## Task Board

![[Project Tasks Board.base#Compact]]

> [!success] Lot Actif — 20 Août 2026
> Le workspace de build canonique est `/Users/sofian/Developer/10-Personal/jarvis`.
>
> Premier parcours vertical : **un compte Mail → Clarify → proposition de TaskNote → accord humain → création vérifiée → Daily Review**.
>
> Capture iOS et Daily Review sont les deux briques suivantes. Jarvis Memory, nouvelle base, Event Bus et microservices restent différés.

## Resource Deck

![[Project Resources.base#Cards]]

## Operational Log

%% col-start %%
%% col-break:55,sep:1,sc:gray,ss:dotted %%
### Decisions

| Date | Décision | Pourquoi |
|---|---|---|
| 2026-06-27 | Lancement projet Jarvis Agent | 3 sessions récentes ont montré les limites de Jarvis actuel |
| 2026-06-27 | Utiliser Omem (existant) plutôt que Mem0 | Omem déjà déployé, juste besoin de le réactiver |
| 2026-06-27 | Approche "build on existing" — pas de nouveau système | Sofian-OS + Homelab-OS + OpenCode = base solide |
| 2026-06-29 | Clean Architecture V3 adoptée | Architecture 4 couches (Interfaces→Gateway→Brain→Adapters) avec Ports/Adapters, multi-service, Event Bus, tool-agnostique via MCP |
| 2026-06-29 | Brainstorming 10 axes de recherche | Comparaison Iron Man JARVIS / Hermes / OpenClaw / blueprint V2 / projets réels — documentée dans [[Jarvis Agent - Architecture V3 Clean Architecture]] |
| 2026-06-29 | Construction bloc par bloc | Ordre strict B0→B10, chaque bloc validé avant le suivant. B0 = OpenCode Jarvis actuel, B1 = Gateway Bun + NATS |
| 2026-06-29 | Mistral AI intégré dans l'architecture | Étudiant/Pro Mistral. Codestral pour code, Pixtral pour vision, mistral-embed alternatif. Provider openai-compatible dans opencode.jsonc. API distincte du compte Le Chat. |
| 2026-08-22 | Workspace applicatif unique créé | Le code, les contrats, fixtures et tests vivent dans `~/Developer/10-Personal/jarvis`; Obsidian reste le cockpit |
| 2026-08-22 | B1 Gateway + NATS n'est plus le prochain lot | Hermes fournit déjà orchestration, CLI et webhooks ; priorité au parcours Mail → TaskNote vérifié |

### Sessions de travail

| Date | Session | Résumé |
|---|---|---|
| 2026-06-27 20h10 | tidy-canyon | Ménage vault : Codename done, MERN done, RCU Phase 6 done, Homelab OS done, Oral Shanisya fixé au 22/07 |
| 2026-06-27 21h30 | mighty-comet | Bilan activités : portfolio ~13 repos polis, 25 tâches done, 6 projets in_progress |
| 2026-06-27 21h34 | cosmic-cabin | Session actuelle — amélioration Jarvis |
| 2026-06-28 | — | Omem rebuild (Gemini embedding → Alibaba MaaS text-embedding-v4), Bruno collection 56 endpoints, MaaS vs DashScope clarifié, config cleanup (GSD/BMAD supprimés, Brave MCP installé), plugin @ourmem/opencode actif |
| 2026-06-29 | — | Session architecture : fix yamlls → yaml-language-server (Neovim), brainstorming Jarvis V3 Clean Architecture, 10 recherches web parallèles, création ressource [[Jarvis Agent - Architecture V3 Clean Architecture]], conciliation 60+ sources, intégration Mistral AI, mise à jour projet |

%% col-break:45,b:alt,sb:1,bc:gray %%
### Next Moves

> [!todo] Prochaines actions
> - [x] Réactiver Omem (container UP sur Nova:3608)
> - [ ] Fixer clé API embedding MaaS (sk-ws-H.*)
> - [x] Nettoyer GSD + BMAD (hooks, commands, skills, agents) — 333+ fichiers supprimés
> - [x] Installer plugin @ourmem/opencode
> - [x] Brave Search MCP installé
> - [x] Phase 1 Diagnostic & Recherche — terminée (29 juin)
> - [x] Documenter l'architecture finale → [[Jarvis Agent - Architecture V3 Clean Architecture]]
> - [x] Intégrer Mistral AI dans l'architecture
> - [ ] Sécuriser opencode.jsonc (clés API → `{env:...}`)
> - [ ] Configurer Mistral dans opencode.jsonc (provider openai-compatible)
> - [ ] Obtenir clé API Mistral (compte développeur)
> - [ ] Dédoublonner les AGENTS.md (1 seul canonique)
> - [ ] Déployer NATS sur Homelab (prérequis Gateway B1)
> - [ ] Spécifier le Gateway Service B1 (Bun + Hono + NATS)
> - [ ] Ajouter MCP : Sequential Thinking + Obsidian
> - [ ] Créer le plugin jarvis-hooks.ts (error logging)
> - [ ] Créer le subagent @auditor
> - [ ] Créer `/morning-brief` commande
> - [ ] Bruno collection Omem : ajouter tests assertions
%% col-end %%
