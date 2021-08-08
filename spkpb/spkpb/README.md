The `Python` module `spkpb`
===========================


> **I beg your pardon for my english...**
>
> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.


About `spkpb`
-------------

This module proposes two classes.

  1. `Speaker`, the `spk` of `spkpb`, has methods tho print informations on a terminal and/or in a log file.
  
  1. `Problems`, the `pb` of `spkpb`, allows to indicate and store warnings, "criticals" and errors.


This classes simplify the writing of programs which have to be verbose about a process on files and directories, and that have to emit informations, warnings and errors.


An example of use
-----------------

#### A `Python` code

Let's consider the following `Python` file where `Path` is a class proposed by the module `pathlib`.

```python
from speaker  import *
from problems import *

speaker = Speaker(
    logfile = Path('mylog.log')
)

problems = Problems(speaker)

problems.new_warning(
    src_relpath = Path('one/strange/file.txt'),
    info        = "some strange behaviors."
)

problems.new_error(
    src_relpath = Path('one/bad/file.txt'),
    info        = "bad things appear."
)

speaker.recipe(
    NL,
    'One basic showcase.',
    FORTERM,
        {VAR_STEP_INFO: 'Write just on the terminal.',
         VAR_LEVEL    : 1},
    FORLOG,
        {VAR_STEP_INFO: 'Only in the log?',
         VAR_LEVEL    : 1},
)
    
problems.resume()
```

#### The terminal output

Launching our `Python` code from a terminal, we will see the following output.

```
1) [ #1 ] WARNING: some strange behaviors.
2) [ #2 ] ERROR: bad things appear.

One basic showcase.
    * Write just on the terminal.

---------------
1 WARNING FOUND
---------------

Look at the log file and/or above for details.

    * "one/strange/file.txt"
        + 1 warning.
          See #.: [1].

-------------
1 ERROR FOUND
-------------

Look at the log file and/or above for details.

    * "one/bad/file.txt"
        + 1 error.
          See #.: [2].
```


#### The content of the log file `mylog.log`

Launching our `Python` code, `mylog.log` will have the following content.


```
1) [ #1 ] WARNING: some strange behaviors.
2) [ #2 ] ERROR: bad things appear.

One basic showcase.
    * Only in the log?

---------------
1 WARNING FOUND
---------------

    * "one/strange/file.txt"
        + 1 warning.
          See #.: [1].

-------------
1 ERROR FOUND
-------------

    * "one/bad/file.txt"
        + 1 error.
          See #.: [2].
```


<!-- :tutorial-START: -->
<!-- :tutorial-END: -->


<!-- :version-START: -->
<!-- :version-END: -->
