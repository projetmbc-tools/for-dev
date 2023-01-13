#!/usr/bin/env python3

from pathlib import Path
from runpy   import run_path

THIS_DIR = Path(__file__).parent

data = run_path((THIS_DIR / 'folder-1') / 'data.py')

print(data["XTRA"])
