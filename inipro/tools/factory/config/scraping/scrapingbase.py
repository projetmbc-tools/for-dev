#!/usr/bin/env python3

from typing import (
    Dict,
    List,
    Tuple,
)

from requests import get as getwebcontent

from bs4 import BeautifulSoup

from mistool.os_use import PPath as Path


# -------------------------------------- #
# -- BASE CLASS FOR SCRAPING LICENSES -- #
# -------------------------------------- #

class ScrapingBase:
    STD_SEP = '-'

    def __init__(
        self,
        decotab_1  : str,
        decotab_2  : str,
        license_dir: Path,
    ) -> None:
        self.decotab_1   = decotab_1
        self.decotab_2   = decotab_2
        self.license_dir = license_dir


    def build(self) -> None:
        self._licences = []

        print(f"{self.decotab_1} Extracting infos about licenses.")
        self.extract_licences()

        print(f"{self.decotab_1} Updating license files.")
        self.update_licences()


    def extract_licences(self) -> Dict[str, str]:
        raise NotImplementedError(
            'specific extraction must be implemented.'
        )


    def get_BS_of(self, url: str) -> BeautifulSoup:
        return BeautifulSoup(
            self.get_webtxt(url),
            "html.parser"
        )


    def get_webtxt(self, url: str) -> BeautifulSoup:
        return getwebcontent(url).text


    def idof(self, name: str) -> str:
        for old in ' _.':
            name = name.replace(old, self.STD_SEP)

        return name


    def add_licence(
        self,
        license_name: str,
        file_name   : str,
        content     : str,
    ) -> None:
        self._licences.append(
            (license_name, file_name, content.strip())
        )


    def update_licences(self) -> None:
        for license_name, file_name, content in self._licences:
            lic_file      = self.license_dir / f"{file_name}.txt"
            lic_name_file = self.license_dir / f"{file_name}-[name].txt"

# License in the project.
            if lic_file.is_file():
                with lic_file.open(
                    encoding = 'utf-8',
                    mode     = 'r',
                ) as f:
                    content_stored = f.read()
                    content_stored = content_stored.strip()

            else:
                content_stored = ''

# New license?
            if content_stored == content:
                print(
                    f"{self.decotab_2 } No new content "
                    f"for the license ``{license_name}``."
                )
                continue

            print(
                f"{self.decotab_2 } Updating the file "
                f"``{file_name}.txt``."
            )

            with lic_file.open(
                encoding = 'utf-8',
                mode     = 'w',
            ) as f:
                f.write(content)


            with lic_name_file.open(
                encoding = 'utf-8',
                mode     = 'w',
            ) as f:
                license_name = license_name.upper()
                license_name = license_name.replace('-', ' ')

                f.write(license_name)
