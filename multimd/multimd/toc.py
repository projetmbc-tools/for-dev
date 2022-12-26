#!/usr/bin/env python3

###
# This module is for extracting paths from an existing path::``about.yaml``
# file of one directory.
###


from typing import *

from pathlib import Path
from yaml    import safe_load as yaml_load


# ----------- #
# -- ABOUT -- #
# ----------- #

ABOUT_FILE_NAME = "about.yaml"
TAG_TOC         = "toc"

MD_FILE_EXT    = "md"
MD_FILE_SUFFIX = f'.{MD_FILE_EXT}'


# -------------------------------------------------- #
# -- LOOK FOR A TOC INSIDE AN EXISTING ABOUT FILE -- #
# -------------------------------------------------- #

###
# This class extracts the list of paths from an existing path::``about.yaml``
# file of one directory.
#
# warning::
#     This is not the responsability of this class to test the existence
#     of the path::``about.yaml`` file.
###
class TOC():

###
# prototype::
#     onedir : the path of the directory with the path::``about.yaml`` file.
###
    def __init__(
        self,
        onedir: Path,
    ) -> None:
        self.onedir = onedir

        self._datas: List[str] = []


###
# prototype::
#     :return: the list of paths found in the yaml::``toc`` block.
###
    def extract(self) -> List[Path]:
# Lines in the TOC block.
        self.readyaml()

# Paths from the lines of the TOC block.
        pathsfound: List[str] = []

        for path in self._datas[TAG_TOC]:
# Empty path?
            if not path:
                raise ValueError(
                    f'an empty path found in ``{ABOUT_FILE_NAME}``.'
                )

# Complete short names.
            if not '.' in path:
                path = f'{path}.{MD_FILE_EXT}'

# A new path found.
            pathsfound.append(self.onedir / path)

# Everything seems ok.
        return pathsfound


###
# prototype::
#     :action: this method builds the ¨dict ``self._datas`` from
#              the ¨toc in the path::``about.yaml`` file.
###
    def readyaml(self) -> None:
        try:

            with (self.onedir / ABOUT_FILE_NAME).open(
                encoding = 'utf-8',
                mode     = "r",
            ) as f:
                self._datas = yaml_load(f)

        except Exception as e:
            raise ValueError(
                f'invalid ``{ABOUT_FILE_NAME}`` found in the following dir:'
                 '\n'
                f'{self.onedir}'
                 '\n\n'
                 'Exception from the package ``yaml``:'
                 '\n'
                f'{e}'
            )
