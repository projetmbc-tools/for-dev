from jinjang import *

# Les données.
word       = "TEST"
ascii_code = [
    f"{ord(c):0>3}"
    for c in word
]

DATA = {
    "word"      : word,
    "ascii_code": ascii_code
}

# Les chemines des fichiers "patron" et produit.
TEMPLATE_FILE = Path("template.txt")
OUTPUT_FILE   = Path("output_found.txt")

# Fabrication du contenu.
mybuilder = JNGBuilder(
    flavour = FLAVOUR_ASCII
)

mybuilder.render(
    data     = DATA,
    template = TEMPLATE_FILE,
    output   = OUTPUT_FILE
)
