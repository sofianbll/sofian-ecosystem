---
title: Modèle de preuve
status: active
date: 2026-08-27
---

# Modèle de preuve

## États d’une affirmation

| État | Sens |
|---|---|
| `current_canon` | confirmé dans la source canonique actuelle |
| `live_implementation` | observé dans le code, la configuration, l’API ou le runtime réel |
| `historical_intent` | affirmé par une source datée, sans prétendre être actuel |
| `historical_execution` | action ou résultat prouvé à une date donnée |
| `user_decision` | décision explicite de Sofian dans un contexte compris |
| `user_idea` | envie ou piste, pas un engagement |
| `memory_lead` | trouvé uniquement dans une mémoire secondaire |
| `hypothesis` | interprétation à réfuter ou confirmer |
| `contradicted` | sources incompatibles, aucune fusion silencieuse |
| `unknown` | preuve insuffisante ou inaccessible |

## Structure d’un claim

```yaml
id: CLM-<workstream>-<numéro>
statement: formulation atomique
state: current_canon | live_implementation | historical_intent | ...
subject: identité littérale
valid_time: période décrite
recorded_time: date de la source
source_id: SRC-...
locator: chemin:ligne | commit:path | session_id:message_id | API/version
quote_or_observation: extrait minimal ou résultat vérifiable
confidence: high | medium | low
contradicts: []
review_status: unreviewed | checked | accepted | rejected
reviewer: Jarvis | Sofian
```

## Règles temporelles

Toujours distinguer le temps du fait, le temps d’enregistrement et le temps de vérification. Une mtime, une date de frontmatter et un commit peuvent décrire trois événements différents.

## Citation locale

Format recommandé :

```text
[SRC-ID — chemin ou session — date — lignes/commit/message]
```

Exemples :

- `[SRC-OBS-OLD — Backend/Resources/…md — commit 5ddc27b — lignes 20–35]`
- `[SRC-OPENCODE — ses_… — 2026-06-27 — extrait visible]`
- `[SRC-LIVE — git/status/API — vérifié 2026-08-27]`

## Niveaux de livraison

| Niveau | Preuve minimale |
|---|---|
| `discussed` | conversation exacte |
| `proposed` | option explicitement formulée |
| `documented` | artefact présent et lisible |
| `prototyped` | artefact exécutable borné |
| `technically_tested` | commande et sortie réelles |
| `integrated` | relié aux vraies frontières |
| `exercised_real_case` | cas réel borné traversé |
| `user_accepted` | validation explicite après compréhension |
| `operational` | usage réel maintenu et vérifiable |

Une suite de tests ne monte pas automatiquement le niveau produit.

## Preuve négative

- absence dans un premier résultat ≠ absence du corpus ;
- aucune trace retrouvée ≠ action jamais réalisée ;
- fichier existant ≠ projet actif ;
- mémoire silencieuse ≠ besoin absent ;
- cible vide ≠ statu quo accepté.

## Review

Le reviewer vérifie au minimum identité, source, citation, temps, portée de la conclusion, alternatives ou contradictions et niveau de livraison.
