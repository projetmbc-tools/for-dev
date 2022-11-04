Reading the datas block by block
================================

We go back to our second example with the following file whose path is `user/example.peuf`.

```
book::
    general::
        author = M. Nobody
        title  = What is the title ?
        date   = 2012, May the 1st

    resume::
        This book is an ode to the passing time...
        A challenging thinking.
```


The class `ReadBlock` is a subclass of `Read` so you can use any methods working with `Read`. But the goal of `ReadBlock` is to work with dictionaries instead of reading datas line by line *(for large files this last choice is a better one)*. Let's see first the property `flatdict`.

```python
from pathlib import Path

from orpyste.data import ReadBlock

with ReadBlock(
    content = Path("user/example.peuf"),
    mode    = {
        "container" : ":default:",
        "keyval:: =": "general",
        "verbatim"  : "resume"
    }
) as datas:
    print(datas.flatdict)
```


The code launched in one terminal gives us the following output *(which has been hand formatted)*.

```
MKOrderedDict([
    (id=0,
     key='book/general',
     value=MKOrderedDict([
        (id=0,
         key='author',
         value={'nbline': 4, 'value': 'M. Nobody', 'sep': '='}),
        (id=0,
         key='title',
         value={'nbline': 5, 'value': 'What is the title ?', 'sep': '='}),
        (id=0,
         key='date',
         value={'nbline': 6, 'value': '2012, May the 1st', 'sep': '='})
     ])
    ),
    (id=0,
     key='book/resume',
     value=(
        {'nbline': 9, 'value': 'This book is an ode to the passing time...'},
        {'nbline': 10, 'value': 'A challenging thinking.'})
    )
])
```


As you can see, the keys are "querypaths" and the values are the datas. You can also use the property `treedict` which produces a dictionary with a structure similar to the one of the blocks in the content analyzed. The following code is merly the same as the previous one *(`[...]` indicates the first lines of the preceding code)*.

```python
[...]

with ReadBlock(...) as datas:
    print(datas.treedict)
```


Here are the dictionary produced *(the ouput has been hand formatted)*.

```
RecuOrderedDict([
    ('book',
     RecuOrderedDict([
        ('general',
         RecuOrderedDict([
            ('author',
             {'nbline': 4, 'sep': '=', 'value': 'M. Nobody'}),
            ('title',
             {'nbline': 5, 'sep': '=', 'value': 'What is the title ?'}),
            ('date',
             {'nbline': 6, 'sep': '=', 'value': '2012, May the 1st'})
         ])
        ),
        ('resume',
         (
            {'nbline': 9,
             'value': 'This book is an ode to the passing time...'},
            {'nbline': 10,
             'value': 'A challenging thinking.'}
         )
        )
     ])
    )
])
```


If you want to customize a little the dictionary build by ``ReadBlock``, you can use the method `mydict` like in the following example *(see the "docstrings" for more informations)*.

```python
[...]

with ReadBlock(...) as datas:
    print('--- Standard "flat" dict ---')
    print(datas.mydict("std nosep nonb"))

    print('--- Standard "tree" dict ---')
    print(datas.mydict("tree std nosep nonb"))
```


We obtain here two standard dictionaries with neither separators, nor number lines.

```
--- Standard "flat" dict ---
{
    'book/general': {
        'author': 'M. Nobody',
        'date': '2012, May the 1st',
        'title': 'Does this book have a title ?'
    },
    'book/resume': (
        'This book is an ode to the passing time...'
        'A challenging thinking.'
    )
}
--- Standard "tree" dict ---
{
    'book': {
        'general': {
            'author': 'M. Nobody',
            'date': '2012, May the 1st',
            'title': 'Does this book have a title ?'
        },
        'resume': (
            'This book is an ode to the passing time...',
            'A challenging thinking.'
        )
    }
}
```
