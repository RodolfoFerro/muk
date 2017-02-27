import turtle

def draw_flower(animal):
     animal.right(20)
     animal.forward(60)
     animal.right(20)
     animal.forward(60)
     animal.right(100)
     animal.forward(60)
     animal.right(20)
     animal.forward(60)

def draw_something(animal):
     animal.forward(100)
     animal.right(150)
     animal.forward(200)
     animal.right(150)
     draw_flower(animal)
 #    draw_something(animal)

def draw():

     window=turtle.Screen()
     window.bgcolor("pink")

     gato=turtle.Turtle()
     perro=turtle.Turtle()
     pez=turtle.Turtle()

     gato.speed(1000)
     perro.speed(1000)
     perro.shape("arrow")
     gato.shape("arrow")
     perro.color("red")
     gato.color("blue")

     for i in range(1,35):
          draw_flower(perro)
          draw_something(perro)
          perro.right(29)
          draw_flower(gato)
          draw_something(gato)
          gato.right(35)

     pez.right(180)
     pez.forward(60)
     pez.right(270)
     pez.forward(400)

     window.exitonclick()

draw()
