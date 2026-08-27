---
title: Définitions de fin
status: active
date: 2026-08-27
---

# Definition of Done

## Fondation du dépôt

- [ ] baseline complète et vérifiée ;
- [ ] ancien arbre retiré de l’espace actif ;
- [ ] scope, autorités et confidentialité explicites ;
- [ ] briefs utilisables sans relire la conversation ;
- [ ] liens internes valides ;
- [ ] aucun secret ou contenu personnel inutile ;
- [ ] `git diff --check` propre ;
- [ ] deux commits locaux, aucun remote ni push.

## Audit individuel

- [ ] question et corpus bornés ;
- [ ] identité exacte de chaque objet ;
- [ ] toutes les sources attendues consultées ou marquées indisponibles ;
- [ ] chaque claim important possède une citation ;
- [ ] faits, hypothèses, idées et inconnues séparés ;
- [ ] contradictions conservées ;
- [ ] couverture et limites déclarées ;
- [ ] contre-audit parent terminé.

## Dossier système

- [ ] besoin et bénéficiaire ;
- [ ] responsabilité et langage ;
- [ ] faits possédés et non possédés ;
- [ ] cycle de vie, invariants et correction ;
- [ ] entrées, sorties, contrats et dépendances ;
- [ ] permissions et risques ;
- [ ] historique et noms ;
- [ ] état live ;
- [ ] niveau de livraison exact ;
- [ ] besoins non couverts.

## Architecture cible

- [ ] besoins validés avant solution ;
- [ ] statu quo et alternatives comparés ;
- [ ] scénarios réels testés ;
- [ ] coûts, risques et réversibilité explicites ;
- [ ] autorité de chaque fait ;
- [ ] cible marquée candidate jusqu’à validation ;
- [ ] décision explicite de Sofian ;
- [ ] condition de réexamen.

## Documentation VitePress

- [ ] build réel réussi ;
- [ ] recherche et navigation testées ;
- [ ] Mermaid rendu en clair et sombre ;
- [ ] responsive et réduction de mouvement ;
- [ ] liens et ancres valides ;
- [ ] aucune donnée sensible publiée ;
- [ ] distinction histoire / actuel / candidat / accepté visible ;
- [ ] URL réelle relue seulement après autorisation de déploiement.

## Niveaux de livraison autorisés

```text
discussed → proposed → documented → prototyped
→ technically_tested → integrated → exercised_real_case
→ user_accepted → operational
```

Aucun niveau ne peut être sauté par narration.
