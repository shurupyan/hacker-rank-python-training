#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/one-month-preparation-kit-equal-stacks/problem?
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def get_highest(h_lst):
    return sorted(h_lst, key=sum)


def check_equal(h_lst):
    return sum(h_lst[0]) == sum(h_lst[1]) == sum(h_lst[2])


def equalStacks(h1, h2, h3):
    # Write your code here
    h_list = [h1, h2, h3]
    # print(get_highest(h_list))
    # print(check_equal(h_list))

    while not check_equal(h_list):
        h_list = get_highest(h_list)
        # print(h_list)
        h_list[2].pop(0)
        # print(h_list[2])

    return sum(h_list[2])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
