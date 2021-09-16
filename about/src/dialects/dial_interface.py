?????


#!/usr/bin/env python3

###
# This module defines constants and the interface like class ``AbstractSpeaker``
# that defines a minimal contract for speakers and also some common methods.
###


from abc import ABCMeta, abstractmethod


from typing import *


###
# This class contains technical methods used by the class ``project.Project``.
###

class AbstractDialect(metaclass = ABCMeta):
###
# prototype::
#     style    : a global style for the output. Internally this style is
#                stored in the attribut ``global_style``.
#              @ style in ALL_GLOBAL_STYLES
#     maxwidth : the maw width expected for hard wrapped contents.
###
    def __init__(
        self,
        termstyle   : str,
        maxwidth: int = 80
    ) -> None:
        self.maxwidth  = maxwidth
        self.termstyle = termstyle


###
# prototype::
#     text : a text to add as it.
###
    @abstractmethod
    def print(self, text: str,) -> None:
        raise NotImplementedError
