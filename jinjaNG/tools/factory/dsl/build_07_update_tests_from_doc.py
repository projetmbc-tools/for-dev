#!/usr/bin/env python3

from btools.B01 import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
# print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'jinjaNG'):
   PROJECT_DIR = PROJECT_DIR.parent


DOC_CONTENT_DIR = PROJECT_DIR / 'doc' / 'content'
TO_TEST_YAML    = PROJECT_DIR / 'tests' / 'outputs' / 'docexa.yaml'


addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src import JNGData


EXT_DATA = []

for methattr in dir(JNGData):
    if methattr.startswith('build_from'):
        EXT_DATA.append('.' + methattr.replace('build_from', ''))


# ------------------- #
# -- EXTRACT TESTS -- #
# ------------------- #

def testsfrom(pdir, testfiles):
    for pfile in pdir.glob('**/cfg.jng.yaml'):
        print(
            f"{TAB_3}> Examples using configs are ignored for the moment."
        )

        return None


    for kind in [
        'data',
        'template',
    ]:
        for pfile in pdir.glob(f'**/{kind}.*'):
            if (
                kind == 'data'
                and
                not pfile.suffix in EXT_DATA
            ):
                continue

            testfiles[kind][pfile.parent].append(pfile.name)


def tests2yaml(testfiles):
    testskept = {
        'docdir': str(DOC_CONTENT_DIR),
        'totest': []
    }

    for pdir, datafiles in testfiles['data'].items():
        if not pdir in testfiles['template']:
            raise Exception(
                    "missing template file! See:"
                    '\n'
                f'{pdir}'
            )

        for dfile in datafiles:
            for tfile in testfiles['template'][pdir]:
                testskept['totest'].append([
                    str(pdir - DOC_CONTENT_DIR),
                    dfile,
                    tfile,
                ])


    return testskept


# ---------------------- #
# -- EXAMPLES TO TEST -- #
# ---------------------- #

print(f"{TAB_1}* Doc content - Looking for examples to test.")


testfiles = defaultdict(lambda: defaultdict(list))

for pdir in DOC_CONTENT_DIR.glob('**/examples/*'):
    if not pdir.is_dir():
        continue

    print(f"{TAB_2}+ {pdir - DOC_CONTENT_DIR}")

    testsfrom(pdir, testfiles)


with TO_TEST_YAML.open(
    mode     = "w",
    encoding = "utf-8"
) as f:
    yaml_dump(
        data   = tests2yaml(testfiles),
        stream = f,
        Dumper = IndentDumper
    )
