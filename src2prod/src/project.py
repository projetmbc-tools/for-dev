#! /usr/bin/env python3

###
# This module ???
###


from spkpb import *

from .base import *


# ----------------------- #
# -- PROJECT MANAGMENT -- #
# ----------------------- #

###
# This class ????
###

class Project(BaseCom):
###
# prototype::
#     name   = ; // See Python typing...
#              ???
#     source = ; // See Python typing...
#              ???
#     target = ; // See Python typing...
#              ???
#     ignore = ; // See Python typing...
#              ???
#     usegit = ; // See Python typing...
#              ???
#
# info::
#     Problems and Speaker à changer à la dur si besoin !
###
    def __init__(
        self,
        name  : str,
        source: Path,
        target: Path,
        ignore: str  = '',
        usegit: bool = False,
    ):
# To communicate.
        self.speaker  = Speaker(
            logfile = Path(f'{name}.src2prod.log'),
            style   = GLOBAL_STYLE_COLOR,
        )

        super().__init__(problems = Problems(self.speaker))

# User's choices.
        self.name   = name
        self.source = self.str2path(source)
        self.target = self.str2path(target)
        self.ignore = ignore
        self.usegit = usegit

# Extra attributs.
        self.toupdate: bool       = True
        self.lof     : List[Path] = []


###
# This method ...
###
    def str2path(self, val: Union[str, Path]) -> Path:
        valtype = type(val)

        if valtype == str:
            val = Path(val)

        elif not isinstance(val, Path):
            raise ValueError(
                f'type {valtype} unsupported to indcate '
                 'the source and the target.'
            )

        return val


###
# This method ...
###
    def build(self) -> bool:
# Does the source file exist?
        ...

