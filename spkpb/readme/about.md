About `spkpb`
-------------

This module proposes two classes and one function that simplify the writing of programs which have to talk verbosely to human beeings during a process. `spkpb` can indicate informations, warnings and errors which are easy to analyze by a human.

  1. `Speaker`, the `spk` of `spkpb`, has methods to print informations on a terminal and/or to write in a log file.

  1. `Problems`, the `pb` of `spkpb`, allows to indicate and store warnings, "criticals" and errors.

  1. The function `timestamp` adds time stamps in a log file without printing anything in the terminal.


The following tutorial will starts by using the hard way to work with the `spkpb` tools, and it will finish with more programmer-friendly approach.
