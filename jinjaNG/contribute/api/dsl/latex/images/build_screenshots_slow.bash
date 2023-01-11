# --------------- #
# -- CONSTANTS -- #
# --------------- #

UP_THIS_DIR="$(cd "$(dirname "$0")"/../ && pwd)"

cd "$UP_THIS_DIR"


# --------- #
# -- PDF -- #
# --------- #

cp "jngutils.sty" "images/jngutils.sty"

cd images

latexmk -pdf "exavar.tex"


# ----------------- #
# -- PDF --> PNG -- #
# ----------------- #

convert -density 800 "exavar.pdf" -alpha off -resize 14% "exavar.png"


# ------------------------------ #
# -- MINIMIZE OUR FINGERPRINT -- #
# ------------------------------ #

latexmk -C "exavar.tex"

rm "jngutils.sty"
