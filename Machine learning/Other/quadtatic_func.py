#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:49:33 2021

@author: lkst
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# Coefficients a,b,c
a = random.uniform(-5, 5)
b = random.uniform(-5, 5)
c = random.uniform(-10, 10)

print('Begin equation: ', a, '*X^2 + ', b, '*X + ', c)

# Набор точек (данные)

data = {
    1: 7.5,
    2.3: 17.315,
    -2.5: 39.875,
    3.8: 43.34,
    -5: 115.5,
    -7.7: 246.315,
    6.6: 134.06,
    7.2: 160.64,
    8: 200.0,
    -10: 398.0
}

# Скорость обучения
rate = 0.0001

# Вычисляем у
def proceed(x):
    return(a*x**2 + b*x + c)

# Тренировка сети
for i in range(100000):
    # Получить случайную Х координату точки
    x = random.choice(list(data.keys()))
    true_result = data[x]
    
    # Получаем ответ сети
    out = proceed(x)
    
    # Ошибка сети 
    #print(true_result - out)
    delta = (true_result - out)
    
    # Меняем вес при х в соответствии с дельта-правилом
    a += delta*rate*x**2
    b += delta*rate*x
    c += delta*rate
    #print('a = ', a, 'b = ', b, 'c = ', c)
    
# Вывод данных готовой прямой
print('Готовая прямая: ', a, '*X**2 + ', b, '*X + ', c)


# создаём рисунок с координатную плоскость
fig = plt.subplots()
# создаём область, в которой будет отображаться график
z = np.linspace(-10, 10 ,100)
# значения x, которые будут отображены
# количество элементов в созданном массиве - качество прорисовки графика 
# рисуем график
plt.plot(z, proceed(z))
plt.plot(list(data.keys()),list(data.values()),'ro')
# показываем график
plt.show() 









