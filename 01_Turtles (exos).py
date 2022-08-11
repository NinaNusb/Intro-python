#cercles

import turtle
turtle.speed(8) # permet de régler la vitesse d'animation de la tortue (1 étant le plus lent, 10 le plus rapide)

turtle.begin_fill() # permet d'indiquer à la tortue que l'on souhaite remplir la forme dessinée.
turtle.forward(200) # Ici une instruction permettant d'avancer de 200px
turtle.circle(30) # Ici une instruction permettant de dessiner un cercle de rayon 30px
turtle.end_fill() # permet d'indiquer à la tortue que nous n'avons plus besoin de remplir les nouvelles formes
turtle.circle(90)

# fin des instruction permettant de dessiner.

turtle.done()

#carré
turtle.speed(5)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.done()


#hexagone
v = 72
turtle.speed(5)
turtle.forward(100)
turtle.left(v)
turtle.forward(100)
turtle.left(v)
turtle.forward(100)
turtle.left(v)
turtle.forward(100)
turtle.left(v)
turtle.forward(100)
turtle.done()

#bateau
turtle.speed(3)
turtle.left(47)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(135)
turtle.forward(75)
turtle.right(90)
turtle.forward(75)
turtle.right(180)
turtle.forward(75)
turtle.right(90)
turtle.forward(75)
print(turtle.position())

turtle.penup()
turtle.goto((turtle.position()[0]), (turtle.position()[1])-10)
turtle.pendown()
turtle.left(180)
turtle.forward(150)
turtle.right(130)
turtle.forward(28)
turtle.right(50)
turtle.forward(100)
turtle.right(45)
turtle.forward(28)
turtle.done()

