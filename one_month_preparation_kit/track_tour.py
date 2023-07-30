#!/bin/python3

import math
import os
import random
import re
import sys


#https://www.hackerrank.com/test/4j8jqbol4g4/questions/6sqmn1811gk
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def check_pump(i, ln, pumps):
    tank = 0
    for k in range(ln):
        if i == ln:
            i = 0
        # print(i)
        pump = pumps[i]
        # print(pump)
        tank += pump[0]
        if tank < pump[1]:
            return False
        tank -= pump[1]
        i += 1
    return True


def truckTour(petrolpumps):
    # Write your code here
    ln = len(petrolpumps)
    for i in range(ln):
        # route = petrolpumps[i:ln] + petrolpumps[0:i]
        # route.extend(petrolpumps[0:i])
        # print(route)
        if check_pump(i, ln, petrolpumps):
            return i
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
