import turtle
import random

# -----------------------
# Screen
# -----------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Bloom")

t = turtle.Turtle()
t.speed(10)
t.hideturtle()
t.left(90)
t.penup()
t.goto(0, -280)
t.pendown()

# -----------------------
# Parameters
# -----------------------
ANGLE = 25
STEP = 6
DEPTH = 5

COLORS = ["#ff3c1f", "#ff5f2e", "#ff8c42"]

# -----------------------
# L-System Rules
# -----------------------
rules = {
    "F": "FF+[+F-F-F]-[-F+F+F]"
}

axiom = "F"

# -----------------------
# Build L-System String
# -----------------------
def build(sentence, depth):
    for _ in range(depth):
        new = ""
        for ch in sentence:
            new += rules.get(ch, ch)
        sentence = new
    return sentence

sequence = build(axiom, DEPTH)

# -----------------------
# Draw System
# -----------------------
stack = []

for command in sequence:

    if command == "F":
        t.color(random.choice(COLORS))
        t.pensize(2)
        t.forward(STEP)

    elif command == "+":
        t.right(ANGLE)

    elif command == "-":
        t.left(ANGLE)

    elif command == "[":
        stack.append((t.position(), t.heading()))

    elif command == "]":
        pos, head = stack.pop()
        t.penup()
        t.goto(pos)
        t.setheading(head)
        t.pendown()

        # Blossom Dot
        t.color("#ffaa66")
        t.begin_fill()
        t.circle(3)
        t.end_fill()

turtle.done()
