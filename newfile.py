import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

t.penup()
x = -400
while x < 400:
    width = random.randint(30, 60)
    height = random.randint(80, 250)
    t.goto(x, -300)
    t.pendown()
    t.fillcolor("#111122")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

    for _ in range(int(height / 20)):
        if random.random() > 0.5:
            wx = x + random.randint(5, width - 10)
            wy = -300 + random.randint(5, height - 10)
            t.penup()
            t.goto(wx, wy)
            t.pendown()
            t.dot(4, "blue")

    t.penup()
    x += width

t.goto(0, 0)
t.pendown()
t.pencolor("grey")
for i in range(300):
    t.forward(i)
    t.backward(i)
    t.right(59)

turtle.done()