#!/usr/bin/env python3

from typing import Union

from runpy import run_path

from jinja2 import (
    BaseLoader,
    Environment,
    FileSystemLoader,
)

from .config import *
from .jngdatas  import *


# ----------------------- #
# -- XXXX -- #
# ----------------------- #

###
#
###
class StringLoader(BaseLoader):
    def get_source(self, environment, template):
        return template, None, lambda: True


# ----------------------- #
# -- XXXX -- #
# ----------------------- #

###
#
###
class Builder:
###
# prototype::
#      flavour: ???
#             @ flavour in config.theflavours.ALL_FLAVOURS
#      auto   : ???
###
    def __init__(
        self,
        flavour : str  = FLAVOUR_ASCII,
        auto    : bool = True,
        safemode: bool = True
    ) -> None:
        self.flavour = flavour
        self.auto    = auto

# The update of ``safemode`` implies a new instance of
# ``self._build_datas`` via ``JNGDatas(value).build``.
        self.safemode = safemode


    @property
    def safemode(self):
        return self._safemode

    @safemode.setter
    def safemode(self, value):
        self._safemode    = value
        self._build_datas = JNGDatas(value).build


    @property
    def flavour(self):
        return self._flavour

    @flavour.setter
    def flavour(self, value):
        if not value in ALL_FLAVOURS:
            list_flavours = ', '.join([
                f"''{fl}''"
                for fl in ALL_FLAVOURS
            ])

            raise ValueError(
                f"flavour ''{value}'' is not one of {list_flavours}."
            )

        self._flavour = value
        self._update_internal_configs()


###
# prototype::
###
    def _update_internal_configs(self):
        self.auto_fromext    = AUTO_FROM_EXT[self.flavour]
        self.with_extratools = WITH_EXTRA_TOOLS[self.flavour]

# WARNING!
#
# If, later on, we want to allow the user to make fine configurations
# dynamically, we will expose a class to handle this type of situation.
#
# The `jinja2` environments must be kept private.
        self._jinja2env         = Environment(**JINJA_TAGS[self.flavour])
        self._jinja2env_fromstr = Environment(
            loader = StringLoader(),
            **JINJA_TAGS[self.flavour]
        )


###
# prototype::
###
    def render_fromstr(
        self,
        datas   : dict,
        template: str
    ) -> str:
        jinja2template = self._jinja2env_fromstr.get_template(template)
        content        = jinja2template.render(datas)

        return content


###
# prototype::
###
    def render(
        self,
        datas   : Path,
        template: Path,
        output  : Path
    ) -> Path:
        if output is None:
            output = template.parent / f'output{template.suffix}'

        if self.auto:
            self._auto_flavour(template)

        self._jinja2env.loader = FileSystemLoader(
            str(template.parent)
        )

        jinja2template = self._jinja2env.get_template(
            str(template.name)
        )

        dictdatas = self._build_datas(datas)
        content   = jinja2template.render(dictdatas)

        output.write_text(
            data     = content,
            encoding = "utf-8",
        )


###
# prototype::
###
    def _auto_flavour(self, template):
        flavour_found = FLAVOUR_ASCII

        for flavour, extensions in AUTO_FROM_EXT.items():
            if flavour == FLAVOUR_ASCII:
                continue

            for glob_ext in extensions:
                if template.match(glob_ext):
                    flavour_found = flavour
                    break

            if flavour_found != FLAVOUR_ASCII:
                break

        self.flavour = flavour_found
