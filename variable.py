#coding:utf-8

"""
Nommer une variable : -doit commencer par une lettre ou un underscores (_)
                      -ne dois pas contenir de caractère spéciaux
                      -ne dois pas contenir d'espace
                      -utiliser des underscores (_)
"""



"""
Types standards :   entier numérique (int)
                    nombre flottant (float)
                    chaîne de caractère (str)
                    booléen (bool)
                    autre (listes, dictionnaires, tuples, etc...)              
"""



"""
agePersonne = 27
agePersonne2 = "27"
PrixHT = 27.50
continuer_partie = True

texte = "L'âge de la personne est {} et le prix HT est de {}$."
print(texte.format(agePersonne, PrixHT))
"""



"""
Fontions vues : print() -> afficher à l'écran
                input() -> lire au clavier
                int(), float(), str(), bool() -> "caster" une donnée, la convertir
                type() -> retourne le type d'une donnée, variable, etc...
                str.format() -> formater une chaîne
"""





"""
prixHT = input("Entrez un prix HT : ")
prixHT = int(prixHT)

prixTTC = prixHT + (prixHT * 20 / 100)

print ("Le prix TTC =", prixTTC)
"""




"""
valeur_booleen = False
valeur_booleen = int(valeur_booleen)

print(valeur_booleen)
"""