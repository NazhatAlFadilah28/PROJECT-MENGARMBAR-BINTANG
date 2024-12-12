import turtle
#CREATE A STAR IMAGE
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(5)

# Function to draw a star
def draw_star(size):
    for i in range(5):
        pen.forward(size)
        pen.right(144)  # Angle to make the star

# Start drawing the star
pen.color("blue")  # Color of the star
draw_star(100)

# Hide the turtle
pen.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
