@newvalidator('auth')
def auth(author):
    """
prototype::
    author : one string in the format ``"FirstName LastName [email]"``

    :return: the initial value of ``author``, but stripped


This validator builds automatically two new global parameters.

    1) ``author_fullname`` corresponds to ``"FirstName LastName"``.

    2) ``author_email`` corresponds to ``"email"``.
    """
    ...
