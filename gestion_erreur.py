#coding:utf-8

"""
Gérer les exceptions :  try/except (+ else, finally)

Type d'exception :  ValueError
                    NameError
                    ZeroDivisionError
                    TypeError
                    OSErrorr
                    AssertionError
"""





"""
age_utilisateur = input("Quel âge as-tu ? ")

try:
    age_utilisateur = int(age_utilisateur)
except:
    print("L'âge indiqué est incorrect !")
else:
    print("Tu as", age_utilisateur, "ans")
finally:
    print("Fin du programme !")
"""




"""
nombre1 = 150
nombre2 = input("Choisir le nombre pour diviser : ")

try:
    nombre2 = int(nombre2)
    print("Résultat = {}".format(nombre1 / nombre2))
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par 0 !")
except ValueError:
    print("Vous devez entrer un nomre !")
except:
    print("Valeur incorrect !")
else :
    print("Bravo !!! Tu as entrez un nombre valide !")
finally:
    print("Fin du programme !")
"""





"""
try:
    age = input("Quel âge as-tu ? ")
    age = int(age)
    
    if age < 18:
        raise ZeroDivisionError("coucou !")

except ZeroDivisionError:
    print("J'ai attrapé ton exception inutile")
"""







"""
try:
    age = input("Quel âge as-tu ?")
    age = int(age)
    
    assert age > 18 #Je veux que âge soit plus grand que 18
except AssertionError:
    print("J'ai attrapé l'exception !")
"""