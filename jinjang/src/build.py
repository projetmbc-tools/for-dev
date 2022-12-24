#!/usr/bin/env python3

from typing import Union

from json    import load as jsonload
from pathlib import Path

from jinja2 import (
    BaseLoader,
    Environment,
    FileSystemLoader,
)

from .config import *


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
        flavour: str  = FLAVOUR_ASCII,
        auto   : bool = True,
    ) -> None:
        self.flavour = flavour
        self.auto    = auto


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
        output  : Union[Path, None] = None
    ) -> Path:
        if output is None:
            output = template.parent / f'output{template.suffix}'

        self._jinja2env.loader = FileSystemLoader(
            str(template.parent)
        )

        jinja2template = self._jinja2env.get_template(
            str(template.name)
        )

        with datas.open(
            encoding = 'utf-8',
            mode     = "r",
        ) as f:
            dictdata = jsonload(f)

        content = jinja2template.render(dictdata)

        output.write_text(
            data     = content,
            encoding = "utf-8",
        )
