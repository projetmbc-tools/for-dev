Building a thin copy of the source folder
-----------------------------------------

### What we want...

In our project above, there are some files only useful for the development of the code.

  1. Names using the pattern `x-...-x` indicate files or folders to be ignored by `git` (there are no such file or folder in the `src` folder but we could imagine using some of them).

  1. Names using the pattern `tool_...` are for files and folders to not copy into the final product, but at the same time to be kept by `git`.

  1. The `README.md` file used for `git` servers must also be used for the final product.


The final product built from the `src` folder must have the following name and structure.

~~~
+ texiteasy
    * __init__.py
    * escape.py
    * LICENSE.txt
    * README.md
~~~


### How to do that?

Here is how to acheive a selective copy of the `src` folder to the `texiteasy` one. We will suppose the use of the `cd` command to go inside the parent folder of `TeXitEasy` before launching the following script where we use instances of `Path` from `pathlib`.

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
    readme = Path('README.md')
)

project.update()
~~~

Here are some important points about the code above.

  1. `project`, `source`, `target` and `readme` follows the rules below.

      * The values of this arguments can also be strings (that will be converted to instances of `Path`).

      * The argument `readme` is optional contrary to `project`, `source` and `target`.

      * `project` is a complete path regarding the working directory when launching the file, but `source`, `target` and `readme` are relative to `project`.

  1. The argument `ignore` can be used even if the project doesn't use `git`. It can be either a string containing rules, or an absolute `Path` to a file containg rules (an absolute path allows to use the same rules for several projects). Let's see now how to define rules.

      * Empty lines are ignored (this allows a basic formatting of rules).

      * Each none empty line is internally stripped. This will indicate one rule for either a file or a folder.

      * A rule finishing by `/` is for a folder: internally the last `/` is removed such as to store the rule only for folders.

      * Each rule will be used with the method `match` of `pathlib.Path` (this is very basic).

  1. `usegit = True` asks also to ignore files and folders as `git` does (this action completes the rules defined in `ignore`). This setting implies that there isn't any uncommited file in the `src` folder (even if that files must be ignored).

  1. Errors and warnings are printed in the terminal and written verbosely in the file `TeXitEasy.src2prod.log` where `TeXitEasy` is the name extracted from the path `project`.
