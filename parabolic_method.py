import math as m

def f(x):
    return (x-4)**2+m.log(x)

def f_dx(x):
    return 2*(x-4) + 1/x

def f_ddx(x):
    return 2 - 1/x**2

def parabolic_method(x, eps=10**(-6)):
    count = 0
    x_new = x - f_dx(x)/f_ddx(x)
    while abs(x_new-x) > eps:
        x = x_new
        x_new = x - f_dx(x)/f_ddx(x)
        count += 1
    return x_new, count

xmin, count = parabolic_method(3)

print()
print('-------Метод парабол-------')
print(f'Xmin={xmin:.4f}, f(xmin)={f(xmin):.4f}, count={count}')