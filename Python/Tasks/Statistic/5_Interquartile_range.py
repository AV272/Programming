import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    i3 = 0
    for i in freqs:
        for i2 in range(i-1):
            values.append(values[i3])
        i3=i3+1
    valsort = sorted(values)
    n2 = len(valsort)
    if n2%2 == 0:
        n3 = int(n2/2)
        if n3%2 == 0:
            q1 = (valsort[int(n3/2)-1]+valsort[int(n3/2)])/2
            q3 = (valsort[int(n3/2)-1+n3]+valsort[int(n3/2)+n3])/2
        else:
            q1 = valsort[int((n3-1)/2)]
            q3 = valsort[int((n3-1)/2) + n3]
    else:
        n4 = int((n2-1)/2)
        if n4%2 == 0:
            q1 = (valsort[int(n4/2)-1]+valsort[int(n4/2)])/2
            q3 = (valsort[int(n4/2)+n4]+valsort[int(n4/2)+1+n4])/2
        else:
            q1 = valsort[int((n4-1)/2)]
            q3 = valsort[int((n4-1)/2) + 1+ n4]
    print(round(float(q3-q1),1))
    return(round(float(q3-q1),1))
            
    

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
