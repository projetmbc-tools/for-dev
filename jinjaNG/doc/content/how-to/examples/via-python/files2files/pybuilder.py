from jinjang import *

# Les données.
DATA_FILE = Path("data.py")

# Les chemines des fichiers "patron" et produit.
TEMPLATE_FILE = Path("template.txt")
OUTPUT_FILE   = Path("output_found.txt")

# Fabrication du contenu.
mybuilder = JNGBuilder(
    flavour = FLAVOUR_ASCII
)

mybuilder.render(
    data      = DATA_FILE,
    template  = TEMPLATE_FILE,
    output    = OUTPUT_FILE,
    launch_py = True
)
