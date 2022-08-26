this::
    date = 2022-08-26


abrev::
    currentstep = ¨exatempl/step-2


=============================================================
Compléter un squelette - Le cas des dossiers path::``readme``
=============================================================

L'initialisation des dossiers path::``readme`` des projets ¨cvnum et ¨mathobj s'appuient sur le squelette suivant
((
    La conception de ce squelette est similaire à ``changes`` présenté dans la section précédente.
)).

dirtree::
    ---
    path = ¨exatempl/dir-readme.txt
    ---


Pour faire évoluer l'initialisation du projet ¨cvnum, il faut créer la ¨nelle structure ci-après
((
    Nous verrons plus tard que l'initialisation "modifiée" est faisable même une fois le projet entâmé.
)).

dirtree::
    ---
    path = ¨currentstep/dir-cvnum.txt
    ---


On note l'ajout du fichier path::``last.md`` dans un dossier path::``readme``. Lors de l'initialisation, ¨justcode gardera tout le contenu du dossier path::``readme`` tout en le complétant avec le contenu proposé par le squelette. En cas de conflit, ce sera ¨tjrs ce qui est proposé par le squelette qui sera ignoré.
Finalement, l'initialisation se fait en utilisant la version ci-dessous du fichier path::``justcode.peuf``. Rien de plus à faire.

peuf::
    ---
    path = ¨currentstep/justcode-cvnum.peuf
    ---


Pour le projet ¨mathobj, la démarche est similaire. Facile ! Non ?
