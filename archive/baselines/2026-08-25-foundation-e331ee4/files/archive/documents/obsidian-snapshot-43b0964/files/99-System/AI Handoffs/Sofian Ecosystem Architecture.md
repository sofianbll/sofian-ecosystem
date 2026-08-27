---
type: "⚙️ System Config"
title: "Sofian Ecosystem Architecture"
config_key: ai_handoff_sofian_ecosystem_architecture
config_status: active
projects:
  - "[[Sofian OS]]"
is_system: true
is_template: false
---

# Sofian Ecosystem Architecture

> [!abstract] Rôle
> Point de reprise persistant pour toute IA qui travaille sur l'architecture **Sofian Ecosystem / Sofian OS / Jarvis OS**.
>
> Ce handoff conserve l'altitude, les décisions validées, l'état courant et les prochains contrôles. Il **ne remplace pas** les notes canoniques : il pointe vers elles et doit charger les détails juste à temps.

> [!success] État
> **Actif — mis à jour le 20 août 2026.**
> Couches validées : Domaines de vie, Capacités transverses, Systèmes et autorité des faits.
>
> Phase active : premier incrément livrable [[Jarvis — Socle v0.1]], brief à la demande en lecture seule depuis Sofian OS et TaskNotes.

---

## Reprise En 60 Secondes

1. Lire ce handoff en entier.
2. Lire [[Sofian Ecosystem - Architecture Niveau 0]].
3. Lire [[Sofian Ecosystem - Capacités Transverses]], puis [[Sofian Ecosystem - Systèmes et Autorité des Faits]].
4. Exécuter `git status --short` dans le vault avant toute écriture.
5. Pour le build actif, lire [[Jarvis — Socle v0.1]] et ses TaskNotes.
6. Séparer `Confirmé`, `Hypothèse`, `Inconnu` et `Différé` dans toute proposition.

---

## Mission Et Altitude

Sofian Ecosystem architecture **toute la vie de Sofian**. Le numérique sert cette vie ; il n'en définit pas le périmètre.

Ordre de travail obligatoire :

```text
1. Domaines de vie          — validé
2. Capacités transverses    — validé
3. Systèmes et ownership    — validé comme base v0.1
4. Contrats inter-systèmes  — différé
5. Modèles internes         — différé
6. Implémentation / outils  — premier incrément actif
```

Ne pas descendre d'un niveau pour résoudre une ambiguïté du niveau courant.

---

## Vocabulaire De Contrôle

| Niveau | Question | Ne signifie pas automatiquement |
|---|---|---|
| **Domaine de vie** | Où existe une responsabilité durable ? | Area, application ou OS |
| **Capacité** | Que faut-il pouvoir accomplir ? | Workflow, module ou Bot |
| **Système** | Qui possède règles, état et cycle de vie ? | Déploiement séparé |
| **Module** | Quelle responsabilité logique est encapsulée ? | Service réseau |
| **Projet** | Quel changement temporaire vise un résultat ? | Frontière permanente |
| **Outil / adapter / runtime** | Comment cela fonctionne aujourd'hui ? | Définition métier |

---

## Décisions Validées

### 20 Août 2026 — Carte Niveau 0

Sofian valide [[Sofian Ecosystem - Architecture Niveau 0]] comme base de travail.

La décision confirme :

- périmètre : **toute la vie**, numérique comme moyen ;
- trois familles et neuf domaines :
  - Soi et liens : Santé & équilibre ; Famille & relations ; Logement & cadre de vie ;
  - Développement et contribution : Études & apprentissage ; Carrière, travail & entreprise ; Création & expression ;
  - Sécurité et environnement : Finances personnelles ; Droits, identité & protections ; Environnement numérique & fabrication ;
- une situation possède un domaine principal et peut garder des liens secondaires ;
- les Areas opérationnelles restent `[[🏠 Perso]]` et `[[🎓 Epitech]]` ;
- aucun nouvel OS, aucune nouvelle Area et aucun déplacement de données ne découlent de cette carte.

Le brouillon technique antérieur est conservé mais différé dans [[Sofian Ecosystem - Architecture des Systèmes - Brouillon]].

---

## Couche Validée — Capacités Transverses

[[Sofian Ecosystem - Capacités Transverses]] propose actuellement quatre familles regroupant dix capacités :

1. **Faire entrer & qualifier** — Capturer ; Clarifier & qualifier ;
2. **Transformer & agir** — Transformer en engagement ; Organiser & planifier ; Exécuter & faire avancer ;
3. **Maintenir la continuité** — Conserver & retrouver ; Coordonner & suivre ; Revoir & réaligner ;
4. **Piloter l'évolution** — Décider & gouverner ; Améliorer progressivement.

**Statut : base de travail validée par Sofian le 20 août 2026.**

La validation couvre les quatre familles, les dix capacités, leurs noms et leurs frontières. Restent à éprouver séparément :

- `Administration`, `automatisation`, `mémoire`, `routine` et `dashboard` sont-ils correctement classés comme applications, mécanismes ou surfaces ?

---

## Couche Validée — Systèmes Et Autorité Des Faits

[[Sofian Ecosystem - Systèmes et Autorité des Faits]] est validée comme **base de travail v0.1** depuis le 20 août 2026.

La validation confirme :

- l'autorité est définie par fait précis, pas par application entière ;
- TaskNotes possède l'état des tâches ;
- Sofian OS possède les projets, décisions et engagements humains enregistrés ;
- les services et documents externes restent autorités de leurs faits ;
- Finance OS possède uniquement les états financiers qu'il persiste réellement ;
- Homelab-OS possède la configuration et la reconstruction, pas les faits métier hébergés ;
- Hermes/Jarvis possède son historique, ses jobs, traces et mémoires agentiques, jamais la vérité universelle de la vie de Sofian ;
- une projection, un résumé ou un handoff ne possède aucune autorité propre ;
- toute autorité non démontrée reste **non établie**.

Restent explicitement non établis ou différés : cycle commercial complet, contrat Sofian OS ↔ Jarvis, architecture détaillée de Jarvis Memory et automatisations.

---

## Scénarios De Référence

Toujours tester les cartes avec des situations réelles avant de créer une frontière :

1. prendre et suivre un rendez-vous médical ;
2. faire avancer un dossier familial sensible ;
3. trouver une alternance liée à Epitech ;
4. déclarer le chiffre d'affaires à l'URSSAF ;
5. préparer une date ou une sortie Køya ;
6. entretenir une imprimante 3D pour produire une pièce.

Format de test :

```text
Déclencheur → domaine principal → capacité mobilisée → fait autoritaire
→ action humaine/agentique → permission → résultat vérifié → correction
```

---

## Sources Canoniques À Charger Juste À Temps

| Besoin | Source autoritaire |
|---|---|
| Carte de vie validée | [[Sofian Ecosystem - Architecture Niveau 0]] |
| Carte de capacités active | [[Sofian Ecosystem - Capacités Transverses]] |
| Carte des autorités validée | [[Sofian Ecosystem - Systèmes et Autorité des Faits]] |
| Premier lot livrable | [[Jarvis — Socle v0.1]] |
| Projet opérationnel | [[Sofian OS]] |
| Point d'entrée V4 | [[Sofian OS V4 - Architecture Référence]] |
| Décisions V4 | [[Sofian OS V4 - Journal De Décisions]] |
| Backlog V4 | [[Sofian OS V4 - Travail Restant]] |
| Pourquoi et refus | [[Sofian OS V4 - Governance Intent]] |
| Entités et invariants | [[Sofian OS V4 - Domain Core]] |
| Commands, queries, dashboards | [[Sofian OS V4 - Application Core]] |
| Mutations et classification | [[Sofian OS V4 - Workflows]] |
| Routines humaines | [[Sofian OS V4 - Operating Layer]] |
| Mapping vers Obsidian | [[V4 Obsidian Adapter Mapping]] |
| Propriétés du vault | [[Properties Schema]] |
| Tâches | [[TaskNotes Schema]] |
| Architecture logicielle de référence | `/Users/sofian/Documents/00-Inbox/Guide-ultime-ingenierie-logicielle.pdf` |
| Papiers personnels | `/Users/sofian/Documents/10-Perso/` — source canonique, lecture sensible |
| Ancien travail | Ancien `Sofian's Vault` et historiques — preuves secondaires, jamais canon actuel par défaut |

Ne pas recopier le contenu de ces sources dans ce handoff. Conserver le pointeur, la décision et la raison de lecture.

---

## Passages Obligatoires Du Guide Ultime

| Sujet | Passage | Application |
|---|---|---|
| Incréments et petits lots | ch. 5, p. 22–25 imprimées / p. 65–68 PDF | Produire un résultat vertical vérifiable, pas plusieurs couches inertes |
| Réversibilité et YAGNI | ch. 6, p. 27–31 / p. 70–74 PDF | Ne construire ni futur imaginaire ni dépendance diffuse |
| Responsabilités avant topologie | ch. 35 §35.2.2, p. 189 / p. 232 PDF | Définir domaine et capacité avant outil, base ou service |
| Systèmes de référence | ch. 46, p. 257–262 / p. 300–305 PDF | Une autorité par fait ; copies avec provenance et correction |
| Cartes séparées | ch. 66 §66.3, p. 376 / p. 419 PDF | Ne pas confondre domaine, context, service, équipe ou capacité |
| Contexte comme budget d'attention | ch. 73, p. 416–420 / p. 459–463 PDF | Petit socle stable, récupération juste à temps, divulgation progressive |
| État externalisé | ch. 73 §73.6, p. 418 / p. 461 PDF | Garder objectif, décisions, faits référencés, erreurs et prochaine étape |
| Cadrage | annexe C, p. 469 / p. 512 PDF | Acteur, valeur, risques, scénarios, plus petit incrément et réexamen |

---

## Garde-Fous

- **Lecture seule par défaut.** Avant toute mutation : annoncer fichiers, changement exact et effet attendu ; attendre l'accord.
- **Sofian arbitre.** Une proposition agentique n'est pas une décision validée.
- **Une source canonique par fait.** Le handoff, la mémoire Jarvis et les résumés restent des pointeurs ou projections.
- **Aucun OS par taille perçue.** Valeur, langage, état, cycle de vie, risque, consommateurs et coût de coordination doivent justifier la frontière.
- **Pas d'automatisation spéculative.** Stabiliser le chemin humain, puis tester un incrément réversible.
- **Pas de raw dump.** Conclusion d'abord, trois blocs maximum, une décision à la fois.
- **Pas de Computer Use ou navigateur visible.** Tests web uniquement headless/CLI isolés sans accord explicite.
- **Aucun secret.** Ne jamais lire ou reproduire un secret pour documenter l'architecture.

---

## Protocole De Travail

### Avant Une Proposition

1. Reprendre l'altitude et la couche active depuis ce fichier.
2. Lire la source directe avant l'historique ou la mémoire.
3. Inspecter l'état Git et préserver les changements sans rapport.
4. Tester la frontière avec au moins trois scénarios réels.
5. Distinguer fait confirmé, hypothèse et option.

### Avant Une Mutation

1. Nommer exactement les fichiers ou enregistrements visés.
2. Expliquer l'effet et les non-effets.
3. Obtenir l'accord de Sofian.
4. Faire le plus petit changement cohérent et réversible.

### Après Une Mutation

1. Vérifier frontmatter, liens et `git diff --check`.
2. Tester le résultat réel, pas seulement le contenu écrit.
3. Relire la cible externe après toute mutation hors fichier.
4. Mettre à jour ce handoff seulement si un jalon, une décision ou la prochaine étape change.
5. Ne pas committer sans accord explicite ; si un commit est autorisé, limiter strictement son scope.

---

## État Du Projet

### Terminé Et Vérifié

- Inventaire multi-source des domaines de vie.
- Séparation entre domaines, capacités, systèmes et outils.
- Carte Niveau 0 matérialisée et validée par Sofian.
- Carte des quatre familles et dix capacités transverses validée par Sofian.
- Carte des systèmes et de l'autorité des faits validée par Sofian.
- Artefact interactif complet vérifié par 49 assertions JSDOM.
- Brouillon technique précédent conservé comme travail différé.

### En Cours

- [[Jarvis — Socle v0.1]] : premier parcours vertical livrable.
- Tâche active : [[Jarvis Socle v0.1 - Spécifier le contrat du brief]].
- Sources obligatoires du premier lot : Sofian OS et TaskNotes, en lecture seule.

### Différé

- Contrats Sofian OS ↔ Jarvis OS ↔ systèmes spécialisés.
- Architecture de mémoire et connaissances de Jarvis.
- Évolution des Areas V4.
- Nouveaux OS, Bots, bases, event bus ou déploiements.

### Prochaine Étape Unique

> Spécifier le contrat déterministe du brief Jarvis : trois priorités maximum, provenance, certitude et aucune mutation silencieuse.

---

## Maintenance Du Handoff

Mettre ce fichier à jour uniquement lorsqu'un des événements suivants se produit :

- Sofian valide, corrige ou annule une décision structurante ;
- la couche active change ;
- une source canonique change de chemin ou d'autorité ;
- un risque ou un blocage modifie la prochaine étape ;
- un incrément est réellement vérifié.

À chaque mise à jour :

1. conserver la date ;
2. retirer l'état devenu faux au lieu d'empiler des résumés ;
3. garder les liens vers les preuves ;
4. distinguer décision, hypothèse et différé ;
5. maintenir une seule prochaine étape.

Ce handoff est une **mémoire externe révisable**, pas une archive de conversation.
