### What we want...

In the project `mockproject`, there are some files that are only useful for code development.

  1. Names using the pattern `x-...-x` indicate files or folders that `git` must ignore: se `x-roadmap-x.txt` in the `src` directory.

  1. Names using the pattern `tool_...` are for files and folders not to be included in the final product, but which `git` must retain.

  1. The `README.md` file used for `git` servers must also be included in the final product code.


By copying files, we wish to add one new folder `mockproject` to obtain the following structure.

~~~
+ MockProject
    * about.yaml
    * pyproject.toml
    * README.md
    + changes [...]
    + mockproject
        * __init__.py
        * mockthis.py
        * LICENSE.txt
        * README.md
    + src [...]
    + tests [...]
~~~
