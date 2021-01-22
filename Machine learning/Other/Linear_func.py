#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:56:16 2021

@author: lkst
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# Коэффициент при х
k = random.uniform(-5, 5)

# Свободный член в уравнении прямой
c = random.uniform(-5, 5)

print('Начальная прямая: ', k, '*X + ', c)

# Набор точек (данные)

data = {
    1: 2,
    2: 4.2,
    2.5: 5,
    3.8: 7.9,
    4: 9,
    6: 10.2,
    6.6: 13,
    7.2: 15.3,
    8: 17.1,
    8.5: 19.5
}

# Скорость обучения
rate = 0.0001

# Вычисляем у
def proceed(x):
    return x*k + c

# Тренировка сети
for i in range(100000):
    # Получить случайную Х координату точки
    x = random.choice(list(data.keys()))
    true_result = data[x]
    
    # Получаем ответ сети
    out = proceed(x)
    
    # Ошибка сети 
    delta = true_result - out
    
    # Меняем вес при х в соответствии с дельта-правилом
    k += delta*rate*x
    c += delta*rate
    
# Вывод данных готовой прямой
print('Готовая прямая: ', k, '*X + ', c)


# создаём рисунок с координатную плоскость
fig = plt.subplots()
# создаём область, в которой будет отображаться график
z = np.linspace(0, 10 ,100)
# значения x, которые будут отображены
# количество элементов в созданном массиве - качество прорисовки графика 
# рисуем график
plt.plot(z, proceed(z))
plt.plot(list(data.keys()),list(data.values()),'ro')
# показываем график
plt.show() 
    
    
    
    
    
    
    