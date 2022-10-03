#!/usr/bin/env python3

from collections import defaultdict
from json        import load

from mistool.os_use import PPath as Path

from core import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

DATAS_DIR = THIS_DIR / 'datas'
FINAL_DIR = DATAS_DIR / 'final'

PREFERRED_JSON_FILE = THIS_DIR / 'preferred-rules.json'

MINIMIZE_DIR         = DATAS_DIR / 'minimize'
MINIMIZE_AUTO_DIR    = MINIMIZE_DIR / 'auto'
MINIMIZE_BY_HAND_DIR = MINIMIZE_DIR / 'byhand'

MAIN_FILE = '_MAIN_.txt'

PREFERRED_RULES      = set()
DUPLICATES_TO_REMOVE = set()

for choice, toremove in {
# online/C++ | online/FORTRAN
    "online/C++": [
        "online/FORTRAN",
    ],
# online/CLOJURE | online/LEININGEN
    "online/CLOJURE": [
        "online/LEININGEN",
    ],
# online/JBOSS-6-X | online/JBOSS6
    "online/JBOSS6": [
        "online/JBOSS-6-X",
    ],
# online/MAGENTO | online/MAGENTO1
    "online/MAGENTO": [
        "online/MAGENTO1",
    ],
# online/PIMCORE | online/PIMCORE4
    "online/PIMCORE": [
        "online/PIMCORE4",
    ],
}.items():
    PREFERRED_RULES.add(choice)

    for kind_name in toremove:
        DUPLICATES_TO_REMOVE.add(kind_name)


PREFERRED_BY_HAND_NAMES = {
# online/BLOOP | online/METALS
    "['online/BLOOP', 'online/METALS']": 'online/BLOOP',
# online/DRUPAL | online/TYPO3-COMPOSER
    "['online/DRUPAL', 'online/TYPO3-COMPOSER']": 'online/DRUPAL',
# online/ERLANG | online/HOMEASSISTANT
    "['online/ERLANG', 'online/HOMEASSISTANT']": 'online/ERLANG',
# online/EXTJS | online/SENCHATOUCH
    "['online/EXTJS', 'online/SENCHATOUCH']": 'online/EXTJS',
# online/FLASHBUILDER | online/FLEX
    "['online/FLASHBUILDER', 'online/FLEX']": 'online/FLEX',
# online/FSHARP | online/MIKROC
    "['online/FSHARP', 'online/MIKROC']": 'online/FSHARP',
# online/GIT | online/KDIFF3
    "['online/GIT', 'online/KDIFF3']": 'online/GIT',
# online/GRAILS | online/PLAYFRAMEWORK
    "['online/GRAILS', 'online/PLAYFRAMEWORK']": 'online/PLAYFRAMEWORK',
# online/HOMEASSISTANT | online/WEB
    "['online/HOMEASSISTANT', 'online/WEB']": 'online/WEB',
# online/VIVADO | online/XILINXVIVADO
    "['online/VIVADO', 'online/XILINXVIVADO']": 'online/VIVADO',
}


NB_RULES_ADDED = 0


ALL_KINDS = [
    TAG_CONTRIB := 'contribute',
    TAG_ONLINE  := 'online',
]

RULES = {}

for kind in ALL_KINDS:
    with (DATAS_DIR / kind /'0-rules-0.json').open(
        encoding = 'utf-8',
        mode     = 'r',
    ) as f:
        for name, rules in load(f).items():
            RULES[build_kindname(kind, name)] = rules

# ! -- DEBUGGING -- ! #
# print('')
# print(f"{RULES.keys() = }")
# exit()
# ! -- DEBUGGING -- ! #


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3
TAB_4 = TAB_1*4


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ---------------------- #
# -- RULES OF THE API -- #
# ---------------------- #

print(
    f"{TAB_1}* Collecting the rules proposed by the API."
)

apirules = set()

for p in FINAL_DIR.glob('*/*.txt'):
    apirules = apirules.union(
        rulesfrom(
            p.read_text(
                encoding = 'utf-8'
            )
        )
    )

nb_apirules = len(apirules)

if nb_apirules == 0:
    print(
        f"{TAB_2}+ No rules in the API."
    )

else:
    plurial = "" if nb_apirules == 1 else "s"

    print(
        f"{TAB_2}+ {nb_apirules} rule{plurial} in the API."
    )


# -------------------------------- #
# -- NO DUPLICATE SETS OF RULES -- #
# -------------------------------- #

# ! -- DEBUGGING -- ! #
# print('')
# print(f"{PREFERRED_RULES = }")
# print('')
# print(f"{DUPLICATES_TO_REMOVE = }")
# exit()
# ! -- DEBUGGING -- ! #

print(
    f"{TAB_1}* Looking for duplicated sets of rules."
)

setofpatterns_DEPS = defaultdict(set)

for kind_name, patterns in RULES.items():
    setofpatterns_DEPS[repr(patterns)].add(f"{kind_name}")

duplicates_unsolved = []

for repr_patterns, deps in setofpatterns_DEPS.items():
    if len(deps) > 1:
        for onedep in deps:
            if onedep in DUPLICATES_TO_REMOVE:
                del RULES[onedep]

            elif not onedep in PREFERRED_RULES:
                duplicates_unsolved.append(deps)


if duplicates_unsolved:
    duplicates_unsolved = '\n'.join(
        '# ' + ' | '.join(sorted(s))
        for s in duplicates_unsolved
    )

    print(f"""
-------------------------
DUPLICATE DEPS TO RESOLVE
-------------------------

{duplicates_unsolved}
    """)

    exit()


# ---------------------------- #
# -- PRE-HIERARCHICAL RULES -- #
# ---------------------------- #

print(
    f"{TAB_1}* Construction of pre-hierarchical rules."
)

pattern_DEPS = defaultdict(list)

for kind_name, patterns in RULES.items():
    for onerule in patterns:
        pattern_DEPS[onerule].append(kind_name)


# ! -- DEBUGGING -- ! #
# nb_debug = 0

# for onerule, deps in pattern_DEPS.items():
#     if len(deps) > 1:
#         print()
#         print(f"{onerule = }")
#         print(f"{deps    = }")

#         nb_debug += 1

#         if nb_debug % 4 == 0:
#             exit()
# ! -- DEBUGGING -- ! #


several_deps = {}

for onerule, deps in pattern_DEPS.items():
# A pattern used at several places!
    if len(deps) > 1:
        for kind_name in deps:
            RULES[kind_name].remove(onerule)

        several_deps[onerule] = deps


# ! -- DEBUGGING -- ! #
# print()

# print(f"{several_deps['!.vscode/launch.json'] = }")
# print(f"{RULES['online/VISUALSTUDIO'] = }")
# print(f"{RULES['online/VISUALSTUDIOCODE'] = }")

# # p = '*.[oa]'
# # deps = ['online/1C-BITRIX', 'online/FREEPASCAL']
# # p = '*.csv'
# # deps = ['online/1C-BITRIX', 'online/DATA', 'online/KICAD', 'online/STRAPI']
# # p = '*.db'
# # deps = ['online/1C-BITRIX', 'online/DATABASE', 'online/FINALE']

# print(f"{RULES['online/1C-BITRIX'] = }")
# exit()
# ! -- DEBUGGING -- ! #


# -- EMPTIED RULES -- #

emptied_rules = []

for kind_name, patterns in RULES.items():
    if not patterns:
        emptied_rules.append(kind_name)

for kind_name in emptied_rules:
    del RULES[kind_name]

if emptied_rules:
    nb_emptied_rules = len(emptied_rules)
    plurial          = "" if nb_emptied_rules == 1 else "s"

    print(
        f"{TAB_2}+ {nb_emptied_rules} set{plurial} of rules emptied."
    )


# -- AUTO RULES -- #

if RULES:
    nb_auto_rules = len(RULES)
    plurial       = "" if nb_auto_rules == 1 else "s"

    print(
        f"{TAB_2}+ Prebuild of the {nb_auto_rules} "
        f"auto minimized rule{plurial}."
    )


    for kind_name, rules in RULES.items():
        if keep_thisrules(kind_name):
            NB_RULES_ADDED += 1

            writerules(
                dirpath   = MINIMIZE_AUTO_DIR,
                kind_name = kind_name,
                rules     = rules
            )


# -- "BY HAND" RULES -- #

if several_deps:
    print(
        f"{TAB_2}+ Prebuild of rules to ''manage by hand''."
    )


# ! -- DEBUGGING -- ! #
    # deps_printed = []

    # for onerule, deps in several_deps.items():
    #     if not deps in deps_printed:
    #         deps_printed.append(deps)
    #         print(deps)

    # exit()
# ! -- DEBUGGING -- ! #


    cardinalities = defaultdict(int)

    for onerule, deps in several_deps.items():
        for onedep in deps:
            cardinalities[onedep] += 1


    autonames_unresolved = []
    byhand_rules         = defaultdict(list)
    byhand_rules_used_by = defaultdict(list)

    for onerule, deps in several_deps.items():
        maxcard = max(
            cardinalities[onedep]
            for onedep in deps
        )

        autonames = list(
            onedep
            for onedep in deps
            if cardinalities[onedep] == maxcard
        )


        if len(autonames) == 1:
            name = autonames[0]

        else:
            autonames.sort()

            repr_autonames = repr(autonames)

            if repr_autonames in PREFERRED_BY_HAND_NAMES:
                name = PREFERRED_BY_HAND_NAMES[repr_autonames]

            else:
                print(f"""
------------------------------
AUTO-NAMES "BY HAND" TO CHOOSE
------------------------------

# {' | '.join(autonames)}
    "{autonames}": '',
                """)

                exit()


        byhand_rules[name].append(onerule)
        byhand_rules_used_by[name].extend(deps)


    for kind_name, rules in byhand_rules.items():
        used_by = set(byhand_rules_used_by[kind_name])
        used_by = list(used_by)
        used_by.sort()
        used_by = "\n#     + ".join(used_by)
        used_by = f"""
###
# Rules used by the following sets of rules.
#
#     + {used_by}
#
###
        """.strip()


        if keep_thisrules(kind_name):
            NB_RULES_ADDED += 1

            writerules(
                dirpath   = MINIMIZE_BY_HAND_DIR,
                kind_name = kind_name,
                rules     = rules,
                header    = used_by,
            )


# -- WHAT WE HAVE DONE... -- #

if NB_RULES_ADDED == 0:
    print(
        f"{TAB_1}* No set of rules created."
    )

else:
    plurial = "" if NB_RULES_ADDED == 1 else "s"

    print(
        f"{TAB_1}* {NB_RULES_ADDED} set{plurial} of rules managed."
    )


# -------------------------- #
# -- PREPARING FINAL JOBS -- #
# -------------------------- #

if NB_RULES_ADDED:
    for kind_name in RULES:
        if not keep_thisrules(kind_name):
            continue

        _, name = extract_kindname(kind_name)

        finaljob_dir = FINAL_DIR / name

        if not finaljob_dir.is_dir():
            print(
                f"{TAB_2}+ ''final/{name}''"
                 "\n"
                f"{TAB_4}--> Folder added"
            )

            finaljob_dir.create('dir')

        finaljob_main = finaljob_dir / MAIN_FILE

        if not finaljob_main.is_file():
            print(
                f"{TAB_2}+ ''final/{name}/{MAIN_FILE}''"
                 "\n"
                f"{TAB_4}--> File added"
            )

            finaljob_main.write_text(
                encoding = 'utf-8',
                data     = """
###
# this::
#     author = First Name, NAME [your@email.org]
#     desc   = Describe a little the rules.
#
#
# info::
#     This rules have been made after analyzing the similar ones given
#     by the project ¨gitignoreio.
###
                """.strip() + '\n'
            )

        finaljob_ignore = finaljob_dir / "0-ignore-0.txt"

        if not finaljob_ignore.is_file():
            print(
                f"{TAB_2}+ ''final/{name}/0-ignore-0.txt''"
                 "\n"
                f"{TAB_4}--> File added"
            )

            finaljob_ignore.write_text(
                encoding = 'utf-8',
                data     = '# List of rules to ignore for comparisons'
            )
