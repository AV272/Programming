#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:21:55 2023

@author: lkst
"""

import turtle as trtl
from math import sin, pi

trtl.shape('turtle')

R = 50


for i in range(3,10):
    trtl.penup()
    trtl.setpos(R,0)
    trtl.pendown()
    angle = 360/i
    l = 2*R*sin(pi/i)
    trtl.setheading((180-angle)/2)
    for j in range(i):
        trtl.left(angle)
        trtl.forward(l)
        
    R+=50
    
    
     
trtl.exitonclick()
trtl.mainloop()