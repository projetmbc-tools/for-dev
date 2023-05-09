The `Python` module `multimd`
=============================

> **I beg your pardon for my english...**
>
> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.

This document is a short tutorial showing the most useful features without being exhaustive.


About `multimd`
---------------

Working with moderate sized `MD` documents in a single file can quickly become tedious. This project allows you to go through separate small `MD` files to be merged into a final single `MD` file.


`README.md` part by part
------------------------

With `multimd`, you can write a `MD` document by typing small section-like parts which are easy to maintain. Consider the `README.md` file from the `src2prod` project which was written using the following tree on 6 May 2023.

~~~
+ src2prod
    * README.md
    + readme
        * about.yaml
        * about.md
        * build.md
        * cli.md
        * example-used.md
        * only-files.md
        * prologue.md
        * readme-splitted.md
    + ...
~~~

The special `about.yaml` file is used to specify a specific order in which the different `MD` files are put together (without this file, a "natural" order is used). Its content is as follows.

~~~yaml
toc:
  - prologue
  - about
  - example-used
  - build
  - only-files
  - readme-splitted
  - cli
~~~

Building the final `README.md` file is done quickly on the command line using `multimd` after using the `cd` command to go into the `src2prod` folder.

~~~
> multimd
File successfully built:
  + README.md
~~~


There is also an easy-to-use `Python` API.

~~~python
from multimd import MMDBuilder

mybuilder = MMDBuilder()
mybuilder.build()
~~~


Without the special `about.yaml` file
-------------------------------------

Without an `about.yaml` file, all the `MD` files will be merged into one after sorting them in a "natural" order.