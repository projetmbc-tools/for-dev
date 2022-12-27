from jinjang import *

# Les données.
word       = "TEST"
ascii_code = [
    f"{ord(c):0>3}"
    for c in word
]

DATAS = {
    "word"      : word,
    "ascii_code": ascii_code
}

# Les chemines des fichiers "patron" et produit.
TEMPLATE_STR = """
Le mot "{{ word }}" se code en ASCII :
"{{ ascii_code }}" .
""".strip()


# Fabrication du contenu.
mybuilder = JNGBuilder(
    flavour = FLAVOUR_ASCII
)

output_str = mybuilder.render_fromstr(
    datas    = DATAS,
    template = TEMPLATE_STR
)
