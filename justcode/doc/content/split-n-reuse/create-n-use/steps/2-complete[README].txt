this::
    date = 2022-10-18


abrev::
    currentstep = ¨exatempl/steps/2


================================================
Compléter un patron - Le cas du path::``readme``
================================================

L'initialisation des dossiers similaires path::``readme`` des projets ¨cvnum et ¨mathobj s'appuient sur le patron commun suivant
((
    La conception de ce patron est similaire à ``changes`` présenté dans la section précédente.
)).

dirtree::
    ---
    path = ¨exatempl/readme/dirtree.txt
    ---


Le contenu du fichier path::``about.md`` est le suivant. Ceci va nous donner l'occasion de parler des ¨params attendus par un patron, à savoir ici jinjang::``author_name`` et jinjang::``author_mail``.

jinjang::
    ---
    path = ¨exatempl/readme/about.md
    ---


Commençons par faire évoluer l'initialisation du projet ¨cvnum. Pour cela, il faut créer la ¨nelle structure ci-après
((
    Nous verrons plus tard que l'initialisation "modifiée" est faisable même une fois le projet entâmé.
    Ceci est intéressant pour la ¨maj d'un projet existant vis à vis d'une ¨tte ¨nelle version d'un patron.
)).

dirtree::
    ---
    path = ¨currentstep/dirtree.txt
    ---


On note l'ajout du fichier path::``last.md`` dans un dossier path::``readme`` : lors de l'initialisation, ¨justcode gardera tout le contenu du dossier path::``readme`` tout en le complétant avec le contenu proposé par le patron. **En cas de conflit, ce sera ¨tjrs ce qui est proposé par le patron qui sera ignoré.**
Finalement, l'initialisation se fait en utilisant la version ci-dessous du fichier path::``params.peuf`` qui tient compte des ¨params pour le patron. Rien de plus à faire, et pour le projet ¨mathobj, la démarche est similaire. Facile ! Non ?.

peuf::
    ---
    path = ¨currentstep/params.peuf
    ---


note::
    Les ¨params ont été définis localement dans chacun des blocs peuf::``changes`` et peuf::``readme``. On note certaines répétitions. Ceci est évitable facilement via le bloc peuf::``main`` : voir la section cf::``?/goingfurther/global.txt``.
