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


pdf2imag() {
    convert -density 800 "$1" -alpha off -resize 14% "$2"
}


# ----------------- #
# -- PDF --> PNG -- #
# ----------------- #

PDF_FILE="exavar.pdf"

IMG_KEPT="exavar.png"
IMG_CANDIDATE="exavar_candidate.png"
IMG_DIFF="exavar_diff.png"

if [ -f "exavar.png" ]
then
    pdf2imag $PDF_FILE $IMG_CANDIDATE

# Sources.
#     * https://imagemagick.org/script/compare.php
#     * https://stackoverflow.com/a/38561570/4589608
    metric=$(magick compare -metric PSNR $IMG_KEPT $IMG_CANDIDATE /dev/null 2>&1)

    if [[ "$metric" != "0 (0)" ]]
    then
        cp $IMG_CANDIDATE $IMG_KEPT
    fi

else
    pdf2imag $PDF_FILE $IMG_KEPT
fi

# ------------------------------ #
# -- MINIMIZE OUR FINGERPRINT -- #
# ------------------------------ #

latexmk -C "exavar.tex"

rm $IMG_CANDIDATE "jngutils.sty"
