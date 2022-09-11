#!/usr/bin/python3

import platform

from justcode import (
    GLOBAL_TAG,
    Params,
    Type,
)

Params[GLOBAL_TAG]['osname'] = Type.str(
    f"{platform.system()} - {platform.release()}"
)


# ----------------- #
# -- QUICK DEBUG -- #
# ----------------- #

if __name__ == '__main__':
    print(Params['osname'])
