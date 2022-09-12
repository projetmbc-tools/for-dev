#!/usr/bin/python3

import platform

from justcode import (
    TAG_MAIN,
    Params,
    Type,
)

Params[TAG_MAIN]['osname'] = Type.str(
    f"{platform.system()} - {platform.release()}"
)


# ----------------- #
# -- QUICK DEBUG -- #
# ----------------- #

if __name__ == '__main__':
    print(Params['osname'])
