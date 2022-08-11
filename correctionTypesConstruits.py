# Ex1
from unittest import result


nb_utilisateur = int(input("Entrez un entier : "))
ligne = "#"

for _ in range(nb_utilisateur):
    print(ligne)
    ligne = "#"

# Ex2

def somme(liste):
    """
    Fonction qui renvoie la somme des nombres de la liste
    :param liste: (list) une liste de nombre
    :return: (number) la somme des éléments de la liste
    """
    resultat = 0
    for elt in liste:
        resultat += elt
    return resultat

# Ex3

def moyenne(liste):
    """
    Fonction qui renvoie la moyenne des éléments de la liste
    :param liste: (list) une liste de nombre
    :return: (float) La moyenne des éléments de la liste
    """
    return somme(liste)/len(liste) #version en une ligne

# Ex4

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz fuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("fuzz")
    else:
        print(i)

# ex5

# ex5

def retourne_liste(liste):
    """
    Fonction qui renvoie la liste dans l'ordre inverse
    :param liste: (list) La liste à inverser
    :return: (list) la liste à l'enver
    """
    liste_retournee = []
    for elt in liste:
        liste_retournee.insert(0, elt)
    return liste_retournee

liste = [0, 1, 2, 3, 4, 5]
print(retourne_liste(liste))

# Exo 6

# ex 6

dico = {"python" : "Langage de programmation", "javascript" : "Moins bon langage de programmation", "liste": [0,1,2]}

mot_utilisateur = input("Quel est votre mot : ")

if mot_utilisateur in dico:
    print(dico[mot_utilisateur])
else:
    print("Nous ne connaissons pas ce mot")

#Ex 7 et 8

from random import randint

liste = [randint(1, 100) for _ in range(1000)]
list_inf_dix = [elt for elt in liste if elt < 10]


print(list_inf_dix)
print(len(list_inf_dix))


