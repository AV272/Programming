#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:00:23 2021

@author: lkst
"""

import torch
from torch.autograd import Variable

x_data = Variable(torch.Tensor([[1.0], [2.0], [3.0]]))
y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))

class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.linear = torch.nn.Linear(1,1) # (1,1) - 1 input, 1 output
        
    def forward(self, x):
        y_pred = self.linear(x)
        return(y_pred)
    
model = Model()

criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)

for epoch in range(500):
    y_pred = model(x_data)
    
    loss = criterion(y_pred,y_data)
    print(epoch, loss.item())
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
output = Variable(torch.Tensor([[4.0]]))
y_pred = model(output)
print('My prediction after training', 4, model(output).data[0][0])













