#!/usr/bin/env python3

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

            a_href = a['href']

            if not '/licenses/' in a_href:
                continue

            if a_href.startswith('/licenses/'):
                a_href = f'https://opensource.org{a_href}'

            if a_href in hrefs_visited:
                continue

            a_txt = a.getText().lower()

            if (
                not 'license' in a_txt
                or
                any(
                    s in a_txt
                    for s in self.TO_IGNORE
                )
            ):
                continue

# Access to the TXT version makes us work more than
# with Creative Commmons... Why such a violence?
            lic_bs = self.get_BS_of(a_href)

# Not recommanded.
            not_recommanded = False

            for font in lic_bs.select('font'):
                if(
                    'color' in font.attrs
                    and
                    font['color'] == 'red'
                ):
                    not_recommanded = True
                    break

            if not_recommanded:
                continue

# Short ID.
            shortid = a_href.split('/')[-1]

            if shortid in self.SHORT_IDS_UNKEPT:
                continue

# Full name.
            for h1 in lic_bs.select('h1'):
                if 'class' in h1.attrs:
                    name, _, _ = h1.text.partition('(')

                    name = name.strip()

                    break


            assert name, \
                   f"no name found at {a_href}."

# Everything looks OK.
            hrefs_visited.add(a_href)
# ! -- DEBUGGING -- ! #
            print()
            print(f"{a_href  = }")
            print(f"{name    = }")
            print(f"{shortid = }")
            # input('?')
            # exit()
# ! -- DEBUGGING -- ! #


            # self.add_licence(
            #     license_name = license_name,
            #     file_name    = file_name,
            #     content      = content
            # )
