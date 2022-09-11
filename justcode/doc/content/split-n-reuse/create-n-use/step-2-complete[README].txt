this::
    date = 2022-09-11


abrev::
    currentstep = ¨exatempl/step-2


===================================================
Compléter un squelette - Le cas du path::``readme``
===================================================

L'initialisation des dossiers similaires path::``readme`` des projets ¨cvnum et ¨mathobj s'appuient sur le squelette commun suivant
((
    La conception de ce squelette est similaire à ``changes`` présenté dans la section précédente.
)).

dirtree::
    ---
    path = ¨exatempl/readme/dirtree.txt
    ---


Le contenu du fichier path::``about.md`` est le suivant. Ceci va nous donner l'occasion de parler des paramètres attendus par un squelette, à savoir ici jinja::``author_name`` et jinja::``author_mail``.

jinja::
    ---
    path = ¨exatempl/readme/about.md
    ---


Commençons par faire évoluer l'initialisation du projet ¨cvnum. Pour cela, il faut créer la ¨nelle structure ci-après
((
    Nous verrons plus tard que l'initialisation "modifiée" est faisable même une fois le projet entâmé (ceci est intéressant pour la ¨maj d'un projet existant vis à vis d'une ¨tte ¨nelle version d'un squelette).
)).

dirtree::
    ---
    path = ¨currentstep/dir-cvnum.txt
    ---


On note l'ajout du fichier path::``last.md`` dans un dossier path::``readme`` : lors de l'initialisation, ¨justcode gardera tout le contenu du dossier path::``readme`` tout en le complétant avec le contenu proposé par le squelette. **En cas de conflit, ce sera ¨tjrs ce qui est proposé par le squelette qui sera ignoré.**
Finalement, l'initialisation se fait en utilisant la version ci-dessous du fichier path::``params.peuf`` qui tient compte des paramètres pour le squelette. Rien de plus à faire, et pour le projet ¨mathobj, la démarche est similaire. Facile ! Non ?.

peuf::
    ---
    path = ¨currentstep/params-cvnum.peuf
    ---


note::
    Les paramètres ont été définis localement dans chacun des blocs peuf::``changes`` et peuf::``readme``. On note certaines répétitions. Ceci est évitable facilement via le bloc bloc peuf::``global`` : voir la section cf::``?/goingfurther/global.txt``.
