`jinjaNG` tools for (La)Tex like files
======================================

How to use the tools?
---------------------

Here is the miminal way to use the tools from the package `jngutils`. Note the use of `%: if False ... %: endif` suchas to import the package `jngutils` only when working on the template.

~~~latex
\documentclass[12pt]{article}
%: if False
\usepackage{jngutils}
%: endif

\begin{document}

The smallest \JNGVALOF{txt_example} in the world.

\end{document}
~~~

This template will produce the output shown in the following picture.

---

![output](images/exavar.png)

---

> **WARNING.**
>
> The `jinja` variables can't be used as one `LaTeX` parameter.


What is done behind the scenes?
-------------------------------

Two things are done.

  1. The special character `_` is transfomed to a textual underscore.

  1. The `color` package is used to format the names of `jinja` variables in red inside a red box.
