#! /usr/bin/env python3

###
# This module ???
###


from spkpb import *


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
#              the name of the project that will be used to communicate 
#              during the analysis.
#     source = ; // See Python typing...
#              the path of the source dir.
#     target = ; // See Python typing...
#              the path of the final product dir.
#     ignore = ; // See Python typing...
#              the rules for ignoring files in addition to what ¨git does.
#     usegit = ( False ) ; // See Python typing...
#              ''True'' aksks to use git contrary to ``False``.
#
# warning::
#     The target folder is totaly remove and reconstruct at each new
#     update.
###
    def __init__(
        self,
        name  : str,
        source: Union[str, Path],
        target: Union[str, Path],
        ignore: str  = '',
        usegit: bool = False,
    ):
# To communicate.
        self._logfilename = f'{name}.src2prod.log'

        super().__init__(
            Problems(
                Speaker(
                    logfile = Path(self._logfilename),
                    style   = GLOBAL_STYLE_COLOR,
                )
            )
        )

# User's choices.
        self.name   = name
        self.source = self.cv2path(source)
        self.target = self.cv2path(target)
        self.ignore = ignore
        self.usegit = usegit


###
# prototype::
#     value = ; // See Python typing...
#             a path.
#
#     :return: = ; // See Python typing...
#                the path converted to an instance of ``pathlib.Path``.
###
    def cv2path(self, value: Union[str, Path]) -> Path:
        valtype = type(value)

        if valtype == str:
            value = Path(value)

        elif not isinstance(value, Path):
            raise ValueError(
                f'type {valtype} unsupported to indicate '
                 'the source and the target.'
            )

        return value


###
# This method ...
###
    def reset(self) -> None:
# ????
        super().reset()

        self.recipe(
            FORLOG,
                {VAR_TITLE: f'"{self.name}": SOURCE --> FINAL PRODUCT'},
        )

# Extra attributs.
        self.toupdate: bool       = True
        self.lof     : List[Path] = []


###
# This method ...
###
    def build(self) -> None:
# Time is... time.
        self.timestamp("build - start")

# New start...
        self.reset()
        
# Say "Hello!".
        self.recipe(
            FORTERM,
                {VAR_STEP_INFO: 
                    f'The log file used will be "{self._logfilename}".'},
            FORALL,
                {VAR_STEP_INFO: 
                    'Start the analysis of the source folder.'},
        )

# Does the source file exist?




# Time is... time.
        self.timestamp("build - end")
