#!/bin/bash

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

FOLDER_LIST="build-test-all-folders.txt"

USAGE="Usage: bash launch_all.bash [OPTIONS]"
TRY="'bash launch_all.bash --help' for help."

HELP="$USAGE

  Launch all 'launch.bash' files in each of the folders given in
  'launch-all-folders.txt'.

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


QUICKOPTION=""

if (( $# == 1 ))
then
    if [[ "$1" == "-q" || "$1" == "--quick" ]]
    then
        QUICKOPTION="-q"
    
    else
        if [[ "$1" == "--help" ]]
        then
            print_cli_info 0 "$HELP"
        fi
    fi
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
            
            bash $launcherfile "$QUICKOPTION" || exit 1
        done < <(find "$folder" -name 'launch.bash'  -type f | sort)
    fi
done < "$FOLDER_LIST"
