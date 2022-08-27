this::
    date = 2022-08-28


abrev::
    currentstep = ¨exatempl/step-3


================================================================================
Modifier certains fichiers d'un squelette - Retour des dossiers path::``readme``
================================================================================

Le titre principal du fichier path::``prologue.md`` proposé par le squelette du dossier  path::``readme`` est de la forme verb::{{The Python module `cvnum`}}, or celui attendu pour ¨mathobj doit être verb::{{The monorepo `math-objects`}}.
Ceci s'obtient très facilement en ajoutant un fichier path::``prologue.md`` personnalisé comme ci-après.

dirtree::
    ---
    path = ¨currentstep/dir-mathobj.txt
    ---


Il faut retenir que ¨justcode empile les propositions faites en n'appliquant au final que la dernière proposition rencontrée. Dans notre cas, le fichier path::``prologue.md`` étant rencontré en dernier, ce sera celui-ci qui sera dans le dossier initialisé.
