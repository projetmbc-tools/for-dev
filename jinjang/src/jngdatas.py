#!/usr/bin/env python3

from json    import load as json_load
from pathlib import Path
from runpy   import run_path
from yaml    import safe_load as yaml_load


JNGDATAS_PYNAME = "JNG_DATAS"


class JNGDatas:
    def __init__(
        self,
        safemode: bool
    ) -> None:
        self.safemode = safemode

    def build(self, datas: Path):
        ext = datas.suffix[1:]

        try:
            builder = getattr(self, f"build_from{ext}")

        except:
            raise ValueError(
                f"no datas builder for the extension {ext}."
            )

# Builders working one path.
        if ext == 'py':
            dictdatas = builder(datas)

# Builders working one IO content.
        else:
            with datas.open(
                encoding = 'utf-8',
                mode     = "r",
            ) as f:
                dictdatas = builder(f)

        return dictdatas


    def build_fromjson(self, file):
        return json_load(file)


    def build_fromyaml(self, file):
        return yaml_load(file)


    def build_frompy(self, datas):
        if self.safemode:
            raise Exception(
                "safemode activated, no Python file can't be launched "
                "to build datas."
            )

        runner    = run_path(datas)
        dictdatas = runner.get(JNGDATAS_PYNAME, None)

        if dictdatas is None:
            raise Exception(
                f"no ``{JNGDATAS_PYNAME}`` variable found in the Python file :"
                 "\n"
                f"{datas}"
            )

        return dictdatas
