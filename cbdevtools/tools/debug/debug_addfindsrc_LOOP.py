#!/usr/bin/env python3

from pathlib import Path

project_dir = Path(__file__).parent
rootdir     = Path('/')

while(
    project_dir != rootdir
    and
    project_dir.name != 'cbdevtools'
):
    project_dir = project_dir.parent

print(project_dir)
