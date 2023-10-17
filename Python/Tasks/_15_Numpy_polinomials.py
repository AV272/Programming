"""
# Функция poly по заданным корням полинома возвращает коэффициенты при этом полиноме.
print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]

# Функция roots() наоборот возвращает корни уравнения по заданным коэффициентам при степенях.
print numpy.roots([1, 0, -1])           #Output : [-1.  1.]

# Функция polyint() возвращает неопределенный интеграл (коэф. при полиноме) от заданного полинома.
print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]

# Функция polyder() возвращает производную от заданного полинома.
print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]

# Функция поливалка возвращает значение полинома при заданном значении x.
print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34

# Функция polyfit фитирует точки на плоскости (x,y) методом наименьших квадратов к полиному указанной степени.
print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]

polyadd(pol1,pol2) -- суммирует два полинома
polysub() -- вычитает два полинома
polymul() -- вычисляет произведение двух полиномов
polydiv() -- вычисляет деление двух полиномов
"""

import numpy as np

pol = np.array(input().split(),float)
x = int(input())
print(np.polyval(pol,x))