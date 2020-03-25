"""
Dans ce module on souhaure faire deviner un nombre a un utilisateur


"""
registre = {}


def devine(restants, solution, get_user_input=input):
    while restants > 0:
        if int(get_user_input()) == solution:
            return "gagne"
        restants -= 1
    return "perdu"


def renvoie1():
    """ Cette fonction renvoie toujours 1
    >>> renvoie1()
    1
    """

    return 1


def fake_input(saisies):
    for saisie in saisies:
        yield saisie


if __name__ == "__main__":
    saisies = [2, 12]
    fausse_entree = fake_input(saisies)
    print(devine(3, 12, get_user_input=fausse_entree.__next__))
    pass
