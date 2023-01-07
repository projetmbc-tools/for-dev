Contribute to the documentation of `jinjaNG`
============================================

> **I beg your pardon for my english...**
>
> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.


How to create one new flavour?
------------------------------

In the section *"All flavours, and status"* at the end of this document, you can find all the flavours indicated as **"ok"**. If none of them meet your expectations, you can decide to suggest a new flavour. To do this, follow the steps below.


#### Required file structure

The first step in creating a new flavour, which we will call `myflavour`, is to use the following structure.

~~~
+ myflavour
    * specs.yaml
    + usecases
~~~


> The project's `GitHub` repository also shows a `status.yaml` file for each flavour. This file is the responsibility of the developer of `jinjaNG`. It allows you to know the status of the integration, or not, of a flavour.

#### Contents of the folder `usecases`

The `usecases` folder contains some short use cases for testing the validity of the specifications. Here is some of the content of the `usecases` folder for the `ASCII` flavour.

~~~
+ usecases
    + no-param-1
        * output.txt
        * template.txt
        * datas.json
    + no-param-2
        * output.txt
        * template.txt
        * datas.json
~~~

Each case corresponds to a folder with a short and meaningful name. This folder must necessarily contain two files named `template`, and `output` with the expected extension, here a simple `TXT`, as well as a `datas.json` file for the populating data.

  1. The file named `template` is a short, but well-chosen template. It is better to use more than one use case to isolate what is being tested.

  1. The file named `datas.json` provides the populating data.

  1. The file named `output` is the expected output.


#### The file `specs.yaml`

To indicate the specifications of a flavour, the `specs.yaml` file is used with the following contents; we explain the expected values for the various `<GENERIC-NAME>` below.

~~~yaml
about:
    author: <AUTHOR>
    desc  : <DESCRIPTION>
    date  : <DATE>

ext:
    - <EXT-1>
    - <EXT-2>

src-comment:
    block : <BLOCK-COMMENT>
    inline: <INLINE-COMMENT>

var: <VARIABLE>
~~~

For the `about` block, the following should be specified.

  1. `<AUTHOR>` indicates the author of the ¨specs in the format `Firstname, Lastname [email]`.

  1. `<DESCRIPTION>` is a very short description of the flavour.

  1. `<DATE>` gives the date of creation, or last modification, in the format `YYYY-MM-DD` such as `2022-12-19`.

The `ext` block is used to specify a list of file extensions for the automatic association of a flavour with a pattern. For example, for the `LaTeX` flavour, the following block is used.

~~~yaml
ext:
    - tex
    - sty
    - tkz
~~~

The special feature of `jinjaNG` is to considerate that the templates used have a comment system to build on to suggest different ways of using `jinjaNG` instructions. For example, for the `ASCII` flavour, the following block is used where the ellipsis `...` symbolises the instructions that will be used in a pattern. Note here the quotation marks which are not always mandatory (here it is the `#` symbols which must be protected).

~~~yaml
src-comment:
    block : "{# ... #}"
    inline: "# ..."
~~~

Finally, the `var` variable is used to define how a "data variable" should be typed into a pattern. For example, for the `HTML` flavour, it is `var: "{{ ... }}"` that is specified.


#### Make a proposal

There are two possible methods to propose a new flavour.

  1. If you are not familiar with `GitHub`, here are the steps to follow.

      * Start by compressing the flavour folder to `ZIP` format.

      * Send the compressed folder to `projetmbc@gmail.com`, making sure to indicate *"jinjaNG - Contribute - flavour"* as the email subject.

  1. If you are familiar with `GitHub`, here are the steps to follow.

      * Start by cloning the `jinjaNG` project.

      * Add the contribution to the `contribute/api/dsl` folder.

      * Finally, juts go through a `git merge requests`.



All flavours, and statuses
-------------------------

#### The flavours, and their status

<!-- LIST OF FLAVOURS AND THEIR STATUS - AUTO - START -->

  * **[ok]** `ascii`
  * **[ok]** `html`
  * **[update]** `latex`

<!-- LIST OF FLAVOURS AND THEIR STATUS - AUTO - END -->


#### Statuses with their relevant flavours

<!-- LIST OF STATUSES WITH THE RELEVANT FLAVOURS - AUTO - START -->

  * Status **''ok''**
    + `ascii`
    + `html`
    + `latex`
  * Status **''update''**
    + `latex`

<!-- LIST OF STATUSES WITH THE RELEVANT FLAVOURS - AUTO - END -->

