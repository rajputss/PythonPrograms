import turtle

def draw_things():
    #Initialize Window
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()
    
def draw_square():
    #Initialize Brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    #Function draws a square using the given turtle
    sides = 0
    
    while(sides < 4):
        brad.forward(100)
        brad.right(90)
        sides += 1

def draw_circle():
    #Initialize Angie
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    #Initialize Kelly
    kelly = turtle.Turtle()
    kelly.shape("turtle")
    kelly.color("yellow")
    kelly.left(180)

    #Function draws a triangle using the given turtle
    sides = 0
    
    while(sides < 3):
        kelly.forward(100)
        kelly.left(120)
        sides += 1

draw_things()
