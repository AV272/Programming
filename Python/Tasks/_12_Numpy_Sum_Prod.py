'''
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24

Enter:
2 2 # dimentions of array
1 2 # first line
3 4 # second line

Task:
Read the array.
Compute sum of array on axis 0.
Then print the product of that sum.

'''


import numpy

n,m = map(int,input().split())
a = []
for i in range(n):
    line = numpy.array(input().split(),int)
    a.append(line)
arr = numpy.array(a)
print(numpy.prod(numpy.sum(arr,axis =0)))
