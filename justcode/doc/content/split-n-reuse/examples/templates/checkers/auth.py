#!/usr/bin/python3

from justcode import (
    newvalidator,
    testfilter,
    TAG_MAIN,
    Params,
    JSCType
)

# Un valideur est associé à un type justcode via le paramètre fourni
# au décorateur ``newvalidator``.
# Dans la mesure du possible, il est conseillé d'utiliser le même nom
# que la fonction Python faisant le travail, mais ceci n'est pas une
# obligation (sinon cela aurait été automatisé).
@newvalidator('auth')
def auth(author):
# Préparation des variables.
    name , _ , email = author.partition('[')
    email, _ , _     = email.partition(']')

    name  = name.strip()
    email = email.strip()

# Une vérification basique vraiment pas sérieuse...
    assert '@' in email, \
           (
            f"Bad email format << {email} >>."
             "\n"
            f"See : {author}"
           )

# Création de paramètres globaux de type "chaîne de caractères".
    Params[TAG_MAIN]['author_fullname'] = JSCType.str(name)
    Params[TAG_MAIN]['author_email']    = JSCType.str(email)

# Il est possible de transformer la valeur avant de la renvoyer.
# C'est la valeur renvoyée qui sera utilisée dans le squelette.
#
# Il faut obligatoirement renvoyé un type ``justcode`` obtenu via
# l'une des méthodes statiques de la classe ``JSCType``.
    author = JSCType.str(author)

    return author


# ----------------- #
# -- QUICK DEBUG -- #
# ----------------- #

if __name__ == '__main__':
    print(
        testfilter(
            author   = "Christophe BAL [projetmbc@gmail.com]",
            template = """
Auteur tel que tapé :
{{author}}

Prénom et nom de l'auteur :
{{author_fullname}}

Courriel de l'auteur :
{{author_email}}
            """
        )
    )
