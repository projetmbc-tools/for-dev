from typing import *

# toc::
#     + prologue
#     + hardway-all-outputs
#     + hardway-one-output
#     + hardway-onlyresume
#     + hardway-timestamp
#     + basecom
#     + reset


# toc::
#     * listing.sty
#     * listing-direct-FR.tex
#     * listing-input-FR.tex


# ----------- #
# -- ABOUT -- #
# ----------- #

ABOUT_NAME      = "about.peuf"
TOC_TAG         = "toc"
PLACEHOLDER     = "+"
ABOUT_PEUF_MODE = {"verbatim": TOC_TAG}

MD_FILE_EXT    = "md"
MD_FILE_SUFFIX = f'.{MD_FILE_EXT}'


# -------------------------------------------------- #
# -- LOOK FOR A TOC INSIDE AN EXISTING ABOUT FILE -- #
# -------------------------------------------------- #

###
# This class extracts the list of paths from an existing path::``about.peuf``
# file of one directory.
#
# warning::
#     This is not the responsability of this class to test the existence
#     of the path::``about.peuf`` file.
###

class TOC():

###
# prototype::
#     onedir : the path of the directory with the path::``about.peuf`` file.
###
    def __init__(
        self,
        onedir: Path,
    ) -> None:
        self.onedir = onedir

        self._lines: List[str] = []


###
# prototype::
#     :return: the list of paths found in the peuf::``toc`` block.
###
    def extract(self) -> List[Path]:
# Lines in the TOC block.
        self.readlines()

# Paths from the lines of the TOC block.
        pathsfound: List[str] = []

        for nbline, oneline in enumerate(self._lines[TOC_TAG], 1):
            path = self.pathfound(nbline, oneline)

# Empty line?
            if not path:
                continue

# Complete short names.
            if not '.' in path:
                path = f'{path}.{MD_FILE_EXT}'

# A new path found.
            pathsfound.append(self.onedir / path)

# Everything seems ok.
        return pathsfound


###
# prototype::
#     nbline  : the relative number of the line read (for message error).
#     oneline : one line to analyze.
#
#     :return: the stripped text after the placeholder peuf::``+``
#                or an empty string for an empty line.
###
    def pathfound(
        self,
        nbline : int,
        oneline: str,
    ) -> str:
        oneline = oneline.strip()

        if not oneline:
            return ""

# We are lazzy... :-)
        if len(oneline) == 1:
            oneline += " "

        firstchar, otherchars = oneline[0], oneline[1:].lstrip()

        if firstchar != PLACEHOLDER:
            raise ValueError(
                f'missing ``{PLACEHOLDER}`` to indicate a path. '
                f'See line {nbline} (number relative to the block).'
            )

        if otherchars == "":
            raise ValueError(
                f'an empty path after ``{PLACEHOLDER}``. '
                f'See line {nbline} (number relative to the block).'
            )

        return otherchars
