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

    TXT_FILES = {
        '': "",
    }

    def extract_licences(self) -> Dict[str, str]:
# We only take care of the 4.0 versions.
#
# Names and IDs.
        bs = self.get_BS_of(
            "https://opensource.org/licenses/alphabetical"
        )

        hrefs_visited = set()

        for a in bs.select('a'):
            if not 'href' in a.attrs:
                continue

            a_href = self.href_to_keep(
                a_txt         = a.getText().lower(),
                a_href        = a['href'],
                hrefs_visited = hrefs_visited
            )

            if a_href is None:
                continue

# Access to the TXT version makes us work more than
# with Creative Commmons... Why such a violence?
            lic_bs = self.get_BS_of(a_href)

# Not recommanded.
            if not self.license_recommanded(lic_bs):
                continue

# Short ID.
            shortid = a_href.split('/')[-1]

            if shortid in self.SHORT_IDS_UNKEPT:
                continue

# Full name.
            fullname = self.build_fullname(lic_bs)

            assert fullname, \
                   f"no name found at {a_href}."

# Everything looks OK.
            hrefs_visited.add(a_href)

# ! -- DEBUGGING -- ! #
            print()
            print(f"{a_href   = }")
            print(f"{fullname = }")
            print(f"{shortid  = }")
            # input('?')
            # exit()
# ! -- DEBUGGING -- ! #

# We have to fins the TXT version of the licences!

            # self.add_licence(
            #     license_name = license_name,
            #     file_name    = file_name,
            #     content      = content
            # )

    def build_fullname(self, lic_bs: BeautifulSoup) -> str:
        fullname = ''

        for h1 in lic_bs.select('h1'):
            if 'class' in h1.attrs:
                fullname, _ , _ = h1.text.partition('(')

                fullname = fullname.strip()

                break

        return fullname

    def href_to_keep(
        self,
        a_txt        : str,
        a_href       : str,
        hrefs_visited: Set[str]
    ) -> Union[None, str]:
        if a_href.startswith('/licenses/'):
            a_href = f'https://opensource.org{a_href}'

        if (
            a_href in hrefs_visited
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
            return None

        return a_href


    def license_recommanded(self, lic_bs: BeautifulSoup) -> bool:
        for font in lic_bs.select('font'):
            if(
                'color' in font.attrs
                and
                font['color'] == 'red'
            ):
                return False

        return True
