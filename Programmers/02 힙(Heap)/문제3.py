import copy
import heapq
from collections import deque

def solution(operations):
    redefine_operation = []
    operation_stack    = []
    for i1 in operations:
        redefine_operation.append(i1.split())
    del operations
    redefine_operation = deque(redefine_operation)
    
    temp = []
    for i in range(len(redefine_operation)):
        a    = redefine_operation.popleft()

        if a[0] == "I":
            operation_stack.append(int(a[1]))
            temp = copy.deepcopy(operation_stack)

        elif a[0] == "D" and a[1] == "1":
            if len(operation_stack) == 0:
                pass
            else:
                temp  = copy.deepcopy(operation_stack)
                for i in operation_stack:
                    test_heap  = []
                    heapq.heappush(test_heap, (-i,i))
                maxima = int(heapq.heappop(test_heap)[1])
                temp.remove(maxima)
                operation_stack = copy.deepcopy(temp)

                
        elif a[0] == "D" and a[1] == "-1":
            if len(operation_stack) == 0:
                pass
            else:
                temp  = copy.deepcopy(operation_stack)
                heapq.heapify(operation_stack)
                temp.remove(int(heapq.heappop(operation_stack)))

    if len(temp) == 0:
        answer = [0, 0]
    else:
        answer = [max(temp), min(temp)]

    print(answer)
    return answer


def main():
    solution(operations=["I 16","D 1"])
    solution(operations=["I 7","I 5","I -5","D -1"])
    solution(operations=["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
    solution(operations=["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
    solution(operations=["I 1", "I 2", "I 3", "I 4", "D 1", "D 1"])
    solution(operations=["I 1", "I 2", "I 2", "I 3", "I 3", "D 1"])

if __name__ == "__main__":
    main()