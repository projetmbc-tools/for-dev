@newvalidator('auth')
def auth(author):
    """
prototype::
    author : one string following the format ``"FirstName LastName [email]"``

    :return: the initial value of ``author``, but stripped


This validator builds automatically two new global parameters.

    1) ``author_fullname`` corresponds to ``"FirstName LastName"``.

    2) ``author_email`` corresponds to ``"email"``.
    """
    name , _ , email = author.partition('[')
    email, _ , _     = email.partition(']')

    name  = name.strip()
    email = email.strip()

    assert '@' in email, \
           (
            f"Bad email format << {email} >>."
             "\n"
            f"See : {author}"
           )

    Params[TAG_MAIN]['author_fullname'] = JSCType.str(name)
    Params[TAG_MAIN]['author_email']    = JSCType.str(email)

    return JSCType.str(author)
