#!/usr/bin/env python3

from typing import Any

from json    import load as json_load
from pathlib import Path
from runpy   import run_path
from yaml    import safe_load as yaml_load


# ---------------------------- #
# -- DATA TO FEED TEMPLATES -- #
# ---------------------------- #

JNGDATA_PYNAME = "JNGDATA"

###
# This class produces the internal version of data from different kinds
# of input.
###
class JNGData:
###
# prototype::
#     launch_py : this argument with the value ``True`` allows the execution
#                 of ¨python files to build data to feed a template.
#                 Otherwise, no ¨python script will be launched.
###
    def __init__(
        self,
        launch_py: bool
    ) -> None:
        self.launch_py = launch_py


###
# prototype::
#     data : data to feed a template. If the type used is not a ¨python
#            ¨dict, then this argument will be transformed into a string
#            in order to construct a path.
#          @ type(data) != dict ==> exists path(str(config))
#
#     :return: data to feed a template (no chek is done).
###
    def build(
        self,
        data: Any
    ) -> dict:
# Just one dictionary.
        if isinstance(data, dict):
            return data

# We need a path of one existing file.
        data = Path(str(data))

        if not data.is_file():
            raise IOError(
                f"missing file:\n{data}"
            )

# Do we manage this kind of file?
        ext = data.suffix[1:]

        try:
            builder = getattr(self, f"build_from{ext}")

        except:
            raise ValueError(
                f"no data builder for the extension {ext}."
            )

# Special case of the Python files.
        if ext == 'py':
            dictdata = builder(data)

# Other kind of files.
        else:
            with data.open(
                encoding = 'utf-8',
                mode     = "r",
            ) as f:
                dictdata = builder(f)

        return dictdata


###
# prototype::
#     file: path of a ¨json file.
#
#     :return: data to feed a template (no chek is done).
###
    def build_fromjson(
        self,
        file
    ) -> dict:
        return json_load(file)


###
# prototype::
#     file: path of a ¨yaml file.
#
#     :return: data to feed a template (no chek is done).
###
    def build_fromyaml(
        self,
        file
    ) -> dict:
        return yaml_load(file)


###
# prototype::
#     file: path of a ¨python file.
#
#     :return: data to feed a template (no chek is done).
###
    def build_frompy(
        self,
        file: Path
    ) -> dict:
# Are we allowed to launch a Python file?
        if not self.launch_py:
            raise Exception(
                "''launch_py'' disabled, no Python file can't be launched "
                "to build data."
            )

# Lets's launch the Python file, and then recover the expected value
# of the special variable.
        runner    = run_path(file)
        dictdata = runner.get(JNGDATA_PYNAME, None)

# The special variable is missing.
        if dictdata is None:
            raise Exception(
                f"no ``{JNGDATA_PYNAME}`` variable found in the Python file :"
                 "\n"
                f"{file}"
            )

# The job has been done.
        return dictdata
