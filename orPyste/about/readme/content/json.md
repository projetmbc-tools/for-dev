Storing your datas in a `json` variable
=======================================

The class `ReadBlock` has a method `forjson` that allows to store your datas in a `json` file *(the storing has to be done by you)*. The following code will give us just after the structure used.

```python
from orpyste.data import ReadBlock

content = '''
main::
    test::
        a = 1 + 9
        b <>  2
        c = 3 and 4

    sub_main::
        sub_sub_main::
            verb::
                line 1
                    line 2
                        line 3
'''

with ReadBlock(
    content = content,
    mode    = {
        "container"    : ":default:",
        "keyval:: = <>": "test",
        "verbatim"     : "verb"
    }
) as datas:
    jsonobj = datas.forjson
    print(jsonobj)
```


Launched in a terminal, we obtain the following output which has been hand formatted. As you can see, we use the format `[key, value]` so as to store the keys and the values of the `python` dictionary given by the method `ReadBlock.flatdict` and `ReadBlock.recudict`. You can also note that for verbatim content we use a `null` key *(this is to ease other applications to extract informations from a "symmetric" `json` variable)*.

```json
[
    [
        [0, "main/test"],
        [
            [
                [0, "a"],
                {"nbline": 4, "sep": "=", "value": "1 + 9"}
            ],
            [
                [0, "b"],
                {"nbline": 5, "sep": "<>", "value": "2"}
            ],
            [
                [0, "c"],
                {"nbline": 6, "sep": "=", "value": "3 and 4"}
            ]
        ]
    ],
    [
        [0, "main/sub_main/sub_sub_main/verb"],
        [
            null,
            [
                {"nbline": 11, "value": "line 1"},
                {"nbline": 12, "value": "    line 2"},
                {"nbline": 13, "value": "        line 3"}
            ]
        ]
    ]
]
```


You can easily go back to the `python` dictionary thanks to the function `loadjson` that transforms one json variable stored in one string or in a file into a flat dictionary that is an instance of the class `ReadBlock.MKOrderedDict`.
