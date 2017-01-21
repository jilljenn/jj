Problèmes d'algorithmique
=========================

Avec `Christoph Dürr <http://www-desir.lip6.fr/~durrc/>`_, j'anime le site `TryAlgo <http://tryalgo.org>`_, qui regorge de problèmes algorithmiques.

.. contents:: Table des matières
   :local:
   :backlinks: none

Apprendre à coder
-----------------

- Essayez une heure de code : `hourofcode.org/fr <http://hourofcode.org/fr>`_ (notamment pour les enfants)
- La plate-forme d'apprentissage `France-ioi <http://france-ioi.org>`_
- `JJ's Code Week </codeweek/>`_, du 8 au 14 décembre 2014
- `Stage de Python </algo/stage-python/>`_ pour lycéens (par `Science ouverte <http://scienceouverte.fr>`_ et `Prologin <#prologin>`_)


Sujets de TP
------------

.. toctree::
   :maxdepth: 1

   ../tp/index
   ../tp/cs/index


Concours de programmation
-------------------------

On vous donne un problème à résoudre (par ex. trouver un chemin dans un labyrinthe qui mène à la sortie), des contraintes sur les données du problème (la taille du labyrinthe) et vous devez coder un programme qui renvoie, pour une instance donnée en entrée respectant les contraintes, une solution.

Les limites de temps font que votre programme doit non seulement renvoyer une solution correcte, mais de plus dans un temps raisonnable.

Prologin
::::::::

Ouvert aux jeunes de 20 ans et moins : d'octobre à mai. Les sujets écrits des épreuves régionales couvrent des domaines variés de l'informatique théorique, par exemple :

- *amidakuji* : `The Final Problem <http://prologin.org/files/archives/2012/demi-finales/sujet/the-final-problem.pdf>`_ (+ `vidéo d'introduction <a href="http://youtu.be/VczJBIjPXds>`_, activez les sous-titres)
- algorithme du lièvre et de la tortue : `The Two-Ring Machine <http://prologin.org/files/archives/2013/demi-finales/sujet/two-ring-machine.pdf>`_
- 2-approximation du voyageur de commerce : `Distributions tempérées <http://prologin.org/files/archives/2014/demi-finales/sujet/distributions.pdf>`_
- jeux sur les arbres : `Quart de singe <http://prologin.org/files/archives/2012/demi-finales/sujet/quart-de-singe-bordeaux.pdf>`_
- contamination dans les arbres : `The Game <http://prologin.org/files/archives/2011/demi-finales/sujet/the-game.pdf>`_
- graphes dans certains jeux Nintendo : `Dance floor <http://prologin.org/files/archives/2011/demi-finales/sujet/dance-floor.pdf>`_
- algorithmes streaming : `Prologin Plays Pokémon <http://prologin.org/files/archives/2014/demi-finales/sujet/prologinplayspokemon.pdf>`_
- bin packing : `Death Note <http://prologin.org/files/archives/2012/demi-finales/sujet/death-note.pdf>`_
- ordonnancement de tâches : `The Shining <http://prologin.org/files/archives/2011/demi-finales/sujet/the-shining.pdf>`_
- couverture minimale : `MRKRPXZKRMTFRZ <http://prologin.org/files/archives/2012/demi-finales/sujet/mrkrpxzkrmtfrz.pdf>`_
- code de Huffman : `The Marchand Identity <http://prologin.org/files/archives/2013/demi-finales/sujet/marchand-identity.pdf>`_
- arbre couvrant minimal distribué : `The Imitation Game <http://prologin.org/files/archives/2013/demi-finales/sujet/the-imitation-game.pdf>`_
- à composante historique : `Enigma <http://prologin.org/files/archives/2013/demi-finales/sujet/enigma.pdf>`_
- d'autres problèmes en vrac : `MinisterMind <http://prologin.org/files/archives/2013/demi-finales/sujet/ministermind.pdf>`_, `Comic-Con <http://prologin.org/files/archives/2012/demi-finales/sujet/comic-con.pdf>`_, `Memento Somniare <http://prologin.org/files/archives/2011/demi-finales/sujet/memento-somniare.pdf>`_

ACM/ICPC
::::::::

Le concours ACM/ICPC est un concours de programmation en **C, C++ ou Java** à destination des étudiants en licence ou master. La particularité : 10 problèmes, 5 heures, 3 étudiants, 1 seul clavier par équipe. C'est terrible.

Pour s'entraîner :

.. toctree::
   :maxdepth: 1

   acm/index

- Le vivier d'exercices `UVa Online Judge <http://uva.onlinejudge.org>`_ et son outil pour tester ses fichiers de test `UVa Toolkit <http://uvatoolkit.com>`_
- La version polonaise `spoj.com <http://spoj.com>`_
- La version chinoise `poj.org <http://poj.org>`_
- Les `références bibliographiques <#bibliographie>`_ ci-dessous.

Autres concours
:::::::::::::::

Avec Alexis Comte et Stéphane Henriot, nous avons rédigé une `liste des différents concours de programmation <http://jill-jenn.net/codeweek/4-competitions.html>`_. En voici quelques-uns notables.

- `Google Code Jam <http://code.google.com/codejam/>`_ : concours annuel débutant en avril, composé d'excellents sujets parfois très difficiles.
- `Codeforces <http://codeforces.com>`_ : un site russe anglophone avec des concours fréquents d'excellente qualité (plusieurs par mois).

Bibliographie
:::::::::::::

Je ne recommande pas le Cormen que je trouve trop lourd, en revanche :

- `Éléments d'algorithmique <http://www-igm.univ-mlv.fr/~berstel/Elements/Elements.pdf>`_ de Beauquier, Berstel, Chrétienne (surnommé le BBC) : une référence pour les calculs de complexité et arbres équilibrés qui fait bien la distinction entre types abstraits (par ex. une file à priorité) et structures de données (par ex. un tas).
- *Algorithms* de Sedgewick : la seule référence d'une explication claire de l'algorithme de Knuth-Morris-Pratt.
- `Programmation efficace <http://tryalgo.org>`_ de Vie-Dürr : implémentations efficaces en Python.

La Faute à l'algo
-----------------

.. figure:: /_static/fautealgo.png
   :align: left

`La Faute à l'algo <http://fautealgo.fr>`_ est une émission de 6 minutes sur `Nolife <http://www.nolife-tv.com>`_ coréalisée avec Michel Blockelet, sur le rôle grandissant de l'algorithmique dans nos vies.

`Voir les épisodes. <http://fautealgo.fr>`_

.. isso-comments:: fr
