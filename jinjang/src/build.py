#!/usr/bin/env python3

from pathlib import Path

from jinja2 import *

from .config import *

# ----------------------- #
# -- XXXX -- #
# ----------------------- #

class Builder:
    def __init__(self, auto = True):
        self.auto = auto

# Via des chemins
    def render(
        self,
        datas   : Path,
        template: Path
    ) -> Path:
        ...

# Via des chapines
    def render_fromstr(
        self,
        datas   : str,
        template: str
    ) -> str:
        ...

# Update the ``jinja2`` environment class.
    def __uodate_jinja2_env(self):
        self._jenv = latex_jinja_env = Environment(
            variable_start_string = '<:',
            variable_end_string   = ':>',

            block_start_string    = '%<:',
            block_end_string      = ':>%',
            line_statement_prefix = '%%',

            comment_start_string  = '%<#',
            comment_end_string    = '#>%',
            line_comment_prefix   = '%#',

            trim_blocks           = True,
            autoescape            = False,
            loader                = FileSystemLoader(str(THIS_DIR))
        )
