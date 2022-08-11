
# Liste 
test = ['Adam', 'Tom', 'Jon']
test2 = [1, 2, 8, 17]

# fonctions
print('Adam' in test) # Vérifie si élément est dans liste

print(len(test)) # Retourne le nombre d'éléments dans la liste

print(test.index('Tom')) # Renvoie première occurence de l'élément dans la liste

print(test.count('Tom')) # Renvoie le nombre d'éléments dans la liste

print(test.append(', and beans')) # Concatène l'élément à la suite de la liste
print(test)

print(min(test)) # (Affiche l'élément avec le plus de lettres....??)

print(max(test)) # (Affiche l'élément avec le moins de lettres...????)

print(min(test2)) # Renvoie l'élément le plus petit de la liste

print(max(test2)) # Retourne l'élément le plus grand de la liste

print(test[0:3]) # [Slicing] Exclue les éléments à partir des :
print(test)

test3 = test[1:2]
print(test3)








ma_liste = ['test', 2, 0.89]

print(ma_liste[0]) #Affiche l'élément désigné

ma_liste.insert(1, "valeur") #Ajoute élément indiqué à l'indice indiqué
print(ma_liste)

ma_liste.pop(0) #Supprime élément à l'indice indiqué
ma_liste.remove(8) #Supprime première occurence élément indiqué

ma_liste2 = ma_liste.copy() #Crée une copie de ma_liste dans ma_liste2 // Si pas .copy, crée une référence et donc les deux listes seraient modifiées en cas de changement. Donc INUTILE



#Portée des variables
a =0
b = 2

def additionner(nb1, nb2):
    resultat = nb1 + nb2
    return resultat

print additionner(a, b)

print(resultat) #IMPOSSIBLE car fonction utilisable que dans la fonction définie et non en-dehors

