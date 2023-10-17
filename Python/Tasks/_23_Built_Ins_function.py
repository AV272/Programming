# Zip function #############################
'''
>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>> 
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>> 
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>> 
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]

##########################
# any() and all() functions

>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False

>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False
'''

stud, subj = map(int,input().split())

arr = [list(map(float, input().split())) for i in range(subj)]
for i in zip(*arr):
    print(sum(i)/len(i))


##################################
# Athlete sort

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    # Сортируем матрицу arr по функции key, т.е. по столбцу x[k]
    arr.sort(key= lambda x: x[k])
    for i in arr:
        print(*i, sep=' ')
        
        
#############################
# Any and all

n = int(input())
l = input().split() # Создаем лист из строк
# i2==i2[::-1] работает только со строками, т.к. строка интерпритируется как лист
print(all([int(i)>0 for i in l]) and any([i2==i2[::-1] for i2 in l]))

#############################
# Sorting (input: Sorting1234; output: ginortS1324)
s = input()
low = sorted([i for i in s if i.islower()]) # выбираем из строки буквы нижнего регистра
up = sorted([i for i in s if i.isupper()]) # выбираем буквы верхнего регистра
dig = sorted([i for i in s if i.isdigit()]) # числа
even = []
odd = []
for i in dig:
    if int(i)%2 ==0:
        even.append(i)
    else:
        odd.append(i)
print(''.join(low + up + odd +even))
