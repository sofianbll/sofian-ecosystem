---
title: Définitions de fin
status: active
date: 2026-08-27
---

# Definition of Done

> Les cases décrivent des gates vérifiables. L’état global et la couverture courante restent affichés dans `README.md`, `roadmap.md` et `docs/audits/coverage.md`.

## Fondation du dépôt — vérifiée

- [x] baseline complète et vérifiée ;
- [x] ancien arbre retiré de l’espace actif ;
- [x] scope, autorités et confidentialité explicites ;
- [x] briefs utilisables sans relire la conversation ;
- [x] liens internes valides ;
- [x] aucun secret ou contenu personnel inutile ;
- [x] `git diff --check` propre ;
- [x] checkpoint initial vérifié avec commits locaux sans remote ni push ; cette contrainte était bornée au lot de fondation et a ensuite été supersédée.

Cela prouve la fondation méthodologique, pas la couverture de l’écosystème.

## Audit individuel

Les six audits `AUD-001` à `AUD-006` satisfont ces gates documentaires ; cela ne vaut ni acceptation des dossiers système ni fonctionnement opérationnel.

- [x] question et corpus bornés ;
- [x] identité exacte de chaque objet ;
- [x] toutes les sources attendues consultées ou marquées indisponibles ;
- [x] chaque claim important possède une citation ;
- [x] faits, hypothèses, idées et inconnues séparés ;
- [x] contradictions conservées ;
- [x] couverture et limites déclarées ;
- [x] contre-audit parent terminé.

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

- [x] build réel réussi ;
- [ ] recherche et navigation testées ;
- [ ] Mermaid rendu en clair et sombre ;
- [ ] responsive et réduction de mouvement ;
- [x] liens locaux valides ;
- [x] gate anti-secrets/PII testée ; locators techniques publics explicitement acceptés ;
- [x] distinction histoire / actuel / candidat / accepté visible ;
- [x] URL réelle relue après autorisation de déploiement.

## Niveaux de livraison autorisés

```text
discussed → proposed → documented → prototyped
→ technically_tested → integrated → exercised_real_case
→ user_accepted → operational
```

Aucun niveau ne peut être sauté par narration.
