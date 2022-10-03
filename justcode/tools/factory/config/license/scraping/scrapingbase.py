#!/usr/bin/env python3

from typing import (
    Dict,
    List,
    Tuple,
)

from concurrent.futures  import ThreadPoolExecutor
from json                import dumps
from requests            import (
    ConnectionError,
    get as getwebcontent
)

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

        self.nb_failures = 0
        self.nb_success  = 0


    def build(self) -> None:
        self.licences        = set()
        self.failed_licences = set()

        print(f"{self.decotab_1} Extracting infos about licenses.")
        self.extract_licences()

        self.nb_failures = len(self.failed_licences)
        self.nb_success  = len(self.licences)

        if self.nb_failures:
            percent_failures  = self.nb_failures / (self.nb_failures + self.nb_success)
            percent_failures *= 100

            print(f"{self.decotab_1} Failures: {percent_failures:.2f}%.")

        else:
            print(f"{self.decotab_1} No failure.")

        print(f"{self.decotab_1} Updating license files.")

        self.update_licences()

        print(f"{self.decotab_1} {self.nb_success} licenses found with success.")


    def extract_licences(self) -> Dict[str, str]:
# hrefs of licenses proposed. Fast to do.
        print(
            f"{self.decotab_2} Looking for refs proposed."
        )

        href_elts = self.find_href_elts_proposed()

        print(
            f"{self.decotab_2} {len(href_elts)} refs proposed."
        )

# Licenses kept for our project. Slow, but we use multiprocessing.
        with ThreadPoolExecutor(max_workers = 5) as exe:
            exe.map(self.select_one_license, href_elts)


    def find_href_elts_proposed(self):
        raise NotImplementedError(
            'code the build of the list of HTML href elements for the licenses'
        )


    def select_one_license(self, href_elt):
        raise NotImplementedError(
            'code the selection of one license indicated by an HTML href element'
        )


    def get_BS_of(self, url: str) -> BeautifulSoup:
        return BeautifulSoup(
            self.get_webtxt(url),
            "html.parser"
        )


    def get_webtxt(self, url: str) -> BeautifulSoup:
        return getwebcontent(url).text


    def filenamefrom(self, shortid: str) -> str:
        for old in ' _.':
            shortid = shortid.replace(old, self.STD_SEP)

        shortid = shortid.upper()

        return shortid


    def add_licence(
        self,
        fullname: str,
        shortid : str,
        url     : str,
        content : str,
    ) -> None:
        self.licences.add(
            (fullname, shortid, url, content)
        )


    def add_failed_licence(
        self,
        fullname: str,
        shortid : str,
    ) -> None:
        self.failed_licences.add(
            (shortid, fullname)
        )


    def update_licences(self) -> None:
        for fullname, shortid, url, content in self.licences:
            file_name = self.filenamefrom(shortid)

# ! -- DEBUGGING -- ! #
            # print(file_name)
            # continue
# ! -- DEBUGGING -- ! #

            lic_file_TXT  = self.license_dir / f"{file_name}.txt"
            lic_file_JSON = self.license_dir / f"{file_name}.json"

# License in the project.
            if lic_file_TXT.is_file():
                content_stored = lic_file_TXT.read_text(
                    encoding = 'utf-8'
                )

            else:
                content_stored = ''

# New license?
            if content_stored == content:
                print(
                    f"{self.decotab_2} No new content "
                    f"for the license ``{shortid}``."
                )
                continue


            print(
                f"{self.decotab_2} Updating the file "
                f"``{file_name}.txt``."
            )

            lic_file_TXT.write_text(
                encoding = 'utf-8',
                data     = content
            )


            print(
                f"{self.decotab_2} Updating the file "
                f"``{file_name}.json``."
            )

            lic_file_JSON.write_text(
                encoding = 'utf-8',
                data     = dumps(
                    {
                        'fullname': fullname,
                        'shortid' : shortid,
                        'urls'    : {
                            'official': None,
                            'content' : url,
                        }
                    },
                    indent = 4
                )
            )
