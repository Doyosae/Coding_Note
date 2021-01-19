import heapq

'''힙큐 풀이'''
def solution(scoville, K):
    answer   = 0
    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)

        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        answer = answer + 1

    return answer

# from collections import deque

# def solution(scoville, K):
#     answer = 0

#     while len(scoville) > 0:
#         scoville = deque(scoville)
#         v1 = scoville.popleft()

#         if v1 > K:
#             break
#         if len(scoville) == 0:
#             return -1

#         v2 = scoville.popleft()
#         scoville.appendleft(v1 + v2*2)
#         answer = answer + 1

#         scoville = list(scoville)
#         scoville.sort()

#     print(scoville, answer)
    
#     return answer


def main():
    solution([1, 2, 3, 9, 10, 12], 7)

if __name__ == "__main__":
    main()