#!/usr/bin/env python3

###
# This module ????
###

from typing import *

from abc import ABCMeta, abstractmethod


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
#     ???
###
    def __init__(
        self,
    ) -> None:
        ...


###
# prototype::
#     text : a text to add as it.
###
    @abstractmethod
    def print(self, text: str,) -> None:
        raise NotImplementedError
