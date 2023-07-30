#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#
import sys


def bigSorting(unsorted):
# Write your code here
    sys.set_int_max_str_digits(1000000)
    return sorted(unsorted, key=int)