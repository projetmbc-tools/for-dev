#!/usr/bin/env python3

from typing import (
    Set,
    Union,
)

from .scrapingbase import *


# ----------------------- #
# -- OPEN SOURCE CLASS -- #
# ----------------------- #

class OpenSource(ScrapingBase):
    TO_IGNORE = [
        'licenses by',
        'creative commons',
    ]

    SHORT_IDS_UNKEPT = [
        'Artistic-1.0',
        'BSD-1-Clause',
        'BSD-2-Clause',
        'ECL-1.0',
        'EPL-1.0',
        'EFL-1.0',
        'GPL-2.0',
        'LGPL-2.1',
        'LPL-1.0',
        'MPL-1.0',
        'OSL-1.0',
        'OSL-2.1',
        'PHP-3.0',
        'Python-2.0',
        'RPL-1.1',
        'ZPL-2.0',
    ]


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__xtraspaces = " "*(
            len(f"{self.decotab_2} Extracting content of ")
        )


    def find_hrefs_proposed(self):
        bs = self.get_BS_of(
            "https://opensource.org/licenses/alphabetical"
        )

        hrefs = []

        for elt in bs.select('a'):
            if not 'href' in elt.attrs:
                continue

            if self._href_to_keep(
                a_txt  = elt.getText().lower(),
                a_href = elt['href'],
                hrefs  = hrefs
            ):
                hrefs.append(elt)

        return hrefs


    def select_licenses(self, elt):
        a_href = a_href = self._normalize_href(elt['href'])

# Access to the TXT version makes us work more than
# with Creative Commmons... Why such a violence?
        lic_bs = self.get_BS_of(a_href)

# License no more recommanded.
        if not self._license_recommanded(lic_bs):
            return

# Short ID.
        shortid = a_href.split('/')[-1]

        if shortid in self.SHORT_IDS_UNKEPT:
            return

# Full name.
        fullname = self._build_fullname(lic_bs)

        assert fullname, \
               f"no name found at {a_href}."

# Everything seems OK.

# ! -- DEBUGGING -- ! #
        # print()
        # print(f"{a_href   = }")
        # print(f"{fullname = }")
        # print(f"{shortid  = }")
        # input('?')
        # exit()
# ! -- DEBUGGING -- ! #

# We have to find the TXT version of the licences!
        content_url = self._find_content(
            fullname = fullname,
            shortid  = shortid,
            a_href   = a_href,
            lic_bs   = lic_bs
        )

        if content_url is None:
            self.add_failed_licence(
                fullname = fullname,
                shortid  = shortid,
            )
            return

        content, url = content_url

# Just add this new license.
        self.add_licence(
            fullname = fullname,
            shortid  = shortid,
            url      = url,
            content  = content
        )


    def _build_fullname(self, lic_bs: BeautifulSoup) -> str:
        fullname = ''

        for h1 in lic_bs.select('h1'):
            if 'class' in h1.attrs:
                fullname, _ , _ = h1.text.partition('(')

                fullname = fullname.strip()

                break

        return fullname


    def _normalize_href(self, a_href):
        if a_href.startswith('/licenses/'):
            a_href = f'https://opensource.org{a_href}'

        return a_href


    def _href_to_keep(
        self,
        a_txt         : str,
        a_href        : str,
        hrefs: Set[str]
    ) -> Union[None, str]:
        a_href = self._normalize_href(a_href)

        if (
            a_href in hrefs
            or
            not '/licenses/' in a_href
            or
            not 'license' in a_txt
            or
            any(
                s in a_txt
                for s in self.TO_IGNORE
            )
        ):
            return False

        return True


    def _license_recommanded(self, lic_bs: BeautifulSoup) -> bool:
        for font in lic_bs.select('font'):
            if(
                'color' in font.attrs
                and
                font['color'] == 'red'
            ):
                return False

        return True


    def _find_content(
        self,
        fullname: str,
        shortid : str,
        a_href  : str,
        lic_bs  : BeautifulSoup,
    ) -> Union[None, Tuple[str, str]]:
        about = (
            f"[{shortid}]"
            f"\n{self.__xtraspaces}"
            f"{fullname}"
        )

# We only keep license founded on ``choosealicense.com``.
        url = f"https://choosealicense.com/licenses/{shortid.lower()}"

        response = getwebcontent(url)

        if response.status_code != 200:
            print(
                f"{self.decotab_2} No content online for {about}"

            )

            return None

        print(               # No content online for
            f"{self.decotab_2} Extracting content of {about}"
        )

        bs = self.get_BS_of(url)

        for p in bs.select('pre'):
            if (
                'id' in p.attrs
                and
                p['id'] == "license-text"
            ):
                content = p.getText()

        return content, url
