n = int(input("Entrez un nombre "))
if (n%2) ==0:
    print("Votre nombre est pair")
else:
    print("Votre nombre est impair")

g1 = int(input("Entrez un nombre "))
g2 = int(input("Entrez un nombre "))
g3 = int(input("Entrez un nombre "))
if g1 > g2 and g1 > g3:
    print("Le nombre le plus grand est " + str(g1))
elif g2 > g1 and g2 > g3:
    print("Le nombre le plus grand est " + str(g2))
else:
    print("Le nombre le plus grand est " + str(g3))"
