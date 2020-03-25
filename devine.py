"""
Dans ce module on souhaure faire deviner un nombre a un utilisateur


"""
registre = {}


def devine(restants, solution, get_user_input=input):
    while restants > 0:
        if int(get_user_input("Entrez un nombre : ")) == solution:
            return "gagne"
        restants -= 1
    return "perdu"


def renvoie1():
    """ Cette fonction renvoie toujours 1
    >>> renvoie1()
    1
    """

    return 1


class fake_input:
    def __init__(self, saisies):
        self._iter = iter(saisies)

    def __call__(self, *args):
        print(args)
        return next(self._iter)


if __name__ == "__main__":
    resultat = devine(3, 12)
    print(resultat)
    pass
