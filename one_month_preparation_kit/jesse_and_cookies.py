#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/one-month-preparation-kit-jesse-and-cookies/problem
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
from heapq import heappush, heappop, heapify


def cookies(k, A):
    # Write your code here
    heapify(A)

    iters = 0
    while A[0] < k:
        if len(A) == 1:
            return -1
        new_cookie = heappop(A) + heappop(A) * 2
        heappush(A, new_cookie)
        iters += 1
    return iters


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
