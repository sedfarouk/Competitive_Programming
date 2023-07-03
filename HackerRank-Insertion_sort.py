# HackerRank - Insertion Sort

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, len(arr)):
        temp_val, loc = arr[i], i
        while loc>0 and arr[loc-1] > temp_val:
            arr[loc] = arr[loc-1]
            print(*arr)
            loc-=1
        arr[loc] = temp_val
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
