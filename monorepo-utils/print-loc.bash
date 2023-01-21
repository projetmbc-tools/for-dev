#!/bin/bash

THIS_DIR="$(cd "$(dirname "$0")" && pwd)"
THIS_FILE=$(basename "$0")
THIS_FILE=${THIS_FILE%%.*}

MAX_NBLINES_PRINTED=20

USAGE="Usage: bash $THIS_FILE.bash [OPTIONS]"
TRY="'bash $THIS_FILE.bash --help' for help."

HELP="$USAGE

  Print the differences between the current branch and the main one.

Options:
  -f, --folder  This ask to only print the folders changed.
  -p, --project This ask to only print the projects changed.
  --help        Show this message and exit.
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


ONLYFOLDER=0
ONLYPROJECT=1
ALLFILES=2

WHATISPRINTED=$ALLFILES

GROUPING_INFO="grouped by $MAX_NBLINES_PRINTED.
Type  Q + ENTER  to stop the printing"
WHAT_INFO="all the files $GROUPING_INFO"

if (( $# == 1 ))
then
    case $1 in
        "-f"|"--folder")
            WHATISPRINTED=$ONLYFOLDER
            WHAT_INFO="only the folders $GROUPING_INFO"
        ;;

        "-p"|"--project")
            WHATISPRINTED=$ONLYPROJECT
            WHAT_INFO="only the projects"
        ;;

        "--help")
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

printf "\033[32m"

echo ""
echo "===== CHANGES MADE ====="
echo ""
echo "We show $WHAT_INFO."
echo ""

printf "\033[0m"


LASTFOLDER=""
NBLINES_PRINTED=0


while read -r filechanged  # <(git diff main --name-only | sort)
do
    case $WHATISPRINTED in
        $ALLFILES)
            echo "$filechanged"
                (( NBLINES_PRINTED+=1 ))
        ;;

        $ONLYFOLDER)
            folder=$(dirname "$filechanged")

            if [[ "$LASTFOLDER" != "$folder" ]]
            then
                echo "$folder"
                LASTFOLDER="$folder"
                (( NBLINES_PRINTED+=1 ))
            fi
        ;;

# Source used.
#     + https://stackoverflow.com/a/68582698/4589608
        $ONLYPROJECT)
            projectfolder=$(dirname "$filechanged")
            projectfolder=${projectfolder%${projectfolder#*/}}

            if [[ $projectfolder != "" && $projectfolder != "changes/" && "$LASTFOLDER" != "$projectfolder" ]]
            then
                echo "$projectfolder"
                LASTFOLDER="$projectfolder"
                (( NBLINES_PRINTED+=1 ))
            fi
        ;;
    esac

    if [[ $NBLINES_PRINTED == $MAX_NBLINES_PRINTED ]]
    then
        read -r -s key < /dev/tty

        if [[ $key == "q" || $key == "Q" ]]
        then
            exit 0
        fi

        NBLINES_PRINTED=0
    fi
done < <(git diff main --name-only | sort)
