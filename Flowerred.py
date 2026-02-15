import turtle
import random

# --- Screen Configuration ---
screen = turtle.Screen()
screen.bgcolor("#0a0a0a")  # Deep black makes the pink pop
# We removed screen.tracer(0,0) so you can see the visualization

t = turtle.Turtle()
t.hideturtle()
t.left(90)
t.speed(0) # '0' is the fastest animation speed, but still visible

def draw_leaf(t):
    """Draws a bright, glowing leaf at the branch tip."""
    # Using different shades of Hot Pink and Magenta
    leaf_colors = ["#FF1493", "#FF69B4", "#FF00FF", "#D81B60"]
    t.color(random.choice(leaf_colors))
    
    t.begin_fill()
    t.circle(random.randint(3, 5)) # Slightly larger leaves for beauty
    t.end_fill()

def draw_tree(branch_len, pensize, t):
    if branch_len > 8:
        t.pensize(pensize)
        
        # Color matching: Everything stays in the Red/Hot Pink family
        if branch_len > 40:
            t.color("#C21031") # Medium Violet Red for thicker stems
        else:
            t.color("#C51B3D") # Deep Pink for thinner stems
            
        t.forward(branch_len)
        
        # Create triple-branching for a bushier, more "beautiful" look
        angle = random.randint(20, 30)
        reduction = random.uniform(8, 12)
        
        # Right Branch
        t.right(angle)
        draw_tree(branch_len - reduction, pensize * 0.7, t)
        
        # Left Branch
        t.left(angle * 2)
        draw_tree(branch_len - reduction, pensize * 0.7, t)
        
        # Return to center
        t.right(angle)
        t.penup()
        t.backward(branch_len)
        t.pendown()
    else:
        # Draw the leaf when the branch is finished
        draw_leaf(t)

# --- Start Drawing ---
t.penup()
t.goto(0, -280) # Start from the very bottom
t.pendown()

# Start: Length 100, Thickness 7
draw_tree(100, 7, t)

# Keep the window open
screen.mainloop()