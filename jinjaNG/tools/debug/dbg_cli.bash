KIND="json"
KIND="py"
#KIND="yaml"

NB="01"

UNSAFE="-u"
#UNSAFE="--unsafe"
#UNSAFE=""

error_exit() {
    echo ""
    echo "ERROR - Following command opens the file that has raised an error."
    echo ""
    echo "  > open ./files/$1"
    exit 1
}

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JINJANG_DIR="$(cd "$THIS_DIR/../.." && pwd)"

TESTED_FOLDER="$THIS_DIR/files/$KIND-$NB"
DATA="$TESTED_FOLDER/datas.$KIND"
TEMPLATE="$TESTED_FOLDER/template.txt"
OUTPUTFOUND="$TESTED_FOLDER/output_found.txt"

cd "$JINJANG_DIR"

echo "\"$DATA\""
echo "\"$TEMPLATE\""

python -m src $UNSAFE "$DATA" "$TEMPLATE" "$OUTPUTFOUND"  || error_exit "$KIND-$NB"





