#!/usr/bin/env python3

###
# This module contains the ¨specs of the templates proposed by default.
###

TEMPLATES_SPECS = {}


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TAG_MERGED_TEMPLATES = 'merged-templates'
TAG_LICENSES_ADDED   = 'added-licenses'

TAG_ROOT_DIR = None

# -- Tags for licenses "AUTO" - START -- #

TAG_CC_BY_NC_SA_4 = "BY-NC-SA 4.0"
TAG_GPL3          = "GPL-3.0-only"

# -- Tags for licenses "AUTO" - END -- #


# ------------------ #
# -- cbdev-python -- #
# ------------------ #

TEMPLATES_SPECS['cbdev-python'] = {
    TAG_MERGED_TEMPLATES: [
        'changes',
        'poetry',
        'readme',
    ],
    TAG_LICENSES_ADDED: {
        'src'  : TAG_GPL3,
        'tools': TAG_GPL3,
        'tests': TAG_GPL3,
    }
}


# ------------- #
# -- changes -- #
# ------------- #

TEMPLATES_SPECS['changes'] = {
    TAG_LICENSES_ADDED: {
        TAG_ROOT_DIR: TAG_CC_BY_NC_SA_4,
    }
}


# ------------- #
# -- readme -- #
# ------------- #

TEMPLATES_SPECS['readme'] = {
    TAG_LICENSES_ADDED: {
        TAG_ROOT_DIR: TAG_CC_BY_NC_SA_4,
    }
}


# --------------------------- #
# -- readme (not a native) -- #
# --------------------------- #

TEMPLATES_SPECS['readme-not-a-native'] = {
    TAG_LICENSES_ADDED: {
        TAG_ROOT_DIR: TAG_CC_BY_NC_SA_4,
    }
}
