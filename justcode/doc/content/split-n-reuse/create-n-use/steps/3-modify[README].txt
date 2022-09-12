this::
    date = 2022-09-11


abrev::
    currentstep = ¨exatempl/steps/3


=================================================================
Modifier des fichiers d'un squelette - Retour du path::``readme``
=================================================================

Le titre principal du fichier path::``prologue.md`` proposé par le squelette du dossier  path::``readme`` est de la forme verb::{{The Python module `cvnum`}}, or celui attendu pour ¨mathobj doit être verb::{{The monorepo `math-objects`}}. Un moyen simple d'obtenir ceci consiste à ajouter un fichier path::``prologue.md`` personnalisé comme ci-après.

dirtree::
    ---
    path = ¨currentstep/dirtree.txt
    ---


Il faut retenir que ¨justcode empile les propositions faites en n'appliquant au final que la dernière proposition rencontrée
((
    Ce fonctionnement est celui des feuilles de style ¨css.
)).
Dans notre cas, le fichier path::``math-objects/readme/prologue.md`` étant rencontré en dernier, ce sera celui-ci qui sera employé pour initiliaser le dossier.
