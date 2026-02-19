from sympy import symbols, sympify, diff, integrate, sin
import turtle as tl

# Define variable
x = symbols('x')

# Define function from a string
expr = sympify("sin(x) + x**2")

# Differentiate
derivative = diff(expr, x)

# Integrate
integral = integrate(expr, x)

print("f(x) =", expr)
print("f'(x) =", derivative)
print("∫f(x) dx =", integral)

x = symbols('x')
expr = sympify("sin(x) + x**2")  # converts string → symbolic math object

print(type(expr))  # <class 'sympy.core.add.Add'>
print(expr.subs(x, 3))  # substitute x = 3
print(expr.diff(x))     # differentiate
print(expr.integrate(x)) # integrate

x = symbols('x')
expr = sympify("sin(x) + x**2")   # turn string into symbolic expression

# Differentiate
derivative = diff(expr, x)

# Evaluate derivative at x=2
value = derivative.subs(x, 2).evalf()

print("Derivative:", derivative)
print("Value at x=2:", value)


