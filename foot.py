
nomFichier = 'FIFA-2022.txt'

# 1_Récupere les donner du fichier en liste
def recup_liste(fichier):
    # Ouvre le fichier en mode lecture
    with open(fichier, 'r', encoding='utf-8') as file:
        # Lit le contenu du fichier
        contenu = file.read()

    # Remplacer les retours à la ligne par des points
    contenu_modifie = contenu.replace('\n', '.')

    # Création d'une liste sans les points
    liste_resultante = contenu_modifie.split('.')

    # Initiation de la liste de liste
    liste_fin = []

    # Parcourir la liste_resultante pour faire la liste_fin
    for i in range(len(liste_resultante)):
        liste_chaine = liste_resultante[i]
        chaine_split = liste_chaine.split(',')
        liste_fin.append(chaine_split)

    # Suppression de la première ligne
    del(liste_fin[0])

    # Return le résultat
    return liste_fin


liste = recup_liste(nomFichier)
print(liste)
