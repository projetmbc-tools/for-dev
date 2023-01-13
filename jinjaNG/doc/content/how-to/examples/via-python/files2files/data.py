word       = "TEST"
ascii_code = ''.join([
    f"{ord(c):0>3}"
    for c in word
])

JNGDATA = {
    "word"      : word,
    "ascii_code": ascii_code
}
