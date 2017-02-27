import turtle


def draw_square () :
	window = turtle.Screen()
	window.bgcolor ("pink")
	turtle.speed (0)
	turtle.color("blue")

def shape (size, sides):
	for i in range(sides):
		turtle.forward(size)
		turtle.left(360/sides)

for i in range(100):
	shape(i, i)
	turtle.left(i)



window.exitonclick ()

draw_square()
