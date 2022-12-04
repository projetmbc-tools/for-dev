`jinjaNG` tools for (La)Tex like files
======================================

How to use the tools?
---------------------

Here is the miminal way to use the tools from the package `<:TOOLS:>`. Note the use of `%: if False ... %: endif` suchas to import the package `<:TOOLS:>` only when working on the template.

~~~latex
\documentclass[12pt]{article}
%: if False
\usepackage{<:TOOLS:>}
%: endif

\begin{document}

The smallest \JNGVAR{txt_example} in the world.

\end{document}
~~~

The tiny template above will produce an ouput similar to the following one.

<div style="border: solid 1px; padding: 4px 6px, margin-bottom:12px;">
The smallest <span style="color: red; border: solid 1px; padding: 1px 3px">txt_example</span> in the world.
</div>
<br/>

> **WARNING.**
>
> The `jinja` variables can't be used as one `LaTeX` argument.


What is done behind the scenes?
-------------------------------

The `color` package is used to format the names of `jinja` variables in red inside a red box.
