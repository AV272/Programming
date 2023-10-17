#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:18:29 2023

@author: lkst
"""

def is_simple_number(x):
    """ Определяет, является ли числом простым.
        x - целое положительное число.    
        Если число простое, то возвращает True,
        а иначе - False.
    """
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor+=1
    
    return True

def factorize_number(x):
    """ Раскладывает число на множители.
        Печатает их на экран.
        x - целое положительное число.
    """
    
    divisor = 2
    while x > 1:
        if x%divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor +=1
        