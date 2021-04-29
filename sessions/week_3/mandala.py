import turtle


monk = turtle.Turtle()
screen = turtle.Screen()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for step in range(500):
    monk.color(colors[step % len(colors)])
    monk.forward(25)
    monk.left(30)

    if step % 12 == 0:
        monk.left(15)

screen.exitonclick()
