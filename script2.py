import os

def rechercher_tous_fichiers(repertoire):
    """Recherche tous les fichiers dans un répertoire et ses sous-répertoires."""
    fichiers_trouves = []
    for dossier, sous_dossiers, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            chemin_fichier = os.path.join(dossier, fichier)
            fichiers_trouves.append(chemin_fichier)
    return fichiers_trouves

# Exemple d'utilisation :
repertoire = '/chemin/vers/repertoire'
fichiers_trouves = rechercher_tous_fichiers(repertoire)

if fichiers_trouves:
    print("Fichiers trouvés :")
    for fichier in fichiers_trouves:
        print(fichier)
else:
    print("Aucun fichier trouvé dans le répertoire spécifié.")
