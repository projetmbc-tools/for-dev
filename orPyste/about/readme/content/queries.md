Searching for blocks
====================

Here we consider the following file whose path remains equal to `user/example.peuf`.

```
main::
    test::
        a = 1 + 9
        b <>  2
        c = 3 and 4

    sub_main::
        sub_sub_main::
            verb::
                line 1
                    line 2
                        line 3
```


The classes `Read` and `ReadBlock` allow to search for data blocks using queries on "querypaths". The special syntax to use tries to catch the best of the Python regex and the Unix-glob syntaxes. Take a look at the documentation of the function ``data.regexify`` for details. The following examples give some examples of queries.

```python
from pathlib import Path

from orpyste.data import Read

with Read(
    content = Path("user/example.peuf"),
    mode    = {
        "container"    : ":default:",
        "keyval:: = <>": "test",
        "verbatim"     : "verb"
    }
) as datas:
    for query in [
        "main/test",    # Only one path
        "**",           # Anything
        "main/*",       # Anything "contained" inside "main"
    ]:
        title = "Query: {0}".format(query)
        hrule = "="*len(title)

        print("", hrule, title, hrule, sep = "\n")

        for oneinfo in datas[query]:
            if oneinfo.isblock():
                print(
                    "",
                    "--- {0} [{1}] ---".format(
                        oneinfo.querypath,
                        oneinfo.mode
                    ),
                    sep = "\n"
                )

            else:
                for data_rtu in onedata.yrtu():
                    print(data_rtu)
```


This gives the following outputs as expected.

```
================
Query: main/test
================

--- main/test [keyval] ---
(4, 'a', '=', '1 + 9')
(5, 'b', '<>', '2')
(6, 'c', '=', '3 and 4')

=========
Query: **
=========

--- main/test [keyval] ---
(4, 'a', '=', '1 + 9')
(5, 'b', '<>', '2')
(6, 'c', '=', '3 and 4')

--- main/sub_main/sub_sub_main/verb [verbatim] ---
(11, 'line 1')
(12, '    line 2')
(13, '        line 3')

=============
Query: main/*
=============

--- main/test [keyval] ---
(4, 'a', '=', '1 + 9')
(5, 'b', '<>', '2')
(6, 'c', '=', '3 and 4')
```
