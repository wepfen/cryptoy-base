# Maths 2600 - Cryptoy

Ce repository contient le code à compléter pour les exercices de TPs de la dernière session sur le thème de la cryptographie.

## Mise en place

Ce projet nécessite l'installation de [poetry](https://python-poetry.org/), un outil de gestion de dépendance python plus haut niveau que `pip`.

Vous pouvez suivre la documentation pour installer poetry: [Introduction | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) ⏳ 4m

Après installation, placez vous dans le repertoire du projet et lancez la commande suivante:

```bash
poetry install
```

Vous pouvez ensuite activer le script `.bashrc` pour activer l'environnement virtuel python du projet:

```bash
source .bashrc
```

## Instructions

Tous les tests définis dans `tests/*` qui doivent passer après votre implémentation.

Vous pouvez lancer tous les tests via la commande `python -m pytest`.

Ou bien lancer un seul test via la commande `python -m pytest -k [nom_du_test]`

## Modalité de rendu

Le rendu se fera via la méthode des merge requests détaillée dans [le README du repository Arithmatoy](https://gitlab.com/maths-2600/arithmatoy-base).
