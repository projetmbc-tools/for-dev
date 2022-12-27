#!/usr/bin/env python3

from typing import Any

from json    import load as json_load
from pathlib import Path
from runpy   import run_path
from yaml    import safe_load as yaml_load


# ----------------------------- #
# -- DATAS TO FEED TEMPLATES -- #
# ----------------------------- #

JNGDATAS_PYNAME = "JNG_DATAS"

###
# This class produces the internal version of data from different kinds
# of input.
###
class JNGDatas:
###
# prototype::
#     pydatas : this argument with the value ``True`` allows the execution
#               of ¨python files to build data to feed a template.
#               Otherwise, no ¨python script will be launched.
###
    def __init__(
        self,
        pydatas: bool
    ) -> None:
        self.pydatas = pydatas


###
# prototype::
#     datas : datas to feed a template. If the type used is not a ¨python
#             ¨dict, then this argument will be transformed into a string
#             in order to construct a path.
#           @ type(datas) != dict ==> exists path(str(config))
#
#     :return: data to feed a template (no chek is done).
###
    def build(
        self,
        datas: Any
    ) -> dict:
# Just one dictionary.
        if isinstance(datas, dict):
            return datas

# We need a path of one existing file.
        datas = Path(str(datas))

        if not datas.is_file():
            raise IOError(
                f"missing file:\n{datas}"
            )

# Do we manage this kind of file?
        ext = datas.suffix[1:]

        try:
            builder = getattr(self, f"build_from{ext}")

        except:
            raise ValueError(
                f"no datas builder for the extension {ext}."
            )

# Special case of the Python files.
        if ext == 'py':
            dictdatas = builder(datas)

# Other kind of files.
        else:
            with datas.open(
                encoding = 'utf-8',
                mode     = "r",
            ) as f:
                dictdatas = builder(f)

        return dictdatas


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
        if not self.pydatas:
            raise Exception(
                "''pydatas'' disabled, no Python file can't be launched "
                "to build datas."
            )

# Lets's launch the Python file, and then recover the expected value
# of the special variable.
        runner    = run_path(file)
        dictdatas = runner.get(JNGDATAS_PYNAME, None)

# The special variable is missing.
        if dictdatas is None:
            raise Exception(
                f"no ``{JNGDATAS_PYNAME}`` variable found in the Python file :"
                 "\n"
                f"{file}"
            )

# The job has been done.
        return dictdatas
