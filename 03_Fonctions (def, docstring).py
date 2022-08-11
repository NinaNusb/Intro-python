# Documentation fonction
def est_pair(nb):
    """
    #phrase de description de  la fonction#
    : param nb: (int) #indiquer le type de nb #Phrase de description du nombre
    : return : (boulean) #Phrase de description du boulean
    """

# Exemple
def est_pair(nb):
    """
    Cette fonction permet d'indiquer si le nombre entré par l'utilisateur est pair ou impair.
    : param nb: (int) Nombre dont on veut savoir s'il est pair. Doit être 
    : return : (Boulean)
    """
    nb = int(input("Entrez un nombre "))
    if (nb%2) == 0:
        print("Votre nombre est pair")
    else:
        print("Votre nombre")

# Exemple 2
# la docstring s'affiche lorsque que la fonction est appelée ce qui permet de s'avoir faciliment à quoi elle sert et comment l'utiliser
def somme(nombre1, nombre2):
    """
    Fonction qui renvoie la somme de deux nombres
    : param nombre1: (number) un nombre
    : param nombre2: (number) un second nombre à additionner au premier
    : return: (number) La somme des deux nombres
    """

    return nombre1 + nombre2

somme()

def afficher_bonjour():
    print("Bonjour")

afficher_bonjour

def calculer_somme (nb1, nb2):
    resultat = nb1 + nb2
    print(resultat)

calculer_somme(5,8)

résultat = calculer_somme(5, 8)

def calculer_somme2 (nb1, nb2):
    resultat = nb1 + nb2
    return resultat

test = calculer_somme (5, calculer_somme2(10, 5))


def est_pair(nb):
    if nb % 2 == 0:
        return True
    else:
        return False


