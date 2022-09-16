#!/usr/bin/env python3

from .scrapingbase import *


# ---------------------------- #
# -- CREATIVE COMMONS CLASS -- #
# ---------------------------- #

class CreativeCommons(ScrapingBase):
    def find_href_elts_proposed(self):
# We only take care of the 4.0 versions.
#
# Names and IDs.
        bs = self.get_BS_of(
            "https://creativecommons.org/2014/01/07/"
            "plaintext-versions-of-creative-commons-4-0-licenses/"
        )

        hrefs = []

        for elt in bs.select('a'):
            if not elt['href'].endswith('/4.0/legalcode.txt'):
                continue

            hrefs.append(elt)

        return hrefs


    def select_one_license(self, href_elt):
        a_href = href_elt['href']

        shortid = href_elt.getText()
        shortid = shortid.strip()

        for old, new in [
            ('(plaintext)', ''),
            (' ', '-'),
        ]:
            shortid = shortid.replace(old, new)

            if not new:
                shortid = shortid.strip()

        print(
            f"{self.decotab_2} Extracting content of "
            f"``Creative Commons {shortid}``"
        )


# ! -- DEBUGGING -- ! #
        # print()
        # print(f"{a_href   = }")
        # print(f"{fullname = }")
        # print(f"{shortid  = }")
        # input('?')
        # exit()
# ! -- DEBUGGING -- ! #

# Easy access to the TXT version of the license.
        content = self.get_webtxt(a_href)

# Full name is inside the content of the license.
        nb_equals_line = 0

        for line in content.split('\n'):
            line = line.strip()

            if not line:
                continue

            if set(line) == set('='):
                nb_equals_line += 1

            elif nb_equals_line == 2:
                fullname = line
                break

# Just add this new license.
        self.add_licence(
            fullname = fullname,
            shortid  = shortid,
            url      = a_href,
            content  = content
        )
