#!/usr/bin/env python3

from json import load, dumps
import           re

from mistool.os_use import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'justcode'):
   PROJECT_DIR = PROJECT_DIR.parent


THIS_FILE_REL_PROJECT_DIR = THIS_FILE - PROJECT_DIR

LICENSE_DIR       = PROJECT_DIR / 'src' / 'config' / 'license'
LICENSE_DATAS_DIR = LICENSE_DIR / 'datas'


URL_CC = "https://creativecommons.org"


TAB_1 = ' '*4
TAB_2 = TAB_1*2
TAB_3 = TAB_1*3


# ----------- #
# -- TOOLS -- #
# ----------- #

URL_TO_IGNORE = [
    'https://fsf.org/',
    'http://www.apache.org/licenses/LICENSE-2.0',
]

PATTERN_URL = re.compile(
    "https?://\S*"
)


def cleanurl(url):
    while url[-1] in ')>.':
        url = url[:-1]

    return url


def baseurl(urls):
    urls = list(urls)
    urls.sort()

    minimalurl = urls.pop(0)

    if not minimalurl[-1] == "/":
        minimalurl += "/"

    for url in urls:
        assert url.startswith(minimalurl), \
               f"{minimalurl = } not in {url = } ."

    return minimalurl[:-1]


def extracturl(content):
    urls = set(
        cleanurl(u)
        for u in re.findall(PATTERN_URL, content)
    )

    urls = set(
        u
        for u in urls
        if not u in URL_TO_IGNORE
    )

    if urls:
        return baseurl(urls)

    return None


# --------------- #
# -- LET'S GO! -- #
# --------------- #

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ----------------------- #
# -- UPDATE JSON FILES -- #
# ----------------------- #

print(f"{TAB_1}* Trying to add official urls to the JSON files.")

nb_official_OK = 0
nb_official_KO = 0

for p in LICENSE_DATAS_DIR.walk("file::**.json"):
    with p.open(
        encoding = "utf-8",
        mode     = "r"
    ) as f:
        infos = load(f)

    if not infos['urls']['official'] is None:
        nb_official_OK += 1
        continue


    if infos['fullname'].startswith("Creative Commons"):
        urlfound = URL_CC

    else:
        with p.with_ext('txt').open(
            encoding = "utf-8",
            mode     = "r"
        ) as f:
            content = f.read()

        urlfound = extracturl(content)


    if urlfound is None:
        nb_official_KO += 1
        continue


    print(f"{TAB_2}+ Official url found for the license ''{p.stem}''.")

    nb_official_OK += 1

    infos['urls']['official'] = urlfound


    with p.open(
        encoding = 'utf-8',
        mode     = 'w',
    ) as f:
        f.write(
            dumps(infos)
        )


if nb_official_OK == 0:
    print(f"{TAB_1}* No change made.")

else:
    print(
        f"{TAB_1}* {nb_official_OK}/{nb_official_KO} official "
         "urls added."
        )
