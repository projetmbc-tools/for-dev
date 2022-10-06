#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``tools/factory/gitignore/build_06_update_src.py``

RULES = {
    "main": {
        "desc": "#### Main rules for standard ``(La)TeX`` projects, see https://github.com/latex3.",
        "rules": [
            {
                "comment": "## Core latex/pdflatex",
                "rules": [
                    "*.aux",
                    "*.cb",
                    "*.cb2",
                    "*.fls",
                    "*.f[om]t",
                    "*.lo[fgt]",
                    ".*.lb",
                    "*.out",
                    "*.toc",
                ],
            },
            {
                "comment": "## Intermediate documents",
                "rules": ["*.dvi", "*.xdv", "*-converted-to.*"],
            },
            {
                "comment": '## Generated if empty string is given at\n## "Please type another file name for output:".',
                "rules": [".pdf"],
            },
            {
                "comment": '## Extra "standard" tools.',
                "rules": [
                    "*.fdb_latexmk",
                    "*.synctex",
                    "*.synctex(busy)",
                    "*.synctex.gz",
                    "*.synctex.gz(busy)",
                    "*.pdfsync",
                ],
            },
        ],
    },
    "packages": {
        "music": {
            "gregoriotex": {
                "desc": "#### Specific rules for the package ``gregoriotex``.",
                "rules": [{"comment": "##", "rules": ["*.gaux", "*.glog", "*.gtex"]}],
            }
        },
        "bibliography": {
            "biblio": {
                "desc": "#### Specific rules for bibliographies.",
                "rules": [
                    {
                        "comment": "##",
                        "rules": [
                            "*.bbl",
                            "*.bcf",
                            "*.blg",
                            "*-blx.aux",
                            "*-blx.bib",
                            "*.run.xml",
                        ],
                    }
                ],
            }
        },
        "computer-science": {
            "algorithms": {
                "desc": "#### Specific rules for the package ``algorithms``.",
                "rules": [{"comment": "##", "rules": ["*.alg", "*.loa"]}],
            }
        },
        "science": {
            "gnuplottex": {
                "desc": "#### Specific rules for the package ``gnuplottex``.",
                "rules": [{"comment": "##", "rules": ["*-gnuplottex-*"]}],
            },
            "sympytex": {
                "desc": "#### Specific rules for the package ``sympytex``.",
                "rules": [
                    {
                        "comment": "##",
                        "rules": ["*.sout", "*.sympy", "sympy-plots-for-*.tex/"],
                    }
                ],
            },
            "sagetex": {
                "desc": "#### Specific rules for the package ``sagetex``.",
                "rules": [
                    {
                        "comment": "##",
                        "rules": ["*.sagetex.sage", "*.sagetex.py", "*.sagetex.scmd"],
                    }
                ],
            },
            "feynmfp": {
                "desc": "#### Specific rules for the packages ``feynmf`` and ``feynmp``.",
                "rules": [
                    {
                        "comment": "##",
                        "rules": ["*.m[fp]", "*.t[1-9]", "*.t[1-9][0-9]", "*.tfm"],
                    }
                ],
            },
        },
        "pdf": {
            "pdfpc": {
                "desc": "#### Specific rules for the package ``pdfpc``.",
                "rules": [{"comment": "##", "rules": ["*.pdfpc"]}],
            },
            "newpax": {
                "desc": "#### Specific rules for the package ``newpax``.",
                "rules": [{"comment": "##", "rules": ["*.newpax"]}],
            },
            "xmpincl": {
                "desc": "#### Specific rules for the package ``xmpincl``.",
                "rules": [{"comment": "##", "rules": ["*.xmpi"]}],
            },
            "pdfcomment": {
                "desc": "#### Specific rules for the package ``pdfcomment``.",
                "rules": [{"comment": "##", "rules": ["*.upa", "*.upb"]}],
            },
            "pax": {
                "desc": "#### Specific rules for the package ``pax``.",
                "rules": [{"comment": "##", "rules": ["*.pax"]}],
            },
        },
        "html": {
            "htlatex": {
                "desc": "#### Specific rules for the tool ``htlatex``.",
                "rules": [
                    {
                        "comment": "##",
                        "rules": ["*.4ct", "*.4tc", "*.idv", "*.lg", "*.trc", "*.xref"],
                    }
                ],
            }
        },
        "editing": {
            "achemso": {
                "desc": "#### Specific rules for the package ``achemso``.",
                "rules": [{"comment": "##", "rules": ["acs-*.bib"]}],
            },
            "elsarticle": {
                "desc": "#### Specific rules for the package ``elsarticle`` (documentclass of Elsevier journals).",
                "rules": [{"comment": "##", "rules": ["*.spl"]}],
            },
            "ledmac": {
                "desc": "#### Specific rules for the package ``(r)(e)ledmac`` and ``(r)(e)ledpar``.",
                "rules": [
                    {
                        "comment": "##",
                        "rules": [
                            "*.end",
                            "*.?end",
                            "*.[1-9]",
                            "*.[1-9][0-9]",
                            "*.[1-9][0-9][0-9]",
                            "*.[1-9]R",
                            "*.[1-9][0-9]R",
                            "*.[1-9][0-9][0-9]R",
                            "*.eledsec[1-9]",
                            "*.eledsec[1-9]R",
                            "*.eledsec[1-9][0-9]",
                            "*.eledsec[1-9][0-9]R",
                            "*.eledsec[1-9][0-9][0-9]",
                            "*.eledsec[1-9][0-9][0-9]R",
                        ],
                    }
                ],
            },
        },
        "formatting": {
            "tcolorbox": {
                "desc": "#### Specific rules for the package ``tcolorbox``.",
                "rules": [{"comment": "##", "rules": ["*.listing"]}],
            },
            "thmtools": {
                "desc": "#### Specific rules for the package ``thmtools``.",
                "rules": [{"comment": "##", "rules": ["*.loe"]}],
            },
            "xcolor": {
                "desc": "#### Specific rules for the package ``xcolor``.",
                "rules": [{"comment": "##", "rules": ["*.xcp"]}],
            },
            "beamer": {
                "desc": "#### Specific rules for the package ``beamer``.",
                "rules": [
                    {"comment": "##", "rules": ["*.nav", "*.pre", "*.snm", "*.vrb"]}
                ],
            },
            "amsthm": {
                "desc": "#### Specific rules for the package ``amsthm``.",
                "rules": [{"comment": "##", "rules": ["*.thm"]}],
            },
            "xwatermark": {
                "desc": "#### Specific rules for the package ``xwatermark``.",
                "rules": [{"comment": "##", "rules": ["*.xwm"]}],
            },
            "standalone": {
                "desc": "#### Specific rules for the package ``standalone``.",
                "rules": [{"comment": "##", "rules": ["*.sta"]}],
            },
            "endfloat": {
                "desc": "#### Specific rules for the package ``endfloat``.",
                "rules": [{"comment": "##", "rules": ["*.ttt", "*.fff"]}],
            },
            "endnotes": {
                "desc": "#### Specific rules for the package ``endnotes``.",
                "rules": [{"comment": "##", "rules": ["*.ent"]}],
            },
        },
        "linguistic": {
            "expex": {
                "desc": "#### Specific rules for the package ``expex``.",
                "rules": [
                    {
                        "comment": "## Forward references with \\gathertags.",
                        "rules": ["*-tags.tex"],
                    }
                ],
            },
            "minted": {
                "desc": "#### Specific rules for the package ``minted``.",
                "rules": [{"comment": "##", "rules": ["_minted*", "*.pyg"]}],
            },
        },
        "dev": {
            "vhistory": {
                "desc": "#### Specific rules for the package ``vhistory``.",
                "rules": [{"comment": "##", "rules": ["*.hst", "*.ver"]}],
            },
            "fixme": {
                "desc": "#### Specific rules for the package ``fixme``.",
                "rules": [{"comment": "##", "rules": ["*.lox"]}],
            },
            "easy-todo": {
                "desc": "#### Specific rules for the package ``easy-todo``.",
                "rules": [{"comment": "##", "rules": ["*.lod"]}],
            },
            "morewrites": {
                "desc": "#### Specific rules for the package ``morewrites``.",
                "rules": [{"comment": "##", "rules": ["*.mw"]}],
            },
            "changes": {
                "desc": "#### Specific rules for the package ``changes``.",
                "rules": [{"comment": "##", "rules": ["*.soc"]}],
            },
            "cprotect": {
                "desc": "#### Specific rules for the package ``cprotect``.",
                "rules": [{"comment": "##", "rules": ["*.cpt"]}],
            },
            "todonotes": {
                "desc": "#### Specific rules for the package ``todonotes``.",
                "rules": [{"comment": "##", "rules": ["*.tdo"]}],
            },
            "comment": {
                "desc": "#### Specific rules for the package ``comment``.",
                "rules": [{"comment": "##", "rules": ["*.cut"]}],
            },
        },
        "listing": {
            "listings": {
                "desc": "#### Specific rules for the package ``listings``.",
                "rules": [{"comment": "##", "rules": ["*.lol"]}],
            }
        },
        "graphics": {
            "xypic": {
                "desc": "#### Specific rules for the package ``xypic``.",
                "rules": [
                    {
                        "comment": "## Precompiled matrices and outlines",
                        "rules": ["*.xy[cd]"],
                    }
                ],
            },
            "tikz-pgf": {
                "desc": "#### Specific rules for the packages ``TikZ`` and  ``PGF``.",
                "rules": [{"comment": "##", "rules": ["*.dpth", "*.md5", "*.auxlock"]}],
            },
            "svg": {
                "desc": "#### Specific rules for the package ``svg``.",
                "rules": [{"comment": "##", "rules": ["svg-inkscape/"]}],
            },
        },
        "reference": {
            "titletoc": {
                "desc": "#### Specific rules for the package ``titletoc``.",
                "rules": [{"comment": "##", "rules": ["*.ptc"]}],
            },
            "makeidx": {
                "desc": "#### Specific rules for the package ``makeidx``.",
                "rules": [{"comment": "##", "rules": ["*.idx", "*.ilg", "*.ind"]}],
            },
            "minitoc": {
                "desc": "#### Specific rules for the package ``minitoc``.",
                "rules": [
                    {
                        "comment": "##",
                        "rules": [
                            "*.maf",
                            "*.ml[ft]",
                            "*.mtc[0-9]*",
                            "*.sl[cft][0-9]*",
                        ],
                    }
                ],
            },
            "xindy": {
                "desc": "#### Specific rules for the package ``xindy``.",
                "rules": [{"comment": "##", "rules": ["*.xdy"]}],
            },
            "glossaries": {
                "desc": "#### Specific rules for the package ``glossaries``.",
                "rules": [
                    {
                        "comment": "##",
                        "rules": [
                            "*.ac[nr]",
                            "*.gl[gos]",
                            "*.glsdefs",
                            "*.lz[os]",
                            "*.sl[gos]",
                        ],
                    }
                ],
            },
            "makeindex": {
                "desc": "#### Specific rules for the standard tool ``Makeindex``.",
                "rules": [{"comment": "## Log files.", "rules": ["*.lpz"]}],
            },
            "nomencl": {
                "desc": "#### Specific rules for the package ``nomencl``.",
                "rules": [{"comment": "##", "rules": ["*.nl[gos]"]}],
            },
            "hyperref": {
                "desc": "#### Specific rules for the package ``hyperref``.",
                "rules": [{"comment": "##", "rules": ["*.brf"]}],
            },
        },
        "extra-tools": {
            "pythontex": {
                "desc": "#### Specific rules for the package ``pythontex``.",
                "rules": [
                    {"comment": "##", "rules": ["*.pytxcode", "pythontex-files-*/"]}
                ],
            },
            "scrwfile": {
                "desc": "#### Specific rules for the package ``scrwfile``.",
                "rules": [{"comment": "##", "rules": ["*.wrt"]}],
            },
        },
    },
    "editor": {
        "kbibtex": {
            "desc": "#### Specific rules for ``KBibTeX``, see https://apps.kde.org/fr/kbibtex/.",
            "rules": [{"comment": "##", "rules": ["*~[0-9]*"]}],
        },
        "gummi": {
            "desc": "#### Specific rules for ``gummi``, see https://gummi.app/.",
            "rules": [{"comment": "##", "rules": [".*.swp"]}],
        },
        "kile": {
            "desc": "#### Specific rules for ``Kile``, see https://kile.sourceforge.io/.",
            "rules": [{"comment": "##", "rules": ["*.backup"]}],
        },
        "lyx": {
            "desc": "#### Specific rules for ``LyX``, see https://www.lyx.org/.",
            "rules": [{"comment": "##", "rules": ["*.lyx~"]}],
        },
        "emacs": {
            "desc": "#### Specific rules for ``emacs``, see https://www.gnu.org/software/emacs/.",
            "rules": [
                {
                    "comment": "## Auto folder when using auctex",
                    "rules": ["./auto/*", "*.el"],
                }
            ],
        },
        "texniccenter": {
            "desc": "#### Specific rules for ``TeXnicCenter``, see https://www.texniccenter.org/.",
            "rules": [{"comment": "##", "rules": ["*.tps"]}],
        },
        "texpad": {
            "desc": "#### Specific rules for ``Texpad``, see https://www.textpad.com/home.",
            "rules": [{"comment": "##", "rules": [".texpadtmp"]}],
        },
        "winedt": {
            "desc": "#### Specific rules for ``WinEdt``, see https://www.winedt.org/.",
            "rules": [{"comment": "##", "rules": ["*.bak", "*.sav"]}],
        },
    },
}
