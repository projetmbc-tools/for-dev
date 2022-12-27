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
    page.screenshot(path = PNG_FILE)
    browser.close()


# ------------------ #
# -- TRIM - TOOLS -- #
# ------------------ #

def findposition(im, dir, is_xcoord, background):
    if is_xcoord:
        tofind = im.size[0] - 1
        other  = im.size[1]

    else:
        tofind = im.size[1] - 1
        other  = im.size[0]

    if dir == 1:
        tofind = 0

    while True:
        onlybg = True

        for o in range(0, other):
            if is_xcoord:
                totest = (tofind, o)

            else:
                totest = (o, tofind)

            # print(totest)
            if im.getpixel(totest) != background:
                onlybg = False
                break

        if not onlybg:
            break

        tofind += dir

    return tofind - dir



# -------------------- #
# -- TRIM OUR IMAGE -- #
# -------------------- #

im = Image.open(PNG_FILE)

background = im.getpixel((0, 0))

right = findposition(
    im         = im,
    dir        = -1,
    is_xcoord  = True,
    background = background
)

left = findposition(
    im         = im,
    dir        = 1,
    is_xcoord  = True,
    background = background
)

up = findposition(
    im         = im,
    dir        = 1,
    is_xcoord  = False,
    background = background
)

down = findposition(
    im         = im,
    dir        = -1,
    is_xcoord  = False,
    background = background
)

im = im.crop((left, up, right, down))
im.save(PNG_FILE)
