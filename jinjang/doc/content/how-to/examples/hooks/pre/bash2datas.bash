TODAY=$(date "+%d-%m-%y")
NOW=$(date   "+%H:%M:%S")

jq --null-input                    \
   --arg today "$TODAY"            \
   --arg now   "$NOW"                \
   '{"day": $today, "time": $now}' \
> lastchanges.json
