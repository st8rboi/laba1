import math

def f(x):
    return (x - 4)**2 + math.log(x)

def f_dx(x):
    return 2*(x - 4) + 1/x

def f_ddx(x):
    return 2 - 1/(x**2)

def newton_method(x0, eps=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f_dx(x)/f_ddx(x)
        if abs(x_new - x) < eps:
            return x_new, f(x_new), i+1
        x = x_new
    return x, f(x), max_iter

xmin, fmin, steps = newton_method(2.0)
print(f"Минимум в точке x = {xmin}, f(x) = {fmin}, шагов = {steps}")
