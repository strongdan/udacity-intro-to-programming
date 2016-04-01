# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('white')
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('green')
    brad.speed(1)
    for i in range (1, 36):
        draw_square(brad)
        brad.right(10)
        
    window.exitonclick()
#draw_square()
#draw_circle()
#draw_triangle()

draw_art()
# Your code here.
