#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/one-month-preparation-kit-maxsubarray/problem
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    curr_sum = -math.inf
    best_sum = -math.inf

    for x in arr:
        curr_sum = max(x, curr_sum + x)
        best_sum = max(best_sum, curr_sum)

    non_neg_arr = [x for x in arr if x >= 0]
    if len(non_neg_arr) > 0:
        subarr_summ = sum(non_neg_arr)
    else:
        subarr_summ = max(arr)

    return best_sum, subarr_summ


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
