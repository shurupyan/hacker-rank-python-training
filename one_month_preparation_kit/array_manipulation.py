#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/one-month-preparation-kit-crush/problem
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
from itertools import accumulate


def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n + 1)

    for q in queries:
        # print(arr)
        s = q[0] - 1
        e = q[1]
        v = q[2]

        arr[s] += v
        arr[e] -= v

        # print(arr)
        # print("---------------")
    return max(accumulate(arr))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
