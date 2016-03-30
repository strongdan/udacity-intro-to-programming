# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('white')
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('green')
    brad.speed(1)
    i = 0
    while i < 4:
        brad.forward(100)
        brad.left(90)
        i += 1
    
def draw_circle():
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)

def draw_triangle():
    jimmie = turtle.Turtle()
    jimmie.shape('classic')
    jimmie.color('brown')
    i = 0
    while i < 3:
        jimmie.forward(100)
        jimmie.right(120)
        i += 1

    window.exitonclick()
draw_square()
draw_circle()
draw_triangle()
# Your code here.
