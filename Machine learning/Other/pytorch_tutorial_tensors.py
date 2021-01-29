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


##################################################
# Tensor operations

# Move to GPU
if torch.cuda.is_available():
    tensor2 = tensor.to('cuda')
    
print(torch.cuda.is_available())

# Numpy-like indexing and slicing
tensor = torch.ones(4,4)
tensor[:, 2] = 0
print(tensor)

# Joining tensors
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)
print(t1.shape)

# Multiplying tensors

t0 = [[1],[2],[3],[4]]
t00 = [5, 6, 7, 8]
#t1 = tensor.new_full((1,4), 5)
#t2 = tensor.new_full((4,1), 3)
t1 = torch.tensor(t0)
t2 = torch.tensor(t00)

# Поэлементное умножение тензоров (не матричное)
print(f't1 * t2 \n {t1*t2} \n')
print(f't1.mul(t2) \n {t1.mul(t2)} \n')
print(f't1*t1 {t1*t1}')

# Matrix multiplication
print(t1.shape, t2.shape)
#print(f'tensor.matmul(t2,t1) \n {torch.matmul(t2,t1)} \n')
#print(f'tensor.matmul(t1,t2) \n {torch.matmul(t1,t2)} \n')

#print(f't1.matmul(t2) \n {t1.matmul(t2)} \n')
print(f't2.matmul(t1) \n {t2.matmul(t1)} \n')

print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
# Alternative syntax:
print(f"tensor @ tensor.T \n {tensor @ tensor.T}")

# In-place operations (with _ symbol)
print(tensor, "\n")
tensor.add_(5)
print(tensor)
tensor.mul_(4)
print(tensor)


# Tensor to NumPy array
t = torch.ones(5,1)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

## Change in tensor reflects on array
t.add_(4)
print(f"t: {t}")
print(f"n: {n}")


# Array to tensor
n = np.ones(5)
t = torch.from_numpy(n)
print(t)
np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")



















 
