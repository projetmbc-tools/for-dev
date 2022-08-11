### Signature of a callable object

To produce good quality code, it is very important to know the signature of a function, or a method. The purpose of the fucntion `.easysign`is to give an eays-to-use dictionary giving all the informations about a signature.

Let's start with the code above where we use `pprint` to obtain well formatted output.

~~~python
from pprint              import pprint
from cbdevtools.easysign import easysign

def funcOK(a:int, b: int = 1) -> str:
    ...

pprint(easysign(funcOK))
~~~

Launched in a terminal, we obtain the output below showing that the dictionary returned is very easy to use.

~~~
{'optional': ['b'],
 'params': {'a': {'default': None, 'typing': 'int'},
            'b': {'default': '1', 'typing': 'int'}},
 'return': 'str'}
~~~

***WARNING!*** *When nothing has been indicated in the original code, the value `None` is used.*


The signature of a method is also easy to obtain as it is done in the following code.

~~~python
class Test:
    def nothing(self):
        ...
    def noparam(self) -> str:
        ...
    def partialsign(self, a: str, b):
        ...
    def paramOK(self, a, b: bool = True) -> str:
        ...

mytest = Test()

for name in [
    "nothing",
    "noparam",
    "partialsign",
    "paramOK",
]:
    print(f"easysign(mytest.{name})")
    pprint(
        easysign(
            mytest.__getattribute__(name)
        )
    )
    print()
~~~

Here is the corresponding output.

~~~
easysign(mytest.nothing)
{'optional': [], 'params': {}, 'return': None}

easysign(mytest.noparam)
{'optional': [], 'params': {}, 'return': 'str'}

easysign(mytest.partialsign)
{'optional': [],
 'params': {'a': {'default': None, 'typing': 'str'},
            'b': {'default': None, 'typing': None}},
 'return': None}

easysign(mytest.paramOK)
{'optional': ['b'],
 'params': {'a': {'default': None, 'typing': None},
            'b': {'default': 'True', 'typing': 'bool'}},
 'return': 'str'}
~~~


To end this section, you have to know that using `easysign(1)` will raise the following error.

~~~
[...]
TypeError: 1 is not a callable object
~~~
