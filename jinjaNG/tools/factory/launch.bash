#!/bin/bash

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$THIS_DIR"


error_exit() {
    echo ""
    echo "ERROR - The following command opens the file that has raised an error."
    echo ""
    echo "  > open \"$1/$2\""
    exit 1
}


while read -r builderfile  # <(find . -name 'build_*'  -type f | sort)
do
    if [[ $(basename "$builderfile") =~ ^build_(1|0[2-9]).* ]]
    then
        echo ""
    fi

    echo ""
    echo "Launching $builderfile"
    echo ""
    python "$builderfile" || error_exit "$THIS_DIR" "$builderfile"
done < <(find . -name 'build_*'  -type f | sort)

echo ""
