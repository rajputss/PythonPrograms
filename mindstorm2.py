import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_triangle(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.left(90)
        some_turtle.right(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad to draw Square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)

    #Create the turtle Angie to draw a circle
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue")
    angie.circle(100)

    #Create the turtle Ted to draw a triangle
    ted = turtle.Turtle()
    ted.shape("turtle")
    ted.color("purple")
    draw_triangle(ted)

    window.exitonclick()

draw_art()
