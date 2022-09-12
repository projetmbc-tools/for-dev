"""
This hook determines the name and the release number of the OS used when
one skeleton initiates one project. This two informations are gathered
to build one new global parameter ``osname``.
"""

import platform

from justcode import (
    TAG_MAIN,
    Params,
    JSCType,
)

Params[TAG_MAIN]['osname'] = JSCType.str(
    f"{platform.system()} - {platform.release()}"
)
