#!/bin/bash

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
THIS_FILE=$(basename "$0")
THIS_FILE=${THIS_FILE%%.*}

FOLDER_LIST="$THIS_FILE-folders.txt"

USAGE="Usage: bash $THIS_FILE.bash [OPTIONS]"
TRY="'bash $THIS_FILE.bash --help' for help."

HELP="$USAGE

  Launch all 'launch.bash' files in each of the folders given in
  '$FOLDER_LIST'.

Options:
  -q, --quick Any builder file named 'build_..._slow' wil be ignored.
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


QUICKOPTION=""

if (( $# == 1 ))
then
    case $1 in
        "-q"|"--quick")
            QUICKOPTION="-q"
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


cd "$THIS_DIR"

while read -r line
do
    if [[ $line =~ ^-.* ]]
    then
        folder="${line:2}"

        while read -r launcherfile  # <(find . -name 'build_*'  -type f | sort)
        do
            printf "\033[34m\033[1m"

            echo ""
            echo "=====[ $launcherfile ]====="

            if [[ "$folder" == "tests" ]]
            then
                echo ""
            fi

            printf "\033[0m"

            bash $launcherfile $QUICKOPTION || exit 1
        done < <(find "$folder" -name 'launch.bash'  -type f | sort)
    fi
done < "$FOLDER_LIST"
