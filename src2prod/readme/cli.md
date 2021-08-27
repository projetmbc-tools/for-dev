Using a `CLI`
-------------

The project proposes one `CLI`, aka one "Command Line Interface", to update a project. Let's consider the following script `mycli.py`.

~~~python
from src2prod import cmdline

cmdline.update()
~~~

The following `Unix` terminal session shows how to use this basic script to update a project.


### What we have before

~~~
> ls
spkpb         src2prod
ignore.txt    mycli.py

> cat ignore.txt
tool_*/
tool_*.*

> ls spkpb
README.md     src
changes       tools
~~~


### How to use the tiny script

~~~
> python mycli.py --usegit --notsafe --readme='README.md' --ignore='ignore.txt' spkpb
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


### What we obtain after

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


### Help

You can have an help as usual in the `Unix` command line world.


~~~
> python mycli.py --help
Usage: cmdline.py [OPTIONS] PROJECT

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

  --notsafe      This flag allows to remove a none empty target folder.
  --help         Show this message and exit.
~~~
