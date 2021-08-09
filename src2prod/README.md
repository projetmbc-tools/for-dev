The `Python` module `src2prod`
==============================


> **I beg your pardon for my english...**
>
> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.


About `src2prod`
----------------

This module is useful for people who like to use directly a `src` folder to develop projects and to publish the final product in another folder wich is a "thin" version of the `src` folder. If you use `git`, this module will talk with it to do a precise job. 


### One example - A `Python` project

#### What we have...

Let's consider a project of the author named [`TeXitEsay`](https://github.com/projetmbc/tools-for-latex/tree/master/TeXitEasy) which had the more or less following tree structure on August 8, 2021 (this was the very begining of the project).

~~~
+ changes
    + 2021
        * 08.txt
    * LICENSE.txt
    * x-todo-x.txt
+ src
    * __init__.py
    * escape.py
    * LICENSE.txt
    + tool_config
        * escape.peuf
    * tool_debug.py
    * tool_escape.py
+ tests
    + escape
        * escape.peuf
        * fstringit.peuf
        * test_fstringit.py
        * test_escape.py
* about.peuf
* pyproject.toml
* README.md
~~~


#### What we want...

In the tree above, we just use some files when developping the code.

  1. Names using the pattern `x-...-x` indicate files or folders to be ignored by `git` (there are no such file or folder in the `src` folder but we could imagine using it).

  1. Names using the pattern `tool_...` are for files or folders to be ignored in the final product but that are not ignored by `git`.


The final product built from the `src` folder must have the following name and structure. 

~~~
+ texiteasy
    * __init__.py
    * escape.py
    * LICENSE.txt
~~~


#### How to do that?

Here is how to acheive a whole selective copy of `src` folder to `texiteasy` one. We will suppose the use of the `cd` command to go inside `TeXitEasy` before using the following script.

~~~python
from src2prod import *

builder = Builder(
    source = 'src'
    target = 'texiteasy'
    ignore = '''
        tool_*/
        tool*.*
    ''',
    usegit = True
)

builder.update()
~~~

Here are some important points about the code above.

  1. The rules follow the `glob` grammar with one rule by line.

  1. Thanks to `usegit = True`, ignored files and folders by `git` will be also ignored for the update of the target.

  1. `usegit = True` also allows to only apply real changes comparing to the last commit in the active branch: creation, deletion or update of files and folders will be done only when it is necessary.


<!-- :tutorial-START: -->
<!-- :tutorial-END: -->


<!-- :version-START: -->
<!-- :version-END: -->
