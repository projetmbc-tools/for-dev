#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``tools/factory/gitignore/build_06_update_pyfiles.py``

from .TAGS import *

RULES = {
    "main": {
        TAG_DESC: "#### Main rules for standard Python projects, see https://github.com/python/.",
        TAG_RULES_N_COMMENTS: [
            {TAG_COMMENTS: "## Byte-compiled", TAG_RULES: ["__pycache__/", "*.py[co]"]},
            {TAG_COMMENTS: "## Cython debug", TAG_RULES: ["cython_debug/"]},
        ],
    },
    "tasks": {
        "celery": {
            TAG_DESC: "#### Specific rules for ``Celery``, see https://github.com/celery/celery/.",
            TAG_RULES_N_COMMENTS: [
                {
                    TAG_COMMENTS: "##",
                    TAG_RULES: ["celerybeat-schedule", "celerybeat.pid"],
                }
            ],
        }
    },
    "web": {
        "flask": {
            TAG_DESC: "#### Specific rules for ``Flask``, see https://github.com/pallets/flask.",
            TAG_RULES_N_COMMENTS: [
                {TAG_COMMENTS: "##", TAG_RULES: ["instance/", ".webassets-cache"]}
            ],
        },
        "django": {
            TAG_DESC: "#### Specific rules for ``Django``, see https://github.com/django/django.",
            TAG_RULES_N_COMMENTS: [
                {
                    TAG_COMMENTS: "##",
                    TAG_RULES: [
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
            TAG_DESC: "#### Specific rules for ``Jupyter``, see https://github.com/jupyter.",
            TAG_RULES_N_COMMENTS: [
                {TAG_COMMENTS: "## Notebook", TAG_RULES: [".ipynb_checkpoints"]},
                {
                    TAG_COMMENTS: "## IPython",
                    TAG_RULES: ["profile_default/", "ipython_config.py"],
                },
            ],
        },
        "sagemath": {
            TAG_DESC: "#### Specific rules for ``SageMath``, see https://www.sagemath.org.",
            TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.sage.py"]}],
        },
    },
    "datas": {
        "scrapy": {
            TAG_DESC: "#### Specific rules for ``Scrapy``, see https://github.com/scrapy/scrapy.",
            TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: [".scrapy"]}],
        }
    },
    "dev": {
        "env": {
            TAG_DESC: "#### Specific rules for working with virtual environments.",
            TAG_RULES_N_COMMENTS: [
                {
                    TAG_COMMENTS: "##",
                    TAG_RULES: [
                        ".env",
                        ".venv",
                        "env/",
                        "venv/",
                        "ENV/",
                        "env.bak/",
                        "venv.bak/",
                    ],
                },
                {TAG_COMMENTS: "## pyenv", TAG_RULES: [".python-version"]},
                {TAG_COMMENTS: "## pipenv", TAG_RULES: ["Pipfile.lock"]},
            ],
        },
        "pybuilder": {
            TAG_DESC: "#### Specific rules for ``PyBuilder``, see https://github.com/pybuilder/pybuilder.",
            TAG_RULES_N_COMMENTS: [
                {TAG_COMMENTS: "##", TAG_RULES: [".pybuilder/", "target/"]}
            ],
        },
        "pyinstaller": {
            TAG_DESC: "#### Specific rules for ``PyInstaller``, see https://github.com/pyinstaller/pyinstaller.",
            TAG_RULES_N_COMMENTS: [
                {TAG_COMMENTS: "##", TAG_RULES: ["*.manifest", "*.spec"]}
            ],
        },
        "testing": {
            TAG_DESC: "#### Specific rules for testing flow.",
            TAG_RULES_N_COMMENTS: [
                {
                    TAG_COMMENTS: "##",
                    TAG_RULES: [".tox/", ".nox/", "nosetests.xml", ".pytest_cache/"],
                },
                {
                    TAG_COMMENTS: "## Coverage",
                    TAG_RULES: [
                        "htmlcov/",
                        ".coverage",
                        ".coverage.*",
                        "coverage.xml",
                        "*.cover",
                        "*.py,cover",
                        "cover/",
                    ],
                },
                {TAG_COMMENTS: "##", TAG_RULES: [".hypothesis/"]},
            ],
        },
        "typing": {
            TAG_DESC: "#### Specific rules for typing specifications.",
            TAG_RULES_N_COMMENTS: [
                {
                    TAG_COMMENTS: "##",
                    TAG_RULES: [".mypy_cache/", ".dmypy.json", "dmypy.json"],
                },
                {TAG_COMMENTS: "##", TAG_RULES: [".pyre/"]},
                {TAG_COMMENTS: "## pytype", TAG_RULES: [".pytype/"]},
            ],
        },
        "packaging": {
            TAG_DESC: "#### Specific rules for packaging projects.",
            TAG_RULES_N_COMMENTS: [
                {TAG_COMMENTS: "##", TAG_RULES: ["MANIFEST.in"]},
                {TAG_COMMENTS: "##", TAG_RULES: ["build/", "dist/", "sdist/"]},
                {
                    TAG_COMMENTS: "##",
                    TAG_RULES: [
                        "develop-eggs/",
                        "eggs/",
                        ".eggs/",
                        "*.egg-info/",
                        "*.egg",
                    ],
                },
                {TAG_COMMENTS: "##", TAG_RULES: ["wheels/", "share/python-wheels/"]},
                {TAG_COMMENTS: "##", TAG_RULES: ["poetry.lock"]},
                {TAG_COMMENTS: "## pdm", TAG_RULES: [".pdm.toml"]},
            ],
        },
        "rope": {
            TAG_DESC: "#### Specific rules for ``Rope``, see https://github.com/python-rope/rope.",
            TAG_RULES_N_COMMENTS: [
                {TAG_COMMENTS: "## Project settings", TAG_RULES: [".ropeproject"]}
            ],
        },
    },
    "os": {
        "windows": {
            TAG_DESC: "#### Specific rules for the ``Windows`` OS.",
            TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "## DLL like", TAG_RULES: ["*.pyd"]}],
        }
    },
    "editor": {
        "spyder": {
            TAG_DESC: "#### Specific rules for ``Spyder``, see https://github.com/spyder-ide/spyder.",
            TAG_RULES_N_COMMENTS: [
                {
                    TAG_COMMENTS: "## Project settings",
                    TAG_RULES: [".spyderproject", ".spyproject"],
                }
            ],
        }
    },
}
