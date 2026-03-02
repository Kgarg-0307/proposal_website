import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ----- Write Text Once -----
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.goto(0, -30)
text_turtle.color("red")
text_turtle.write("Will You Be Mine? 💍", align="center", font=("Arial", 24, "bold"))

# ----- Heart Function -----
def draw_heart(x, y, size=25):
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

# ----- Animation Loop -----
radius = 200
num_hearts = 16
angle_offset = 0

while True:
    t.clear()
    
    for i in range(num_hearts):
        angle = 2 * math.pi * i / num_hearts + angle_offset
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        draw_heart(x, y)

    angle_offset += 0.05
    time.sleep(0.03)