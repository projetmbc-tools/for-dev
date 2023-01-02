#!/bin/bash

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROJECTNAME=$(basename "$THIS_DIR" | tr '[:upper:]' '[:lower:]')

echo "Calling 'src2prod' to try to build a new '$PROJECTNAME' folder to publish it."

python -m src2prod --usegit --notsafe --readme='readme' "$THIS_DIR"
