---
id: AUD-004
title: Hermes et ourmem
status: brief_ready
date: 2026-08-27
owner: Jarvis
output_path: none
source_ids:
  - SRC-HERMES
  - SRC-OURMEM
---

# AUD-004 — Hermes et ourmem

## Mission unique

Reconstituer les décisions et travaux Hermes liés à Sofian Ecosystem, puis déterminer ce que la mémoire ourmem apporte réellement comme contexte secondaire sans la traiter comme vérité opérationnelle.

## Sources obligatoires

1. sessions Hermes exactes via `session_search` ;
2. session du chantier commencée le 2026-08-19 et reprises liées ;
3. sessions Clarify, mémoire, StudioFlow et autres résultats uniquement lorsqu’ils modifient l’écosystème ;
4. MCP ourmem en lecture ;
5. état live Hermes et configuration seulement si la question l’exige, sans exposer de secret ;
6. documentation officielle Hermes pour toute capacité actuelle.

## Questions

1. Quelles décisions de méta-architecture Sofian a-t-il réellement acceptées, corrigées ou rouvertes ?
2. Quels artefacts et mutations ont été effectués dans chaque session ?
3. Quels niveaux de livraison ont été annoncés et lesquels sont prouvés ?
4. Comment Hermes, Jarvis, Bots, skills, mémoire et orchestration ont-ils été distingués ou confondus ?
5. Quels souvenirs ourmem sont pertinents, frais et corroborés ?
6. Quelles limites d’accès, quota ou fraîcheur empêchent un audit complet ?

## Méthode et skills

Charger le socle obligatoire du dépôt, puis `cross-agent-session-handoff`, `personal-system-reconciliation`, `hermes-agent`, `ourmem` et `grounded-citations`. Pour toute capacité Hermes actuelle, les docs officielles sont prioritaires.

## Règles ourmem

- Une mémoire est `memory_lead` jusqu’à corroboration.
- Ne pas stocker, mettre à jour, partager ou supprimer de mémoire.
- Si la recherche embedding échoue, documenter le blocage ; ne pas boucler.
- Ne pas ingérer les sessions ou documents pendant cet audit.

## Règles Hermes

- Utiliser les liens `@session:` comme provenance.
- Lire les messages autour du vrai checkpoint.
- Distinguer conversation, résultat d’outil et état externe actuel.
- Les anciennes explications Hermes sont vérifiées contre les docs officielles actuelles si elles portent sur une capacité produit.

## Découpage parallèle possible

- Worker A : session architecture du 19–25 août ;
- Worker B : sessions Clarify et corrections ;
- Worker C : sessions mémoire / Hermes ;
- Worker D : ourmem, uniquement mémoire secondaire ;
- Parent : décisions et contradictions.

## Sortie

Utiliser `templates/audit-report.md` et retourner le rapport dans la session. Aucune écriture dans le dépôt par défaut.

## Definition of Done

- [ ] sessions attendues et liens enregistrés ;
- [ ] décisions utilisateur séparées des recommandations ;
- [ ] mutations et résultats live relus ;
- [ ] claims ourmem corroborés ou marqués secondaires ;
- [ ] limites de quota et fraîcheur visibles ;
- [ ] aucune mémoire ou configuration modifiée.
