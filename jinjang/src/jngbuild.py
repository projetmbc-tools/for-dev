#!/usr/bin/env python3

from typing import Union

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

AUTO_FLAVOUR = ":auto-flavour:"
AUTO_CONFIG  = ":auto-config:"
NO_CONFIG    = ":no-config:"

###
#
###
class JNGBuilder:
    DEFAULT_CONFIG_FILE = "cfg.jng.yaml"

###
# prototype::
#      flavour: ???
#             @ flavour = AUTO_FLAVOUR
#               or flavour in config.theflavours.ALL_FLAVOURS
#      pydatas : ???
#      config : ???
#             @ config in [AUTO_CONFIG, NO_CONFIG]
#               or exists path(config)
###
    def __init__(
        self,
        flavour: str              = AUTO_FLAVOUR,
        pydatas: bool             = False,
        config : Union[str, Path] = NO_CONFIG
    ) -> None:
        self.flavour = flavour
        self.config  = config

# The update of ``pydatas`` implies a new instance of
# ``self._build_datas`` via ``JNGDatas(value).build``.
        self.pydatas = pydatas


###
# prototype::
###
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
# Case of a path for a specific config file.
        if not value in [AUTO_CONFIG, NO_CONFIG]:
            raise NotImplementedError(
                "no config features for the moment..."
            )

        self._config = value


###
# prototype::
###
    @property
    def pydatas(self):
        return self._pydatas

    @pydatas.setter
    def pydatas(self, value):
        self._pydatas      = value
        self._build_datas = JNGDatas(value).build


###
# prototype::
###
    @property
    def flavour(self):
        return self._flavour

    @flavour.setter
    def flavour(self, value):
        if (
            value != AUTO_FLAVOUR
            and
            not value in ALL_FLAVOURS
        ):
            list_flavours = ', '.join([
                f"''{fl}''"
                for fl in ALL_FLAVOURS
            ])

            raise ValueError(
                f"flavour ''{value}'' is neither AUTO_FLAVOUR, "
                f"not one of {list_flavours}."
            )

        self._flavour = value


###
# prototype::
###
    def render_frompy(
        self,
        datas   : dict,
        template: str
    ) -> str:
        if self.flavour == AUTO_FLAVOUR:
            raise ValueError(
                "no ''auto-flavour'' when working with strings."
            )

        if not isinstance(datas, dict):
            raise TypeError(
                "''datas'' must be a ''dict'' variable."
            )

        jinja2env        = self._build_jinja2env(self.flavour)
        jinja2env.loader = StringLoader()

        jinja2template = jinja2env.get_template(template)
        content        = jinja2template.render(datas)

        return content


###
# prototype::
###
    def render(
        self,
        datas   : Union[dict, Path],
        template: Path,
        output  : Path,
        pydatas  = None,
        config  = None
    ) -> Path:
        if pydatas is not None:
            old_pydatas  = self.pydatas
            self.pydatas = pydatas

        if config is not None:
            old_config  = self.config
            self.config = config


        if self.flavour == AUTO_FLAVOUR:
            flavour = self._auto_flavour(template)

        else:
            flavour = self.flavour

        jinja2env        = self._build_jinja2env(flavour)
        jinja2env.loader = FileSystemLoader(
            str(template.parent)
        )

        jinja2template = jinja2env.get_template(
            str(template.name)
        )

        dictdatas = self._build_datas(datas)
        content   = jinja2template.render(dictdatas)

        output.write_text(
            data     = content,
            encoding = "utf-8",
        )

        if pydatas is not None:
            self.pydatas = old_pydatas

        if config is not None:
            self.config = old_config


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

        return flavour_found


###
# prototype::
###
    def _build_jinja2env(self, flavour):
        return Environment(**JINJA_TAGS[flavour])
