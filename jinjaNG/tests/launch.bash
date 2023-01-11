#!/bin/bash

THIS_DIR="$(cd "$(dirname "$0")" && pwd)"


HELP="$USAGE

  Launch all test files.

Options:
  -q, --quick Any builder file named 'test_..._slow' will be ignored.
              This option is useful during the development phase, but
              not when the project has to be published.
  -h, --help  Show this message and exit.
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
    case $1 in
        "-q"|"--quick")
            QUICKOPTION=1
        ;;

        "-h"|"--help")
            print_cli_info 0 "$HELP"
        ;;

        *)
            message="$USAGE
$TRY

Error: No such option: $1"

            print_cli_info 1 "$message"
        ;;
    esac
fi

# ------------ #
# -- PYTEST -- #
# ------------ #

cd "$THIS_DIR"

if [[ $QUICKOPTION == 1 ]]
then
    printf "\033[33m"

    echo "Slow tests are ignored."
    echo ""

    printf "\033[0m"

    pytest -v -k "not slow" ./
else
    pytest -v ./
fi
