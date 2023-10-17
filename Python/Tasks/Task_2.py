#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:57:31 2020

@author: alex
"""

'''
Task: function square must take one argument - square side, and back three 
values - perimetr, square and diagonal of square.
'''
import math

def square(x):
    p = 4*x
    s = x**2
    d = math.sqrt(2*(x**2))
    
    tup = (p,s,d) # tuple - cortez
    print(tup)
    