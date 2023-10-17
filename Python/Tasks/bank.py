#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:14:22 2020

@author: alex

Task: function takes two arguments - amount of money and time, and returns
two values - full amount of money on account and sum of percent (10% for year).
"""

def bank(money,years):
    x=0;
    x = money
    for i in range(years):
        x = x + x*0.1
        
    xx = x - money
    print('Full amount of money = ' + str(x))
    print('Percent amount = ' + str(xx))
