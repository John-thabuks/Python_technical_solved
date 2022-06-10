'''
Given an array of integers, find the sum of its elements.
for example, if the array 
    ar = [1,2,3] 1+2+3 = 6
        so return 6
Function description
    complete the simpleArraySum function.
    It must return the sum of the array elements as an iteger
    simpleArraySum has the following parameters
        ar: an array integers

input format:
the first line contains an integer, n denotinng the size of the array.
the second line contains n space separeted integers representing the array's eleents

'''

import os
import sys
from unittest import result

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result)+ '\n')
    fptr.close()