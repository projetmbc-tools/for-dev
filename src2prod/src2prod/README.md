The `Python` module `src2prod`
==============================

> **I beg your pardon for my english...**
>
> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.


About `src2prod`
----------------

This module allows to develop a project within a source folder and to publish the final product in another folder, this last directory being a "thin" version of the source one. If you use `git`, this module can talk with it to do a better job.

> We give detailed examples using `Python`, and then this document ends with an explanation of how to use `python -m src2prod` in a terminal.


The example used for this short tutorial
----------------------------------------

We will consider a fictitious development project `MockProject` with the following tree structure.

~~~
+ MockProject
    + changes
        + 2022
            * 12.txt
        * LICENSE.txt
        * x-todo-x.txt

    + src
        * __init__.py
        * LICENSE.txt
        * mockthis.py
        + tool_config
            * escape.yaml
        * tool_debug.py
        * tool_escape.py

    + tests
        + mockthis
            * escape.yaml
            * test_escape.py

    * pyproject.toml
    * README.md
~~~


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


The special file `about.yaml` is used to specify the order in which the different `MD` files are merged. Its contents were as follows.

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


Working in a terminal
---------------------

The project provides a `CLI`, aka a `Command Line Interface`, for updating a project. The following `Unix` terminal session shows how to use this feature.


#### What we have before

~~~
> ls
spkpb         src2prod
ignore.txt

> cat ignore.txt
tool_*/
tool_*.*

> ls spkpb
README.md     src
changes       tools
~~~


#### How to use `src2prod`

~~~
> python -m src2prod --usegit --notsafe --readme='README.md' --ignore='ignore.txt' spkpb
---------------
"spkpb": UPDATE
---------------

1) The log file used will be :
   "spkpb/spkpb.src2prod.log".
2) External "README" file to use:
   "spkpb/README.md".
3) Ignore rules in the file:
   "ignore.txt"
4) Checking "git".
5) Working in the branch "master".
6) Starting the analysis of the source folder:
   "spkpb/src".
7) 21 files found using the rules from "ignore".
8) Removing unwanted files using "git".
9) 10 files found using "git". 11 new files ignored thanks to "git".
10) Target folder has been created:
    "spkpb/spkpb".
11) Copying 10 files from source to target.
12) "README.md" added to the target.
13) Target folder updated.
~~~


#### What we obtain after

~~~
> ls spkpb
README.md     spkpb.src2prod.log
src           changes
spkpb         tools

> ls spkpb/spkpb/*
spkpb/spkpb/LICENSE.txt        spkpb/spkpb/__init__.py
spkpb/spkpb/problems.py        spkpb/spkpb/README.md
spkpb/spkpb/base.py            spkpb/spkpb/timer.py

spkpb/spkpb/speaker:
__init__.py         log.py
term.py             allinone.py
spk_interface.py
~~~


#### Help

You can have an help as usual in the `Unix` command line world.

~~~
> python -m src2prod --help
Usage: __main__.py [OPTIONS] PROJECT

  Update your "source-to-product" like projects using the Python module
  src2prod.

  PROJECT: the path of the project to update.

Options:
  --src TEXT     Relative path of the source folder of the project. The
                 default value is "src".

  --target TEXT  Relative path of the targer folder of the project. The
                 default value "", an empty string, indicates to use the name,
                 in lower case, of the project.

  --ignore TEXT  Path to a file with the rules for ignoring files in addition
                 to what git does. The default value "", an empty string,
                 indicates to not use any rule.

  --usegit       This flag is to use git.
  --readme TEXT  Relative path of an external "README" file or "readme"
                 folder. The default value "", an empty string, indicates to
                 not use any external "README" file.

  --notsafe      TO USE WITH A LOT OF CAUTION! This flag allows to remove a
                 none empty target folder.

  --help         Show this message and exit.
  ~~~