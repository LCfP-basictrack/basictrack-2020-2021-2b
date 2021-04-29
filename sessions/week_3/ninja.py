import turtle


ninja = turtle.Turtle()
screen = turtle.Screen()

for step in range(50):
    print(step)
    ninja.forward(5 * step)
    ninja.left(72)

ninja.forward(100)

screen.exitonclick()
