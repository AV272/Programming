# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:37:30 2020

@author: Алексей
"""

##############################################################################
## Модули

import math

math
Out[2]: <module 'math' (built-in)>

math.pi
Out[3]: 3.141592653589793

## import
# Функция import подключает модуль в код


## Чтобы не писать название модуля каждый раз можно использовать 
# Доступны только указанные функции
from random import uniform, choice

uniform(0,1)
Out[13]: 0.7992587774023948

choice([3,7,234,43])
Out[14]: 234

## Можно экспортировать все функции из модуля, но лучше этого не делать
from random import *

gauss(0,1)
Out[16]: -1.063993696883884



## Можно двать модулям клички (alias)

from random import uniform as uni

uni(0,1)
Out[18]: 0.8462290298994931

import numpy as np

np.arccos(0.5)
Out[20]: 1.0471975511965979


## Модули могут иметь подмодули. Если модуль импортирован, то подмодуль 
# не импортируется автоматически.

 from os.path import abspath

abspath('..')
Out[22]: 'C:\\Users\\Алексей'

import os

os.getcwd()
Out[24]: 'C:\\Users\\Алексей\\.spyder-py3'

import os.path

abspath('..')
Out[26]: 'C:\\Users\\Алексей'

os.path.basename(os.getcwd())
Out[27]: '.spyder-py3'

## Можно задавать несколько модулей одновременно, но не рекомендуется
import os, math, random

## Можно записать так

from math import (
exp,
log,
e,
floor
)

floor(exp(log(e)))
Out[29]: 2













