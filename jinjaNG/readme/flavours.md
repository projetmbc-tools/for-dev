All the flavours
----------------

To indicate a dialect for templates, a flavour must be given. Here are the minimalist technical descriptions of each of these flavours.


<!-- FLAVOURS - TECH. DESC. - START -->

---

#### Flavour `ascii`

> ***Short description:*** *generic behaviour of `jinjaNG`.*

  1. **Extensions for the auto-detection.**
      * Any extension not associated with another flavour is associated with that flavour (which is like a default one).

  1. **Tools to assist in typing templates.**
      * Nothing available.

  1. **Variables, `jinja` instructions and comments.**
  Here is a fictive `how-to` code.

~~~markdown
In our templates, we use {{variable}} .

It is always possible to work with block jinja instructions, and comments.

##_ Comments: one basic loop. _##

##: for i in range(5) :##
We can use {{i + 4}} .
##: endfor :##

Most of flavours propose inline jinja instructions, and comments.

#_ Comments: the same loop as above.

#: for i in range(5)
We can use {{i + 4}} .
#: endfor
~~~

---

#### Flavour `html`

> ***Short description:*** *useful settings and tools for HTML templating.*

  1. **Extension for the auto-detection.**
      * `HTML`

  1. **Tools to assist in typing templates.**
      * See the folder `jng-extra-tools/html`.

  1. **Variables, `jinja` instructions and comments.**
  Here is a fictive `how-to` code.

~~~markdown
In our templates, we use {{variable}} .

It is always possible to work with block jinja instructions, and comments.

<!--_ Comments: one basic loop. _-->

<!--: for i in range(5) :-->
We can use {{i + 4}} .
<!--: endfor :-->

This flavour doesn't propose inline jinja instructions, and comments.
~~~

---

#### Flavour `latex`

> ***Short description:*** *useful settings and tools for LaTeX templating.*

  1. **Extensions for the auto-detection.**
      * `STY`
      * `TEX`
      * `TKZ`

  1. **Tools to assist in typing templates.**
      * See the folder `jng-extra-tools/latex`.

  1. **Variables, `jinja` instructions and comments.**
  Here is a fictive `how-to` code.

~~~tex
In our templates, we use \JNGVALOF{variable} .

It is always possible to work with block jinja instructions, and comments.

%%_ Comments: one basic loop. _%%

%%: for i in range(5) :%%
We can use \JNGVALOF{i + 4} .
%%: endfor :%%

Most of flavours propose inline jinja instructions, and comments.

%_ Comments: the same loop as above.

%: for i in range(5)
We can use \JNGVALOF{i + 4} .
%: endfor
~~~

<!-- FLAVOURS - TECH. DESC. - END -->
