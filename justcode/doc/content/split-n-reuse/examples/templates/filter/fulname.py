#!/usr/bin/python3

from justcode import newfilter, testfilter

@newfilter
def fullname(author):
    name, _, _ = author.partition('[')

    return name.strip()


# ----------------- #
# -- QUICK DEBUG -- #
# ----------------- #

if __name__ == '__main__':
    print(
        testfilter(
            author   = "Christophe BAL [projetmbc@gmail.com]",
            template = """
Auteur tel que tapé :
`{{author}}`

Prénom et nom de l'auteur :
`{{author | fullname}}`
            """.strip()
        )
    )
