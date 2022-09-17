#!/usr/bin/env python3


# que si nouveau !!!"#$

# json à valider la classe

# mode validation via un drapeau !!! sinon on build



from mistool.os_use import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)

PROJECT_DIR = Path(THIS_FILE).parent

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


GITIGNORE_DIR       = PROJECT_DIR / 'src' / 'config' / 'gitignore'
GITIGNORE_DATAS_DIR = GITIGNORE_DIR / 'datas'

CONTRIBUTE_DIR       = PROJECT_DIR / 'contribute' / 'api' / 'gitignore'
CONTRIBUTE_DATAS_DIR = CONTRIBUTE_DIR / 'datas'


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #



# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ------------------------------- #
# -- LOOKING FOR CONTRIBUTIONS -- #
# ------------------------------- #

print(f"{TAB_1}* GITIGNORE rules - Looking for contributions.")

code = []

allpaths = [p for p in CONTRIBUTE_DATAS_DIR.walk("file::**.txt")]
allpaths.sort()

for p in allpaths:
    rules_filename_withext = p.name
    rules_filename         = p.stem

    print(f"{TAB_2}+ Checking ``{rules_filename_withext}``.")

    if (GITIGNORE_DATAS_DIR / rules_filename_withext).is_file():
        print(f"{TAB_3}- The file already exists in the API.")

    rules_filename = p.stem


exit()

license_found   = set()
license_by_kind = defaultdict(list)

for f in LICENSE_DIR.walk("file::**.txt"):
    lic_file_TXT_name = f.stem

    kind = f'__{f.parent.name}__'

    assert not lic_file_TXT_name in license_found, \
           (
            f"name ``{lic_file_TXT_name}`` already used somewhere."
             "\n"
            f"See the folder ``{kind.replace('_', '')}``."
           )

    lic_file_JSON = f.parent / f"{lic_file_TXT_name}.json"

    with lic_file_JSON.open(
        encoding = 'utf8',
        mode     = 'r',
    ) as sf:
        specs = load(sf)

# ! -- DEBUGGING -- ! #
    # print(specs)
    # exit()
# ! -- DEBUGGING -- ! #

    license_found.add(lic_file_TXT_name)

    license_by_kind[kind].append(
        (lic_file_TXT_name, specs)
    )


code_EACH_TAG = []

ALL_LICENSES = []

TAG_ONLINE  = '__online__'
TAG_SPECIAL = '__special__'

ALL_TAGS = [
    TAG_ONLINE,
    TAG_SPECIAL,
]

for kind in ALL_TAGS:
    sortednames = sorted(
        (tagfrom(specs['shortid']), specs)
        for _ , specs in license_by_kind[kind]
    )

    if not sortednames:
        continue

    ALL_LICENSES.append(kind)
    ALL_LICENSES += [t for t, _ in sortednames]

    code_EACH_TAG.append(kind)

    for (tag, specs) in sortednames:
        code_EACH_TAG += [
            f"# {specs['fullname']}",
            f"#     + See: {specs['url']}",
            f"TAG_LICENSE_{tag} = \"{specs['shortid']}\""
        ]

    code_EACH_TAG.append('')


code_ALL_TAGS = f"{ALL_LICENSES = }"

code_ALL_TAGS = black.format_file_contents(
    code_ALL_TAGS,
    fast = False,
    mode = black.FileMode()
)


code_EACH_TAG = '\n'.join(code_EACH_TAG)


for kind in ALL_TAGS:
    ctitle = kind.replace('_', '').title()

    code_EACH_TAG = code_EACH_TAG.replace(
        kind,
        f"# {ctitle}\n#"
    )

    code_ALL_TAGS = code_ALL_TAGS.replace(
        ' '*4 + f'"{kind}",',
        f"# {ctitle}"
    )

for n in ALL_LICENSES:
    code_ALL_TAGS = code_ALL_TAGS.replace(
        f'"{n}"',
        f'TAG_LICENSE_{n.replace("-", "_")}'
    )


with PYFILE.open(
    encoding = 'utf8',
    mode     = 'w',
) as f:
    f.write(
        f"""
#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``{THIS_FILE_REL_PROJECT_DIR}``

# EACH TAG

{code_EACH_TAG}

# ALL THE TAGS

{code_ALL_TAGS}
        """.strip()
        +
        '\n'
    )


nb_licences = myCC.nb_success + myOpenSrc.nb_success

print(f"{TAB_1}* {nb_licences} licenses proposed.")
