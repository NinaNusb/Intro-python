#Boucles

#Exercice 1
from sympy import TribonacciConstant, numbered_symbols


str = "#"
for i in range(int(input('Entrez un nombre: '))): #CORRECTION: input peut être mis dans une variable type nb_utilisateur
    print(str)                                    #CONVENTION: Utiliser _ à a place de i car variable ne sera pas utilisée
    str += "#"


#Exercice 2
liste = [1, 2, 3] #CORRECTION: liste pas nécessaire si on fait ensuite un print(calculer_somme(1, 2, 3))
def calculer_somme(liste):
    """
    Fonction qui calcule la somme des éléments de la liste
    :param nb1: (number) un nombre ==> CORRECTION: param liste: (list) une liste de nombres
    :param nb2: (number) un nombre
    :param nb3: (number) un nombre
    :return: (number) la somme des trois nombres
    """
    result = 0
    for nb in liste: # CORRECTION: nb peut être remplacé par elt
        result += nb
    return(result)
          
print(calculer_somme(liste))



#Exercice 3
liste = [10, 20, 30]
def calculer_moyenne(liste):
    """
    Fonction qui calcule la moyenne des éléments de la liste
    :param nb1: (number) un nombre
    :param nb2: (number) un nombre
    :param nb3: (number) un nombre
    :return: (float) la moyenne des éléments de la liste
    """
    result = 0      #CORRECTION: return calculer_somme(liste)/len(liste) car déjà utilisée précédemment
    for nb in liste:
        result += nb
    result2 = result / (len(liste))
    return (result2)

print(calculer_moyenne(liste))



#Exercice 4
list = []
print(list)
for i in range(1,100): #CORRECTION (1, 101)
    if i%3 == 0 and i%5 ==0:
        list.append("Fazz") #CORRECTION: print("fizz fuzz") car pas mentionné qu'il fallait créer une liste
    elif i%3 == 0:          #Condition la plus spécifique à tester en premier (ici double condition)
        list.append("Fizz") #CORRECTION: print("fizz")
    elif i%5 == 0:
        list.append("Fuzz") #CORRECTION: print("fuzz")
    else:
        list.append(i) #CORRECTION: print(i)
print(list)


#Exercice 5
phrase = ['soir', 'vendredi', 'le', "j'aime"]
def inverser(phrase):
    """
    Fonction inversant l'ordre des éléments de la liste
    :param élément1: (str) un mot ==> CORRECTION: param phrase: (list) la liste à inverser
    :param élément2: (str) un mot
    :param élément3: (str) un mot
    :param élément4: (str) un mot
    :return: les éléments dans le sens inverse
    """
    phrase2 = []
    for i in phrase: #CORRECTION: elt à la place de i
        print(i) #CORRECTION: pas nécessaire
        phrase2.insert(0,i) #placer avant élément précédent
    return phrase2
    
print(inverser(phrase))



#Exercice 6
dict = {"arbre" : "tronc", "famille" : "personnes", "informatique" : "ordinateur"} #{clé : valeur} Chaque clé associée à une seule valeur mais pourrait être une liste ==> {"liste": [0, 1, 2,]}

mot = input('Entrez un mot ') #SUGGESTION mot_utilisateur
if mot in dict:
    print(dict[mot])
else:
    print('Nous ne connaissons pas ce mot')



#Exercice 7
from random import randrange #random = module(ou bibliothèque)
from random import randint


lancer = [randint(1,100) for _ in range(1000)] # _ car variable i non utilisée, mais fonctionnerait
print(lancer)

#Exercice 8
# Méthode avec compréhenson de liste
lancer2 = [elt for elt in lancer if elt< 10 ]  #i = indice // elt = élément
print(lancer2)

# Méthode avec boucle
lancer3 = [] 
for i in lancer:
    if i<10:
        lancer3.append(i)
    else:
        None
print(lancer3)

#BONUS carré
liste_carre = [i*i for i in range(1000)] #très modulable: i+i
print(liste_carre)