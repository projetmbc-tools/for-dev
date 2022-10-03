#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``tools/factory/config/gitignore/build_06_update_pyfiles.py``

RULES = {
    "_main_": '#### Main rules for standard ``(La)TeX`` projects, see https://github.com/latex3.\n\n## Core latex/pdflatex\n*.aux\n*.cb\n*.cb2\n*.fls\n*.f[om]t\n*.lo[fgt]\n.*.lb\n*.out\n*.toc\n\n## Intermediate documents\n*.dvi\n*.xdv\n*-converted-to.*\n\n## Generated if empty string is given at\n\n## "Please type another file name for output:".\n.pdf\n\n## Extra "standard" tools.\n*.fdb_latexmk\n*.synctex\n*.synctex(busy)\n*.synctex.gz\n*.synctex.gz(busy)\n*.pdfsync\n\n',
    "packages": {
        "music": {
            "gregoriotex": "#### Specific rules for the package ``gregoriotex``.\n\n##\n*.gaux\n*.glog\n*.gtex\n\n"
        },
        "bibliography": {
            "biblio": "#### Specific rules for bibliographies.\n\n##\n*.bbl\n*.bcf\n*.blg\n*-blx.aux\n*-blx.bib\n*.run.xml\n\n"
        },
        "computer-science": {
            "algorithms": "#### Specific rules for the package ``algorithms``.\n\n##\n*.alg\n*.loa\n\n"
        },
        "science": {
            "gnuplottex": "#### Specific rules for the package ``gnuplottex``.\n\n##\n*-gnuplottex-*\n\n",
            "sympytex": "#### Specific rules for the package ``sympytex``.\n\n##\n*.sout\n*.sympy\nsympy-plots-for-*.tex/\n\n",
            "sagetex": "#### Specific rules for the package ``sagetex``.\n\n##\n*.sagetex.sage\n*.sagetex.py\n*.sagetex.scmd\n\n",
            "feynmfp": "#### Specific rules for the packages ``feynmf`` and ``feynmp``.\n\n##\n*.m[fp]\n*.t[1-9]\n*.t[1-9][0-9]\n*.tfm\n\n",
        },
        "pdf": {
            "pdfpc": "#### Specific rules for the package ``pdfpc``.\n\n##\n*.pdfpc\n\n",
            "newpax": "#### Specific rules for the package ``newpax``.\n\n##\n*.newpax\n\n",
            "xmpincl": "#### Specific rules for the package ``xmpincl``.\n\n##\n*.xmpi\n\n",
            "pdfcomment": "#### Specific rules for the package ``pdfcomment``.\n\n##\n*.upa\n*.upb\n\n",
            "pax": "#### Specific rules for the package ``pax``.\n\n##\n*.pax\n\n",
        },
        "html": {
            "htlatex": "#### Specific rules for the tool ``htlatex``.\n\n##\n*.4ct\n*.4tc\n*.idv\n*.lg\n*.trc\n*.xref\n\n"
        },
        "editing": {
            "achemso": "#### Specific rules for the package ``achemso``.\n\n##\nacs-*.bib\n\n",
            "elsarticle": "#### Specific rules for the package ``elsarticle`` (documentclass of Elsevier journals).\n\n##\n*.spl\n\n",
            "ledmac": "#### Specific rules for the package ``(r)(e)ledmac`` and ``(r)(e)ledpar``.\n\n##\n*.end\n*.?end\n*.[1-9]\n*.[1-9][0-9]\n*.[1-9][0-9][0-9]\n*.[1-9]R\n*.[1-9][0-9]R\n*.[1-9][0-9][0-9]R\n*.eledsec[1-9]\n*.eledsec[1-9]R\n*.eledsec[1-9][0-9]\n*.eledsec[1-9][0-9]R\n*.eledsec[1-9][0-9][0-9]\n*.eledsec[1-9][0-9][0-9]R\n\n",
        },
        "formatting": {
            "tcolorbox": "#### Specific rules for the package ``tcolorbox``.\n\n##\n*.listing\n\n",
            "thmtools": "#### Specific rules for the package ``thmtools``.\n\n##\n*.loe\n\n",
            "xcolor": "#### Specific rules for the package ``xcolor``.\n\n##\n*.xcp\n\n",
            "beamer": "#### Specific rules for the package ``beamer``.\n\n##\n*.nav\n*.pre\n*.snm\n*.vrb\n\n",
            "amsthm": "#### Specific rules for the package ``amsthm``.\n\n##\n*.thm\n\n",
            "xwatermark": "#### Specific rules for the package ``xwatermark``.\n\n##\n*.xwm\n\n",
            "standalone": "#### Specific rules for the package ``standalone``.\n\n##\n*.sta\n\n",
            "endfloat": "#### Specific rules for the package ``endfloat``.\n\n##\n*.ttt\n*.fff\n\n",
            "endnotes": "#### Specific rules for the package ``endnotes``.\n\n##\n*.ent\n\n",
        },
        "linguistic": {
            "expex": "#### Specific rules for the package ``expex``.\n\n## Forward references with \\gathertags.\n*-tags.tex\n\n",
            "minted": "#### Specific rules for the package ``minted``.\n\n##\n_minted*\n*.pyg\n\n",
        },
        "dev": {
            "vhistory": "#### Specific rules for the package ``vhistory``.\n\n##\n*.hst\n*.ver\n\n",
            "fixme": "#### Specific rules for the package ``fixme``.\n\n##\n*.lox\n\n",
            "easy-todo": "#### Specific rules for the package ``easy-todo``.\n\n##\n*.lod\n\n",
            "morewrites": "#### Specific rules for the package ``morewrites``.\n\n##\n*.mw\n\n",
            "changes": "#### Specific rules for the package ``changes``.\n\n##\n*.soc\n\n",
            "cprotect": "#### Specific rules for the package ``cprotect``.\n\n##\n*.cpt\n\n",
            "todonotes": "#### Specific rules for the package ``todonotes``.\n\n##\n*.tdo\n\n",
            "comment": "#### Specific rules for the package ``comment``.\n\n##\n*.cut\n\n",
        },
        "listing": {
            "listings": "#### Specific rules for the package ``listings``.\n\n##\n*.lol\n\n"
        },
        "graphics": {
            "xypic": "#### Specific rules for the package ``xypic``.\n\n## Precompiled matrices and outlines\n*.xy[cd]\n\n",
            "tikz-pgf": "#### Specific rules for the packages ``TikZ`` and  ``PGF``.\n\n##\n*.dpth\n*.md5\n*.auxlock\n\n",
            "svg": "#### Specific rules for the package ``svg``.\n\n##\nsvg-inkscape/\n\n",
        },
        "reference": {
            "titletoc": "#### Specific rules for the package ``titletoc``.\n\n##\n*.ptc\n\n",
            "makeidx": "#### Specific rules for the package ``makeidx``.\n\n##\n*.idx\n*.ilg\n*.ind\n\n",
            "minitoc": "#### Specific rules for the package ``minitoc``.\n\n##\n*.maf\n*.ml[ft]\n*.mtc[0-9]*\n*.sl[cft][0-9]*\n\n",
            "xindy": "#### Specific rules for the package ``xindy``.\n\n##\n*.xdy\n\n",
            "glossaries": "#### Specific rules for the package ``glossaries``.\n\n##\n*.ac[nr]\n*.gl[gos]\n*.glsdefs\n*.lz[os]\n*.sl[gos]\n\n",
            "makeindex": "#### Specific rules for the standard tool ``Makeindex``.\n\n## Log files.\n*.lpz\n\n",
            "nomencl": "#### Specific rules for the package ``nomencl``.\n\n##\n*.nl[gos]\n\n",
            "hyperref": "#### Specific rules for the package ``hyperref``.\n\n##\n*.brf\n\n",
        },
        "extra-tools": {
            "pythontex": "#### Specific rules for the package ``pythontex``.\n\n##\n*.pytxcode\npythontex-files-*/\n\n",
            "scrwfile": "#### Specific rules for the package ``scrwfile``.\n\n##\n*.wrt\n\n",
        },
    },
    "editor": {
        "kbibtex": "#### Specific rules for ``KBibTeX``, see https://apps.kde.org/fr/kbibtex/.\n\n##\n*~[0-9]*\n\n",
        "gummi": "#### Specific rules for ``gummi``, see https://gummi.app/.\n\n##\n.*.swp\n\n",
        "kile": "#### Specific rules for ``Kile``, see https://kile.sourceforge.io/.\n\n##\n*.backup\n\n",
        "lyx": "#### Specific rules for ``LyX``, see https://www.lyx.org/.\n\n##\n*.lyx~\n\n",
        "emacs": "#### Specific rules for ``emacs``, see https://www.gnu.org/software/emacs/.\n\n## Auto folder when using auctex\n./auto/*\n*.el\n\n",
        "texniccenter": "#### Specific rules for ``TeXnicCenter``, see https://www.texniccenter.org/.\n\n##\n*.tps\n\n",
        "texpad": "#### Specific rules for ``Texpad``, see https://www.textpad.com/home.\n\n##\n.texpadtmp\n\n",
        "winedt": "#### Specific rules for ``WinEdt``, see https://www.winedt.org/.\n\n##\n*.bak\n*.sav\n\n",
    },
}
