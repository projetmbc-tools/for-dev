#!/usr/bin/env python3

from typing import Tuple, List

from collections import defaultdict
from yaml        import safe_load as yaml_load

from cbdevtools.addfindsrc import addfindsrc
from mistool.os_use        import PPath as Path


# ------------- #
# -- MESSAGE -- #
# ------------- #

def message(template):
    dirpb = template.parent

    return (
         "\n"
         "In the source dir, see the folder:"
         "\n"
        f"+ {dirpb}"
         "\n"
    )


# ----------- #
# -- OUPUT -- #
# ----------- #

def build_output(
    builder,
    datas,
    template
):
    output_found = template.parent / f"output_found{template.suffix}"

    builder.render(
        datas    = datas,
        template = template,
        output   = output_found
    )

    return output_found


def remove_output_found(subdir, template):
    (subdir / f"output_found{template.suffix}").unlink()


# ------------------------ #
# -- NON-STRICT CONTENT -- #
# ------------------------ #

def minimize_content(path):
    return [
        lstripped
        for l in path.read_text(encoding = 'utf-8').split('\n')
        if (lstripped:= l.rstrip())
    ]


# -------------------- #
# -- STRICT CONTENT -- #
# -------------------- #

# Verbatim equivalences of the contents except for the final empty lines that are striped.

def content(path):
    return path.read_text(encoding = 'utf-8').split('\n')


# -------------------- #
# -- USECASES DATAS -- #
# -------------------- #

def yielddirs(pdir: Path) -> Path:
    if not pdir.is_dir():
        raise Exception(
            f"one dir expected, see:\n{pdir}"
        )

    for subdir in pdir.glob('*'):
        if(
            subdir.is_dir()
            and
            not subdir.name.startswith('.')
            and
            not subdir.name.startswith('x-')
        ):
            yield subdir


def extract_dto(pdir: Path) -> Tuple[Path, Path, Path]:
    dto = {
        n: []
        for n in ['datas', 'template', 'output']
    }

    for pfile in pdir.glob('*'):
        name = pfile.stem

        if name in dto:
            dto[pfile.stem].append(pfile)

    for name, pathsfound in dto.items():
        if len(pathsfound) != 1:
            nbpaths = len(pathsfound)

            howmany = 'no' if nbpaths == 0 else nbpaths
            plural  = ''   if nbpaths == 0 else 's'

            raise Exception(
                f"one file, and only one, can be named ''{name}'': "
                f"{howmany} file{plural} found. Look at the folder:\n{pdir}"
            )

    return tuple(
        p[0]
        for _, p in dto.items()
    )


def build_usecases_datas(
    datas_dir: Path
) -> List[Tuple]:
    usecases_folders = defaultdict(list)

    for pdir in yielddirs(datas_dir):
        flavour = pdir.name

        for ucdir in yielddirs(pdir):
            usecases_folders[flavour].append(ucdir)

# ! -- DEBUGGING -- ! #
    # from pprint import pprint
    # pprint(dict(USECASES_FOLDERS))
# ! -- DEBUGGING -- ! #

    usecases_datas = []

    for flavour, usecases in usecases_folders.items():
        for ucdir in usecases:
            jngdatas, template, output = extract_dto(ucdir)
            test_name                  = ucdir.name

            usecases_datas.append(
                (
                    flavour,
                    test_name,
                    jngdatas,
                    template,
                    output
                )
            )

    return usecases_datas


# -------------------- #
# -- USECASES DATAS -- #
# -------------------- #

def build_docexas_datas(
    docexa_yaml : Path
) -> Tuple[Path, List]:
    with docexa_yaml.open(
        encoding = 'utf-8',
        mode     = 'r'
    ) as f:
        docexa_totest = yaml_load(f)

    doc_content_dir = Path(docexa_totest['docdir'])
    docexa_totest   = docexa_totest['totest']

    return doc_content_dir, docexa_totest
