Reading the datas line by line
==============================

Let's consider the following file where `book` is a container, `general` is a classical key-value content using the separator `=` and `resume` has a verbatim content.  

```
book::
    general::
        author = M. Nobody
        title  = Does this book have a title ?
        date   = 2012, May the 1st

    resume::
        This book is an ode to the passing time...
        A challenging thinking.
```


Let's suppose that `user/example.peuf` is the path of our storing file. Using the following code shows how to read our datas.

```python
from pathlib import Path
import pprint

from orpyste.data import Read

with Read(
    content = Path("user/example.peuf"),
    mode    = {
        "container" : ":default:",
        "keyval:: =": "general",
        "verbatim"  : "resume"
    }
) as datas:
    for onedata in datas:
        if onedata.isblock():
            print('--- {0} ---'.format(onedata.querypath))
        elif onedata.isdata():
            pprint.pprint(onedata.rtu)
```

Launching in a terminal, the script will produce the following output where you can note that a "querypath" like `book/general` indicates that the block `general` is inside the block `book`.

```
--- book/general ---
(4, 'author', '=', 'M. Nobody')
(5, 'title', '=', 'Does this book have a title ?')
(6, 'date', '=', '2012, May the 1st')
--- book/resume ---
(9, 'This book is an ode to the passing time...')
(10, 'A challenging thinking.')
```

You can see that verbatim contents are given line by line, and that the separator between one key and its value is always indicated. This last behavior is due to the fact that you can use different separators if you want.
The number of lines in the original content are always given so as to let other applications the possibility to use them for messages.


Let's see another example with the following data file.

```
logic::
    A <==> B
    A ==> B
    A <== P
```

This file is easy to read with the code above where `mode = "multikeyval:: <==> <== ==>"` is a shortcut for `mode = {"multikeyval:: <==> <== ==>": ":default:"}`. This setting allows multiple uses of the same key.

```python
from pathlib import Path
import pprint

from orpyste.data import Read

with Read(
    content = Path("user/example.peuf"),
    mode    = "multikeyval:: <==> <== ==>"
) as datas:
    for onedata in datas:
        if onedata.isblock():
            print('--- {0} ---'.format(onedata.querypath))
        elif onedata.isdata():
            pprint.pprint(onedata.rtu)
```

The output below shows the necessity here to always have the separators.

```
--- logic ---
(3, 'A', '<==>', 'B')
(4, 'A', '==>', 'B')
(5, 'A', '<==', 'P')
```
