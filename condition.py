#coding:utf-8
"""
Opérateurs de comparaison :  == (égal à)
                            != (différent de)
                            < (plus petit que)
                            > (plus grand que)
                            <= (plus petit ou égal à)
                            >= (supérieur ou égal à)


Conditions multiples :  and (l'un et l'autre)
                        or (l'un ou l'autre)
                        in / not in (dans / pas dans)
"""

"""
identifiant = "iammoussline"
mot_de_passe = "password123"


print("Interface de connexion")

user_id = input("Entrez votre identifiant : ")
user_password = input("Entrez votre mot de passe : ")

if user_id == identifiant and user_password == mot_de_passe:
    print("Vous êtes connectés, bienvenue", user_id)
"""


"""
lettre_hasard = "m"

if lettre_hasard in "aeiouy":
    print("c'est une voyelle")
else:
    print("C'est une consonne")
"""

age = input("Quel âge as-tu ? ")
age = int(age)

"""
age > 0 and age <= 100    ----->    0 < age <= 100
"""

if age < 18:
    print("Vous êtes mineur !")
elif age == 18:
    print("Felicitation vous êtes nouveau majeur !")
else:
    print("Vous êtes majeur !")