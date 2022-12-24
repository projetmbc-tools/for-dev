Working with `Python` strings
-----------------------------

#### ????

~~~python
datas = {'max_i': 4, 'txt_example': 'example'}
~~~

~~~python
template = """
One small {{ txt_example }} with automatic calculations.
{#: for i in range(1, max_i + 1) :#}
    {{ i }}) I count using squares: {{ i**2 }}.
{#: endfor :#}
""".strip()
~~~


~~~python
output = """One small example with automatic calculations.

    1) I count using squares: 1.

    2) I count using squares: 4.

    3) I count using squares: 9.

    4) I count using squares: 16."""
~~~
