A ready-to-use communicating class
----------------------------------

We have seen the hard use of the API of `spkpb`. Indeed you can heritate the class `BaseCom` to do things easily: see the following code and outputs.


### `Python` code

~~~python
from spkpb import *

project = BaseCom(
    Problems(
        Speaker(
            logfile   = Path('mylog.log'),
            termstyle = GLOBAL_STYLE_COLOR
        )
    )
)

project.timestamp(kind = 'start')

project.new_warning(
    what = Path('one/strange/file.txt'),
    info = "some strange behaviors."
)

print(f'>>>>>>>> sucess = {project.success}')

project.new_error(
    what = Path('one/bad/file.txt'),
    info = "bad things appear."
)

print(f'>>>>>>>> sucess = {project.success}')

project.recipe(
    NL,
    'One basic showcase.',
    FORTERM,
        {VAR_STEP_INFO: 'ONLY FOR THE TERMINAL OUPUT!',
         VAR_LEVEL    : 1},
    FORLOG,
        {VAR_STEP_INFO: 'ONLY IN THE LOG FILE!',
         VAR_LEVEL    : 1},
)

project.resume()

project.recipe(NL)
project.timestamp(kind = 'end')
~~~


### The terminal output

~~~
1) [ #1 ] WARNING: some strange behaviors.
>>>>>>>> sucess = True
2) [ #2 ] ERROR: bad things appear.
>>>>>>>> sucess = False

One basic showcase.
    * ONLY FOR THE TERMINAL OUPUT!

---------------
1 WARNING FOUND
---------------

Look at the log file or above for details.

    * one/strange/file.txt
        + 1 warning.
          See #.: [1].

-------------
1 ERROR FOUND
-------------

Look at the log file or above for details.

    * one/bad/file.txt
        + 1 error.
          See #.: [2].
~~~


### The content of the log file `mylog.log`

~~~
---------------------------------------
START TIME STAMP: 2021-08-10 (11:40:02)
---------------------------------------

1) [ #1 ] WARNING: some strange behaviors.
2) [ #2 ] ERROR: bad things appear.

One basic showcase.
    * ONLY IN THE LOG FILE!

---------------
1 WARNING FOUND
---------------

    * one/strange/file.txt
        + See [ #.1 ] : some strange behaviors.

-------------
1 ERROR FOUND
-------------

    * one/bad/file.txt
        + See [ #.2 ] : bad things appear.

-------------------------------------
END TIME STAMP: 2021-08-10 (11:40:02)
-------------------------------------
~~~
