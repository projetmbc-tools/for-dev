All the flavours
----------------

To indicate a dialect for templates, a flavour must be indicated. Here are the minimalist technical descriptions of each of these flavours.


<!-- FLAVOURS - TECH. DESC. - START -->

---

#### Flavour `ascii`

> **Short description:** generic behaviour of `jinjaNG`.

  1. **Extensions for the auto-detection, and possible tools for the templates.**

      * Any extension not associated to any other flavour is associated to this flavour which is like a default one.

      * No tools are available to assist in typing templates.

  1. **Variables** are typed `{{ one_jinja_var }}` .

  1. **Using `jinja` instructions.**

     `...` symbolizes some Jinja instructions.

      * For inline instructions, use `#: ...` .

      * For block instructions, use `{#: ... :#}` .

  1. **Writing comments.**

     `...` symbolizes some comments.

      * For inline comments, use `#_ ...` .

      * For block comments, use `{#_ ... _#}` .

---

#### Flavour `html`

> **Short description:** useful settings and tools for HTML templating.

  1. **Extensions for the auto-detection, and possible tools for the templates.**

      * Files having extensions `HTML` are associated to this flavour.

      * Tools to assist in typing templates are available: see the folder `jng-extra-tools/html`.

  1. **Variables** are typed `{{ one_jinja_var }}` .

  1. **Using `jinja` instructions.**

     `...` symbolizes some Jinja instructions.

      * No inline instructions are available.

      * For block instructions, use `<!--: ... :-->` .

  1. **Writing comments.**

     `...` symbolizes some comments.

      * No inline comments are available.

      * For block comments, use `<!--_ ... _-->` .

---

#### Flavour `latex`

> **Short description:** useful settings and tools for LaTeX templating.

  1. **Extensions for the auto-detection, and possible tools for the templates.**

      * Files having extensions `TEX`, `STY`, or `TKZ` are associated to this flavour.

      * Tools to assist in typing templates are available: see the folder `jng-extra-tools/latex`.

  1. **Variables** are typed `\JNGVALOF{ one_jinja_var }` .

  1. **Using `jinja` instructions.**

     `...` symbolizes some Jinja instructions.

      * For inline instructions, use `%: ...` .

      * For block instructions, use `%%: ... :%%` .

  1. **Writing comments.**

     `...` symbolizes some comments.

      * For inline comments, use `%_ ...` .

      * For block comments, use `%%_ ... _%%` .

<!-- FLAVOURS - TECH. DESC. - END -->
