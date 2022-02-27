#!/usr/bin/env python3

###
# This file implements the interface like class ``AbstractDialect`` which
# defines a minimal contract for dialects but also some common methods.
###


from typing import *

from abc import ABCMeta, abstractmethod

from pathlib import Path

from orpyste.data      import ReadBlock
from orpyste.parse.ast import ASTError


# -------------------------------- #
# -- ABSTRACT / INTERFACE CLASS -- #
# -------------------------------- #

###
# This abstract class / interface defines the common ¨api of the dialects.
###
class AbstractDialect(metaclass = ABCMeta):
# Source to have a "real" interface in Python:
#     * https://realpython.com/python-interface/#using-abcabcmeta
    @classmethod
    def __subclasshook__(cls, subclass) -> None:
        goodinterface = all(
            hasattr(subclass, methodname)
            and
            callable(getattr(subclass, methodname))
            for methodname in [
                'extract',
            ]
        )

        return goodinterface


###
# prototype::
#     file : the path of the file to analyze.
#
#     :return: a specific structure proposed by one dialect.
###
    @abstractmethod
    def extract(self, file: Path) -> Any:
        raise NotImplementedError


###
# prototype::
#     file : the path of the file to analyze.
#     mode : the ¨orpyste mode of the file to analyze.
#
#     :return: a standard dict build by the class ``ReadBlock`` from
#              the module ¨orpyste.
###
    def stddict(
        self,
        file: Path,
        mode: Union[str, dict]
    ) -> Dict:
        try:
            with ReadBlock(
                content = file,
                mode    = mode
            ) as datas:
                return datas.mydict("std nosep nonb")

        except ASTError:
            raise ValueError(
                f'invalid file:'
                 '\n'
                f'{file}'
            )
