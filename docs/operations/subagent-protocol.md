---
title: Protocole subagents
status: active
date: 2026-08-27
---

# Protocole subagents

## Contrat minimal du prompt

Tout prompt de worker contient :

1. objectif unique ;
2. contexte suffisant ;
3. chemins ou identifiants exacts ;
4. période et exclusions ;
5. sources prioritaires ;
6. skills obligatoires ;
7. interdiction de mutation et de secrets ;
8. format de sortie ;
9. critères de fin ;
10. niveau de détail attendu.

## Résoudre le Guide et les skills

- Guide : `/Users/sofian/Documents/00-Inbox/Guide-ultime-ingenierie-logicielle.pdf`.
- Charger le socle défini dans `AGENTS.md`.
- Charger les références pertinentes via `software-engineering-lifecycle` plutôt que le PDF entier lorsque le brief cible un chapitre.
- Charger ensuite le spécialiste de la source : `notion`, `docx`, `opencode-history`, `obsidian`, `grounded-citations` ou un skill système.

## Résoudre un `source_id`

1. lire `docs/audits/source-registry.md` ;
2. trouver l’ID exact ;
3. utiliser uniquement la source, période et méthode indiquées ;
4. vérifier le chemin ou l’accès ;
5. déclarer `blocked` au lieu de deviner.

## Niveaux de détail

- **Chat :** verdict, trois preuves/risques et prochaine décision.
- **Rapport :** claims atomiques complets, locators, citations, couverture et limites.
- **Raw data :** jamais dans le chat ; conserver seulement si un artefact séparé est autorisé.

## Règles d’exécution

- Lire les instructions les plus proches de la source.
- Utiliser les APIs, Git ou bases en mode read-only.
- Ne jamais imprimer une valeur secrète.
- Commencer par les métadonnées, puis lire le minimum pertinent.
- Paginer les corpus longs et enregistrer le compte traité.
- Préserver l’orthographe des identifiants.
- Ne pas présenter un résultat `completed` comme preuve.
- Ne pas proposer la cible pendant un audit historique.

## Format de retour

```yaml
workstream: AUD-xxx
coverage:
  expected: N | unknown
  inspected: N
  excluded: N
  blocked: N
claims:
  - id: CLM-...
    statement: ...
    state: ...
    source_id: ...
    locator: ...
    confidence: ...
contradictions: []
unknowns: []
source_health: []
conclusion: ...
```

Le rapport humain commence par un verdict bref, puis les preuves. Aucun transcript brut.

## Écriture éventuelle

Par défaut, le worker retourne sa réponse sans écrire. Une écriture est permise seulement si le parent et Sofian ont nommé un chemin isolé exact. Le worker ne modifie jamais le catalogue, la timeline globale ou un autre workstream. Le parent intègre.

## Arrêts obligatoires

- identité ambiguë ;
- source décisive absente ;
- besoin de lire un secret ;
- volume ou pagination sans dénominateur ;
- contradiction changeant le sens du brief ;
- mutation requise ;
- correction utilisateur invalidant la direction.
