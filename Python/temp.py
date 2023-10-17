# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
print("Hello World!")

math.sin(math.pi/2)
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
Out[10]: 1

7//3
Out[11]: 2

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
Out[17]: 3

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
Out[19]: 2

a=5+7j

b=5+3j

a+b
Out[22]: (10+10j)

(a+b).conjugate()
Out[23]: (10-10j)

a.imag
Out[24]: 7.0

a.real
Out[25]: 5.0

abs(a)
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

d='Text: {0},{1},{2}'

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

d=[1,2,3,4,5]

d
Out[63]: [1, 2, 3, 4, 5]