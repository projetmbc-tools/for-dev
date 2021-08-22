Reset the management of problems
--------------------------------

### What we want...

A communicating process can be restarted several times. This needs to reset every informations stored and displayed. To acheive that, the classes `BaseCom`, `Problems` and `Speaker` all have a method `reset`. The following weird example shows how this method works.

### `Python` code

~~~python
from spkpb import *

project = BaseCom(
    Problems(
        Speaker(logfile = Path('mylog.log'))
    )
)

project.new_warning(
    what = Path('one/strange/file.txt'),
    info = "some strange behaviors."
)

project.reset()

project.new_error(
    what = Path('one/bad/file.txt'),
    info = "bad things appear."
)

project.resume()
~~~


### The terminal output

~~~
1) [ #1 ] WARNING: some strange behaviors.
1) [ #1 ] ERROR: bad things appear.

-------------
1 ERROR FOUND
-------------

Look at the log file or above for details.

    * one/bad/file.txt
        + 1 error.
          See #.: [1].
~~~

Who has chosen this stupid example? :-)


### The content of the log file `mylog.log`

~~~
1) [ #1 ] ERROR: bad things appear.

-------------
1 ERROR FOUND
-------------

    * one/bad/file.txt
        + See [ #.1 ] : bad things appear.
~~~

