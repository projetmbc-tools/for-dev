Only the source files to copy
-----------------------------

Sometimes, the final product is not just a "selective clone" of the folder `src`: for example, a final file may be the merging of several source files (the author of `src2prod` uses this technique to develop his `LaTeX` projects). In such a case, you can use the following method and attribute.

  1. The method `build` just looks for files to keep for the product folder without creating anything.

  1. After the use of `build`, the attribute `lof` is the list of all files to be kept for the folder `src` (`lof` is for `list of files`).

Here is an example of code that prints the list of source files to be kept for the final product.

~~~python
from src2prod import *

project = Project(
    name   = 'MockProject',
    source = Path('src'),
    target = Path('mockproject'),
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

This script run in a terminal gives the following output. Note that the list does not contain the path to the `README` file, this must be handled manually (see the `check_readme` and `copy_readme` methods of the class `Project`).

~~~
/full/path/to/MockProject/src/__init__.py
/full/path/to/MockProject/src/escape.py
/full/path/to/MockProject/src/LICENSE.txt
~~~
