import turtle


def calculate_turning_angle(sides: int):
    return 360 / sides


def draw_polygon(drawing_turtle: turtle.Turtle, sides: int = 4, size: int = 15):
    print("I should be drawing", sides, "sides")
    for _ in range(sides):
        drawing_turtle.forward(size)
        drawing_turtle.left(calculate_turning_angle(sides))


nick = turtle.Turtle()
screen = turtle.Screen()

# do my drawing stuff
for no_sides in range(3, 12):
    draw_polygon(nick, no_sides, no_sides * 5)

screen.exitonclick()
