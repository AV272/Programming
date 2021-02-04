#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:31:05 2021

@author: lkst
"""

import imageio
import numpy as np
import matplotlib.pyplot as mpl
import glob # helps work with filepath

our_own_dataset = []

# ? -- one symbol
for image_file_name in glob.glob('/home/lkst/github/Programming/Machine learning/Other/Data/?.png'):
    print('loading ...', image_file_name)
    # take true answer from file name
    label = int(image_file_name[-5:-4])
    # load image from png into array
    img_array = imageio.imread(image_file_name, as_gray=True)
    # reshape 28x28 into 784 array
    img_data = 255.0 - img_array.reshape(784)
    img_data = (img_data/255.0*0.99) + 0.01
    print(np.min(img_data))
    print(np.max(img_data))
    # create list from label and image data
    record = np.append(label, img_data)
    print(record)
    our_own_dataset.append(record)
    pass

mpl.imshow(our_own_dataset[3][1:].reshape(28,28), cmap='Greys',interpolation='None')







