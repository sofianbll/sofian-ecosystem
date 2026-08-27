---
title: Baseline documentaire initiale
status: archived
snapshot_date: 2026-08-25
extracted_at: 2026-08-27T16:17:54+02:00
source_commit: e331ee4e0a1006f813cf89f3a5c6f6bb262d2d29
source_repository: /Users/sofian/Developer/10-Personal/sofian-ecosystem
---

# Baseline documentaire initiale

## Rôle

Cette baseline préserve **byte-for-byte** l’intégralité des fichiers suivis dans le premier commit de `sofian-ecosystem`, avant la création du nouveau système d’audit.

Elle constitue une preuve historique et un point de retour. Elle ne valide pas les affirmations contenues dans les documents archivés et ne remplace aucune source canonique externe.

## Périmètre

- commit source complet : `e331ee4e0a1006f813cf89f3a5c6f6bb262d2d29` ;
- date du commit source : `2026-08-25T17:57:47+02:00` ;
- fichiers extraits : **73** ;
- octets extraits : **255 869** ;
- racine des payloads : `files/` ;
- manifeste : `MANIFEST.sha256` ;
- `.git/` exclu : l’historique Git reste dans le dépôt lui-même.

## Méthode et vérification

Chaque payload a été lu depuis le blob Git du commit source, écrit sans modification sous son chemin original dans `files/`, puis comparé à nouveau octet par octet. `MANIFEST.sha256` enregistre une empreinte SHA-256 pour chacun des 73 fichiers.

Aucune source externe, aucun vault, aucun service et aucun fichier du commit source n’a été modifié pendant cette extraction.

## Statut documentaire

- **Persisté** ne signifie pas **validé**.
- Les statuts historiques, contradictions et annonces de livraison restent à réexaminer depuis leurs sources réelles.
- Le système actif qui remplace cette fondation est décrit à la [racine du dépôt](../../../README.md).
