#!/bin/bash

THIS_DIR="$(cd "$(dirname "$0")" && pwd)"


USAGE="Usage: bash launch.bash [OPTIONS]"
TRY="'bash launch.bash --help' for help."

HELP="$USAGE

  Launch all buider files.

Options:
  -q, --quick Any builder file named 'build_..._slow' wil be ignored.
              This option is useful during the development phase, but
              not when the project has to be published.
  --help      Show this message and exit.
"


print_cli_info() {
    echo "$2"
    exit $1
}


if (( $# > 1 ))
then
    message="$USAGE
$TRY

Error: Too much options."

    print_cli_info 1 "$message"
fi


QUICKOPTION=0

if (( $# == 1 ))
then
    if [[ "$1" == "-q" || "$1" == "--quick" ]]
    then
        QUICKOPTION=1

    else
        if [[ "$1" == "--help" ]]
        then
            print_cli_info 0 "$HELP"
        fi
    fi
fi

cd "$THIS_DIR"


error_exit() {
    printf "\033[91m\033[1m"
    echo "  ERROR , see the file:"
    echo "    + $1/$2"
    exit 1
}

print_about() {
    printf "\033[$1"
    echo "$2"
    printf "\033[0m"
}

echo ""

while read -r builderfile  # <(find . -name 'build_*'  -type f | sort)
do
    filename=$(basename "$builderfile")
    ext=${filename##*.}

    if [[ $QUICKOPTION == 1 && $filename =~ ^build_.*_slow\..* ]]
    then
        print_about "33m"  "Ignoring slow $builderfile"

    else
        print_about "32m" "Launching $builderfile"

        if [ "$ext" == "py" ]
        then
            command=python
        else
            command=bash
        fi

        $command "$builderfile" > /dev/null || error_exit "$THIS_DIR" "$builderfile"
    fi

    echo ""
done < <(find . -name 'build_*'  -type f | sort)
