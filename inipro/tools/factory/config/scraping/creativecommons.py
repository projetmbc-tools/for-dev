#!/usr/bin/env python3

from .scrapingbase import *


# ---------------------------- #
# -- CREATIVE COMMONS CLASS -- #
# ---------------------------- #

class CreativeCommons(ScrapingBase):
    def extract_licences(self) -> Dict[str, str]:
# We only take care of the 4.0 versions.
#
# Names and IDs.
        bs = self.get_BS_of(
            "https://creativecommons.org/2014/01/07/plaintext-versions-of-creative-commons-4-0-licenses/"
        )

        for elt in bs.select('a'):
            href = elt['href']

            if not elt['href'].endswith('/4.0/legalcode.txt'):
                continue

            name = elt.getText()
            name = name.replace('(plaintext)', '')
            name = name.strip()

            pyid =self.idof(name)

            content = self.get_webtxt(href)

            self.add_licence(
                license_name    = name,
                file_name    = pyid,
                content = content
            )
