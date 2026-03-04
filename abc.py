import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ---- Text ----
t.penup()
t.goto(0, -30)
t.color("red")
t.write("Will You Be Mine? 💍", align="center", font=("Arial", 24, "bold"))

# ---- Heart Function ----
def draw_heart(x, y, size=30):
    t.penup()
    t.goto(x, y)
    t.setheading(140)
    t.pendown()
    t.color("hotpink")
    t.begin_fill()
    t.forward(size)
    t.circle(-size/2, 200)
    t.left(120)
    t.circle(-size/2, 200)
    t.forward(size)
    t.end_fill()

# ---- Circular Pattern ----
radius = 200
num_hearts = 20

for i in range(num_hearts):
    angle = 2 * math.pi * i / num_hearts
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    draw_heart(x, y)

turtle.done()