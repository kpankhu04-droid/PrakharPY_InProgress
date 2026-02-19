import math
import turtle

tl = turtle.Turtle()
tl.speed(9)
tl.penup()

print("enter which equation you want to use for the complex plane")
system = (input("Euler's formula or notation(E or N): ")).upper()
if system = 'E':
    

def draw_complex_plane():
    # X axis
    tl.goto(-350,0)
    tl.setheading(90)
    for i in range(-14,15):
        x = 25*i
        tl.pendown()
        tl.goto(x,0)
        tl.forward(10)
        tl.backward(20)
        tl.forward(10)
        tl.penup()
    # Y axis
    tl.goto(0,-350)
    tl.setheading(0)
    for i in range(-14,15):
        y = 25*i
        tl.pendown()
        tl.goto(0,y)
        tl.forward(10)
        tl.backward(20)
        tl.forward(10)
        tl.penup()

draw_complex_plane()
