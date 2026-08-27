---
title: Confidentialité et publication
status: active
date: 2026-08-27
publication_mode: private-first
---

# Confidentialité

## Décision actuelle

La documentation est construite et validée **en privé**. L’hébergement sera décidé plus tard. Le modèle public de StudioFlow ne s’applique pas automatiquement.

## Classes de données

| Classe | Traitement documentaire |
|---|---|
| Architecture et décisions non sensibles | citation et synthèse possibles |
| Chemins locaux | permis dans le corpus privé, à expurger avant partage |
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

## Gate de publication futur

Avant tout partage ou déploiement :

1. choisir public expurgé, privé authentifié ou local ;
2. construire un inventaire des pages et assets ;
3. scanner secrets, chemins, PII et dépendances externes ;
4. vérifier les Mermaid et sources embarquées ;
5. relire manuellement les pages sensibles ;
6. obtenir l’accord exact de Sofian ;
7. déployer puis relire l’URL réelle.

Aucun remote, action ou hébergement n’est configuré dans cette fondation.
