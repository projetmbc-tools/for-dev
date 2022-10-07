#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``tools/factory/gitignore/build_06_update_pyfiles.py``

from .TAGS import *

RULES = {
    "main": {
        TAG_DESC: "#### Main rules for standard ``(La)TeX`` projects, see https://github.com/latex3.",
        TAG_RULES_N_COMMENTS: [
            {
                TAG_COMMENTS: "## Core latex/pdflatex",
                TAG_RULES: [
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
                TAG_COMMENTS: "## Intermediate documents",
                TAG_RULES: ["*.dvi", "*.xdv", "*-converted-to.*"],
            },
            {
                TAG_COMMENTS: '## Generated if empty string is given at\n## "Please type another file name for output:".',
                TAG_RULES: [".pdf"],
            },
            {
                TAG_COMMENTS: '## Extra "standard" tools.',
                TAG_RULES: [
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
                TAG_DESC: "#### Specific rules for the package ``gregoriotex``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "##", TAG_RULES: ["*.gaux", "*.glog", "*.gtex"]}
                ],
            }
        },
        "bibliography": {
            "biblio": {
                TAG_DESC: "#### Specific rules for bibliographies.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "##",
                        TAG_RULES: [
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
                TAG_DESC: "#### Specific rules for the package ``algorithms``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "##", TAG_RULES: ["*.alg", "*.loa"]}
                ],
            }
        },
        "science": {
            "gnuplottex": {
                TAG_DESC: "#### Specific rules for the package ``gnuplottex``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "##", TAG_RULES: ["*-gnuplottex-*"]}
                ],
            },
            "sympytex": {
                TAG_DESC: "#### Specific rules for the package ``sympytex``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "##",
                        TAG_RULES: ["*.sout", "*.sympy", "sympy-plots-for-*.tex/"],
                    }
                ],
            },
            "sagetex": {
                TAG_DESC: "#### Specific rules for the package ``sagetex``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "##",
                        TAG_RULES: ["*.sagetex.sage", "*.sagetex.py", "*.sagetex.scmd"],
                    }
                ],
            },
            "feynmfp": {
                TAG_DESC: "#### Specific rules for the packages ``feynmf`` and ``feynmp``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "##",
                        TAG_RULES: ["*.m[fp]", "*.t[1-9]", "*.t[1-9][0-9]", "*.tfm"],
                    }
                ],
            },
        },
        "pdf": {
            "pdfpc": {
                TAG_DESC: "#### Specific rules for the package ``pdfpc``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.pdfpc"]}],
            },
            "newpax": {
                TAG_DESC: "#### Specific rules for the package ``newpax``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.newpax"]}],
            },
            "xmpincl": {
                TAG_DESC: "#### Specific rules for the package ``xmpincl``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.xmpi"]}],
            },
            "pdfcomment": {
                TAG_DESC: "#### Specific rules for the package ``pdfcomment``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "##", TAG_RULES: ["*.upa", "*.upb"]}
                ],
            },
            "pax": {
                TAG_DESC: "#### Specific rules for the package ``pax``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.pax"]}],
            },
        },
        "html": {
            "htlatex": {
                TAG_DESC: "#### Specific rules for the tool ``htlatex``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "##",
                        TAG_RULES: [
                            "*.4ct",
                            "*.4tc",
                            "*.idv",
                            "*.lg",
                            "*.trc",
                            "*.xref",
                        ],
                    }
                ],
            }
        },
        "editing": {
            "achemso": {
                TAG_DESC: "#### Specific rules for the package ``achemso``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["acs-*.bib"]}],
            },
            "elsarticle": {
                TAG_DESC: "#### Specific rules for the package ``elsarticle`` (documentclass of Elsevier journals).",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.spl"]}],
            },
            "ledmac": {
                TAG_DESC: "#### Specific rules for the package ``(r)(e)ledmac`` and ``(r)(e)ledpar``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "##",
                        TAG_RULES: [
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
                TAG_DESC: "#### Specific rules for the package ``tcolorbox``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.listing"]}],
            },
            "thmtools": {
                TAG_DESC: "#### Specific rules for the package ``thmtools``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.loe"]}],
            },
            "xcolor": {
                TAG_DESC: "#### Specific rules for the package ``xcolor``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.xcp"]}],
            },
            "beamer": {
                TAG_DESC: "#### Specific rules for the package ``beamer``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "##",
                        TAG_RULES: ["*.nav", "*.pre", "*.snm", "*.vrb"],
                    }
                ],
            },
            "amsthm": {
                TAG_DESC: "#### Specific rules for the package ``amsthm``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.thm"]}],
            },
            "xwatermark": {
                TAG_DESC: "#### Specific rules for the package ``xwatermark``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.xwm"]}],
            },
            "standalone": {
                TAG_DESC: "#### Specific rules for the package ``standalone``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.sta"]}],
            },
            "endfloat": {
                TAG_DESC: "#### Specific rules for the package ``endfloat``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "##", TAG_RULES: ["*.ttt", "*.fff"]}
                ],
            },
            "endnotes": {
                TAG_DESC: "#### Specific rules for the package ``endnotes``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.ent"]}],
            },
        },
        "linguistic": {
            "expex": {
                TAG_DESC: "#### Specific rules for the package ``expex``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "## Forward references with \\gathertags.",
                        TAG_RULES: ["*-tags.tex"],
                    }
                ],
            },
            "minted": {
                TAG_DESC: "#### Specific rules for the package ``minted``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "##", TAG_RULES: ["_minted*", "*.pyg"]}
                ],
            },
        },
        "dev": {
            "vhistory": {
                TAG_DESC: "#### Specific rules for the package ``vhistory``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "##", TAG_RULES: ["*.hst", "*.ver"]}
                ],
            },
            "fixme": {
                TAG_DESC: "#### Specific rules for the package ``fixme``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.lox"]}],
            },
            "easy-todo": {
                TAG_DESC: "#### Specific rules for the package ``easy-todo``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.lod"]}],
            },
            "morewrites": {
                TAG_DESC: "#### Specific rules for the package ``morewrites``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.mw"]}],
            },
            "changes": {
                TAG_DESC: "#### Specific rules for the package ``changes``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.soc"]}],
            },
            "cprotect": {
                TAG_DESC: "#### Specific rules for the package ``cprotect``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.cpt"]}],
            },
            "todonotes": {
                TAG_DESC: "#### Specific rules for the package ``todonotes``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.tdo"]}],
            },
            "comment": {
                TAG_DESC: "#### Specific rules for the package ``comment``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.cut"]}],
            },
        },
        "listing": {
            "listings": {
                TAG_DESC: "#### Specific rules for the package ``listings``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.lol"]}],
            }
        },
        "graphics": {
            "xypic": {
                TAG_DESC: "#### Specific rules for the package ``xypic``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "## Precompiled matrices and outlines",
                        TAG_RULES: ["*.xy[cd]"],
                    }
                ],
            },
            "tikz-pgf": {
                TAG_DESC: "#### Specific rules for the packages ``TikZ`` and  ``PGF``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "##", TAG_RULES: ["*.dpth", "*.md5", "*.auxlock"]}
                ],
            },
            "svg": {
                TAG_DESC: "#### Specific rules for the package ``svg``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "##", TAG_RULES: ["svg-inkscape/"]}
                ],
            },
        },
        "reference": {
            "titletoc": {
                TAG_DESC: "#### Specific rules for the package ``titletoc``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.ptc"]}],
            },
            "makeidx": {
                TAG_DESC: "#### Specific rules for the package ``makeidx``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "##", TAG_RULES: ["*.idx", "*.ilg", "*.ind"]}
                ],
            },
            "minitoc": {
                TAG_DESC: "#### Specific rules for the package ``minitoc``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "##",
                        TAG_RULES: [
                            "*.maf",
                            "*.ml[ft]",
                            "*.mtc[0-9]*",
                            "*.sl[cft][0-9]*",
                        ],
                    }
                ],
            },
            "xindy": {
                TAG_DESC: "#### Specific rules for the package ``xindy``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.xdy"]}],
            },
            "glossaries": {
                TAG_DESC: "#### Specific rules for the package ``glossaries``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "##",
                        TAG_RULES: [
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
                TAG_DESC: "#### Specific rules for the standard tool ``Makeindex``.",
                TAG_RULES_N_COMMENTS: [
                    {TAG_COMMENTS: "## Log files.", TAG_RULES: ["*.lpz"]}
                ],
            },
            "nomencl": {
                TAG_DESC: "#### Specific rules for the package ``nomencl``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.nl[gos]"]}],
            },
            "hyperref": {
                TAG_DESC: "#### Specific rules for the package ``hyperref``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.brf"]}],
            },
        },
        "extra-tools": {
            "pythontex": {
                TAG_DESC: "#### Specific rules for the package ``pythontex``.",
                TAG_RULES_N_COMMENTS: [
                    {
                        TAG_COMMENTS: "##",
                        TAG_RULES: ["*.pytxcode", "pythontex-files-*/"],
                    }
                ],
            },
            "scrwfile": {
                TAG_DESC: "#### Specific rules for the package ``scrwfile``.",
                TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.wrt"]}],
            },
        },
    },
    "editor": {
        "kbibtex": {
            TAG_DESC: "#### Specific rules for ``KBibTeX``, see https://apps.kde.org/fr/kbibtex/.",
            TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*~[0-9]*"]}],
        },
        "gummi": {
            TAG_DESC: "#### Specific rules for ``gummi``, see https://gummi.app/.",
            TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: [".*.swp"]}],
        },
        "kile": {
            TAG_DESC: "#### Specific rules for ``Kile``, see https://kile.sourceforge.io/.",
            TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.backup"]}],
        },
        "lyx": {
            TAG_DESC: "#### Specific rules for ``LyX``, see https://www.lyx.org/.",
            TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.lyx~"]}],
        },
        "emacs": {
            TAG_DESC: "#### Specific rules for ``emacs``, see https://www.gnu.org/software/emacs/.",
            TAG_RULES_N_COMMENTS: [
                {
                    TAG_COMMENTS: "## Auto folder when using auctex",
                    TAG_RULES: ["./auto/*", "*.el"],
                }
            ],
        },
        "texniccenter": {
            TAG_DESC: "#### Specific rules for ``TeXnicCenter``, see https://www.texniccenter.org/.",
            TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.tps"]}],
        },
        "texpad": {
            TAG_DESC: "#### Specific rules for ``Texpad``, see https://www.textpad.com/home.",
            TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: [".texpadtmp"]}],
        },
        "winedt": {
            TAG_DESC: "#### Specific rules for ``WinEdt``, see https://www.winedt.org/.",
            TAG_RULES_N_COMMENTS: [{TAG_COMMENTS: "##", TAG_RULES: ["*.bak", "*.sav"]}],
        },
    },
}
