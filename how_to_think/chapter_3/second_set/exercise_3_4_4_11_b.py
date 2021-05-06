import turtle

screen = turtle.Screen()
cogsworth = turtle.Turtle()

screen.bgcolor("limegreen")

cogsworth.shape("turtle")
cogsworth.penup()
cogsworth.color("blue")
cogsworth.pensize(3)
cogsworth.left(90)

number_of_marks = 12

for _ in range(number_of_marks):
    cogsworth.forward(150)
    cogsworth.pendown()
    cogsworth.forward(10)
    cogsworth.penup()
    cogsworth.forward(20)
    cogsworth.stamp()
    cogsworth.backward(180)
    cogsworth.right(360 / number_of_marks)

screen.exitonclick()
