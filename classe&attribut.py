#codint:utf-8

class Humain:
    """
    classe des être humains
    """
    def __init__(self, c_prenom, c_age):
        print("Création d'un humain...")
        """
        self.prenom = "Mouss"
        self.age = 0
        """
        self.prenom = c_prenom
        self.age = c_age


print("Lancement du programme...")


h1 = Humain("Mouss", 1)
print("Prénom de h1 : {}".format(h1.prenom))
print("Age de h1 : {}".format(h1.age))


h2 = Humain("Oui", 34)