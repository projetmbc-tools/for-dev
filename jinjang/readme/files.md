Working with files
------------------

#### Our goal

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



#### What we really type

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

One \JNGVAR{txt_exa}.

\begin{enumerate}
%: for oneval in values
    \item Value nb. \JNGVAR{loop.index}: "\JNGVAR{oneval}".
%: endfor
\end{enumerate}

\end{document}
~~~

This is how the previous template was typed.

  1. Let's start with the content after the `begin{document}`. With `JNGVAR{txt_exa}`, we indicate to use the value associated with the `txt_exa` variable in the `YAML` data file. In our case, `JNGVAR{txt_exa}` corresponds to `example`.

  1. At the begining of the template, the lines between `%: if False` and `%: endif` will not be in the final output. Here we use `%: some jinja instructions` with an always-false condition which causes the block to be ignored when making the final file. This allows the `jnglatex` package to be used only in the template file, but not in the final output. This package allows `jinjaNG` variables to be clearly highlighted after the `LaTeX` template is compiled: this small feature greatly simplifies template design.


>  For now, the `jnglatex.sty` file must be in the same folder as the `LaTeX` template, or it must be installed by hand in the `LaTeX` distribution: you will find it in the `jng-extra-tools` folder.



#### When `jinjaNG` finishes the job - Using `Python` code

Using a `Python` file, it is easy to produce the desired output. Here are the instructions to use where we suppose the use of the command `cd` inisde a folder containing our `Python`, `YAML` and `LaTeX` files.


~~~python
from jinjang import *

mybuilder = JNGBuilder()

mybuilder.render(
    datas    = "datas.yaml",
    template = "template.tex",
    output   = "output.tex"
)
~~~

This code uses one useful default behaviour: `jinjaNG` associates automatically the `LaTeX` dialect, or flavour because the template has the extension `TEX`. The flavours available are given in the last section of this document.



#### Building the data via a `Python` script

In our case, by knowing the existence of [cvnum](https://pypi.org/project/cvnum/), for example, we can be more efficient in constructing the data. Here is one possible `datas.py` file where `JNG_DATAS` is a reserved name for the data that `jinjaNG` will use. We'll see next that producing the final output can no longer be done using the default behaviour of an instance of the `JNGBuilder` class.

~~~python
from cvnum.textify import *

nameof = IntName().nameof

JNG_DATAS = {
    'txt_exa': "example",
    'values' : [nameof(x) for x in range(1, 6)]
}
~~~


The `Python` code producing the final output becomes the following one, where `pydatas = True` allows the class `JNGBuilder` to execute the `Python` file .

~~~python
from jinjang import *

mybuilder = JNGBuilder(pydatas = True)

mybuilder.render(
    datas    = "datas.py",
    template = "template.tex",
    output   = "output.tex"
)
~~~
