#!/usr/bin/env python3

from btools.B01 import *


SRC_DIR = addfindsrc(
    file    = __file__,
    project = 'jinjaNG',
)

from src.config.jngflavours import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
# print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = Path(__file__)
THIS_DIR  = Path(THIS_FILE).parent

PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'jinjaNG'):
   PROJECT_DIR = PROJECT_DIR.parent

README_DIR       = PROJECT_DIR / 'readme'
FLAVOURS_MD_FILE = README_DIR / 'flavours.md'


FLAVOURS_PY_CONTENT = (
    SRC_DIR / "src" / "config" / "jngflavours.py"
).read_text(
    encoding = 'utf-8'
)

TEMPL_BEFORE = """
# -- {flname} -- #
# {deco} #
#
""".strip()

AFTER = """
#
# Last change:
""".strip()


TEMPL_ONE_FLAVOUR = """
---

#### Flavour `{flname}`

> ***Short description:*** *{desc}*

  1. **Extension{exts_plurals} for the auto-detection.**
      * {exts}

  1. **Tools to assist in typing templates.**
      * {tools}

  1. **Variables, `jinja` instructions and comments.**
  Here is a fictive `how-to` code.

~~~{md_code}
In our templates, we use {variable_start_string}variable{variable_end_string} .

It is always possible to work with block jinja instructions, and comments.

{comment_start_string} Comments: one basic loop. {comment_end_string}

{block_start_string} for i in range(5) {block_end_string}
We can use {variable_start_string}i + 4{variable_end_string} .
{block_start_string} endfor {block_end_string}

{inline}
~~~
""".strip()


TEMPL_INLINE_FLAVOUR = """

Most of flavours propose inline jinja instructions, and comments.

{line_comment_prefix} Comments: the same loop as above.

{line_statement_prefix} for i in range(5)
We can use {variable_start_string}i + 4{variable_end_string} .
{line_statement_prefix} endfor
""".strip()


# ----------------- #
# -- THE CONTENT -- #
# ----------------- #

print(f'{TAB_1}* README - "flavours.md" - Building the content.')

content = []

for flname, specs in JINJA_TAGS.items():
    print(f'{TAB_2}+ Flavour "{flname}" found.')

# Description.
    _, desc, _ = between(
        text = FLAVOURS_PY_CONTENT,
        seps = [
            TEMPL_BEFORE.format(
                flname = flname.upper(),
                deco   = '-'*(2*3 + len(flname))
            ),
            AFTER
        ]
    )

    desc = desc.strip()
    desc = desc[1:].strip()
    desc = desc[0].lower() + desc[1:]

# Extensions.
    exts = AUTO_FROM_EXT[flname]

    if exts == ['*']:
        md_code = "markdown"

        exts_plurals = True
        exts         = (
            "Any extension not associated with another flavour is "
            "associated with that flavour (which is like a default one)."
        )

    else:
        md_code = exts[0][2:]

# HTML bug in listing!
        if md_code == "html":
            md_code = "markdown"

        exts_plurals = (len(exts) != 1)
        exts         = "\n      * ".join(
            f"`{e[2:].upper()}`" for e in sorted(exts)
        )

# Tools.
    tools = (
        f"See the folder `jng-extra-tools/{flname}`."
        if WITH_EXTRA_TOOLS[flname] else
        "Nothing available."
    )

# Inline?
    if specs[TAG_INLINE_INSTR] is None:
        inline = (
            "This flavour doesn't propose inline jinja "
            "instructions, and comments."
        )

    else:
        inline = TEMPL_INLINE_FLAVOUR.format(**specs)

# New piece of content.
    exts_plurals = 's' if exts_plurals else ''

    content.append(
        TEMPL_ONE_FLAVOUR.format(
            flname       = flname,
            desc         = desc,
            exts_plurals = exts_plurals,
            exts         = exts,
            tools        = tools,
            md_code      = md_code,
            inline       = inline,
            **specs
        )
    )

content = '\n\n'.join(content)


# ---------------------------- #
# -- UPDATING "flavours.md" -- #
# ---------------------------- #

print(f'{TAB_1}* README - "flavours.md" - Updating the content.')

before, _ , after = between(
    text = FLAVOURS_MD_FILE.read_text(encoding = 'utf-8'),
    seps = [
        '<!-- FLAVOURS - TECH. DESC. - START -->',
        '<!-- FLAVOURS - TECH. DESC. - END -->'
    ],
    keepseps = True,
)

FLAVOURS_MD_FILE.write_text(
    data     = f"{before}\n\n{content}\n\n{after}",
    encoding = 'utf-8'
)
