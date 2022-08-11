XXX
-----------------------

    :return: an instance of ``ReadBlock`` associated to a path::``peuf``
             file automatically named.
warning::
    The name of the path::``peuf`` file is obtained by removing the prefix
    path::``test_`` from the name of the testing file (see the ¨tech ¨doc
    of ``peuf_fixture`` for a concrete example).

Here is a real example of use with the following partial tree structure.

tree-dir::
    + TeXitEasy
        + src
            * __init__.py
            * escape.py
        + tests
            + escape
                + fstringit.peuf
                + test_fstringit.py

The ¨python testing file path::``test_fstringit.py`` is associated
to the path::``PEUF`` file path::``fstringit.peuf`` where the prefix
path::``test_`` has been removed. Using the datas stored in this
path::``PEUF`` file becomes very easy: here is the code used where
``tests`` is an intuitive ¨dict version of the path::``PEUF`` file.

python::
    from cbdevtools import *

    addfindsrc(
        file    = __file__,
        project = 'TeXitEasy',
    )

    from src.escape import fstringit

    def test_latex_use_fstringit(peuf_fixture):
        tests = peuf_fixture(__file__)

        for infos in tests.values():
            found  = fstringit(infos['source'])
            wanted = infos['fstring']

            assert wanted == found
