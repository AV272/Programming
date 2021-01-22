#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:53:28 2021

@author: lkst
"""

import torch
import numpy as np

################################################3
# Tensor initialisation

# directly from the data
data = [[1,2],[3,4]]
x_data = torch.tensor(data)
print(x_data)

# from NumPy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(x_np)

# from another tensor
x_ones = torch.ones_like(x_data) # retains the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")

# Tensors with random or constant values
shape = (2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f'Random tensor: \n {rand_tensor} \n')
print(f'Tensor from ones: \n {ones_tensor} \n')
print(f'Tensor from zeros: \n {zeros_tensor} \n')


##################################################
# Tensor attributes

# Tensor attributes is shape, datatype and device on which they stored
tensor = torch.rand(5,4)

print(f'Tensor shape: {tensor.shape}') 
print(f'Tensor datatype:  {tensor.dtype}') 
print(f'Tensor device:  {tensor.device}')
























 
