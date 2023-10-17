# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:02:36 2020

@author: Алексей

Задача: написать функцию трех аргументов - два числа и операция над ними. 
Операции + - * /. Если что-то другое - вывести сообщение "Неизвестная операция"

"""
def arithmetic(x,y,z):
    if type(x) != int and type(x) != float:
        return "Первый аргумент не число"
    elif type(y) != int and type(y) != float:
        return "Второй аргумент не число"
    
    if z == '+':
        return x+y
    elif z == '-':
        return x-y
    elif z == '*':
        return x*y
    elif z == '/':
        return x/y
    else: 
        return 'Неизвестная операция'
    

