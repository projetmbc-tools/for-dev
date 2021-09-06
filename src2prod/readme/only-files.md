Only the source files to copy
-----------------------------

Sometimes the final product is not just a "selective clone" of the `src` folder: for example, it can be a melting of several source files in a single final one (the author of `src2prod` uses this technic to develop his `LaTeX` projects). In such a case, you can use the following method and attribut.

  1. The method `build` just looks for the files to keep for the `texiteasy` folder.

  1. The attribut `lof` is the list of all files to keep in the `src` folder (`lof` is for `list of files`).

Here is an example of code printing the list of only the source files to keep.

~~~python
from src2prod import *

project = Project(
    name   = 'TeXitEasy',
    source = Path('src'),
    target = Path('texiteasy'),
    ignore = '''
        tool_*/
        tool_*.*
    ''',
    usegit = True,
    readme = Path('README.md')
)

project.build()

for f in project.lof:
    print(f)
~~~

This script gives the following output in a terminal. Note that the list doesn't contain the path of the `README` file, this last one must be manage by hand (see the methods `check_readme` and `copy_readme` of the class `Project`).

~~~
/full/path/to/TeXitEasy/src/__init__.py
/full/path/to/TeXitEasy/src/escape.py
/full/path/to/TeXitEasy/src/LICENSE.txt
~~~
