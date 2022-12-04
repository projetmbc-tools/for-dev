#!/usr/bin/env python3

from playwright.sync_api import sync_playwright

from mistool.os_use import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent



# ------------------------ #
# -- LET'S DO ONE PHOTO -- #
# ------------------------ #

with sync_playwright() as p:
    browser = p.firefox.launch()

    page = browser.new_page()
    page.goto("file://" + str(THIS_DIR / 'exavar.html'))
    page.locator('p').screenshot(path = str(THIS_DIR / 'exavar.png'))
    browser.close()
