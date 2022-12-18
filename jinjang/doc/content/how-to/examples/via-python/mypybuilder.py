from jinjang import (
    FLAVOUR_ASCII,
    JNGBuilder,
    Path,
)

# Les données.
word       = "TEST"
ascii_code = [
    f"{ord(c):0>3}"
    for c in word
]

MY_DATAS = {
    "word"      : word,
    "ascii_code": ascii_code
}

# Le fichier "patron", et le produit.
#
# On doit utiliser une classe de type ``Path``
# pour indiquer un chemin.
TMPL_FILE   = Path("tmpl-test-in.txt")
OUTPUT_FILE = Path("output.txt")

# Fabrication du contenu.
mybuilder = JNGBuilder(
    flavour  = FLAVOUR_ASCII,
    template = TMPL_FILE,
)

mybuilder.build(
    datas  = MY_DATAS,
    output = OUTPUT_FILE
)
