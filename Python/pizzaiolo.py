# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 22:16:39 2019

@author: Алексей
"""

import sys  ## модуль позволяет добавлять аргументы из командной строки как 
## свойство argv 
import time

def make_pizza(*toppings):  # Определяем переменную
    ''' Make a delicious pizza from the toppings'''
    print('Making pizza ...')
    for t in toppings:
        print('Adding {0}'.format(t))
        time.sleep(1) # Задержка на 1 секунду
    print('Done!')
    return 'Pizza with toppings: {0}'.format(toppings)

#print('sys.argv:', sys.argv)
#toppings = sys.argv[1:]
#pizza = make_pizza(*toppings)

arguments = sys.argv[1:] # Записывает введенные через командную строку 
# аргументы в переменную arguments

if '--help' in arguments:
    print('Make a pizza.')
    print('Usage: pizzaiolo.py topping1 topping2 ...')
    sys.exit() # Выход из программы

if '--verbose' in arguments:
    verbose = True
    # We don't want the flag passed as a topping! Убираем из аргументов
    arguments.remove('--verbose') 
else:
    verbose = False

if verbose:
    print('About to call make_pizza')
pizza = make_pizza(*arguments)
if verbose:
    print('Finished')

#pizza = make_pizza('cheese','olives')



