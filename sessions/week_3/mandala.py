import turtle


monk = turtle.Turtle()
screen = turtle.Screen()

monk.speed(2)

#         0      1         2         3        4       5
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for step in range(480):
    monk.color(colors[step % len(colors)])
    monk.forward(25)
    monk.left(30)

    if step % 12 == 0:
        monk.left(15)

screen.exitonclick()
