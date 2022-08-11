plateau = {'A':["X", "X", "O"], 'B':["-", "-", "O"], 'C':["-", "-", "X"]}


def remplacer_valeur(joueur, grille, coup): # jouer_coup(nom_joueur, plateau, coup)
    """
    Fonction qui remplace une valeur du dictionnaire par le symbole du joueur1 ou du joueur2
    :param plateau:  (dict) dictionnaire alliant coordonnées(clés) et espaces vides(valeurs)
    :return: (dict) dictionnaire alliant coordonnées(clés), espaces vides ou symbole des joueurs 1 et 2 (valeurs)
    """
    coup = input('lol')
    #pour vérifier si coup est valide
    if grille[coup[0]] == 'A' or grille[coup[0]] == 'B' or grille[coup[0]] == 'C':
        return True
    if grille[int(coup[1])] in [1,2,3]: #ou (i for i in range(3))
        return True
    #pour vérifier si coordonnée libre
    if grille[coup[0]][int(coup[1])-1] == '-':
        grille[coup[0]][int(coup[1])-1] = joueur
    return False

print(remplacer_valeur(plateau))
