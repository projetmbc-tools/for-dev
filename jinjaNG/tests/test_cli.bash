THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JINJANG_DIR="$(cd "$THIS_DIR/.." && pwd)"
DATAS_DIR="$THIS_DIR/usecases/datas"


function error_exit() {
    localdir=$(dirname "$DATAS_DIR/$2")

    printf "\033[91m\033[1m"
    echo ""
    echo "  ERROR - $1 , see the folder:"
    echo "  + $localdir"
    exit 1
}


cd "$DATAS_DIR"

# WARNING!
#
# We can't use pipes first like below because this will launch
# subprocesses, and this will make the ``exit 1`` of ``error_exit``
# inefficient.
#
#     find . -name 'datas.*'  -type f | sort | while read -r datafile
#     do
#         ...
#     done

while read -r datafile  # <(find . -name 'datas.*'  -type f | sort)
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

    data="$DATAS_DIR/$datafile"

    while read -r templatefile  # <(find . -name 'template.*'  -type f | sort)
    do
        filename=$(basename "$templatefile")
        ext=${filename##*.}

        template="$DATAS_DIR/$templatefile"
        output="$DATAS_DIR/$localdir/output.$ext"
        outputfound="$DATAS_DIR/$localdir/output_found.$ext"

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
    done < <(find $localdir -name 'template.*'  -type f | sort)

    cd "$DATAS_DIR"
done < <(find . -name 'datas.*'  -type f | sort)


printf "\033[92m\033[1m"

echo ""
echo "SUCCESS!"
