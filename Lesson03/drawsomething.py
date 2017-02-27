import turtle

def draw_something():
	window = turtle.Screen()
	window.bgcolor("black")

	draw_circleofsquares()
	draw_little_circle()
	draw_yellowcircle()
	draw_tallo()

	window.exitonclick()

def draw_circleofsquares():
	jess = turtle.Turtle()
	turtle.shape("turtle")
	jess.color("pink")
	jess.speed(10)

	for i in range (1,37):
		o=0
		while (o<4):
			jess.forward(100)
			jess.right(90)
			o = o + 1

		jess.right(10)

def draw_yellowcircle():
	yellow = turtle.Turtle()
	turtle.shape("arrow")
	yellow.color("yellow")
	yellow.speed(10)

	for i in range (1,37):
		o=0
		while (o<4):
			yellow.forward(25)
			yellow.right(90)
			o = o + 1

		yellow.right(10)

def draw_little_circle():
	little = turtle.Turtle()
	turtle.shape("turtle")
	little.color("purple")
	little.speed(10)

	for i in range (1,37):
		o=0
		while (o<4):
			little.forward(50)
			little.right(90)
			o = o + 1

		little.right(10)

def draw_tallo():
	tallo = turtle.Turtle()
	turtle.shape("arrow")
	tallo.color("green")
	tallo.speed(10)

	tallo.right(90)
	tallo.forward(500)

draw_something()

