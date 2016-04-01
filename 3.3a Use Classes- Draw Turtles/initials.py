import turtle

def draw_first(some_turtle):
    some_turtle.left(90)
    some_turtle.forward(100)
        
def draw_triangle(some_turtle):
    for i in range (1,4):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('white')
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('green')
    brad.speed(1)
    brad.left(90)
    brad.forward(200)
    for i in range (1, 36):
        draw_triangle(brad)
        brad.right(10)
        
        
    window.exitonclick()
#draw_square()
#draw_circle()
#draw_triangle()

draw_art()
