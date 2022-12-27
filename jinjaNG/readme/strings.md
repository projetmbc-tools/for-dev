Working with `Python` variables
-------------------------------

To work directly from `Python` without using any file, you need to produce a dictionary for the data, and a string for the template, so as to get a string for the final output. Let's take an example where the dialect, or flavour, must be specified always.

~~~python
from jinjang import *

mydatas = {
    'txt_exa': "small example",
    'max_i'  : 4
}

mytemplate = """
One {{ txt_exa }} with automatic calculations.
{#: for i in range(1, max_i + 1) :#}
  {{ i }}) I count using squares: {{ i**2 }}.
{#: endfor :#}
""".strip()

mybuilder = JNGBuilder(flavour = FLAVOUR_ASCII)

output = mybuilder.render_frompy(
    datas    = mydatas,
    template = mytemplate
)
~~~


The content of the string `output` will be the following one.

~~~markdown
One small example with automatic calculations.

  1) I count using squares: 1.

  2) I count using squares: 4.

  3) I count using squares: 9.

  4) I count using squares: 16.

~~~
