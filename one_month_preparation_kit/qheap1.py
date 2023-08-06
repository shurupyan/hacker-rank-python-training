# Enter your code here. Read input from STDIN. Print output to STDOUT
from heapq import heappush, heappop
s = input()

heap = []
del_heap = []
for i in range(int(s)):
    s = input()

    cmd = list(map(int, s.split()))
    if cmd[0] == 1:
        heappush(heap, cmd[1])

    if cmd[0] == 2:
        heappush(del_heap, cmd[1])

    if cmd[0] == 3:
        while del_heap and del_heap[0] == heap[0]:
            heappop(del_heap)
            heappop(heap)
        print(heap[0])
