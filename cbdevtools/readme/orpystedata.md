Using `orpyste` datas with `pytest`
----------------------------------

The author of this package uses [orpyste](https://github.com/bc-python-OLD-IT-WILL-BE-REMOVED/orpyste) to work with ready-to-make `PEUF` data files in his tests.

To avoid problem with `pytest`, a fixture `peuf_fixture` is proposed wich follows the convention that the name of the `PEUF` file is obtained by removing the prefix `test_` from the name of the testing file Here is a real example of use with the following partial tree structure.

~~~
+ TeXitEasy
    + src
        * __init__.py
        * escape.py
    + tests
        + escape
            + fstringit.peuf
            + test_fstringit.py

~~~


The `Python` testing file `test_fstringit.py` is associated to the `PEUF` file `fstringit.peuf` where the prefix
`test_` has been removed. Using the datas stored in this `PEUF` file becomes very easy: here is the code used where
`tests` is an intuitive dictionary version of the `PEUF` file.

~~~python
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
~~~
