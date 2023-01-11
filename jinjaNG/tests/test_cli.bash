THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JINJANG_DIR="$(cd "$THIS_DIR/.." && pwd)"
DATA_DIR="$THIS_DIR/01-usecases/data"


function error_exit() {
    localdir=$(dirname "$DATA_DIR/$2")

    printf "\033[91m\033[1m"
    echo ""
    echo "  ERROR - $1 , see the folder:"
    echo "  + $localdir"
    exit 1
}


cd "$DATA_DIR"

# WARNING!
#
# We can't use pipes first like below because this will launch
# subprocesses, and this will make the ``exit 1`` of ``error_exit``
# inefficient.
#
#     find . -name 'data.*'  -type f | sort | while read -r datafile
#     do
#         ...
#     done

while read -r datafile  # <(find . -name 'data.*'  -type f | sort)
do
    localdir=$(dirname "$datafile")

    echo "* Testing ''$localdir''."

    filename=$(basename "$datafile")
    ext=${filename##*.}

    if [ "$ext" == "py" ]
    then
        unsafe="-u"
    else
        unsafe=""
    fi

    data="$DATA_DIR/$datafile"

    while read -r templatefile  # <(find . -name 'template.*' -type f | sort)
    do
        filename=$(basename "$templatefile")
        ext=${filename##*.}

        template="$DATA_DIR/$templatefile"
        output="$DATA_DIR/$localdir/output.$ext"
        outputfound="$DATA_DIR/$localdir/output_found.$ext"

        cd "$JINJANG_DIR"

        # -- COMMAND TESTED -- #
        python3.9 -m src $unsafe "$data" "$template" "$outputfound" > /dev/null || error_exit "BUILDING" "$templatefile"

        # -- OUTPUT TESTED -- #
        if cmp -s "$output" "$outputfound"; then
            ok=0
        else
            error_exit "CONTENTS" "$templatefile"
        fi

        # -- REMOVE THE OUPUT -- #
        rm "$outputfound"
    done < <(find $localdir -name 'template.*' -type f | sort)

    cd "$DATA_DIR"
done < <(find . -name 'data.*'  -type f | sort)


printf "\033[92m\033[1m"

echo ""
echo "SUCCESS!"
