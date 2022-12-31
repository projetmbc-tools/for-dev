# Des traitements Python : libre cours à votre imagination.
my_nb = 777

def shortbin(nb: int) -> str:
    return bin(nb)[2:]

# ``JNGDATAS`` est un nom imposé pour communiquer les données.
JNGDATAS = {
    'mynb'      : my_nb,
    'mynb_base2': shortbin(my_nb),
}
