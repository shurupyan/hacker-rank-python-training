#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER k
# 2. INTEGER_ARRAY arr
#
def pairs(k, arr):
    # Write your code here
    arr.sort()
    cnt = 0
    arr1 = arr.copy()
    for i, v in enumerate(arr):
        try:
            ind = arr1.index(v + k)
            cnt += 1
            del arr1[ind]
        except ValueError:
            print(arr1)
        if not arr1:
            break

    return cnt