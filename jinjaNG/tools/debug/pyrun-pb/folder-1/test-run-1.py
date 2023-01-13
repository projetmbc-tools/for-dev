#!/usr/bin/env python3

from pathlib import Path
from runpy   import run_path

THIS_DIR = Path(__file__).parent

data = run_path(THIS_DIR / 'data.py')

print(data["XTRA"])
