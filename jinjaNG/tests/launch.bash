#!/bin/bash

THIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"


# ------------ #
# -- PYTEST -- #
# ------------ #

cd "$THIS_DIR"

pytest -v ./


# --------- #
# -- CLI -- #
# --------- #

printf "\033[1m"

echo ""
echo ""
echo "===== CLI FUNCTIONAL ? ====="
echo ""

printf "\033[33m"

echo "Warning: the contents are not analyzed (see the tests above for this)."
echo ""

printf "\033[0m"

bash "$THIS_DIR/test_cli.bash"
