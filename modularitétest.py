#coding:utf-8

"""
Module pour le joueur
"""


def parler(personnage, message):
    print("{} : {}".format(personnage, message))


def au_revoir():
    print("Au revoir !")

"""
TEST :

if __name__ == "__main__":
    parler("Mouss", "Bienvenue !")
    au_revoir()
"""