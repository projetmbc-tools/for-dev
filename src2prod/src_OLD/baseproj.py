#!/usr/bin/env python3

###
# This module is just a factorization of technical and stupid methods.
###


from typing import Union

from shutil     import copyfile
from subprocess import run

from spkpb import *


# ------------------------------------------ #
# -- ABSTRACT CLASS FOR LOW LEVEL ACTIONS -- #
# ------------------------------------------ #

###
# This class contains technical methods used by the class ``project.Project``.
###
class BaseProj(BaseCom):
    DIR_TAG  = 'dir'
    FILE_TAG = 'file'

###
# prototype::
#     project : the folder project that will be used to communicate during
#               the analysis.
#     src     : the **relative** path of the src dir (regarding the project
#               folder).
#     dest    : the **relative** path of the final product dir (regarding the
#               project folder).
#     ignore  : if a string is used then this gives the rules for ignoring
#               files in addition to what \git does.
#               If an instance of ``Path`` is used, thent we have a file
#               containing the rules.
#     usegit  : ``True`` asks to use \git contrary to ``False``.
#     readme  : ``None`` is to import an external path::``README`` file,
#               otherwise give a **relative** path.
#
# warning::
#     The dest folder is totally removed and reconstructed at each new
#     update.
#
# note::
#     Additional attributes are created/reseted by the method ``reset``.
###
    def __init__(
        self,
        project: Path,
        src    : Path,
        dest   : Path,
        ignore : Union[str, Path]  = '',
        usegit : bool              = False,
        readme : Union[None, Path] = None,
    ) -> None:
# To communicate.
        self.logfile = project / f'{project.name}.src2prod.log'

        super().__init__(
            Problems(
                Speaker(
                    logfile = self.logfile,
                    style   = GLOBAL_STYLE_COLOR,
                )
            )
        )

# User's choices.
        self.project = project
        self.src     = self.project / src
        self.dest    = self.project / dest

        self.ignore = ignore
        self.usegit = usegit

        if not readme is None:
            readme = self.project / readme

        self.readme_src            = readme
        self._readme_is_file: bool = True
        self._readme_dest   : Path = self.dest / 'README.md'


###
# prototype::
#     kind : the kind of making made
#
#     :action: this method resets everything.
#
#     :see: spkpb.problems.Problems.reset
###
    def reset(
        self,
        kind: str = 'SRC --> FINAL PRODUCT'
    ) -> None:
        super().reset()

        self.recipe(
            FORLOG,
                {VAR_TITLE:
                    f'"{self.project.name}": {kind}'},
        )

# Extra attributs.
        self.success         = True
        self.lof: List[Path] = []


###
# prototype::
#     :action: this method builds ``self.ignore_rules`` which is a dictionary.
#
# Here is how the dictionary looks like.
#
# python::
#     {
#         self.DIR_TAG : [
#             rule_1_to_ignore_some_dirs,
#             rule_2_to_ignore_some_dirs,
#             ...
#         ],
#         self.FILE_TAG : [
#             rule_1_to_ignore_some_files,
#             rule_2_to_ignore_some_files,
#             ...
#         ],
#     }
###
    def build_ignore(self) -> None:
# A file to read?
        if not isinstance(self.ignore, Path):
            ignorerules = self.ignore

        else:
            self.recipe(
                {VAR_STEP_INFO:
                    f'Ignore rules in the file:'
                     '\n'
                    f'"{self.ignore}"'},
            )

            if not self.ignore.is_file():
                self.new_error(
                    what = self.ignore,
                    info = f'file with ignore rules not found.',
                )

                self.ignore_rules = None
                return

            with self.ignore.open(
                encoding = 'utf-8',
                mode     = 'r',
            ) as f:
                ignorerules = f.read()

# Let's build our internal dictionary.
        self.ignore_rules = {
            self.DIR_TAG : [],
            self.FILE_TAG: [],
        }

        for rule in ignorerules.split('\n'):
            if not(shortrule := rule.strip()):
                continue

# A dir rule.
            if shortrule.endswith('/'):
                context   = self.DIR_TAG
                shortrule = shortrule[:-1]

# A file rule.
            else:
                context = self.FILE_TAG

            self.ignore_rules[context].append(shortrule)


###
# prototype::
#     fileordir : the path of a file or a dir.
#     kind      : the kind of \io object.
#               @ kind in [self.DIR_TAG, self.FILE_TAG]
#
#     :return: ``True`` if the \io object must be kept regarding the ignore
#              rules, and ``False`` otherwise.
#
# note::
#     \git is not used here.
###
    def keepthis(
        self,
        fileordir: Path,
        kind     : str
    ) -> bool:
        for onerule in self.ignore_rules[kind]:
            if fileordir.match(onerule):
                return False

        return True


###
# prototype::
#     onedir : a dir to analyze.
#
#     :yield: the files in the folder ``onedir`` kept after the application
#             of the ignore rules.
#
# note::
#     \git is not used here.
###
    def iterfiles(self, onedir: Path) -> Path:
        for fileordir in onedir.iterdir():
            if fileordir.is_dir():
                if self.keepthis(
                    fileordir = fileordir,
                    kind      = self.DIR_TAG
                ):
                    for onefile in self.iterfiles(onedir = fileordir):
                        yield onefile

            elif self.keepthis(
                fileordir = fileordir,
                kind      = self.FILE_TAG
            ):
                yield fileordir


###
# prototype::
#     onedir : a dir.
#
#     :return: ``True`` if the folder doesn't exist yet or is empty and
#              ``False`` otherwise.
###
    def isempty(self, onedir: Path) -> bool:
# The folder doesn't exist.
        if not onedir.is_dir():
            return True

# Does the folder contain something?
        nothingfound = True

        for _ in onedir.iterdir():
            nothingfound = False
            break

# The job has been done.
        return nothingfound


###
# prototype::
#     src : the path of the src file to copy.
#     dest : the path of the dest file that will be the copy.
#
#     :action: this method copies one file.
###
    def copyfile(
        self,
        src: Path,
        dest: Path,
    ) -> None:
        dest.parent.mkdir(
            parents  = True,
            exist_ok = True
        )

        copyfile(src, dest)


###
# prototype::
#     options : a list of options.
#
#     :return: the stripped standard output sent by the command.
#
# This method launches the command terminal::``git`` with the options given
# in the list ``options``.
###
    def rungit(self, options: List[str]) -> str:
        cmd = ['git'] + options

# Launch the command in the project folder.
        try:
            output = run(
                cmd,
                capture_output = True,
                cwd            = self.project
            )

# Can't launch the command.
        except FileNotFoundError as e:
            cmd = " ".join(cmd)

            self.new_error(
                what = self.src,
                info = f'can\'t use "{cmd}".',
            )
            return

# Command launched throws an error.
        if output.stderr:
            self.new_error(
                what = self.src,
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
# prototype::
#     bytedatas : a byte content.
#
#     :return: the string obtained by decoding with the \utf8 encoding.
###
    def decode(self, bytedatas: bytes) -> str:
        return bytedatas.decode('utf-8')
