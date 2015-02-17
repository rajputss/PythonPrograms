import turtle

def draw_s(some_turtle):
    #for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.left(90)
        some_turtle.forward(100)
        some_turtle.right(90)

        some_turtle.backward(100)
        some_turtle.right(90)
        some_turtle.backward(100)
        some_turtle.left(90)
        some_turtle.forward(100)

def draw_r(some_turtle):
    #for i in range(1,3):
        some_turtle.forward(200)
        some_turtle.left(90)
        some_turtle.forward(200)
        some_turtle.right(90)

        some_turtle.forward(100)
        some_turtle.right(90)
        some_turtle.forward(100)
        some_turtle.right(90)
        some_turtle.forward(100)
        some_turtle.left(135)
        some_turtle.forward(145)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed("3")

    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("white")
    angie.speed("3")    
    draw_s(brad)
    draw_r(angie)

    window.exitonclick()

draw_art()
