'''
import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7

Enter:
4 2 # dimentions
1 2
3 4
5 6
7 8

Task:
Compute minimum by axis 1 and print maximum of this array.

'''


import numpy as np

n,m = map(int, input().split())
a =[]
for i in range(n):
    l = np.array(input().split(),int)
    a.append(l)
arr = np.array(a)
print(np.max(np.min(arr, axis=1)))
