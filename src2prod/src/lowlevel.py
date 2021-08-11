#! /usr/bin/env python3

###
# This module ???
###

from os import getcwd, popen
from subprocess import run

from spkpb import *


# ----------------------- #
# -- ??? -- #
# ----------------------- #

###
# This class contains technical methods used by the class ``project.Project``.
###

class LowLevel(BaseCom):
    DIR_TAG  = 'dir'
    FILE_TAG = 'file'

###
# prototype::
#     name   = ; // See Python typing...
#              the folder project that will be used to communicate 
#              during the analysis.
#     source = ; // See Python typing...
#              the relative path of the source dir (regarding the project
#              folder).
#     target = ; // See Python typing...
#              the relative path of the final product dir (regarding the
#              project folder).
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
        project: Union[str, Path],
        source : Union[str, Path],
        target : Union[str, Path],
        ignore : str  = '',
        usegit : bool = False,
    ):
# To communicate.
        self.logfile_name = f'{project.name}.src2prod.log'

        super().__init__(
            Problems(
                Speaker(
                    logfile = Path(self.logfile_name),
                    style   = GLOBAL_STYLE_COLOR,
                )
            )
        )

# User's choices.
        self.project = self.cv2path(project)
        self.source  = self.project / self.cv2path(source)
        self.target  = self.project / self.cv2path(target)
        self.usegit  = usegit
        
        self.build_ignore(ignore)


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
        super().reset()

        self.recipe(
            FORLOG,
                {VAR_TITLE: f'"{self.project}": SOURCE --> FINAL PRODUCT'},
        )

# Extra attributs.
        self.lof: List[Path] = []

        self._cwd            = getcwd()
        self._source_rel_cwd = self.source.relative_to(self._cwd)
        

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
###
    def build_ignore(self, ignore: str) -> None:
        self.ignore = {
            self.DIR_TAG : [],
            self.FILE_TAG: [],
        }

        for rule in ignore.split('\n'):
            if not(shortrule := rule.strip()):
                continue

# A dir rule.
            if shortrule.endswith('/'):
                context   = self.DIR_TAG
                shortrule = shortrule[:-1]

# A file rule.
            else:
                context = self.FILE_TAG
            
            self.ignore[context].append(shortrule)

###
# This method ...
# no git here!!!
###
    def keepthis(
        self,
        fileordir: Path,
        context  : str
    ) -> bool:            
        for onerule in self.ignore[context]:
            if fileordir.match(onerule):
                return False

        return True

###
# This method ...
###
    def iterfiles(self, onedir: Path) -> str:
        for fileordir in onedir.iterdir():
            if fileordir.is_dir():
                if self.keepthis(
                    fileordir = fileordir,
                    context   = self.DIR_TAG
                ):
                    for onefile in self.iterfiles(onedir = fileordir):
                        yield onefile

            elif self.keepthis(
                fileordir = fileordir,
                context   = self.FILE_TAG
            ):
                yield fileordir


###
# This method ...
###
    def rungit(self, options: str) -> None:
        cmd = ['git'] + options

# Launch the command.
        try:
            output = run(
                cmd, 
                capture_output = True,
                cwd            = self._cwd
            )

# Can't launch the command.
        except FileNotFoundError as e:
            cmd = " ".join(cmd)
    
            self.new_error(
                what = self.source,
                info = f'can\'t use "{cmd}".',
            )
            return

# Command launched throws an error.
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

# The work has been done correctly.
        return self.decode(output.stdout).strip()

###
# This method ...
###
    def decode(self, bytedatas: bytes) -> str:
        return bytedatas.decode('utf-8').strip()