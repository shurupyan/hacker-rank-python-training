#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#
from bisect import bisect, bisect_left


def hackerlandRadioTransmitters(x, k):
    x.sort()
    radio_houses = []
    leftmost_house_id = 0

    while leftmost_house_id < len(x):
        print(leftmost_house_id)
        print(f"x[leftmost_house_id]: {x[leftmost_house_id]}")
        range_center = x[leftmost_house_id] + k
        print(f"range_center: {range_center}")
        radio_id = bisect(x, range_center)
        print(f"radio_id: {radio_id}")
        radio_houses.append(x[radio_id - 1])

        leftmost_house_id = bisect(x, radio_houses[-1] + k)
        print(leftmost_house_id)
        print("----")
    return len(radio_houses)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
