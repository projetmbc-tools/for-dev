@newfilter
def fullname(author):
    """
prototype::
    author : a string following the format ``"FirstName LastName [email]"``

    :return: ``"FirstName LastName"`` without ``"[email]"``
    """
    name, _, _ = author.partition('[')

    return name.strip()
