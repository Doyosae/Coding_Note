import heapq
from collections import deque

test = []
heapq.heappush(test, 5)
print(test)
heapq.heappush(test, 4)
print(test)
heapq.heappush(test, 3)
print(test)
heapq.heappush(test, 2)
print(test)
heapq.heappush(test, 1)
print(test)

print(heapq.heappop(test))
print(test)