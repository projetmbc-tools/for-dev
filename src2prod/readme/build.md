Building a thin copy of the source folder
-----------------------------------------

### What we want...

In the project `mockproject`, there are some files that are only useful for code development.

  1. Names using the pattern `x-...-x` indicate files, or folders that `git` must ignore (there are no such files, or folders in the `src` directory, but we could imagine using some).

  1. Names using the pattern `tool_...` are for files, and folders not to be included in the final product, but which `git` must retain.

  1. The `README.md` file used for `git` servers must also be included in the final product.


By copying files, we wish to add one new folder `mockproject` to obtain the following structure.

~~~
+ MockProject
    + changes [...]

    + mockproject
        * __init__.py
        * mockthis.py
        * LICENSE.txt
        * README.md

    + src [...]

    + tests [...]

    * pyproject.toml
    * README.md
~~~


### How to do that?

Here is how to make a selective copy from the sub-directory `src` to the sub-folder `mockproject`. We will assume that the `cd` command has been used beforehand, so that running the `Python` scripts is done from the development folder `MockProject` (note the use of instances of `pathlib.Path`).

~~~python
from src2prod import *

project = Project(
    project = Path('MockProject'),
    source  = Path('src'),
    target  = Path('mockproject'),
    ignore  = '''
        tool_*/
        tool_*.*
    ''',
    usegit = True,
    readme = Path('README.md')
)

project.update()
~~~

Here are the important points about the above code.

  1. `project`, `source`, `target` and `readme` follow the rules below.

      * The values of these arguments can also be strings (which will be converted to instances `Path`).

      * The argument `readme` is optional unlike `project`, `source` and `target`.

      * `project` is a full path to the source development directory when the `Python` script is launched, but `source`, `target` and `readme` are relative to `project`.

  1. The argument `ignore` can be used even if the project does not use `git`. It can be either a string containing rules, or an absolute `Path` to a file containing rules (an absolute path allows the use of the same rules for multiple projects). Now let's see how to define rules.

      * Empty lines are ignored (this allows a basic formatting of rules).

      * Each none empty line is internally stripped. This will indicate one rule for either a file, or a folder.

      * A rule finishing by `/` is for a folder: internally the last `/` is removed such as to store the rule only for folders.

      * Each rule will be used with the method `match` of `pathlib.Path` (it's very basic, but quite powerful).

  1. `usegit = True` asks to ignore files, and folders as `git` does, if this feature is activated for the development directory (this action completes the rules defined with the argument `ignore`).

  1. Errors and warnings are printed in the terminal, and also written verbatim to the file `mockproject.src2prod.log` where `mockproject` is the name taken from the path specified via `project`.
