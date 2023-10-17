# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:27:50 2019

@author: Алексей
"""

import argparse # Модуль автоматически определяющий и записывающий
# введенные в sys.argv аргументы 
import sys
import time


def make_pizza(*toppings):
    """Make a delicious pizza from the toppings."""
    print('Making pizza...')
    for topping in toppings:
        print('Adding {0}'.format(topping))
        time.sleep(1)
    print('Done!')
    return 'Pizza with toppings: {0}'.format(toppings)


parser = argparse.ArgumentParser(description='Make a pizza')
# Добавляем аргументы из toppings, nargs='+' показывает что аргументы могут
# быть указаны несколько раз 
parser.add_argument('toppings', nargs='+',
                    help='Toppings to put on the pizza.')
# Добавляем флаг '--verbose', указываем сокращение флага '-v'
parser.add_argument('--verbose', '-v', action='store_true',
                    help='Print more information whilst making.')
arguments = parser.parse_args()

if arguments.verbose:
    print('About to call make_pizza')
make_pizza(*arguments.toppings)
if arguments.verbose:
    print ('Finished')