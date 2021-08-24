Using directly the API - Silent mode
------------------------------------

Let's modify a little our first code (the ellipsis indicate lines unchanged).

```python
from spkpb import *

speaker = Speaker(
    logfile = Path('mylog.log'),
    silent  = True
)

...
```

The use of the argument ``silent`` asks to prints only the summaries of problems (that is useful for short processes with no need to be verbose). The terminal and the log file will show the following same verbose resume.

```
---------------
1 WARNING FOUND
---------------

    * one/strange/file.txt
        + Some strange behaviors.

-------------
1 ERROR FOUND
-------------

    * one/bad/file.txt
        + Bad things appear.
```
