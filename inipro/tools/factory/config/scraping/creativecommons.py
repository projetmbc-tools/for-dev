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
            "https://creativecommons.org/2014/01/07/"
            "plaintext-versions-of-creative-commons-4-0-licenses/"
        )

        for elt in bs.select('a'):
            href = elt['href']

            if not href.endswith('/4.0/legalcode.txt'):
                continue

            license_name = elt.getText()
            license_name = license_name.replace('(plaintext)', '')
            license_name = license_name.strip()

            file_name =self.idof(license_name)

# Easy access to the TXT version of the license.
            content = self.get_webtxt(href)

            self.add_licence(
                fullname = license_name,
                shortid    = file_name,
                content      = content
            )
