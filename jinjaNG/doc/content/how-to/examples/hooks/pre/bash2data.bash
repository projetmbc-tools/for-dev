# -- LAUNCH ME ONLY IF I HAVE CHANGED -- #

THIS_DIR="$(cd "$(dirname "$0")" && pwd)"
THIS_FILE="$THIS_DIR/$(basename "$0")"

I_HAVE_CHANGED=0

# We don't want to pollute the change log produced by Git.
while read line
do
    if [[ "$THIS_FILE" == *"/$line" ]]
    then
        I_HAVE_CHANGED=1
    fi
done < <(git a | grep modified: | cut -c11-)

if [[ $I_HAVE_CHANGED -eq 0 ]]
then
    exit 0
fi


# -- DOC CODE -- #

TODAY=$(date "+%d-%m-%Y")
NOW=$(date   "+%H:%M:%S")

jq --null-input                    \
   --arg today "$TODAY"            \
   --arg now   "$NOW"              \
   '{"day": $today, "time": $now}' \
> data.json


# -- FOR TESTING -- #

OUTPUT="output.json"

if [ -f "$OUTPUT" ]
then
    rm "$OUTPUT"
fi

touch  "$OUTPUT"

# {
#     "day": {{day}},
#     "time": {{time}}
# }

cat << EOT >> $OUTPUT
{
    "day" : "$TODAY",
    "time": "$NOW"
}
EOT
