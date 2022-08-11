
liste = [1, 2, 3] 
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

def test(tmpdr):
    assert calculer_somme(liste) == 30