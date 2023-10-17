'''
import numpy

# Reverce numpy array
reversed_arr = numpy.flipud(data)

# Find the shape of array
my__1D_array = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape     #(5,) -> 5 rows and 0 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns 

# Changing shape of array 
change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print change_array      

#Output
[[1 2]
[3 4]
[5 6]]

my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))

#Output
[[1 2]
[3 4]
[5 6]]

# Transposition of the array
my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]]

# Copy array to the one dimention
my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()

#Output
[1 2 3 4 5 6]

# Bring together few arrays into 1D
array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]

'''

import numpy

arr = input().split(' ')
x = numpy.array(arr, int)
print(numpy.reshape(x,(3,3)))


import numpy

n,m,p = map(int, input().split())
l1 =[]
l2 =[]
for i in range(n):
    x1 = numpy.array(input().split(), int)
    l1.append(x1)
arr1 = numpy.array(l1)
for i in range(m):
    x2 = numpy.array(input().split(), int)
    l2.append(x2)
arr2 = numpy.array(l2)

print(numpy.concatenate((arr1, arr2), axis=0))

# same
import numpy
n,m,p = map(input().split(),int)
arr1 = numpy.array([input().split() for i in range(n)],int)
arr2 = numpy.array([input().split() for i in range(m)],int)
print(numpy.concatenate((arr1, arr2), axis=0))
