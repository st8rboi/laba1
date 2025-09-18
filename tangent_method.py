import math as m

def f(x):
    return (x-4)**2+m.log(x)

def f_dx(x):
    return 2*(x-4) + 1/x

def tangent(x, x0):
    return f(x0)+f_dx(x0)*(x-x0)

def cross_line(a, b):
    return (f(a)-f(b)-f_dx(a)*a+f_dx(b)*b)/(f_dx(b)-f_dx(a)) 
    

def tangent_method(a, b, eps=10**(-6)):
    count = 0
    x_m = cross_line(a, b) # 4.0
    x_l = cross_line(a, x_m) # 3.5
    x_r = cross_line(x_m, b) # 4.6
    while abs(b-a) > eps and abs(f(x_m)-tangent(x_m, b)) > eps:
        if f(x_l) < f(x_r):
            a, b = x_l, x_m
            x_m = cross_line(a, b)
            x_l = cross_line(a, x_m) 
            x_r = cross_line(x_m, b) 
        else: 
            a, b = x_m, x_r
            x_m = cross_line(a, b) 
            x_l = cross_line(a, x_m) 
            x_r = cross_line(x_m, b) 
        count += 1
    return x_m, count

xmin, count = tangent_method(3, 5)
print()
print('-------Метод касательных-------')
print(f'Xmin={xmin:.4f}, f(xmin)={f(xmin):.4f}, count={count}')