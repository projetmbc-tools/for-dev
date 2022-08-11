The `Python` module `cbdevtools`
================================


> **I beg your pardon for my english...**
>
> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.


Last version: 0.0.10-beta
-------------------------

This version **0.0.10-beta** was made on **2021-08-13** .


About `cbdevtools`
-----------------

This project is a *"Common Box of Dev Tools"* (the name comes also from "Christophe BAL Dev Tools"). `cbdevtools` proposes small scripts that can be helpful... at least for the author of this package. :-)


### Append one package to `sys.path`

The function `addfindsrc.addfindsrc` adds one project folder to the system path.


Let's see one fictive example with the following tree structure.

~~~
+ mymod
    + doc
    + dist
    + src
        * __init__.py
        * ...
    + tools
        + debug
            * cli.py
~~~

The `Python` script `tools/debug/cli.py` can easily load the local
`Python` module `src` thanks to the module `addfindsrc` as it is shwon in the following code.

~~~python
from cbdevtools.addfindsrc import addfindsrc

addfindsrc(
    file    = __file__,
    project = 'mymod',
)

from src import *
~~~

If you need to have the path of the project added, just use the value returned by `addfindsrc.addfindsrc`.

---
***WARNING!*** *The directory of the project to add must contain the file `__file__`.*


### Using `orpyste` datas with `pytest`


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