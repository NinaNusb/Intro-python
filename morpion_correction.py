# Déclarations des fonctions

def afficher_grille(grille):
    """
    Fonction qui affiche la grille du jeu
    :param grille: (dict) Dictionnaire qui représente la grille
    :return: (none)
    """
    for cle in grille:
        print("| " + grille[cle][0] + " | " + grille[cle][1] + " | " + grille[cle][2] + " | ")

def est_gagnante(grille):
    """
    Fonction qui vérifie si quelqu'un a gagné sur cette grille
    :param grille: (dict) La grille de morpion
    :return: (boolean) Renvoie vrai si quelqu'un a gagné, False sinon
    """
    # Vérification des lignes
    for cle, ligne in grille.items():
        if (ligne[0] == ligne[1] == ligne[2]) and ligne[0] != "-":
            return True
    # Vérification des colonnes
    for i in range(3):
        if (grille["A"][i] == grille["B"][i] == grille["C"][i]) and grille["A"][i] != "-":
            return True
    # Vérification des diagonales
    if (grille["A"][0] == grille["B"][1] == grille["C"][2]) and grille["A"][0] != "-":
        return True
    if (grille["C"][0] == grille["B"][1] == grille["A"][2]) and grille["A"][0] != "-":
        return True
    return False

def est_pleine(grille):
    """
    Fonction qui renvoie True si la grille est pleine, False sinon
    :param grille: (dict) Le plateau de jeu
    :return: (boolean) True si la grille est plein, False sinon
    """
    for cle, ligne in grille.items():
        if "-" in ligne:
            return False
    return True

def jouer_coup(grille, joueur, coup):
    """
    Fonction qui permet de jouer un coup
    :param grille: (dict) Le plateau de jeu
    :param joueur: (str) Le caractère qui va être placé sur la grille
    :param coup: (str) chaine de caractères qui contient en position 0 une lettre entre A, B ou C, et en position 1 un chiffre entre 0 et 2 inclus
    :return: Renvoie le nouveau plateau de jeu si le coup est valide. False sinon
    """
    if coup[0] in grille and int(coup[1]) in range(3):
        if grille[coup[0]][int(coup[1])] == "-":
            grille[coup[0]][int(coup[1])] = joueur
            return grille
    return False

# Programme principal

plateau = {
    "A" : ["-", "-", "-"],
    "B" : ["-", "-", "-"],
    "C" : ["-", "-", "-"]
}

fin = False
joueur = "X"

while not fin:
    afficher_grille(plateau)
    coup = input("( " + joueur + " ) Entrez votre coup : (Les lignes vont de A à C, les colonnes de 0 à 2 inclus)")
    grille2 = jouer_coup(plateau, joueur, coup) 
    #Grille2 = le nouveau plateau si le coup est valide, sinon False
    while grille2 == False:
        # On demande à l'utilisateur de renter une valeur tant qu'il n'a pas donné une valeur correcte pour le coup
        coup = input("( " + joueur + " ) Entrez votre coup valide : Les lignes vont de A à C, les colonnes de 0 à 2 inclus et qui n'est pas une case déjà occupée")
        grille2 = jouer_coup(plateau, joueur, coup)
    plateau = grille2

    gagnee = est_gagnante(plateau)
    pleine = est_pleine(plateau)

    fin = gagnee or pleine # Permet de savoir si la partie est finie

    if gagnee:
        print("Félicitation joueur " + joueur + " !")
    elif pleine:
        print("Egalité !")
    else:
        if joueur == "X":
            joueur = "O"
        else:
            joueur = "X"
    

