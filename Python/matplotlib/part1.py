#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:21:01 2020

@author: lkst
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

fig = plt.figure() # create figure
ax = fig.add_axes([0,0,1,1]) # create axes
print(type(ax))
plt.scatter(1.0, 1.0) # create marker in point
#plt.savefig('example142a.png', fmt='png')

# Polar frame of reference
fig = plt.figure()
ax = fig.add_axes([0,0,1,1], polar=True)
plt.scatter(1.57, 0.3)
#plt.savefig('example142b.png', fmt='png')

plt.show()
