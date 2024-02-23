import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Moving Circle")
screen.bgcolor("white")

# Create the turtle object
circle = turtle.Turtle()
circle.shape("circle")
circle.color("red")
circle.penup()

# Set the initial position of the circle
circle.goto(0, 0)

# Set the initial movement parameters
speed = 2
dx = speed
dy = speed

# Main game loop
while True:
    # Move the circle
    x = circle.xcor()
    y = circle.ycor()
    circle.goto(x + dx, y + dy)

    # Check for collision with screen edges
    if x >= screen.window_width() / 2 or x <= -screen.window_width() / 2:
        dx *= -1
    if y >= screen.window_height() / 2 or y <= -screen.window_height() / 2:
        dy *= -1

# Exit the program when the turtle window is closed
turtle.done()
