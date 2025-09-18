import math as m

def f(x):
    return (x-4)**2+m.log(x)
    #return x**2
    #return x-1-m.log(x) 

def gold_method(a: int, b: int, eps=10**(-6)):
    count = 0
    phi = (1 + m.sqrt(5)) / 2
    
    # Исходные точки
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    f1 = f(x1)
    f2 = f(x2)

    while abs(b - a) > eps:
        count += 1
        if f1 < f2:
            # Минимум находится в интервале [a, x2]
            b = x2
            x2 = x1  # Новая x2 — старая x1
            f2 = f1  # Новое значение f2 — старое f1
            x1 = b - (b - a) / phi  # Вычисляем новую x1
            f1 = f(x1)
        else:
            # Минимум находится в интервале [x1, b]
            a = x1
            x1 = x2  # Новая x1 — старая x2
            f1 = f2  # Новое значение f1 — старое f2
            x2 = a + (b - a) / phi  # Вычисляем новую x2
            f2 = f(x2)
            
    return (a + b) / 2, count

a = 3
b = 5
xmin, count = gold_method(a, b)

print(f'Точка минимума: {xmin}')
print(f'Значение: {f(xmin)}')
print(f'Кол-во итераций: {count}')