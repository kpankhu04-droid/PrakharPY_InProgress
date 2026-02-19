from sympy import symbols, sympify, diff, integrate, sin
import turtle as tl

tl.speed(0)
tl.penup()

print("eg: x**2+4")
expr = input("enter the equation in with respect to x: ")

# Define variable
x = symbols('x')

# Define function from a string
expr = sympify(expr)

print("")
print("deravitive = D and integral = I")
choice = input("do you want the deravitive of integral of this eq: ").upper()
print("f(x) =", expr)
print('')

if choice == 'D':
    # Differentiate
    eq = diff(expr, x)
    print("f'(x) =", eq)
    num = float(input("enter the input num for x: " ))
    ans = eq.subs(x, num).evalf()
    print(ans)

elif choice == 'I':
    # Integrate
    eq = integrate(expr, x)
    print("∫f(x) dx =", eq)
    num1 = float(input("enter the first num for the integral: " ))
    num2 = float(input("enter the second num for the integral: " ))
    total = eq.subs(x,num1) - eq.subs(x,num2).evalf()
    print(total)

def draw_grid():
    # X axis
    tl.goto(-350,0)
    tl.setheading(90)
    for i in range(-50,50):
        x = i*7
        tl.pendown()
        tl.goto(x,0)
        tl.forward(5)
        tl.backward(10)
        tl.forward(5)
        tl.penup()
    # Y axis
    tl.goto(-350,-350)
    tl.setheading(0)
    for i in range(-50,50):
        y = i*7
        tl.pendown()
        tl.goto(-350,y)
        tl.forward(5)
        tl.backward(10)
        tl.forward(5)
        tl.penup()

draw_grid()


tl.goto(-350,0)
for i in range(-350,350):
    x_axis = i*7
    y = expr.subs(x,x_axis).evalf()
    tl.pendown()
    tl.goto(x_axis,y)
    tl.penup()

tl.goto(-350,0)
tl.pencolor('red')
for i in range(-350,350):
    x_axis = i
    y = eq.subs(x,x_axis).evalf()
    tl.pendown()
    tl.goto(x_axis,y)
    tl.penup()

if choice == 'I':
    for i in range(num1,num2,5):
        tl.goto(i,0)
        y = expr.subs(x,i).evalf()
        tl.penup()
        tl.goto(i,0)
        tl.pendown()
        tl.goto(i,y)
        tl.penup()
