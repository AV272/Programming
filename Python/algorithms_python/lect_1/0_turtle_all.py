#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:21:52 2023

@author: lkst
"""

import turtle

# Five
turtle.shape('turtle')

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

turtle.exitonclick()
turtle.mainloop()

#Square
turtle.shape('turtle')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# Circle
for i in range(360):
    turtle.forward(2)
    turtle.left(1)
    
#Inserted squares
l = 10
x = 0
y = 0

for i in range(10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    
    l+=10
    x-=5
    y-=5
    
#Spyder
n = 12
l = 100
angle = 360/n

for i in range(n):
    turtle.forward(l)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(l)
    turtle.left(180)
    turtle.left(angle)
    
# Spiral
for i in range(1000):
    r = i / 10 * pi
    dx = r*cos(r/5)
    dy = r*sin(r/5)
    turtle.goto(dx, dy)

# for i in range(1000):
#     turtle.forward(i * 0.001)
#     turtle.left(1)


#Square spiral
l=10

for i in range(100):
    trtl.forward(l)
    trtl.left(90)
    l+=10

