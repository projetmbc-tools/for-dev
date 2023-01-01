#!/bin/bash

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$THIS_DIR"


error_exit() {
    echo ""
    echo "ERROR - Following command opens the file that has raised an error."
    echo ""
    echo "  > open \"$1/$2\""
    exit 1
}


find . -name 'build_*'  -type f | sort  | while read -r i
do
    echo ""
    echo ""
    echo "Launching $i"
    echo ""
    python "$i" || error_exit "$THIS_DIR" "$i"
done
