`README.md` part by part
------------------------

You can write you `README.md` typing small section like parts as it is the case for the `README.md` you are reading. The `src2prod` project had merly the following partial tree structure on August 22, 2021.

~~~
+ src2prod
    + changes
        * ...

    + readme
        * about.peuf
        * build.md
        * cli.md
        * example-used.md
        * only-files.md
        * prologue.md
        * readme-splitted.md

    + src
        * ...
    
    * README.md
    * ...
~~~

This section has been written inside the file `readme-splitted.md`. The special file `about.peuf` allows to indicate the order to use to merge the different `MD` files. Its content was the following one.

~~~
toc::
    + prologue
    + example-used
    + build
    + only-files
    + readme-splitted
    + cli
~~~

The way used to build the source of `src2prod` is very simple: we just indicate the folder `readme` instead of a file for the argument `readme`. That's all! See the code below.

~~~python
from src2prod import *

project = Project(
    project = Path('TeXitEasy'),
    source  = Path('src'),
    target  = Path('texiteasy'),
    ignore  = '''
        tool_*/
        tool_*.*
    ''',
    usegit = True,
    readme = Path('readme')
)

project.update()
~~~
