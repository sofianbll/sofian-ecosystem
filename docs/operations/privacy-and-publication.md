---
title: Confidentialité et publication
status: active
date: 2026-08-27
publication_mode: public_temporarily_accepted
---

# Confidentialité

## Décision actuelle

Le dépôt et GitHub Pages restent **publics pour l’instant**, par décision explicite de Sofian le 2026-08-28 (`SRC-HERMES`, session `145c806b6027`, locator `63985`). Cette décision accepte les locators techniques déjà publiés ; elle n’autorise jamais un secret, une clé, un token ou une PII directe.

La gate automatique `scripts/check_publication.py` bloque désormais les motifs évidents de secrets et PII avant le build. Les chemins locaux et adresses de réseau privé restent des avertissements visibles, conformément à la décision actuelle.

## Classes de données

| Classe | Traitement documentaire |
|---|---|
| Architecture et décisions non sensibles | citation et synthèse possibles |
| Chemins locaux | autorisés temporairement dans le corpus public comme locators ; avertissement CI |
| Identité, santé, famille, finance, juridique | minimisation stricte ; pointer vers la source |
| Emails, appels, transcriptions | lire seulement si le besoin d’audit le justifie |
| Secrets, tokens, clés, mots de passe | lecture et copie interdites |
| Historiques agents | outil spécialisé, texte visible seulement, redaction |
| Mémoire sémantique | piste secondaire, jamais raw dump |

## Principes

- Collecter le minimum nécessaire à la décision.
- Préférer une abstraction vérifiable à une donnée personnelle reproduite.
- Conserver une provenance sans exposer le contenu sensible.
- Ne pas inclure de signed URL ou de valeur d’environnement.
- Une donnée accessible n’est pas automatiquement pertinente.
- Une archive privée ne devient pas publiable par défaut.

## Gate de publication courante

Avant tout partage ou déploiement :

1. exécuter les tests de la gate de publication ;
2. bloquer secrets et PII directes ;
3. afficher les avertissements de locators techniques sans révéler de valeur sensible ;
4. obtenir l’accord exact couvrant commit, push et publication ;
5. construire puis relire le workflow, le déploiement et les routes réelles.

État vérifié le 2026-08-28 : huit commits et 991 snapshots texte inspectés sans clé privée, token, secret assigné ou email détecté ; le dépôt, le workflow et les routes GitHub Pages sont accessibles.
