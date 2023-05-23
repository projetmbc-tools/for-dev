`README.md` piece-by-piece
--------------------------

You can write your `README.md` by typing small sections. Let's assume we have done this for our fictitious development project `MockProject` which now has the following tree structure.

~~~
+ MockProject
    + changes [...]

    + readme
        * about.md
        * about.yaml
        * cli.md
        * escape.md
        * prologue.md

    + src [...]

    + tests [...]

    * pyproject.toml
~~~


The special file `about.yaml` is used here to specify the order in which the different `MD` files are merged. Its contents were as follows.

~~~yaml
toc:
  - prologue
  - about
  - escape
  - cli
~~~

The construction of the new final product `mockproject` is very simple: we just specify the folder `readme` instead of a file for the `readme` argument. And that's it! See the code below where the class `Project` guesses that `Path('readme')` is a folder.

~~~python
from src2prod import *

project = Project(
    project = Path('mockproject'),
    source  = Path('src'),
    target  = Path('mockproject'),
    ignore  = '''
        tool_*/
        tool_*.*
    ''',
    usegit = True,
    readme = Path('readme')
)

project.update()
~~~
