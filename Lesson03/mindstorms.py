import turtle

def set_window(color="#212326"):
    # Set window:
    window = turtle.Screen()
    window.bgcolor(color)
    return window

def set_turtle(shape="turtle", turtle_color="#4286f4", path_color="#1f4d96", speed=1):
    # Set turtle:
    leo = turtle.Turtle()
    leo.shape(shape)
    leo.color(turtle_color, path_color)
    leo.speed(speed)
    return leo

def draw_regular_polygon(turtle, num_sides=4, side_size=100):
    # Set angle:
    ang = 180 - (num_sides - 2) * 180. / num_sides

    # Set path:
    for i in range(num_sides):
        turtle.right(ang)
        turtle.forward(side_size)

def draw_circle(turtle, radius=50):
    turtle.circle(radius)

def close(window):
    # Close window:
    window.exitonclick()

window = set_window()
donatello = set_turtle()
draw_regular_polygon(donatello)
draw_circle(donatello)
draw_regular_polygon(donatello, 3)
draw_regular_polygon(donatello, 6)
close(window)
