---
title: Gates de revue et d’approbation
status: active
date: 2026-08-27
---

# Review gates

| Gate | Objet | Preuve requise | Autorité |
|---|---|---|---|
| 0 — Mandat | question, sources, lecture autorisée | scope et exclusions | Sofian |
| 1 — Sources | autorité, santé et accès | registre et conflits | Sofian + sources |
| 2 — Identités | alias, versions, entités distinctes | citations datées | Sofian |
| 3 — État | histoire, actuel, livraison | rapports contre-vérifiés | Jarvis puis Sofian |
| 4 — Besoins | résultats souhaités | situations réelles | Sofian |
| 5 — Architecture | option ou statu quo | alternatives, scénarios, risques | Sofian |
| 6 — Roadmap | ordre et tranches | dépendances et DoD | Sofian |
| 7 — Canonisation | écriture documentaire | preview des fichiers | Sofian |
| 8 — Exécution | mutation externe | cible, version, effet, retour | Sofian |

## Un gate n’autorise pas le suivant

- valider un audit n’autorise pas une architecture ;
- valider une architecture n’autorise pas une migration ;
- valider une roadmap n’autorise pas des TaskNotes ;
- valider des fichiers n’autorise pas un commit ;
- valider un commit n’autorise pas un remote ou un push ;
- valider un build n’autorise pas une publication.

## Paquet de décision TDAH

Chaque gate présente au maximum :

1. conclusion actuelle ;
2. trois preuves ou risques décisifs ;
3. une décision explicite avec conséquences.

Une correction arrête la cascade et ramène au dernier point réellement accepté.
