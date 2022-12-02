`jinjaNG` tools for (La)Tex like files
======================================

How to use the tools?
---------------------

Here is the miminal way to use the tools from the package `jnglatex`. Note the use of `%: if False :% ... %: endif :%` suchas to import the package `jnglatex` only when working on the template.

~~~latex
\documentclass[12pt]{article}

%: if False :%
    \usepackage{jnglatex}
%: endif :%

\begin{document}

The smallest \JNGVAR{txt_example} in the world.

\end{document}
~~~

The tiny template above will produce an ouput similar to the following one. Note that the underscore is interpreted as a subscript.

<div style="border: solid 1px; padding: 4px 6px, margin-bottom:12px;">
The smallest <span style="color: red; font-style: italic;border: solid 1px; padding: 1px 3px">txt_<sub>e</sub>xample</span> in the world.
</div>
<br/>

> **WARNING 1.**
>
> Names of the `jinja` variables can't contain two consecutive underscores.


> **WARNING 2.**
>
> The `jinja` variables can't be used as one `LaTeX` argument.


What is done behind the scenes?
-------------------------------

The `amsmath` and `color` packages are used to format the names of `jinja` variables in red inside a red box, while applying the mathematical mode to allow the use of isolated underscores in the name of a `jinja` variable.
