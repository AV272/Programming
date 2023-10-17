# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:49:01 2019

@author: Алексей
"""

import statistics as stat

help(stat)

x=[1,3,3,5,5,9]


print('Mean= ' + str(stat.mean(x)))
Mean= 4.333333333333333 

print('Variance = ' + str(stat.variance(x)))
Variance = 7.466666666666667 # dispersion

print('StdDev = ' + str(stat.stdev(x)))
StdDev = 2.7325202042558927  # sqrt(variance)

print('Median = ' + str(stat.median(x)))
Median = 4.0

print('Median-low = ' + str(stat.median_low(x)))
Median-low = 3

print('Median-high = ' + str(stat.median_high(x)))
Median-high = 5

from sympy import *

x = symbols ('x')

fx = exp(-x)

integrate(fx, (x, 0, oo))
Out[29]: 
1
    ￼
integrate(x*fx, (x, 0, oo))
Out[30]: 
1
    
￼integrate(x**2*fx, (x, 0, oo))
Out[31]: 
2
￼integrate(x**4*fx, (x, 0, oo))
Out[32]: 
24







