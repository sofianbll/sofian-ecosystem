---
type: "📚 Resource"
title: "Sofian Ecosystem - Systèmes et Autorité des Faits"
area: "[[🏠 Perso]]"
format: note
projects:
  - "[[Sofian OS]]"
  - "[[Jarvis — Socle v0.1]]"
tags:
  - sofian-ecosystem
  - system-ownership
  - authority-map
  - architecture
is_template: false
cssclasses:
  - dashboard
---

# Sofian Ecosystem - Systèmes et Autorité des Faits

> [!abstract] Rôle
> Cette carte identifie **qui possède quel fait**, où se trouve sa preuve, quelles représentations ne sont que dérivées et où l’autorité reste non établie.
>
> Elle complète [[Sofian Ecosystem - Architecture Niveau 0]] et [[Sofian Ecosystem - Capacités Transverses]] sans créer de nouveau système, contrat ou automatisation.

> [!success] État
> **Hypothèse v0.1 validée comme base de travail par Sofian le 20 août 2026**, après revue de l’artefact interactif complet.
>
> Les instantanés techniques restent datés et non structurants. Les autorités non démontrées restent inscrites **« non établie »**.

---

## Règle Centrale

> L’autorité appartient à un **fait précis**, pas automatiquement à une application entière.
>
> Une autorité peut être Sofian, un système logiciel, un service externe ou un document probant. Une copie doit être identifiable comme projection, avec sa provenance et son chemin de correction. Si aucune source ne démontre l’autorité, elle est inscrite **« non établie »**.

```text
Fait précis → autorité → preuve → projection → correction
```

Le système le plus central, le plus ancien ou le plus complet n’obtient pas automatiquement le dernier mot.

---

## Frontières Des Systèmes

| Acteur ou système | Autorité | N’est pas l’autorité de |
|---|---|---|
| **Sofian** | Intentions, consentements, arbitrages et acceptations humaines | Faits légaux, bancaires ou externes vérifiables |
| **Sofian OS** | Projets, aspirations, ressources qualifiées, décisions et engagements humains enregistrés | Transactions financières, runtime technique, preuves externes |
| **TaskNotes** | État des tâches : statut, priorité, planification et complétion | Réalité d’une obligation externe ou preuve de son exécution |
| **Finance OS** | Enregistrements financiers persistés : comptes catalogués, imports, transactions normalisées, cashflow et index documentaire | Cycle commercial complet, vérité bancaire primaire, infrastructure |
| **Homelab-OS** | Configuration technique désirée, reconstruction et procédures d’exploitation | Faits métier des services hébergés |
| **Runtime technique** | État réellement observé d’un service, conteneur, hôte ou gateway à un instant donné | Configuration désirée et faits métier |
| **Hermes / Jarvis** | Sessions, historique conversationnel, jobs, traces techniques et mémoire agentique enregistrée | Tâches, paiements, obligations, déclarations et décisions humaines |
| **Services et documents externes** | Faits émis ou constatés par leur source : banque, URSSAF, Doctolib, MyEpitech, calendrier, facture, ordonnance | Action à entreprendre dans Sofian OS |
| **Dashboards, handoffs et résumés** | Aucune autorité propre : ce sont des projections | Toute mutation canonique |

---

## Registre Des Faits — Action Humaine Et Cockpit

| Fait | Autorité | Preuve ou stockage | Projection | Correction |
|---|---|---|---|---|
| État d’une tâche | TaskNotes | Note `✏️ Task` | Daily, dashboard, Jarvis | Modifier la TaskNote |
| État d’un projet | Sofian OS | Note `📂 Project` | Boards et dashboards | Modifier la note projet |
| Engagement humain accepté | Sofian + Sofian OS | Confirmation humaine et note concernée | Handoff ou brief | Revalider avec Sofian puis corriger la note |
| Décision d’architecture validée | Sofian + note canonique | Note ou ADR portant la validation | Handoff | Corriger la décision, puis actualiser le handoff |
| Ressource ou connaissance locale | Sofian OS | Note `📚 Resource` | Recherche, résumé, Jarvis | Corriger la Resource |
| Dashboard ou Base | Aucune autorité propre | Query reconstruisible | Vue dérivée | Corriger la source, jamais seulement la vue |

---

## Registre Des Faits — Sources Externes Et Preuves

| Fait | Autorité | Preuve | Projection locale |
|---|---|---|---|
| Obligation ou échéance URSSAF | Texte ou service officiel applicable | Portail ou document officiel | `due_date` d’une TaskNote |
| Déclaration URSSAF déposée | URSSAF | Accusé de dépôt | Mention ou lien dans Sofian OS |
| Montant et conditions d’une facture reçue | Émetteur et document émis | Facture originale | Resource, TaskNote ou index Finance OS |
| Paiement ou débit observé | Banque | Relevé ou transaction bancaire | Transaction importée dans Finance OS |
| Rendez-vous médical confirmé | Doctolib ou professionnel | Confirmation du rendez-vous | TaskNote ou calendrier |
| Prescription médicale | Professionnel de santé | Ordonnance originale | Lien ou Resource locale |
| Sujet, échéance ou résultat Epitech | MyEpitech selon le fait | Page ou résultat officiel | Projet ou TaskNote |
| Code effectivement livré | Dépôt Git concerné | Commit, tag ou livraison | Lien depuis le projet |
| Événement calendrier | Fournisseur et organisateur | Événement original, invitation, réponse | Identifiant stocké dans une TaskNote |

> [!warning] Déclaré N’est Pas Vérifié
> Une TaskNote peut affirmer **« action terminée »** sans prouver que le service externe a accepté l’opération. Un identifiant externe ou une phrase dans une note est un lien ou une déclaration locale, pas automatiquement une preuve externe vérifiée.

---

## Finance OS

| Fait | Autorité opérationnelle | Preuve d’origine ou limite |
|---|---|---|
| Catalogue interne des comptes | Finance OS | L’existence réelle et le solde viennent du fournisseur bancaire |
| Provenance et état d’un import | Finance OS | Le fichier source reste la preuve d’entrée |
| Transaction normalisée importée | Finance OS | La banque reste la source d’origine du mouvement |
| Élément de cashflow stocké | Finance OS | Un prévisionnel n’est pas un paiement réel |
| Index et statut d’un document | Finance OS | Le fichier original reste le document probant |
| Clients, missions, devis, factures émises | **Non établie** | Aucune collection canonique démontrée |
| Rapprochement facture ↔ paiement | **Non établie** | Aucun workflow canonique démontré |

Les collections observées sont :

```text
accounts · imports · transactions · cashflow_items · documents
```

Aucun modèle canonique `clients`, `missions`, `devis` ou `factures émises` n’a été démontré.

> [!warning] Limite Bancaire
> Un cashflow marqué `paid` ou `received` n’est pas, à lui seul, une preuve bancaire indépendante. Un `balance` importé n’est pas automatiquement le solde courant.

---

## Homelab Et Runtime

| Fait | Autorité |
|---|---|
| Configuration versionnée, Compose, réseau et volumes attendus | Homelab-OS |
| Organisation canonique de `$HOME` | Décision `67 Unified Home Architecture` |
| Service réellement actif à un instant donné | Runtime de l’hôte/Docker et contrôle de santé |
| Données métier d’une application hébergée | Application métier, jamais Homelab-OS par simple hébergement |
| Secrets réellement utilisés | Emplacement runtime autorisé, hors Git |

```text
Homelab-OS          → configuration désirée et reconstruction
Runtime technique   → état observé à un instant donné
Application métier  → faits métier stockés par le service
```

---

## Hermes, Jarvis Et Mémoire

| Fait | Autorité | Projection ou limite |
|---|---|---|
| Transcript et métadonnées Hermes | `~/.hermes/state.db` | Recherche, export et résumé sont dérivés |
| Contexte de reprise architectural | Notes canoniques + handoff | Le handoff pointe vers les sources sans les remplacer |
| Mémoire built-in | `MEMORY.md` / `USER.md` | Mémoire agentique révisable, jamais preuve métier |
| Souvenirs sémantiques ourmem | Stockage ourmem | Mémoire secondaire ; pas le fournisseur Hermes actif pendant l’audit |
| Définition d’un job planifié | Stockage cron Hermes | Son existence ne prouve pas son exécution |
| Historique d’une tentative cron | Historique Hermes | Le résultat métier doit encore être vérifié à sa source |
| Capacité actuelle à déclencher les jobs | Gateway/runtime Hermes | Le gateway était arrêté pendant l’audit |
| Skills et capacités déclarées | Configuration Hermes | Ne prouvent ni authentification ni permission réelle |

Aucun compteur de sessions n’est conservé dans cette architecture : les valeurs observées variaient selon le périmètre et restent volatiles.

> [!important] Frontière Jarvis
> Jarvis peut lire, proposer, préparer, surveiller et vérifier. Il ne devient pas la source de vérité universelle des faits de vie.

---

## Autorités Non Établies

- clients ;
- missions commerciales ;
- devis ;
- factures émises ;
- rapprochement commercial facture ↔ paiement ;
- preuve actuelle de certaines déclarations URSSAF ;
- validation actuelle de certains états Epitech ;
- confirmation actuelle de certains rendez-vous médicaux ou calendaires ;
- contrat formel entre Sofian OS et Jarvis/Hermes ;
- architecture détaillée de la mémoire Jarvis.

> [!danger] Non-Décision
> Ces trous ne justifient pas la création d’un **Business OS**, d’un **Health OS**, d’une nouvelle base ou d’un bus d’événements.

---

## Instantanés Techniques Non Structurants

> [!warning] Observations Datées Du 20 Août 2026
> - Finance OS répondait `HTTP 200` au healthcheck ; son peuplement et sa fraîcheur ne sont pas démontrés.
> - Deux jobs Hermes étaient définis, mais le gateway était arrêté.
> - Le Morning Briefing rencontrait un blocage de configuration.
> - ourmem répondait via MCP, mais Hermes indiquait `memory.provider: none` : seule la mémoire built-in était active comme fournisseur Hermes.

Ces observations ne définissent aucune autorité permanente.

---

## Règles De Mutation

1. Trouver l’autorité du fait précis avant toute correction.
2. Corriger le fait dans son système ou sa source d’autorité.
3. Mettre à jour ou reconstruire ensuite les projections concernées.
4. Ne jamais corriger seulement un dashboard, résumé ou handoff.
5. Ne jamais réconcilier silencieusement un conflit.
6. Toute mutation financière, légale ou administrative sensible exige confirmation humaine, preuve vérifiable et trace du résultat.
7. Jarvis peut lire, proposer, préparer et vérifier ; ses droits d’écriture seront définis ultérieurement.
8. Si l’autorité reste inconnue, inscrire **« non établie »** au lieu d’inventer une source.
9. Aucun contrat ni automatisation n’est défini dans cette note.

---

## Scénarios De Lecture

### URSSAF

```text
Action à faire      → TaskNotes
Obligation légale   → source officielle
Dépôt accepté       → accusé URSSAF
Paiement observé    → banque
Projection          → Finance OS
```

### Santé

```text
Action à faire       → TaskNotes
Rendez-vous confirmé → Doctolib / professionnel
Prescription         → ordonnance
Événement visible    → calendrier, si synchronisé
Résumé ou rappel     → Jarvis, projection seulement
```

### Freelance

```text
Projet                 → Sofian OS
Prochaine action        → TaskNotes
Accord humain           → personnes + preuve d’échange
Client / devis /
facture émise           → autorité non établie
Paiement reçu           → banque
Transaction importée    → Finance OS
```

### Epitech

```text
Projet et engagement       → Sofian OS
Action à réaliser          → TaskNotes
Sujet / échéance / résultat→ MyEpitech
Code livré                 → dépôt Git
Calendrier / Jarvis        → projections
```

---

## Décisions Différées

- Jarvis Memory ;
- contrats entre Sofian OS, Jarvis, Finance OS et Homelab-OS ;
- automatisations ;
- nouveaux OS ou nouvelles bases ;
- migrations et déplacements de données.

Le premier incrément de build est cadré dans [[Jarvis — Socle v0.1]].

---

## Sources

### Sources Locales

- [[Sofian Ecosystem - Architecture Niveau 0]] ;
- [[Sofian Ecosystem - Capacités Transverses]] ;
- [[Sofian Ecosystem Architecture]] ;
- [[TaskNotes Schema]] ;
- [[V4 Obsidian Adapter Mapping]] ;
- [[Sofian OS]] ;
- `Homelab-OS/docker/stacks/pulsar/finance-os/` ;
- `Homelab-OS/vault-os/60-69 Architecture/67 Unified Home Architecture.md` ;
- `/Users/sofian/Documents/00-Inbox/Guide-ultime-ingenierie-logicielle.pdf`, chapitre 46.

### Documentation Officielle Hermes

1. https://hermes-agent.nousresearch.com/docs/user-guide/sessions
2. https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers
3. https://hermes-agent.nousresearch.com/docs/user-guide/features/cron

---

## Validation

> [!success] Décision Du 20 Août 2026
> Sofian valide cette carte et son artefact interactif complet comme **base de travail v0.1**.
>
> La validation couvre les frontières, le registre des faits, les autorités non établies, les règles de mutation et les décisions différées. Elle n’autorise aucun nouveau système, contrat, stockage ou automatisation.
