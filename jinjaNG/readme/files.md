Working with files
------------------

### Our goal

Suppose we want to type the following `LaTeX` code. This corresponds to a file with extension `TEX`.

~~~latex
\documentclass{article}

\begin{document}

One example.

\begin{enumerate}
    \item Value nb. 1: "one".
    \item Value nb. 2: "two".
    \item Value nb. 3: "three".
    \item Value nb. 4: "four".
    \item Value nb. 5: "five".
\end{enumerate}

\end{document}
~~~

As you can see, most of the content follows a repetitive logic. So it may be a good idea to automate the typing. Here is where `jinjaNG` can help us.


### What we really type

The first thing we can do is to define the repetitive content. Let's use a `YAML` file (a `JSON` file can be used, but it's less fun to type). If we need to go further into the numbers in the `LaTeX` file, we just have to add new names to the list in the `YAML` file.

~~~yaml
txt_exa: example
values :
  - one
  - two
  - three
  - four
  - five
~~~


Next, let's type a minimalist `LaTeX` code using special instructions and tags. Explanations are given below.

~~~latex
\documentclass{article}
%: if False
\usepackage{jnglatex}
%: endif

\begin{document}

One \JNGVALOF{txt_exa}.

\begin{enumerate}
%: for oneval in values
    \item Value nb. \JNGVALOF{loop.index}: "\JNGVALOF{oneval}".
%: endfor
\end{enumerate}

\end{document}
~~~

This is how the previous template was typed.

  1. Let's start with the content after the `\begin{document}`. With `\JNGVALOF{txt_exa}`, we indicate to use the value associated with the `txt_exa` variable in the `YAML` data file. In our case, `\JNGVALOF{txt_exa}` corresponds to `example`.

  1. At the begining of the template, the lines between `%: if False` and `%: endif` will not be in the final output. Here we use `%: some Jinja instructions` with an always-false condition which causes the block to be ignored when making the final file. This allows the `jnglatex` package to be used only in the template file, but not in the final output. This package allows `jinjaNG` variables to be clearly highlighted after the `LaTeX` template is compiled: this small feature greatly simplifies template design.


>  For now, the `jnglatex.sty` file must be in the same folder as the `LaTeX` template, or it must be installed by hand in your `LaTeX` distribution: you will find it in the `jng-extra-tools` folder.


### Building the output via a `Python` code

Using a `Python` file, it is easy to produce the desired output. Here are the instructions to use where we assume that the `cd` command has been used beforehand, so that running the `Python` scripts is done from the folder containing our `Python`, `YAML` and `LaTeX` files.

~~~python
from jinjang import *

mybuilder = JNGBuilder()

mybuilder.render(
    data     = "data.yaml",
    template = "template.tex",
    output   = "output.tex"
)
~~~

This code uses one useful default behaviour: `jinjaNG` associates automatically the `LaTeX` dialect, or flavour because the template has the extension `TEX`. The flavours available are given in the last section of this document.


### Building the output via command lines

The commands below have the same effect as the `Python` code in the previous section.

~~~
> cd path/to/the/good/folder
> jinjang data.yaml template.tex output.tex
File successfully built:
  + output.tex
~~~



### Building the data via a `Python` script

In our case, by knowing the existence of [cvnum](https://pypi.org/project/cvnum/), for example, we can be more efficient in constructing the data. Here is one possible `data.py` file where `JNGDATA` is a reserved name for the data that `jinjaNG` will use. We'll see next that producing the final output can no longer be done using the default behaviour of an instance of the `JNGBuilder` class.

~~~python
from cvnum.textify import *

nameof = IntName().nameof

JNGDATA = {
    'txt_exa': "example",
    'values' : [nameof(x) for x in range(1, 6)]
}
~~~


The `Python` code producing the final output becomes the following one, where `pydata = True` allows the class `JNGBuilder` to execute the `Python` file. **This choice can be dangerous with untrusted `Python` scripts!**

~~~python
from jinjang import *

mybuilder = JNGBuilder(pydata = True)

mybuilder.render(
    data    = "data.py",
    template = "template.tex",
    output   = "output.tex"
)
~~~


To work with a `Python` data file from the terminal, you must use the tag `--unsafe` because **it can be dangerous to launch a `Python` data file**, so `jinjaNG` must know that you really want to do this. The commands below have the same effect as the `Python` code above.

~~~
> cd path/to/the/good/folder
> jinjang --unsafe data.py template.tex output.tex
WARNING: Using a Python file can be dangerous.
File successfully built:
  + output.tex
~~~
