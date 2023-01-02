#!/usr/bin/env python3

from typing import (
    Any,
    Union
)

from jinja2 import (
    BaseLoader,
    Environment,
    FileSystemLoader,
)

from .config    import *
from .jngconfig import *
from .jngdatas  import *


# ------------------------------- #
# -- SPECIAL LOADER FOR JINJA2 -- #
# ------------------------------- #

###
# This class is used to allow the use of string templates.
#
# ref::
#     * https://jinja.palletsprojects.com/en/3.0.x/api/#jinja2.BaseLoader
###
class StringLoader(BaseLoader):
    def get_source(self, environment, template):
        return template, None, lambda: True


# --------------------- #
# -- JINJANG BUILDER -- #
# --------------------- #

AUTO_FLAVOUR = ":auto-flavour:"
AUTO_CONFIG  = ":auto-config:"
NO_CONFIG    = ":no-config:"


###
# This class allows to build either string, or file contents from
# ¨jinjang templates and datas.
###
class JNGBuilder:
    DEFAULT_CONFIG_FILE = "cfg.jng.yaml"

###
# prototype::
#     flavour   : this argument helps to find the dialect of one template.
#               @ flavour = AUTO_FLAVOUR
#                 or
#                 flavour in config.jngflavours.ALL_FLAVOURS
#     launch_py : this argument with the value ``True`` allows the execution
#                 of ¨python files to build data to feed a template.
#                 Otherwise, no ¨python script will be launched.
#     config    : ¨configs used to allow extra features
#               @ type(config) = str  ==> config in [AUTO_CONFIG, NO_CONFIG] ;
#                 type(config) != str ==> exists path(config)
###
    def __init__(
        self,
        flavour  : str  = AUTO_FLAVOUR,
        launch_py: bool = False,
        config   : Any  = NO_CONFIG
    ) -> None:
        self.flavour = flavour
        self.config  = config

# The update of ``launch_py`` implies the use of a new instance of
# ``self._build_datas`` via ``JNGDatas(value).build``.
        self.launch_py = launch_py


###
# One getter, and one setter for ``config`` are used to secure the values
# used for this special attribut.
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

        # self.DEFAULT_CONFIG_FILE

        self._config = value


###
# One getter, and one setter for ``launch_py`` are used to secure the values
# used for this special attribut.
###
    @property
    def launch_py(self):
        return self._launch_py

    @launch_py.setter
    def launch_py(self, value):
        self._launch_py     = value
        self._build_datas = JNGDatas(value).build


###
# One getter, and one setter for ``flavour`` are used to secure the values
# used for this special attribut.
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
#     datas    : datas used to feed one template.
#     template : one template.
#
#     :return: the output made by using ``datas`` on ``template``.
###
    def render_frompy(
        self,
        datas   : dict,
        template: str
    ) -> str:
# With ¨python varaiable, we can't detect automatically the flavour.
        if self.flavour == AUTO_FLAVOUR:
            raise ValueError(
                "no ''auto-flavour'' when working with strings."
            )

# A dict must be used for the values of the ¨jinjang variables.
        if not isinstance(datas, dict):
            raise TypeError(
                "''datas'' must be a ''dict'' variable."
            )

# Let's wirk!
        jinja2env        = self._build_jinja2env(self.flavour)
        jinja2env.loader = StringLoader()

        jinja2template = jinja2env.get_template(template)
        content        = jinja2template.render(datas)

        return content


###
# prototype::
#     datas    : datas used to feed one template.
#     template : one template.
#              @ exists path(str(template))
#     output   : the file used for the output build after using ``datas``
#                on ``template``.
#
#     :action: an output file is created with a content build after using
#              ``datas`` on ``template``.
###
    def render(
        self,
        datas   : Any,
        template: Any,
        output  : Any,
        launch_py : Union[bool, None] = None,
        config  : Any               = None
    ) -> None:
# Can we execute temporarly a ¨python file to build datas?
        if launch_py is not None:
            old_launch_py  = self.launch_py
            self.launch_py = launch_py

# Can we use temporarly specific ¨configs?
        if config is not None:
            old_config  = self.config
            self.config = config

# What is the flavour to use?
        if self.flavour == AUTO_FLAVOUR:
            flavour = self._auto_flavour(template)

        else:
            flavour = self.flavour

# Let's work!
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

# Restore previous settings if local ones have been used.
        if launch_py is not None:
            self.launch_py = old_launch_py

        if config is not None:
            self.config = old_config


###
# prototype::
#     template : one template.
#
#     :return: the flavour to be used on ``template``.
###
    def _auto_flavour(
        self,
        template: Any
    ) -> str:
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
#     flavour : this argument indicates an exiting dialect.
#             @ flavour in config.jngflavours.ALL_FLAVOURS
#
#     :return: a ``jinja2.Environment`` that will create the final output.
###
    def _build_jinja2env(
        self,
        flavour: str
    ) -> Environment:
        return Environment(
            keep_trailing_newline = True,
            **JINJA_TAGS[flavour]
        )
