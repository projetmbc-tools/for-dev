#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``tools/factory/gitignore/build_06_update_src.py``

RULES = {
    "main": {
        "desc": "#### Main rules for standard Python projects, see https://github.com/python/.",
        "rules": [
            {"comment": "## Byte-compiled", "rules": ["__pycache__/", "*.py[co]"]},
            {"comment": "## Cython debug", "rules": ["cython_debug/"]},
        ],
    },
    "tasks": {
        "celery": {
            "desc": "#### Specific rules for ``Celery``, see https://github.com/celery/celery/.",
            "rules": [
                {"comment": "##", "rules": ["celerybeat-schedule", "celerybeat.pid"]}
            ],
        }
    },
    "web": {
        "flask": {
            "desc": "#### Specific rules for ``Flask``, see https://github.com/pallets/flask.",
            "rules": [{"comment": "##", "rules": ["instance/", ".webassets-cache"]}],
        },
        "django": {
            "desc": "#### Specific rules for ``Django``, see https://github.com/django/django.",
            "rules": [
                {
                    "comment": "##",
                    "rules": [
                        "*.log",
                        "local_settings.py",
                        "db.sqlite3",
                        "db.sqlite3-journal",
                    ],
                }
            ],
        },
    },
    "science": {
        "jupyter": {
            "desc": "#### Specific rules for ``Jupyter``, see https://github.com/jupyter.",
            "rules": [
                {"comment": "## Notebook", "rules": [".ipynb_checkpoints"]},
                {
                    "comment": "## IPython",
                    "rules": ["profile_default/", "ipython_config.py"],
                },
            ],
        },
        "sagemath": {
            "desc": "#### Specific rules for ``SageMath``, see https://www.sagemath.org.",
            "rules": [{"comment": "##", "rules": ["*.sage.py"]}],
        },
    },
    "datas": {
        "scrapy": {
            "desc": "#### Specific rules for ``Scrapy``, see https://github.com/scrapy/scrapy.",
            "rules": [{"comment": "##", "rules": [".scrapy"]}],
        }
    },
    "dev": {
        "env": {
            "desc": "#### Specific rules for working with virtual environments.",
            "rules": [
                {
                    "comment": "##",
                    "rules": [
                        ".env",
                        ".venv",
                        "env/",
                        "venv/",
                        "ENV/",
                        "env.bak/",
                        "venv.bak/",
                    ],
                },
                {"comment": "## pyenv", "rules": [".python-version"]},
                {"comment": "## pipenv", "rules": ["Pipfile.lock"]},
            ],
        },
        "pybuilder": {
            "desc": "#### Specific rules for ``PyBuilder``, see https://github.com/pybuilder/pybuilder.",
            "rules": [{"comment": "##", "rules": [".pybuilder/", "target/"]}],
        },
        "pyinstaller": {
            "desc": "#### Specific rules for ``PyInstaller``, see https://github.com/pyinstaller/pyinstaller.",
            "rules": [{"comment": "##", "rules": ["*.manifest", "*.spec"]}],
        },
        "testing": {
            "desc": "#### Specific rules for testing flow.",
            "rules": [
                {
                    "comment": "##",
                    "rules": [".tox/", ".nox/", "nosetests.xml", ".pytest_cache/"],
                },
                {
                    "comment": "## Coverage",
                    "rules": [
                        "htmlcov/",
                        ".coverage",
                        ".coverage.*",
                        "coverage.xml",
                        "*.cover",
                        "*.py,cover",
                        "cover/",
                    ],
                },
                {"comment": "##", "rules": [".hypothesis/"]},
            ],
        },
        "typing": {
            "desc": "#### Specific rules for typing specifications.",
            "rules": [
                {
                    "comment": "##",
                    "rules": [".mypy_cache/", ".dmypy.json", "dmypy.json"],
                },
                {"comment": "##", "rules": [".pyre/"]},
                {"comment": "## pytype", "rules": [".pytype/"]},
            ],
        },
        "packaging": {
            "desc": "#### Specific rules for packaging projects.",
            "rules": [
                {"comment": "##", "rules": ["MANIFEST.in"]},
                {"comment": "##", "rules": ["build/", "dist/", "sdist/"]},
                {
                    "comment": "##",
                    "rules": [
                        "develop-eggs/",
                        "eggs/",
                        ".eggs/",
                        "*.egg-info/",
                        "*.egg",
                    ],
                },
                {"comment": "##", "rules": ["wheels/", "share/python-wheels/"]},
                {"comment": "##", "rules": ["poetry.lock"]},
                {"comment": "## pdm", "rules": [".pdm.toml"]},
            ],
        },
        "rope": {
            "desc": "#### Specific rules for ``Rope``, see https://github.com/python-rope/rope.",
            "rules": [{"comment": "## Project settings", "rules": [".ropeproject"]}],
        },
    },
    "os": {
        "windows": {
            "desc": "#### Specific rules for the ``Windows`` OS.",
            "rules": [{"comment": "## DLL like", "rules": ["*.pyd"]}],
        }
    },
    "editor": {
        "spyder": {
            "desc": "#### Specific rules for ``Spyder``, see https://github.com/spyder-ide/spyder.",
            "rules": [
                {
                    "comment": "## Project settings",
                    "rules": [".spyderproject", ".spyproject"],
                }
            ],
        }
    },
}
