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