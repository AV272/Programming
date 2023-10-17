# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.

change1

"""
print("Hello World!")

import math

math.sin(math.pi/2)  'математические функции'
Out[5]: 1.0

5+8
Out[7]: 13

_
Out[8]: 13

help(math)

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586


7%3 
Out[10]: 1  "возвращает остаток от деления"

7//3
Out[11]: 2  'возвращает целый результат деления с остатком'

math.sin
Out[12]: <function math.sin(x, /)>

math.pi
Out[13]: 3.141592653589793

math.sin(math.pi)
Out[14]: 1.2246467991473532e-16

math.sin(math.pi/2)
Out[15]: 1.0

(1).__add__
Out[16]: <method-wrapper '__add__' of int object at 0x00007FF807959340>

(1).__add__(2)
Out[17]: 3  "замена оператора + его програмным видом"

dir(1)
Out[18]: 
['__abs__',
 '__add__',
 '__and__',
 '__bool__',
 '__ceil__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__divmod__',
 '__doc__',
 '__eq__',
 '__float__',
 '__floor__',
 '__floordiv__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__index__',
 '__init__',
 '__init_subclass__',
 '__int__',
 '__invert__',
 '__le__',
 '__lshift__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__new__',
 '__or__',
 '__pos__',
 '__pow__',
 '__radd__',
 '__rand__',
 '__rdivmod__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rfloordiv__',
 '__rlshift__',
 '__rmod__',
 '__rmul__',
 '__ror__',
 '__round__',
 '__rpow__',
 '__rrshift__',
 '__rshift__',
 '__rsub__',
 '__rtruediv__',
 '__rxor__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__truediv__',
 '__trunc__',
 '__xor__',
 'bit_length',
 'conjugate',
 'denominator',
 'from_bytes',
 'imag',
 'numerator',
 'real',
 'to_bytes']

(4).__sub__(2)
Out[19]: 2  'вычитание'

a=5+7j

b=5+3j

a+b
Out[22]: (10+10j)

(a+b).conjugate()
Out[23]: (10-10j) 'комплексное сопряжение'

a.imag
Out[24]: 7.0

a.real
Out[25]: 5.0

abs(a)  'абсолютное значение комплексного числа' 
Out[26]: 8.602325267042627

math.sqrt(a.real**2+a.imag**2)
Out[27]: 8.602325267042627

int()
Out[28]: 0

float()
Out[29]: 0.0

complex()
Out[30]: 0j

a="bra'"

b="ket"

a+b
Out[33]: "bra'ket"

a+''+b
Out[34]: "bra'ket"

a+'   '+b
Out[35]: "bra'   ket"

a="bra""
  File "<ipython-input-36-7e37a552fbad>", line 1
    a="bra""
            ^
SyntaxError: EOL while scanning string literal




"""one
two
three"""
Out[37]: 'one\ntwo\nthree'

a
Out[38]: "bra'"

10*a
Out[39]: "bra'bra'bra'bra'bra'bra'bra'bra'bra'bra'"

a="bra\""

a
Out[41]: 'bra"'

'A number' + str(55*11)
Out[42]: 'A number605'

'A number  ' + str(55*11)
Out[43]: 'A number  605'

b
Out[44]: 'ket'

b.upper
Out[45]: <function str.upper()>

b.upper()
Out[46]: 'KET'

b.replace('e','EEE')
Out[47]: 'kEEEt'

b
Out[48]: 'ket'

len(b)
Out[49]: 3

len(b.replace('e','EEE'))
Out[50]: 5

c=b.replace('e','EEE')

c
Out[52]: 'kEEEt'

print(a + ' '+b +' ,' +c)
bra" ket ,kEEEt

d='Text: '

d='Text: {0},{1},{2}'    # определяем места-ячейки для текста

print(d.format(a,b,c))
Text: bra",ket,kEEEt

x=6.7

x
Out[58]: 6.7

print(x:.10f)
  File "<ipython-input-59-449721a133a8>", line 1
    print(x:.10f)
           ^
SyntaxError: invalid syntax




print({0:.10f}.format(x))
  File "<ipython-input-60-06ea994a0545>", line 1
    print({0:.10f}.format(x))
                ^
SyntaxError: invalid syntax




print('{0:.10f}'.format(x))
6.7000000000




############################################################
#Последовательности элементов (list)

d=[1,2,3,4,5]

d
Out[63]: [1, 2, 3, 4, 5]

e=[17,'hello',math.sin]

e
Out[65]: [17, 'hello', <function math.sin(x, /)>]

d[3]
Out[66]: 4

d[0]
Out[67]: 1

d[-1]
Out[68]: 5 # Циклическая нумерация от -len до +len

d[-5]
Out[69]: 1

d[99]
Traceback (most recent call last):

  File "<ipython-input-70-928a2da2c7c5>", line 1, in <module>
    d[99]

IndexError: list index out of range




len(d)
Out[71]: 5

d.append(6) 'добавление элемента с конца'

d
Out[73]: [1, 2, 3, 4, 5, 6]

len(d)
Out[74]: 6

del d[-1] 'удаление элемента; номер элементов в последовательности цикличен'

d
Out[76]: [1, 2, 3, 4, 5]

d[1:3]  # Первый включается, последний нет (полуинтервал)
Out[77]: [2, 3]

d
Out[78]: [1, 2, 3, 4, 5]

d[1:0]
Out[79]: []

d[1:5]
Out[80]: [2, 3, 4, 5]

d[1:]
Out[81]: [2, 3, 4, 5]

d
Out[82]: [1, 2, 3, 4, 5]

e=d[1:]

e
Out[84]: [2, 3, 4, 5]

e[:2]=[0,1,2]

e
Out[86]: [0, 1, 2, 4, 5]

e[3:0]=[3]   # Выкинуть 0 элементов начиная с 3-го и заменить их (3)

e
Out[88]: [0, 1, 2, 3, 4, 5]



########################################################################
# Циклы

d
Out[78]: [1, 2, 3, 4, 5]

for i in d:
    print(i)
    
1
2
3
4
5


aa = [6,5,4,3,2,1]
for i in aa:
    print(i)
    
6
5
4
3
2
1


d_copy = d[:]

i=0

for item in d_copy:
    d_copy[i]=2*item
    i += 1
    

d_copy
Out[98]: [2, 4, 6, 8, 10]

a_copy2 =a[:]

d_copy2 =d[:]

for index, item in enumerate(d_copy2): # enumerate присваивает пару чисел 
#первое - номер элемента последовательности, 
#второе - сам элемент последовательности"
    d_copy2[index] = 2*item
    

d_copy2
Out[103]: [2, 4, 6, 8, 10]


a = [6,5,4,3,2,1]
a_double
Out[15]: [12, 10, 8, 6, 4, 2]

for i1,i2 in zip(a,a_double): # Оперируем сразу двумя массивами
    print(i2,i1)
    
12 6
10 5
8 4
6 3
4 2
2 1


list(zip(a,a_double))
Out[18]: [(6, 12), (5, 10), (4, 8), (3, 6), (2, 4), (1, 2)]


for i in range(0,10):   
    print(i)
    
0
1
2
3
4
5
6
7
8
9


for i in range(0,10,2): # Можно задать размер шага
    print(i)
    
0
2
4
6
8


for i1,i2 in zip(range(len(a)),a): # range с одним элементом (0, len(a)) шаг 1
    print(i1,i2)
    
0 6
1 5
2 4
3 3
4 2
5 1


a_double = [2*item for item in a] # цикл можно вставлять внутрь других функций

a_double
Out[5]: [12, 10, 8, 6, 4, 2]


[index*item for index,item in enumerate(a)]
Out[6]: [0, 5, 8, 9, 8, 5]  # можно создавать сложные вложенные конструкции


[[item, item**2] for item in a]
Out[7]: [[6, 36], [5, 25], [4, 16], [3, 9], [2, 4], [1, 1]]


[[item, item**2] for item in a if item%2 ==0]
Out[8]: [[6, 36], [4, 16], [2, 4]]  # можно еще добавить условие


#############################################################################
# Tuples или записи (кортеж). Отличается от последовательности (list) тем,
# что запись нельзя изменить после создания

a= (6,7,8,9)

a
Out[10]: (6, 7, 8, 9)

del a[2]
Traceback (most recent call last):

  File "<ipython-input-11-734682c6a06c>", line 1, in <module>
    del a[2]

TypeError: 'tuple' object doesn't support item deletion



b=(55,'asdf')

b
Out[13]: (55, 'asdf')

c = tuple([65,'yes'])

c
Out[15]: (65, 'yes')



# Вычислить квадрат суммы двух векторов 
sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
    
    
kaon = [3.4, 4.3, 20.0]

pion = [1.4, 0.9, 19.8]


for i1,i2 in zip(kaon,pion):
    print((i1+i2)**2)
    
23.04
27.040000000000003
1584.0399999999997

[(i1+i2)**2 for i1,i2 in zip(kaon,pion)]
Out[29]: [23.04, 27.040000000000003, 1584.0399999999997]

magsq = sum([(i1+i2)**2 for i1,i2 in zip(kaon,pion)])

magsq
Out[31]: 1634.1199999999997

print(magsq**0.5)
40.42425014765271

import math
print(math.sqrt(magsq))
40.42425014765271



###########################################################################
# Dictionary или словари. Элементами словаря могут быть большинство типов данных
# Элементы в словаре неупорядочены, каждому элементу вручную присваивается индекс
# Индексы называются ключами, а объекты которые ключи отображают - значениями.
# Каждая ключ-значение пара называется элементом словаря.


d= {1:0.5, 'll': math.sin, 0.1 : 2}

d['ll']
Out[42]: <function math.sin(x, /)>

d.keys()
Out[48]: dict_keys([1, 'll', 0.1])

d.values()
Out[49]: dict_values([0.5, <built-in function sin>, 2])

d
Out[50]: {1: 0.5, 'll': <function math.sin(x, /)>, 0.1: 2}

for key, value in d.items():
    print(key, ' : ', value)
    
1  :  0.5
ll  :  <built-in function sin>
0.1  :  2

dict(enumerate(['a thing', 'another']))
Out[56]: {0: 'a thing', 1: 'another'}

{i : i**i for i in range(10) if i !=3}
Out[59]: 
{0: 1,
 1: 1,
 2: 4,
 4: 256,
 5: 3125,
 6: 46656,
 7: 823543,
 8: 16777216,
 9: 387420489}


s= "a string"

s.__hash__() # Посмотреть hash-код некоторой переменной

Out[5]: -5521175774378025980


for key in d:
    print(key, ':', d[key])
    
1 : 0.5
ll : <built-in function sin>
0.1 : 2




import string

string.ascii_lowercase
Out[18]: 'abcdefghijklmnopqrstuvwxyz'

for ch in string.ascii_lowercase:
    print(ch)
    
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z

{25-index:item for index,item in enumerate(string.ascii_lowercase)}
Out[25]: 
{25: 'a',
 24: 'b',
 23: 'c',
 22: 'd',
 21: 'e',
 20: 'f',
 19: 'g',
 18: 'h',
 17: 'i',
 16: 'j',
 15: 'k',
 14: 'l',
 13: 'm',
 12: 'n',
 11: 'o',
 10: 'p',
 9: 'q',
 8: 'r',
 7: 's',
 6: 't',
 5: 'u',
 4: 'v',
 3: 'w',
 2: 'x',
 1: 'y',
 0: 'z'}

dd={index:item for index,item in enumerate(string.ascii_lowercase)}

dd
Out[30]: 
{0: 'a',
 1: 'b',
 2: 'c',
 3: 'd',
 4: 'e',
 5: 'f',
 6: 'g',
 7: 'h',
 8: 'i',
 9: 'j',
 10: 'k',
 11: 'l',
 12: 'm',
 13: 'n',
 14: 'o',
 15: 'p',
 16: 'q',
 17: 'r',
 18: 's',
 19: 't',
 20: 'u',
 21: 'v',
 22: 'w',
 23: 'x',
 24: 'y',
 25: 'z'}

rdd = {c:i for i ,c in dd.items()}

rdd
Out[33]: 
{'a': 0,
 'b': 1,
 'c': 2,
 'd': 3,
 'e': 4,
 'f': 5,
 'g': 6,
 'h': 7,
 'i': 8,
 'j': 9,
 'k': 10,
 'l': 11,
 'm': 12,
 'n': 13,
 'o': 14,
 'p': 15,
 'q': 16,
 'r': 17,
 's': 18,
 't': 19,
 'u': 20,
 'v': 21,
 'w': 22,
 'x': 23,
 'y': 24,
 'z': 25}



###############################################################################
## Условия (conditions)

pizzas = ['Pineapple', 'Cheese', 'Pepperoni', 'Hot dog']

for p in pizzas:
    if p == 'Cheese':
        print('Nice pizza!')
    elif p == 'Pepperoni':
        print('Amazing pizza!')
    else:
        print('Weird pizza.')

Weird pizza.
Nice pizza!
Amazing pizza!
Weird pizza.

x = 'ok' if pizzas[2] == "Pepperoni" else 'not ok'

x
Out[39]: 'ok'

x=2

1<x and x<3
Out[41]: True

1<x and x>3
Out[42]: False

1<x or x>3
Out[43]: True

not 1<x
Out[44]: False




x=[1,2]

y=[1,2]

x==y
Out[47]: True

3 in x
Out[48]: False

1 in y
Out[49]: True

z={'a':'b'}

'a' in z
Out[51]: True

'b' in z
Out[52]: False # В словаре оператор in смотрит только на ключи


1 in [[1,2],[3,4]]  # Не работает во вложенных наборах
Out[59]: False

[1,2] in [[1,2],[3,4]]
Out[60]: True

x
Out[65]: [1, 2]

x.__contains__(1)  # Замена для оператора in
Out[66]: True

x.__contains__(2)
Out[67]: True

x.__contains__(3)

Out[68]: False



fact = 'The best hero is Thor' # Строка воспринимается как list

"Thor" in fact
Out[70]: True

"is" in fact
Out[71]: True

"Is" in fact

Out[72]: False

" " in fact
Out[73]: True


if ("Pineapple" in pizzas)== False:
    print('Weird')

if not "Pineapple" in pizzas:
    print('Not Weird')
    

if ("Pineapple" in pizzas)== True:
    print('Weird')
    
Weird


'Pineapple' not in pizzas
Out[78]: False

favourite = None
for p in pizzas:
    if 'Olives' in p:
        favourite = p

if favourite:
    print ('Found favourite: {0}'.format(favourite))
else:
    print ('No favourite :(')
    
No favourite :(
        

        

###############################################################################
# Conditions in loops
        
not_cheesy = [p for p in pizzas if 'cheese' not in p.lower()]

not_cheesy
Out[85]: ['Pineapple', 'Pepperoni', 'Hot dog']        


i = 5
while i > 0:
    print( 'T-minus {0} seconds'.format(i))
    # Equivalent to `i = i - 1`
    i -= 1
print ('Blast off!')
T-minus 5 seconds
T-minus 4 seconds
T-minus 3 seconds
T-minus 2 seconds
T-minus 1 seconds
Blast off!



i = 5
while i > 0:
    print('All work and no play makes Jack a dull boy')


ok=False

i=0

 while not ok:
    ok = 'cheese' in pizzas[i].lower()
    i+=1

i
Out[102]: 2

pizzas[i-1]
Out[103]: 'Cheese'



for pizza in pizzas:
    if 'cheese' in pizza.lower():
        print(pizza)
        break
        
Cheese


###############################################################################
# Methods
############################################################

# Create the function. Задаем коментарий в ''' '''. 
def length(obj):
    ''' Return the number of elements in obj.
    obj must be iterable'''
    i=0
    for _ in obj:
        i += 1
    return i
    

length
Out[16]: <function __main__.length(obj)>

help(length)
Help on function length in module __main__:

length(obj)
    Return the number of elements in obj.
    obj must be iterable


length('A b c!')
Out[18]: 6

length(range(13))
Out[19]: 13


## Функция со многими переменными
def add(x,y,show):
    '''Return sum of arguments
    Optionally return result of this sum'''
    if show:
        print(x+y)
    return x+y
    

add(5,3)
Traceback (most recent call last):

  File "<ipython-input-24-9a2ff24c5fc7>", line 1, in <module>
    add(5,3)

TypeError: add() missing 1 required positional argument: 'show'


add(5,3,False)
Out[26]: 8

add(5,3,True)
8
Out[27]: 8

_ = add(3,4)
Traceback (most recent call last):

  File "<ipython-input-28-1e5d63b86d47>", line 1, in <module>
    _ = add(3,4)

TypeError: add() missing 1 required positional argument: 'show'



_ = add(3,4, True)
7

_ = add(3,4, show=True)
7

def make_incrementor(increment):
    def func(var):
        return var + increment
    return func
    

make_incrementor(10)
Out[32]: <function __main__.make_incrementor.<locals>.func(var)>

make_incrementor(10)(33)
Out[33]: 43

## (*args) помещает все элементы в args в кортеж. 
def total(*args):
    """Return the sum of the arguments"""
    print('Got {0} arguments: {1}'.format(len(args),args))
    return sum(args)
    

total(1)
Got 1 arguments: (1,)
Out[35]: 1

total(1,2)
Got 2 arguments: (1, 2)
Out[36]: 3

total(1,2,3)
Got 3 arguments: (1, 2, 3)
Out[37]: 6


##############################################################################
# Inline methods


## Функция map применяет функцию к каждому элементу последовательности
## и возвращает объект поддерживающий итерации, а не список. Для того чтобы 
## перевести в список используем функцию list.

list(map(str, range(5)))
Out[15]: ['0', '1', '2', '3', '4']


## Для простых операций существует функция (lambda arg: expression) 
## автоматически возвращает результат выражения на аргумент
## 
list(map(lambda x: x*x*x, range(5)))
Out[16]: [0, 1, 8, 27, 64]

div2 = lambda x: x/2

div2
Out[12]: <function __main__.<lambda>(x)>

map(div2,range(5))
Out[13]: <map at 0xf5684d74a8>

print(list(map(div2,range(5))))
[0.0, 0.5, 1.0, 1.5, 2.0]

sqrt = lambda x: x**0.5

sqrt(sum(map(lambda x: x*x, range(10))))
Out[22]: 16.881943016134134

sqrt(sum(map(lambda x: x*x, range(2))))
Out[23]: 1.0

range(2)
Out[24]: range(0, 2)

list(range(2))
Out[25]: [0, 1]

sqrt(sum(map(lambda x: x*x, range(3))))
Out[26]: 2.23606797749979

5**0.5
Out[27]: 2.23606797749979

## Функция filter возвращает элементы последовательности для которых функция 
## возвращает истину 


## Извлечение четных чисел из последовательности

list(filter(lambda x: x%2 == 0, range(10)))
Out[33]: [0, 2, 4, 6, 8]


[i for i in range(10) if i%2 ==0]
Out[36]: [0, 2, 4, 6, 8]

b=[]

for i in range(10):
    if i%2 ==0:
        b.append(i)
        
b
Out[39]: [0, 2, 4, 6, 8]



















































