#MORPION

#Fonctions (4)
def affiche_plateau(grille):     
    """
    Fonction qui affiche la grille du jeu
    :param grille: (dict) Dictionnaire qui représente la grille
    :return: (none) #ligne non nécessaire#
    """
    for clé  in grille:
        print("| " + grille[clé][0] + " | " + grille[clé][1] + " | " + grille[clé][2] + " |")       #for elt in grille[clé]:
                                                                                           #   print("|" + elt + "|")
                                                                                            #print(grille[clé]) 
                            
         #Pourquoi créer une boucle?? et non: print(grille['A']),print(grille['B']), print(grille['C'])


def est_gagnant(grille): # est_gagnante()
    """
    Fonction qui affiche le gagnant ==> CORRECTION: qui vérifie si quelqu'un a gagné sur cette grille
    :param plateau: (dict) dictionnaire alliant coordonnées(clés) et espaces vides ou symboles('X' ou 'O')
    :return: (boolean) Renvoie vrai si quelqu'un a gagné, Faux si non)
    """
    #Vérification des lignes
    for clé,ligne in grille.items():
        if (ligne[0] == ligne[1] == ligne[2]) and ligne != '-':
            return True
    #Vérification des colonnes:
    for i in range(3):
        if (grille['A'][i] == grille['B'][i] == grille['C'][i]) and ligne != '-':
            return True
    #Vérification des diagonales:
    if (grille['A'][0] == grille['B'][1] == grille['C'][2]) and ligne != '-':
            return True
    if (grille['A'][2] == grille['B'][1] == grille['C'][0]) and ligne != '-':
            return True
    return False


def est_plein(grille):
    """
    Fonction qui renvoie True si toutes les cases du plateau sont remplies, False si non
    :param plateau: (dict) dictionnaire de coordonnées(clés) et de symboles ou espaces(valeurs) ==> CORRECTION: le plateau de jeu
    :return: (boolean) True si remplie, False si non
    """
    for clé, ligne in grille.items():
        if '-' in ligne:
            return False
    return True


def remplacer_valeur(grille, coup, joueur): # jouer_coup(nom_joueur, plateau, coup) ==> CORRECTION: ajouter param joueur('X' or 'O') + coup = coordonnées(A1, A2, A3, ...)
    """
    Fonction qui remplace une valeur du dictionnaire par le symbole du joueur1 ou du joueur2 ==> CORRECTION: qui permet de jouer un coup
    :param grille:  (dict) dictionnaire alliant coordonnées(clés) et espaces vides(valeurs)
    :param joueur: (str) Le caractère qui va être placé sur la grille
    :param coup: (str) contient en position 0 une lettre entre A et C et en position 1 un chiffre entre 1 et 3
    :return: (dict) dictionnaire alliant coordonnées(clés), espaces vides ou symbole des joueurs 1 et 2 (valeurs) ==> CORRECTION: Renvoie le nouveau plateau de jeu si le coup est valide. False sinon
    """
    #pour vérifier si coup est valide
    if coup[0] == 'A' or coup[0] == 'B' or coup[0] == 'C': #CORRECTION: if coup[0] in ["A", "B", "C"] /OR/ if coup[0] in grille and coup[1] in range(3):   
        return True
    if int(coup[1]) in [0,1,2]: #ou (i for i in range(3))
        return True
    #pour vérifier si coordonnée libre
    if grille[coup[0]][int(coup[1])-1] != '-':
        print('Rejouez. Les coordonnées ne sont pas valides"')
    #pour remplacer
    else:
        grille[coup[0]][int(coup[1])] = joueur
   

symbole_joueur1 = 'X' #input('[Joueur 1] Entrez votre nom: ')
symbole_joueur2 = 'O' #input('[Joueur 2] Entrez votre nom: ')
joueur = 'X'
plateau = {
    'A':["-", "-", "-"],
    'B':["-", "-", "-"], 
    'C':["-", "-", "-"]}

plateau_fini = est_gagnant(plateau) or est_plein(plateau)
fin = False


#main
#while plateau_fini != True: # OR while plateau_fini ==  False // while not plateau_fini (SOLUTION A PREFERER!)
#    affiche_plateau(plateau)
#    i = 0
#    if i%2 == 0:
#        choix_joueur = input('Entrez les coordonnées: ')
#        if remplacer_valeur(plateau,choix_joueur) == True:
#            grille[coup[0]][int(coup[1])-1] = 'X'
#    else:
#        choix_joueur = input('Entrez les coordonnées: ')
#        if remplacer_valeur(plateau,choix_joueur) == True:
#            grille[coup[0]][int(coup[1])-1] = 'O'
    
"""#joueur1 puis joueur2
    choix_joueur = input('Entrez les coordonnées: ')
    if #tour joueur1:
        remplacer_valeur(symbole_joueur1, plateau, choix_joueur) 
    elif #tour joueur2: 
        remplacer_valeur(symbole_joueur2, plateau, choix_joueur) 
    elif remplacer_valeur(symbole_joueur1 or symbole_joueur2, plateau, choix_joueur) == False: 
        print('Rejouez. Les coordonnées ne sont pas valides"') #comment retourner à l'étape précédente?
est_gagnant(plateau) == True #and XXX
    print('Le gagnant est: ', symbole_joueur1) 
est_gagnant(plateau) == True #and OOO
    print('Le gagnant est: ', symbole_joueur2)
est_plein(plateau) == True
    print('Le jeu est terminé')
"""


while not fin: #while plateau_fini != True: # OR while plateau_fini ==  False // while not plateau_fini (SOLUTION A PREFERER!)
    affiche_plateau(plateau)
    coup = input("( " + joueur + " ) Entrez votre coup: (les lignes vont de A à C, les colonnes de 0 à 2 inclus")
    plateau2 = remplacer_valeur(plateau, joueur, coup)
    #Plateau2 = le nouveau plateau si le coup est valide, sinon False
    while plateau2 == False: #si coup invalide
       # On demande à l'utilisateur de rentrer une valeur tant qu'il n'a pas donné une valeur correcte pour 
        coup = input("( " + joueur + " ) Entrez votre coup: (les lignes vont de A à C, les colonnes de 0 à 2 inclus et qui n'est pas déjà occupée")
        plateau2 = remplacer_valeur(plateau, joueur, coup)
    plateau = plateau2

    gagnee = est_gagnant(plateau)
    pleine = est_plein(plateau)

    fin = gagnee or pleine #Permet de savoir si la partie est finie

    if gagnee:
        print("Félicitation joueur" + joueur + " !")
    elif pleine:
        print("Egalité !")
    else:
        if joueur == 'X':
            joueur = 'O'
        else:
            joueur = 'X'