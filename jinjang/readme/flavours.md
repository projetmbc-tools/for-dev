All the flavours
----------------

A flavour indicates a dialect for templates. Here are the technical descriptions of each of this flavours.


<!-- FLAVOURS - TECH. DESC. - START -->

#### Flavour `ascii`

> **Short description:** generic behaviour of `jinjaNG`.

  1. **Extensions for the auto-detection, and possible tools for the templates.**

      * Any extension not associated to any other flavour is associated to this flavour which is like a default one.

      * No tools are available to assist in typing templates.

  1. **Variables** are typed `{{ one_jinja_var }}`.

  1. **Using `jinja` instructions.**

      * Inline instructions are typed `#: ...` where `...` symbolizes some `Jinja` instructions.

      * Block instructions are typed `{#: ... :#}` where `...` symbolizes some `Jinja` instructions, on several lines if needed.

  1. **Writing comments.**

      * Inline comments are typed `#_ ...` where `...` symbolizes comments only for the template.

      * Block comments are typed `{#_ ... _#}` where `...` symbolizes comments only for the template, on several lines if needed.

#### Flavour `html`

> **Short description:** useful settings and tools for HTML templating.

  1. **Extensions for the auto-detection, and possible tools for the templates.**

      * Files having extensions `HTML` are associated to this flavour.

      * Tools to assist in typing templates are available: see the folder `jng-extra-tools/html`.

  1. **Variables** are typed `{{ one_jinja_var }}`.

  1. **Using `jinja` instructions.**

      * No inline instructions are available.

      * Block instructions are typed `<!--: ... :-->` where `...` symbolizes some `Jinja` instructions, on several lines if needed.

  1. **Writing comments.**

      * No inline comments are available.

      * Block comments are typed `<!--_ ... _-->` where `...` symbolizes comments only for the template, on several lines if needed.

#### Flavour `latex`

> **Short description:** useful settings and tools for LaTeX templating.

  1. **Extensions for the auto-detection, and possible tools for the templates.**

      * Files having extensions `TEX`, `STY`, or `TKZ` are associated to this flavour.

      * Tools to assist in typing templates are available: see the folder `jng-extra-tools/latex`.

  1. **Variables** are typed `\JNGVAR{ one_jinja_var }`.

  1. **Using `jinja` instructions.**

      * Inline instructions are typed `%: ...` where `...` symbolizes some `Jinja` instructions.

      * Block instructions are typed `%%: ... :%%` where `...` symbolizes some `Jinja` instructions, on several lines if needed.

  1. **Writing comments.**

      * Inline comments are typed `%_ ...` where `...` symbolizes comments only for the template.

      * Block comments are typed `%%_ ... _%%` where `...` symbolizes comments only for the template, on several lines if needed.

<!-- FLAVOURS - TECH. DESC. - END -->
