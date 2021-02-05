#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:19:33 2021

@author: lkst
"""

import numpy as np
import matplotlib.pyplot as mpl
import scipy.ndimage as spnd

a = np.zeros([3,2])
a[0,0] = 1
a[0,1] = 2
a[1,0] = 9
a[2,1] = 12

mpl.imshow(a, interpolation=('nearest'))

# class of dogs
class dog:
    
    # метод для инициализации объекта внутренними данными
    def __init__(self, petname, temp):
        self.name = petname
        self.temperature = temp
    
    # получить состояние собаки
    def status(self):
        print('dogs name: ', self.name)
        print('dogs temperature: ', self.temperature)
        pass
    # задать температуру
    def setTemperature(self, temp):
        self.temperature = temp;
        pass
            
    # dods can barking
    def bark(self):
        print('Bark!')
        pass
    pass

sizzles = dog('Sizz', 37)
sizzles.status()


data_file = open('/home/lkst/github/Programming/Machine learning/Other/Data/mnist_test_10.csv')

data_list = data_file.readlines()
data_file.close()

len(data_list)

all_values = data_list[9].split(',')

image_array = np.asfarray(all_values[1:]).reshape((28,28))
img_arr_rotate = spnd.interpolation.rotate(image_array, 45, cval=0.01, reshape=False)
mpl.imshow(img_arr_rotate, cmap='Greys', interpolation=(None))


















