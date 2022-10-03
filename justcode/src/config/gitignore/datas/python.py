#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``tools/factory/config/gitignore/build_06_update_pyfiles.py``

RULES = {
    "_main_": "#### Main rules for standard Python projects, see https://github.com/python/.\n\n## Byte-compiled\n__pycache__/\n*.py[co]\n\n## Cython debug\ncython_debug/\n\n",
    "tasks": {
        "celery": "#### Specific rules for ``Celery``, see https://github.com/celery/celery/.\n\n##\ncelerybeat-schedule\ncelerybeat.pid\n\n"
    },
    "web": {
        "flask": "#### Specific rules for ``Flask``, see https://github.com/pallets/flask.\n\n##\ninstance/\n.webassets-cache\n\n",
        "django": "#### Specific rules for ``Django``, see https://github.com/django/django.\n\n##\n*.log\nlocal_settings.py\ndb.sqlite3\ndb.sqlite3-journal\n\n",
    },
    "science": {
        "jupyter": "#### Specific rules for ``Jupyter``, see https://github.com/jupyter.\n\n## Notebook\n.ipynb_checkpoints\n\n## IPython\nprofile_default/\nipython_config.py\n\n",
        "sagemath": "#### Specific rules for ``SageMath``, see https://www.sagemath.org.\n\n##\n*.sage.py\n\n",
    },
    "datas": {
        "scrapy": "#### Specific rules for ``Scrapy``, see https://github.com/scrapy/scrapy.\n\n##\n.scrapy\n\n"
    },
    "dev": {
        "env": "#### Specific rules for working with virtual environments.\n\n##\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n## pyenv\n.python-version\n\n## pipenv\nPipfile.lock\n\n",
        "pybuilder": "#### Specific rules for ``PyBuilder``, see https://github.com/pybuilder/pybuilder.\n\n##\n.pybuilder/\ntarget/\n\n",
        "pyinstaller": "#### Specific rules for ``PyInstaller``, see https://github.com/pyinstaller/pyinstaller.\n\n##\n*.manifest\n*.spec\n\n",
        "testing": "#### Specific rules for testing flow.\n\n##\n.tox/\n.nox/\nnosetests.xml\n.pytest_cache/\n\n## Coverage\nhtmlcov/\n.coverage\n.coverage.*\ncoverage.xml\n*.cover\n*.py,cover\ncover/\n\n##\n.hypothesis/\n\n",
        "typing": "#### Specific rules for typing specifications.\n\n##\n.mypy_cache/\n.dmypy.json\ndmypy.json\n\n##\n.pyre/\n\n## pytype\n.pytype/\n\n",
        "packaging": "#### Specific rules for packaging projects.\n\n##\nMANIFEST.in\n\n##\nbuild/\ndist/\nsdist/\n\n##\ndevelop-eggs/\neggs/\n.eggs/\n*.egg-info/\n*.egg\n\n##\nwheels/\nshare/python-wheels/\n\n##\npoetry.lock\n\n## pdm\n.pdm.toml\n\n",
        "rope": "#### Specific rules for ``Rope``, see https://github.com/python-rope/rope.\n\n## Project settings\n.ropeproject\n\n",
    },
    "os": {
        "windows": "#### Specific rules for the ``Windows`` OS.\n\n## DLL like\n*.pyd\n\n"
    },
    "editor": {
        "spyder": "#### Specific rules for ``Spyder``, see https://github.com/spyder-ide/spyder.\n\n## Project settings\n.spyderproject\n.spyproject\n\n"
    },
}
