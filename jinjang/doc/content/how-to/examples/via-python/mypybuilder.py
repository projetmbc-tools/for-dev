from jinjang import JNGBuilder, FLAVOUR_ASCII

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
TMPL_FILE   = "tmpl-test-in.txt"
OUTPUT_FILE = "output.txt"

# Fabrication du contenu.
mybuilder = JNGBuilder(
    flavour  = FLAVOUR_ASCII,
    template = TMPL_FILE,
)

mybuilder.build(
    datas  = MY_DATAS,
    output = OUTPUT_FILE
)
