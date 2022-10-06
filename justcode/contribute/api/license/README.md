Contribute to `license`
=======================

How to propose one new license?
-------------------------------

Proposing a new license is simply a matter of providing one `PEUF` file in the folder `datas`. You must respect the following specifications.


### Spec.1 - Only *"Open Source"* licenses are supported

All is said in the title above.


### Spec.2 - Name of the `PEUF` file

This name, all in uppercase, is the short identifier of the license. It can only use the characters below.

  1. Unaccented letters.
  1. Numbers.
  1. Hyphen `-` .


### Spec.3 - Content of the `PEUF` file

This content must respect the following structure.

~~~
about::
    fullname = ?
    url      = ?
    content  = ?
~~~

Let's explain each mandatory key, and their value expected.

  1. `fullname` is the full name of the license.

  1. `url` is an url for an official website of the licence. If no such website exists, the value specified must be `none`.

  1. `content` is an url where the full text of the license is provided.


### One example

Let's say that we wish to propose the *"Do What The Fuck You Want to Public License "*: see [Wikipedia-WTPL](https://fr.wikipedia.org/wiki/WTFPL) (since the `unlicense` license is already proposed, adding the politically incorrect `WTFPL` license doesn't seem useful). Here is what we have.

   1. The identifier of this license is `WTFPL`.

   1. We have no official url for this license, so we will use `url = None`.

   1. In the page https://choosealicense.com/licenses/wtfpl, we have the full text of the license.

Eventually we create the file `WTFPL.peuf` with the following content. That's all!

~~~
about::
    fullname = Do What The Fuck You Want to Public License, Version 2.0
    url      = none
    content  = https://choosealicense.com/licenses/wtfpl
~~~
