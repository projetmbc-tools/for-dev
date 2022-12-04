#!/usr/bin/env python3

from PIL import Image, ImageChops

from playwright.sync_api import sync_playwright

from mistool.os_use import PPath as Path


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent


HTML_FILE = THIS_DIR / 'exavar.html'
PNG_FILE  = THIS_DIR / 'exavar.png'

# ------------------------ #
# -- LET'S DO ONE PHOTO -- #
# ------------------------ #

with sync_playwright() as p:
    browser = p.firefox.launch()

    page = browser.new_page()
    page.goto(f"file://{HTML_FILE}")
    page.locator('p') \
        .screenshot(path = PNG_FILE)
    browser.close()


# -------------------- #
# -- TRIM OUR IMAGE -- #
# -------------------- #

im = Image.open(PNG_FILE)

background = im.getpixel((0, 0))

leftmost = im.size[0] - 1
height   = im.size[1]

while True:
    onlybg = True

    for r in range(0, height):
        if im.getpixel((leftmost, r)) != background:
            onlybg = False
            break

    if not onlybg:
        break

    leftmost -= 1

(left, upper, right, lower) = (0, 0, leftmost, height - 1)
im = im.crop((left, upper, right, lower))

im.save(PNG_FILE)
