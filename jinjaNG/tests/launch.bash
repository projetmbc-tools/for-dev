#!/bin/bash

THIS_DIR="$(cd "$(dirname "$0")" && pwd)"


# ------------ #
# -- PYTEST -- #
# ------------ #

cd "$THIS_DIR"

pytest -v ./


# --------- #
# -- CLI -- #
# --------- #

printf "\033[32m\033[1m"

echo ""
echo ""
echo "===== CLI (via bash) ====="
echo ""

printf "\033[0m"

bash "$THIS_DIR/test_cli.bash"

echo ""
