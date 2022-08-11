# Exercice 1

# FAUX!!

# def nb_utilisateur ():
#   if nb_utilisateur % 2 == 0:
#        print("le nombre est pair")
#   else:
#        print("Le nombre est impair")

#nb_utilisateur = int(input("Entrez un nombre entier : "))


def est_pair(nb_utilisateur):
    if nb_utilisateur % 2 == 0:
        print("le nombre est pair")
    else:
        print("Le nombre est impair")

    return(nb_utilisateur)

print(est_pair(5))


# Exercice 2
def est_pair(nb):
    if nb % 2 == 0:
        return True
    else:
        return False

print(est_pair(5))


# Exercice 3
def est_pluspetit (nb1, nb2, nb3):
    if nb1 < nb2 and nb1 < nb3:
        return nb1
    elif nb2 < nb1 and nb2 < nb3:
        return nb2
    else:
        return nb3

print(est_pluspetit(6, 5, 18))


# Exercice 4
def multiplier_nombrenégatif(nb1, nb2):
    """
    Cette fonction renvoie la multiplication de nombres négatifs ou positifs
    : param nb1: (int) Nombre si négatif est transformé en positif
    : param nb2: (int) Nombre si négatif est transformé en négatif
    : return : (int) Résultat de la multiplication des arguments"""
    if nb1 < 0:
        nb1 = -nb1
    if nb2 < 0:
        nb2 = -nb2
    return nb1*nb2

print(multiplier_nombrenégatif(2, -4))



# Exercice 5
def calculer_moyenne(nb1, nb2, nb3):
    """
    Fonction qui renvoie la moyenne des 3 nombres 
    : param nb1: (number) un nombre
    : param nb2: (number) un nombre
    : param nb3: (number) un nombre
    : return: (number) La moyenne des 3 nombres
    """
    moyenne = (nb1 + nb2 + nb3)/3
    return moyenne

print(calculer_moyenne(5, 10, 15))
