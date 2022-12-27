TODAY=$(date "+%d-%m-%Y")
NOW=$(date   "+%H:%M:%S")

jq --null-input                    \
   --arg today "$TODAY"            \
   --arg now   "$NOW"              \
   '{"day": $today, "time": $now}' \
> datas.json


# ----------- #
# -- TESTS -- #
# ----------- #

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
