import math as m
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x):
    return (x - 4)**2 + np.log(x)

def gold_method_step(a, b, x1, x2, f1, f2):
    phi = (1 + m.sqrt(5)) / 2
    if f1 < f2:
        b = x2
        x2 = x1
        f2 = f1
        x1 = b - (b - a) / phi
        f1 = f(x1)
    else:
        a = x1
        x1 = x2
        f1 = f2
        x2 = a + (b - a) / phi
        f2 = f(x2)
    return a, b, x1, x2, f1, f2

# Исходные параметры
phi = (1 + m.sqrt(5)) / 2
a_init, b_init = 3, 5
eps = 10**(-6)

# Настройка графика
# Увеличение размера окна графика
fig, ax = plt.subplots(figsize=(10, 6)) # figsize=(ширина, высота)

# Установка границ осей, чтобы приблизить график к минимуму
ax.set_xlim(2.5, 5.5)
ax.set_ylim(0, 5)

x_vals = np.linspace(2.5, 5.5, 400)
y_vals = f(x_vals)
ax.plot(x_vals, y_vals, label='f(x)')
ax.set_title('Анимация метода золотого сечения')
ax.grid(True)

# Начальные точки на графике
x1_point, = ax.plot([], [], 'ro', label='$x_1$')
x2_point, = ax.plot([], [], 'go', label='$x_2$')
min_point, = ax.plot([], [], 'bo', markersize=8, label='Минимум')
interval_line, = ax.plot([], [], 'k--', label='Интервал')
ax.legend()

# Данные для анимации
a, b = a_init, b_init
x1 = b - (b - a) / phi
x2 = a + (b - a) / phi
f1, f2 = f(x1), f(x2)

def animate(i):
    global a, b, x1, x2, f1, f2
    
    if abs(b - a) > eps:
        a, b, x1, x2, f1, f2 = gold_method_step(a, b, x1, x2, f1, f2)
    
    x1_point.set_data([x1], [f1])
    x2_point.set_data([x2], [f2])
    
    interval_line.set_data([a, b], [f(a), f(a)])
    
    if abs(b - a) <= eps:
        xmin = (a + b) / 2
        min_point.set_data([xmin], [f(xmin)])
        
    return x1_point, x2_point, min_point, interval_line

# Создание анимации с новыми параметрами
# interval=500 делает анимацию в 5 раз медленнее
# frames=60 увеличивает количество шагов
ani = FuncAnimation(fig, animate, frames=60, blit=True, interval=500)
plt.show()