import turtle
import random

# -----------------------
# Screen Setup
# -----------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Glowing Fractal Flower")

# -----------------------
# Turtle Setup
# -----------------------
flower = turtle.Turtle()
flower.speed(0)
flower.hideturtle()

flower.left(90)
flower.penup()
flower.goto(0, -260)
flower.pendown()

# Glow palette
colors = ["#ff4500", "#ff5a00", "#ff7b00", "#ffaa00", "#ff3300"]

# -----------------------
# Recursive Bloom
# -----------------------
def bloom(length):

    flower.pensize(length / 18)

    if length < 10:
        flower.color(random.choice(colors))
        flower.begin_fill()
        flower.circle(3)
        flower.end_fill()
        return

    flower.color(random.choice(colors))

    flower.forward(length)
    flower.circle(2)  # slight curve

    angle = random.randint(18, 26)

    flower.left(angle)
    bloom(length * 0.72)

    flower.right(angle * 2)
    bloom(length * 0.72)

    flower.left(angle)
    flower.backward(length)

# -----------------------
# Draw Flower
# -----------------------
bloom(140)

turtle.done()
