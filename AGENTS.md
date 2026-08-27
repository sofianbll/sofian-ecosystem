# Sofian Ecosystem — instructions agents

## Mission du dépôt

Ce dépôt est le **système de travail documentaire** utilisé pour reconstruire, auditer puis concevoir Sofian Ecosystem.

Il possède la méthode d’audit, les preuves intégrées, la chronologie reconstruite, les besoins validés, les options d’architecture, les décisions acceptées et les dossiers documentaires. Il ne possède pas les faits métier stockés dans Notion, Obsidian, TaskNotes, Git, les services, les historiques agents ou les documents externes.

## Lire avant tout travail

1. `docs/project/scope.md`
2. `docs/audits/evidence-model.md`
3. `docs/operations/subagent-protocol.md`
4. le `brief.md` du workstream attribué
5. la source directe indiquée par le brief

Pour une reprise de session, lire aussi `docs/operations/session-handoff.md`.

## Méthode obligatoire

Tout travail utilise le *Guide ultime de l’ingénierie logicielle — édition 2026* et les skills :

- `software-engineering-lifecycle` ;
- `opencode-history` ;
- `ourmem` ;
- `obsidian` ;
- `i-have-adhd` ;
- `tdah-visual-responses`.

Charger en plus les skills indiqués dans `docs/reference/skill-routing.md` lorsque leur déclencheur s’applique.

## Règles d’autorité

- Lire une source réelle avant d’affirmer.
- Une mémoire, un résumé, un export ou un index est une piste tant que la source directe existe.
- Préserver les noms littéraux ; ne jamais fusionner deux entités par ressemblance.
- Distinguer `historical_intent`, `current_canon`, `live_implementation`, `user_idea`, `hypothesis`, `contradicted` et `unknown`.
- Une documentation persistée ou un test vert ne prouve ni validation utilisateur ni fonctionnement opérationnel.
- L’écosystème cible n’est pas prédéfini : audit → besoins → capacités → options → cible proposée → validation de Sofian.

## Frontière de mutation

Par défaut, les sources externes sont strictement en lecture seule. Avant toute écriture :

1. annoncer les fichiers ou enregistrements exacts ;
2. décrire le changement et ses non-effets ;
3. obtenir l’accord de Sofian ;
4. vérifier l’état réel après mutation.

Un agent d’audit ne modifie jamais Notion, un vault, TaskNotes, une base, un service, un dépôt voisin, une mémoire, un skill ou une configuration.

## Travail parallèle

Chaque worker reçoit un seul workstream et produit :

```text
question → faits → preuves → contradictions → inconnues → conclusion bornée
```

Les workers ne décident pas de la cible et ne se valident pas eux-mêmes. Jarvis relit les sources citées, contre-audite le rapport puis intègre seulement les conclusions vérifiées.

Pour éviter les conflits :

- un worker écrit uniquement dans le chemin qui lui est attribué ;
- sinon il retourne son rapport sans écrire ;
- les résultats de groupes sont agrégés par le parent ;
- aucune écriture concurrente dans un même fichier.

## Tasks et roadmap

- Le dépôt possède les résultats, spécifications, audits et work packages.
- **Sofian-OS/TaskNotes reste l’autorité des projets, tâches, statuts, dates et priorités opérationnelles.**
- Ne pas créer de second backlog actif en Markdown.
- Un workstream d’audit décrit une couverture à obtenir ; ce n’est pas une TaskNote.

## Documentation et diagrammes

- Le site cible est privé d’abord ; aucun déploiement public sans nouvelle décision.
- Une question par diagramme Mermaid.
- Séparer historique, état actuel, cible candidate et cible acceptée.
- Ajouter date, statut, sources, légende et lecture textuelle.
- Une vue globale reste petite ; les détails vivent dans des sous-vues.
- Aucun sens ne dépend uniquement de la couleur.

## Confidentialité

- Ne jamais lire, afficher, copier ou committer un secret.
- Minimiser les données santé, famille, finance, identité et communications privées.
- Citer la source plutôt que recopier une donnée personnelle inutile.
- Utiliser les outils spécialisés et modes read-only pour les historiques agents et mémoires.

## Git

- Vérifier `git status --short --branch` avant toute écriture.
- Préserver les changements sans rapport.
- Exécuter `git diff --check` avant tout commit.
- Aucun remote, push, tag ou publication sans accord explicite.
- Les payloads sous `archive/baselines/` sont immuables.

## Critère de fin

Un audit n’est terminé que si son périmètre et sa couverture sont explicites, chaque conclusion importante possède une preuve, les contradictions restent visibles, les éléments décisifs sont contre-vérifiés et le niveau de livraison annoncé correspond à l’état réel.
