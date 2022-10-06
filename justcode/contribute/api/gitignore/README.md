Contribute to `gitignore`
=========================

> **For the moment, sorting rules is not supported.**
> If you need this feature, gives clear explanations of this in real use cases suchas to convice the author of `jsutcode` to implement the sorting of rules.


How to contribute?
------------------

Adding new `gitignore` rules is simply a matter of providing a `TXT` file in the folder `datas`, and the content of this file is just the set of rules, but you must respect the following specifications.


### Spec.1 - Name of the `TXT` file

This name, all in uppercase, is the identifier of the set of rules. It can only use the characters below.

  1. Unaccented letters.
  1. Numbers.
  1. Hyphen `-` .
  1. Plus sign `+` .


### Spec.2 - Comments as a documentation

Comments must be used to document your rules.

#### General informations via `### ... ###`

The first lines must be of the following kind.

    ###
    # this::
    #     author = ?
    #     desc   = ?
    ###

Let's explain each mandatory key, and their value expected.

  1. Value of `author` must use one of the following patterns.

     * `LAST NAME`

     * `First name, LAST NAME`

     * `LAST NAME [myemail@appli.com]`

     * `First name, LAST NAME [myemail@appli.com]`

     * `none` if you want to remain anonymous.

  1. `desc` must give a none empty short description of the set of rules.


#### Contexts via `## ...`

Some contexts can be used: this will allow users of `justcode` to select specific subrules. Indicate contexts is done via uppercase comments of the kind `## ...` like above.

    ## SUBCONTEXT 1
    ...

    ## SUBCONTEXT 2
    ...


#### Standard comments via `# ...`

Comments with only one single starting `#` will be kept verbatim in the `gitginore` files produced by `justcode`.


### One example

Here is a short example of one file `CBDEV.txt` for rules that should be identified by `cbdev` in the `API` of `justcode`. No subcontext is proposed here, and the comment `# Hiden files and folders.` will be in `gitignore` files using `cbdev` rules, and build by `justcode`.

    ###
    # this::
    #     author = Christophe, BAL [projetmbc@gmail.com]
    #     desc   = ``cbdev`` coding style.
    ###

    # Hiden files and folders.
    x-*-x/
    x-*-x.*
