# qantica
Un framework web basé sur flask pour les api rest

## Objectif

salut je suis Hydromel Victor Vaddely jeune dans le developpememnt logiciel.<br>
J'aime flask mais a mon grand regret il n'est pas tres utiliser et les raison son multiple.
premierement parcequ'il laisse le libre arbitre a son utilisateur sur le choix de son architecture, mais aussi sa methodologie ainsi que les different fonctionnalités a ajouter bref pour certains sa en fait trop de responsabilité, par contre d'autre le trouve pas tres adapter au grand projets, aux projet lier a la securité et blablabla.

enfin de compte je pense que le probleme ce trouve dans la comprehension de ce framework que je trouve fascinant alors je m'engage sur un chemin avanturieux avec flask en developpant un nouvelle framework web axé sur les api rest dont la base est flask.

moi et mes collaborateur de chez cosmosolver mettrons a disposition de tous un framework ou plutot un encapsuleur de flask semblable a django les liberant de tous configuration ardu dans le but de voir ce bel outil qu'est flask ce rependre dans nos projet.

## Architecture

- project_name (dossier racine du projet)
  - project_name (votre app)
    - __init__.py
    - models.py
    - views.py
    - test.py
  - config.py
  - urls.py
  - qmd.py
  - README.md
  - .gitignore

## utilisation

1. installer qantica

```bash
cosmosolver@engineer:~/workspace$ virtualenv env
cosmosolver@engineer:~/workspace$ . env/bin/activate
(env)cosmosolver@engineer:~/workspace$ pip install qantica
```

2. creer un projet avec qantica

```bash
(env)cosmosolver@engineer:~/workspace$ qant create projectname
(env)cosmosolver@engineer:~/workspace$ cd projectname
(env)cosmosolver@engineer:~/workspace/projectname$ ls
projectname/ qmd.py config.py urls.py README.md
```

3. lancer le projet

```bash
(env)cosmosolver@engineer:~/workspace/projectname$ python qmd.py run
```

4. creer une application

```bash
(env)cosmosolver@engineer:~/workspace/projectname$ qant create-app appname
(env)cosmosolver@engineer:~/workspace/projectname$ cd appname
(env)cosmosolver@engineer:~/workspace/projectname/appname$ ls
__init__.py models.py views.py test.py
```
