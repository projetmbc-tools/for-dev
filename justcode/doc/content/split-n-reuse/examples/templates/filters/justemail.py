#!/usr/bin/python3

from justcode import (
    newfilter,
    loctest
)


# ------------------- #
# -- EXTRACT EMAIL -- #
# ------------------- #

@newfilter
def justemail(author):
    _, _, email = author.partition('[')
    email, _, _ = email.partition(']')

    return email.strip()


# ----------------- #
# -- QUICK DEBUG -- #
# ----------------- #

if __name__ == '__main__':
    print(
        loctest(
            author   = "Christophe BAL [projetmbc@gmail.com]",
            template = """
Auteur tel que tapé :
{{ author }}

Courriel de l'auteur :
{{ author | justemail }}
            """
        )
    )
