#!/usr/bin/env python3

###
# This module ????
###

from typing import *

from abc import ABCMeta, abstractmethod

from pathlib import Path

from orpyste.data      import ReadBlock
from orpyste.parse.ast import ASTError


###
# This class contains technical methods used by the class ``????``.
###

class AbstractDialect(metaclass = ABCMeta):
# Source to have a real interface:
#     * https://realpython.com/python-interface/#using-abcabcmeta
    @classmethod
    def __subclasshook__(cls, subclass) -> None:
        goodinterface = all(
            hasattr(subclass, methodname)
            and
            callable(getattr(subclass, methodname))
            for methodname in [

            ]
        )

        return goodinterface


###
# prototype::
#     aboutfile : ???
###
    @abstractmethod
    def extract(self, aboutfile: Path,) -> Any:
        raise NotImplementedError


###
# This method builds ``self._lines`` the list of lines stored in
# the path::``about.peuf`` file.
###
    def readlines(self) -> None:
        try:
            with ReadBlock(
                content = self.onedir / ABOUT_NAME,
                mode    = ABOUT_PEUF_MODE
            ) as datas:
                self._lines = datas.mydict("std nosep nonb")

        except ASTError:
            raise ValueError(
                f'invalid ``{ABOUT_NAME}`` found ine the following dir:'
                 '\n'
                f'{self.onedir}'
            )
