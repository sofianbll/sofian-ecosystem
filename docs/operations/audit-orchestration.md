---
title: Orchestration des audits
status: active
date: 2026-08-27
---

# Orchestration

## Résultat

Permettre à plusieurs sessions ou groupes d’agents de couvrir des sources distinctes sans perdre la provenance, créer de contradictions invisibles ou écrire dans les systèmes canoniques.

## Cycle d’un workstream

```text
catalogué
→ brief_ready
→ collecte read-only
→ rapport
→ contre-audit parent
→ correction éventuelle
→ intégration des claims acceptés
→ mise à jour couverture / timeline / noms / contradictions
```

## Préparer un lot

1. Choisir une seule question décisionnelle.
2. Définir le corpus exact : chemins, IDs, dates ou pagination.
3. Établir le nombre attendu d’objets lorsque possible.
4. Choisir des lots non chevauchants ou une clé de déduplication.
5. Nommer les sources et leur priorité.
6. Déclarer données sensibles et mutations interdites.
7. Donner le format de rapport et la Definition of Done.
8. Attribuer un parent responsable de l’agrégation.

## Délégation individuelle

Un worker reçoit le `brief.md` complet. Il ne doit pas dépendre de la conversation du parent. Il retourne des claims atomiques, citations, contradictions, inconnues et couverture.

## Groupe parallèle

Utiliser un groupe seulement pour des branches indépendantes :

- un lot de fichiers par worker ;
- une période par worker ;
- une source par worker ;
- ou des questions complémentaires sans état partagé.

Ne pas envoyer le même audit large à plusieurs workers sans rôle de critique distinct.

## Agrégation

Le parent agrège mécaniquement :

- concaténer puis dédupliquer par source + locator + statement ;
- compter objets attendus, lus, exclus et bloqués ;
- trier chronologiquement ou par identité ;
- conserver les désaccords ;
- ne jamais compléter un trou avec une supposition.

## Contre-vérification

Le parent relit directement au minimum :

- chaque décision structurante ;
- chaque renommage ;
- chaque claim actuel ;
- chaque niveau de livraison supérieur à `documented` ;
- chaque conclusion fondée sur une source secondaire ;
- un échantillon des lots mécaniques plus les anomalies.

## Intégration

Un rapport accepté peut alimenter :

- `docs/audits/timeline.md` ;
- `docs/audits/name-lineage.md` ;
- `docs/audits/decisions.md` ;
- `docs/audits/contradictions.md` ;
- un futur dossier sous `docs/systems/` ou `docs/workflows/` ;
- le catalogue de besoins seulement si la distinction fait / idée est préservée.

L’intégration n’autorise aucune TaskNote ni mutation externe.
