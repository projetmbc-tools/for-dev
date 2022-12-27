`README.md` part by part
------------------------

With `multimd`, you can write a `MD` document by typing small section-like parts which are easy to maintain. Consider the `README.md` file from the `src2prod` project which was written using the following tree on 22 August 2021. Note that there are only `MD` files present in the same folder (the purpose of `multimd` is to simplify writing relatively small documents, but certainly not books).

~~~
+ src2prod
    + readme
        * about.yaml
        * build.md
        * cli.md
        * example-used.md
        * only-files.md
        * prologue.md
        * readme-splitted.md

    * README.md
~~~

The special `about.yaml` file is used to specify the order in which the different `MD` files are merged. Its contents are as follows.

~~~yaml
toc:
  - prologue
  - example-used
  - build
  - only-files
  - readme-splitted
  - cli
~~~

This is how `README.md` was constructed. We assume the use of the `cd` command to get into the right folder, before running the following script where instances of `pathlib.Path` are used.

~~~python
from multimd import Builder

mybuilder = Builder(
    output  = Path('README.md'),
    content = Path('readme'),
)

mybuilder.build()
~~~
