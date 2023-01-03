#!/usr/bin/env python3

###
# This module ???
###

from typing import (
    Any,
    List,
    Union
)

import os
import shlex
from subprocess import run, CalledProcessError

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

TAG_HOOKS = 'hooks'
TAG_PRE   = 'pre'
TAG_POST  = 'post'

SPE_VARS = [
    'datas',
    'template',
    'output',
]


###
# This class allows to build either string, or file contents from
# ¨jinjang templates and datas.
###
class JNGBuilder:
###
# prototype::
#     flavour   : this argument helps to find the dialect of one template.
#               @ flavour = AUTO_FLAVOUR
#                 or
#                 flavour in config.jngflavours.ALL_FLAVOURS
#     launch_py : this argument with the value ``True`` allows the execution
#                 of ¨python files to build data to feed a template.
#                 Otherwise, no ¨python script will be launched.
#     config    : :see: jngconfig.JNGConfig
###
    def __init__(
        self,
        flavour  : str  = AUTO_FLAVOUR,
        launch_py: bool = False,
        config   : Any  = NO_CONFIG,
        verbose  : bool = False,
    ) -> None:
        self.flavour = flavour
        self.config  = config
        self.verbose = verbose

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
        if value not in [AUTO_CONFIG, NO_CONFIG]:
            value = str(value)

# Nothing left to do.
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
        self._launch_py   = value
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
#     flavour  : :see: self.__init__ if the value is not ``None``.
#     launch_py: :see: self.__init__ if the value is not ``None``.
#     config   : :see: self.__init__ if the value is not ``None``.
#     verbose  : :see: self.__init__ if the value is not ``None``.
#
#     :action: an output file is created with a content build after using
#              ``datas`` on ``template``.
###
    def render(
        self,
        datas    : Any,
        template : Any,
        output   : Any,
        flavour  : Union[str, None]  = None,
        launch_py: Union[bool, None] = None,
        config   : Any               = None,
        verbose  : Union[bool, None] = None,
    ) -> None:
# Local settings.
        oldsettings = dict()

        for param in [
            "flavour",
            "launch_py",
            "config",
            "verbose",
        ]:
            val = locals()[param]

            if val is not None:
                oldsettings[param] = getattr(self, param)
                setattr(self, param, val)

# What is the flavour to use?
        if self.flavour == AUTO_FLAVOUR:
            flavour = self._auto_flavour(template)

        else:
            flavour = self.flavour

# `Path` version of the paths.
        self._datas    = Path(datas)
        self._template = Path(template)
        self._output   = Path(output)

        self._template_parent = self._template.parent

# Configs used for hooks.
        self._dict_config = build_config(
            config = self.config,
            parent = self._template_parent
        )

# Pre-hooks?
        self._pre_hooks()

# Let's go!
        jinja2env        = self._build_jinja2env(flavour)
        jinja2env.loader = FileSystemLoader(
            str(self._template_parent)
        )

        jinja2template = jinja2env.get_template(
            str(self._template.name)
        )

        dictdatas = self._build_datas(self._datas)
        content   = jinja2template.render(dictdatas)

        output.write_text(
            data     = content,
            encoding = "utf-8",
        )

# Post-hooks?
        self._post_hooks()

# Restore previous settings if local ones have been used.
        for param, oldval in oldsettings.items():
            setattr(self, param, oldval)


    def _pre_hooks(self):
        self._some_hooks(TAG_PRE)

    def _post_hooks(self):
        self._some_hooks(TAG_POST)

    def _some_hooks(self, kind: str):
        if not TAG_HOOKS in self._dict_config:
            return None

        self.launch_commands(
            f"hooks/{kind}",
            self._dict_config[TAG_HOOKS].get(kind, [])
        )

    def launch_commands(
        self,
        kind: str,
        loc : List[str]
    ) -> None:
        if not loc:
            return None

        savedwd = os.getcwd()
        os.chdir(str(self._template_parent))

        tochange = {
            sv: str(getattr(self, f"_{sv}"))
            for sv in SPE_VARS
        }

        for nbcmd, command in enumerate(loc, 1):
            try:
                r = run(
                    shlex.split(
                        command.format(**tochange)
                    ),
                    check          = True,
                    capture_output = True,
                    encoding       = "utf8"
                )

                if self.verbose:
                    print(r.stdout)

            except CalledProcessError as e:
                raise Exception(
f"""
{e.stderr}

Following command has failed (see the lines above).

  + CONFIG   >  {command}
  + EXPANDED >  {command.format(**tochange)}")

See the block '{kind}', and the command nb. {nbcmd}.
""".rstrip()
                )


        os.chdir(savedwd)


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
