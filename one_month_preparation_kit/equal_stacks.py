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

def get_highest_idx(h_list):
    highest = max(h_list)
    return h_list.index(highest)


def equalStacks(h1, h2, h3):
    # Write your code here
    stacks = [h1, h2, h3]
    h_list = list(map(sum, stacks))

    # print(h_list)
    # print(get_highest_idx(h_list))

    while not (h_list[0] == h_list[1] == h_list[2]):
        i = get_highest_idx(h_list)
        h_list[i] -= stacks[i].pop(0)
        # print(h_list)

    return h_list[0]


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
