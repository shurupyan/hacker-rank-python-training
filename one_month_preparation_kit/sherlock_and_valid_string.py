#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-valid-string/problem?

from collections import Counter


def isValid(s):
    # Write your code here

    if len(s) == 1:
        return "YES"

    c = Counter(s)
    lst = c.most_common()
    print(lst)
    print(lst[0])
    print(lst[1])
    print(lst[-1])
    if (lst[1][1] == lst[-1][1]) and (lst[0][1] <= lst[1][1] + 1):
        return "YES"

    if (lst[0][1] == lst[-2][1]) and (lst[-1][1] == 1):
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
