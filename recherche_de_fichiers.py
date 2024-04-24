import os
import sys

def rechercher_fichiers(repertoire, extension):
    fichiers_trouves = []
    for dossier, sous_dossiers, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            if fichier.endswith(extension):
                chemin_fichier = os.path.join(dossier, fichier)
                fichiers_trouves.append(chemin_fichier)
    return fichiers_trouves

if len(sys.argv) < 3:
    print("Usage: python recherche_fichiers.py <répertoire> <extension>")
    sys.exit(1)

repertoire = sys.argv[1]
extension = sys.argv[2]

fichiers_trouves = rechercher_fichiers(repertoire, extension)

if fichiers_trouves:
    print("Fichiers trouvés :")
    for fichier in fichiers_trouves:
        print(fichier)
else:
    print("Aucun fichier correspondant à l'extension spécifiée n'a été trouvé.")

