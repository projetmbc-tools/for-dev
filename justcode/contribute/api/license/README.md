Contribute to `license`
=======================

How to contribute?
------------------

Adding a new licence consists of providing two files named via the same identifier, all in upper case, but with different extensions (an example is given next).

  1) A `PEUF` file is used to give some metadatas about the licence.

  1) The full text of the licence is given in a `TXT` file.


> The identifier of a licence can only use unaccented letters, numbers and possibly the hyphen `-`.


Let's say we want to add the *"Do What The Fuck You Want to Public License "*: see [Wikipedia-WTPL](https://fr.wikipedia.org/wiki/WTFPL) (since the `unlicense` license is already proposed, adding the politically incorrect `WTFPL` license doesn't seem useful). The identifier of this licence is `WTFPL`, so we need to create the files `WTFPL.txt` and `WTFPL.peuf` which have the following contents.


**File `WTFPL.peuf`:**

~~~
about::
    fullname = Do What The Fuck You Want to Public License, Version 2.0
    shortid  = WTFPL
    url      = https://choosealicense.com/licenses/wtfpl
~~~


**File `WTFPL.txt`**

~~~
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
~~~
