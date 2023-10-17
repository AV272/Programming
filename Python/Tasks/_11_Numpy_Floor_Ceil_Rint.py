'''
Enter:
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Numpy functions:

numpy.floor() -- return larger integer number wich less then N
numpy.ceil() -- return smallest integer number wich more then N
numpy.rint() -- return nearest to N integer number (if 5.5 return 6.)  
'''


import numpy

numpy.set_printoptions(sign=' ') # need for larger spase between numbers in array (need for sheck in HackerRank)

array = numpy.array(input().split(),float) # base element in numpy is array
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))

