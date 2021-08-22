#!/usr/bin/env python3

###
# This module simplifies the use of path::``PEUF`` files for datas used
# to achieve unit tests (see the project ¨orpyste).
###


from typing import *

from pathlib import Path
from pytest  import fixture

from orpyste.data import ReadBlock


###
# prototype::
#     :see: = build_datas_block
#
# This fixture yields a ready-to-use data dictionary used to acheive the tests.
# It also finalizes the cleaning of ¨orpyste extra files in case of problem.
#
# info::
#     The "intuitive" dictionary is build via ``mydict("std nosep nonb")``
#     (see ¨orpyste).
# 
# 
# Here is a real example of use with the following partial tree structure.
#
# tree-dir::
#     + TeXitEasy
#         + src
#             * __init__.py
#             * escape.py
#         + tests
#             + escape
#                 + fstringit.peuf
#                 + test_fstringit.py
#
# The ¨python testing file path::``test_fstringit.py`` is associated 
# to the path::``PEUF`` file path::``fstringit.peuf`` where the prefix 
# path::``test_`` has been removed. Using the datas stored in this 
# path::``PEUF`` file becomes very easy: here is the code used where 
# ``tests`` is an intuitive ¨dict version of the path::``PEUF`` file.
#
# python::
#     from cbdevtools import *
#
#     addfindsrc(
#         file    = __file__,
#         project = 'TeXitEasy',
#     )
#
#     from src.escape import fstringit
#
#     def test_latex_use_fstringit(peuf_fixture):
#         tests = peuf_fixture(__file__)
#
#         for infos in tests.values():
#             found  = fstringit(infos['source'])
#             wanted = infos['fstring']
#
#             assert wanted == found
###

# Refs
#    * https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session
#    * https://docs.pytest.org/en/6.2.x/fixture.html#factories-as-fixtures

@fixture(scope = "session")
def peuf_fixture() -> None:
    datas_build = []

###
# This internal function always has the same signature as the function 
# ``build_datas_block``.
###
    def _make_peuf_datas(*args, **kwargs) -> None:
        datas_build.append(
            datas := build_datas_block(*args, **kwargs)
        )
        
        datas.build()

        return datas.mydict("std nosep nonb")

    yield _make_peuf_datas

    for datas in datas_build:
        datas.remove_extras()


###
# prototype::
#     file = just use the magic constant ``__file__`` when calling
#            this function from a testing file.
#
#     :return: = an object containing the datas defined in a 
#                path::``PEUF`` file (see the ¨info below).
#
# This function returns an instance of ``ReadBlock`` associated to 
# a path::``peuf`` file automatically named. 
# 
# info::
#     The name of the path::``peuf`` file is obtained by removing the prefix
#     path::``test_`` from the name of the testing file (see the ¨tech ¨doc
#     of ``peuf_fixture`` for a concrete example).
###

def build_datas_block(
    file: str,
) -> ReadBlock:
    file    = Path(file)
    filedir = file.parent

    whatistested = file.stem
    whatistested = whatistested.replace('test_', '')

    return ReadBlock(
        content = filedir / f'{whatistested}.peuf',
        mode    = {"keyval:: =": ":default:"}
    )
