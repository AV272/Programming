#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 12:35:54 2021

@author: lkst
"""

d = r'/home/lkst/github/Programming/Machine learning/Other/Data/diabetes.csv.gz'
import torch
from torch.autograd import Variable
import numpy as np
import torch.nn.functional as F

xy = np.loadtxt(d, delimiter=',', dtype=np.float32)

x_data = Variable(torch.from_numpy(xy[:,0,-1])) # exclude last colomn
y_data = Variable(torch.from_numpy(xy[:,[-1]]))


class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.l1 = torch.nn.Linear(8,6)
        self.l2 = torch.nn.Linear(6,4)
        self.l3 = torch.nn.Linear(4,1)
        
        self.sigmoid = torch.nn.Sigmoid()
        
    def forward(self,x):
        out1 = F.relu(self.l1(x))
        out2 = F.relu(self.l2(out1))
        y_pred = self.sigmoid(self.l3(out2))
        return(y_pred)
    
    