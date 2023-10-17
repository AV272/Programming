"""
1) det -- вычисляет определитель матрицы
print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0

2) eig -- вычисляет собственные значения и собственные векторы матрицы
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print vals                                      #Output : [ 3. -1.]
print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]

3) inv -- вычисляет обратную мкатирцу
print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]
"""

import numpy as np

n = int(input())
mx =[]
for i in range(n):
    l = np.array(input().split(), float)
    mx.append(l)
print(round(np.linalg.det(mx),2))
