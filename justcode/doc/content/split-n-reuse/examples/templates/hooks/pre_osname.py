#!/usr/bin/python3

import platform

from justcode import (
    TAG_MAIN,
    Params,
    JSCType,
)

Params[TAG_MAIN]['osname'] = JSCType.str(
    f"{platform.system()} - {platform.release()}"
)


# ----------------- #
# -- QUICK DEBUG -- #
# ----------------- #

if __name__ == '__main__':
    print(Params['osname'])
