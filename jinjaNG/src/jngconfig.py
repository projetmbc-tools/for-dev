#!/usr/bin/env python3

###
# This module ???
###

from typing import Union

from pathlib import Path
from yaml    import safe_load as yaml_load


# ---------------------- #
# -- SPECIFIC CONFIGS -- #
# ---------------------- #

AUTO_CONFIG = ":auto-config:"
NO_CONFIG   = ":no-config:"

DEFAULT_CONFIG_FILE = "cfg.jng.yaml"


###
# prototype::
#     config : ¨configs used to allow extra features
#            @ config in [AUTO_CONFIG, NO_CONFIG]
#              or
#              exists path(config)
#     parent : ?????  where we work if we use the autoconf ignored in other cases !
###
def build_config(
    config: str,
    parent: Union[Path, None] = None
) -> dict:
# No config used.
    if config == NO_CONFIG:
        return dict()

# Default name for the config file?
    if config == AUTO_CONFIG:
        if parent is None:
            raise ValueError(
                 "Missing parent directory for the default config file."
            )

        config = parent / DEFAULT_CONFIG_FILE

# User's config file.
    else:
        config = Path(config)

        if config.suffix != '.yaml':
            raise ValueError(
                 "The config file is not a YAML one. See:\n"
                f"  + {config}"
            )

# One YAML direct conversion.
    with config.open(
        encoding = 'utf-8',
        mode     = "r",
    ) as f:
        return yaml_load(f)
