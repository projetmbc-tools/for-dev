#! /usr/bin/env python3

###
# This module ???
###

from subprocess import run

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
#     The target folder is totally removed and reconstructed at each new
#     update.
#
# info::
#     Additional attributes are reseted in the method ``reset``.
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
        self.logfile_name = f'{name}.src2prod.log'

        super().__init__(
            Problems(
                Speaker(
                    logfile = Path(self.logfile_name),
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
        self.toupdate   : bool       = True
        self.lof        : List[Path] = []
        self.lof_ignored: List[Path] = []

###
# This method builds the list of file to copy from source to target and also
# the value of the attribute ``toupdate``.
###
    def build(
        self,
        opensession : bool = True,
        closesession: bool = True,) -> None:
# Reset fo a new start.
        self.reset()

# Open a session?
        if opensession:
            self.open_session()

# Let's work.
        for methodname in [
            'build_lof'
        ]:
            getattr(self, methodname)()

            if not self.success:
                break

# Cose a session?
        if closesession:
            self.close_session()

###
# This method ...
###
    def open_session(self):
        self.timestamp("build - start")

        self.recipe(
                {VAR_TITLE: 'L.O.F + UPDATE OR NOT.'},
            FORTERM,
                {VAR_STEP_INFO: 
                    f'The log file used will be "{self.logfile_name}".'},
        )

###
# This method ...
###
    def close_session(self):
        self.resume()
        
        self.recipe(
            FORLOG,
                NL
        )
        
        self.timestamp("build - end")

###
# This method ...
#
# info::
#     The method ``reset`` has been used just before the call of this method.
###
    def build_lof(self):
# Say "Hello!".
        self.recipe(
            {VAR_STEP_INFO: 
                 'Start the analysis of the source folder:'
                 '\n'
                f'"{self.source}".'},
        )

# Does the source dir exist?
        if not self.source.is_dir():
            self.new_error(
                what = self.source,
                info = (
                     'source folder not found:'
                     '\n'
                    f'"{self.source}"'
                ),
            )
            return

# Do we have to use git?
        if not self.usegit:
            self.toupdate = True

        else:
            self.infos_from_git()

            if not self.success:
                return

# What must be ignored?
        if self.usegit:
            ...

###
# This method ...
###
    def infos_from_git(self):
        infos = {}

        for kind, options in [
# Current branch.
            ('branchused', ['branch']),
# We don't want uncommitted files in our source folder!
            ('uncommitted', ['a']),
        ]:
            infos[kind] =  self.rungit(options)
    
            if not self.success:
                return

        from pprint import pprint;pprint(infos)


###
# This method ...
###
    def rungit(self, options: str) -> None:
        cmd = ['git'] + options

# Launch the command.
        try:
            output = run(
                cmd, 
                capture_output = True
            )

# Can't launch the command.
        except FileNotFoundError as e:
            cmd = " ".join(cmd)
    
            self.new_error(
                what = self.source,
                info = f'can\'t use "{cmd}".',
            )
            return

# Command launched thorwis an error.
        if output.stderr:
            self.new_error(
                what = self.source,
                info = (
                    f'error throwed by "{cmd}":'
                     '\n'
                    f'"{self.decode(output.stderr)}".'
                ),
            )
            return

# The work has been done.
        return self.decode(output.stdout)

###
# This method ...
###
    def decode(self, bytedatas: bytes) -> str:
        return bytedatas.decode('utf-8').strip()

