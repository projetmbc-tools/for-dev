TODAY=$(date "+%d-%m-%y")
NOW=$(date   "+%H:%M:%S")

jq --null-input                    \
   --arg today "$TODAY"            \
   --arg now   "$NOW"              \
   '{"day": $today, "time": $now}' \
> lastchanges.json

# ----------- #
# -- TESTS -- #
# ----------- #

TEMPL_OUT="tmpl-test-out.json"

if [ -f "$TEMPL_OUT" ]
then
    rm "$TEMPL_OUT"
fi

touch  "$TEMPL_OUT"

# {
#     "day": {{day}},
#     "time": {{time}}
# }

cat << EOT >> $TEMPL_OUT
{
    "day": "$TODAY",
    "time": "$NOW"
}
EOT
