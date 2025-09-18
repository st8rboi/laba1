import math as m


def f(x):
    return (x-4)**2+m.log(x)

def f_dx(x):
    return 2*(x-4) + 1/x


def tangent_method(a, b, eps=10**(-12)):
    count = 0
    x1 = (f(a)-f(b)-f_dx(a)*a+f_dx(b)*b)/(f_dx(b)-f_dx(a)) # x1 - пересечение касательных в точках a и b (4.00582)
    x2 = (f(a)-f(x1)-f_dx(a)*a+f_dx(x1)*x1)/(f_dx(x1)-f_dx(a)) # x2 - пересечение касательных в точках a и x1 (3.50501)
    x3 = (f(x1)-f(b)-f_dx(x1)*a+f_dx(b)*b)/(f_dx(b)-f_dx(x1)) # x3 - пересечение касательных в точках b и x1 (4.50385)
    
    while abs(b-a) >= eps:
        if f(x2) < f(x3):
            a, b = x2, x1
            x1 = (f(a)-f(b)-f_dx(a)*a+f_dx(b)*b)/(f_dx(b)-f_dx(a))
            x2 = (f(a)-f(x1)-f_dx(a)*a+f_dx(x1)*x1)/(f_dx(x1)-f_dx(a))  
            x3 = (f(x1)-f(b)-f_dx(x1)*a+f_dx(b)*b)/(f_dx(b)-f_dx(x1)) 
        else:
            a, b = x1, x3
            x1 = (f(a)-f(b)-f_dx(a)*a+f_dx(b)*b)/(f_dx(b)-f_dx(a))
            x2 = (f(a)-f(x1)-f_dx(a)*a+f_dx(x1)*x1)/(f_dx(x1)-f_dx(a)) 
            x3 = (f(x1)-f(b)-f_dx(x1)*a+f_dx(b)*b)/(f_dx(b)-f_dx(x1))
        count += 1 

    print(x1, f(x1), count)


tangent_method(3, 5)