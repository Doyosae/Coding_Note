import heapq
'''
[[0, 3], [1, 9], [2, 6]]
[[0, 3], [2, 6], [1, 9]]
3 + (3+6)-2 + (3+6+9)-1 = 3 + 7 + 15
sum
'''

def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    # 시작시간 초기화
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                # 작업 소요시간으로 min heap을 만들기 위해 (t, s) 푸시
                heapq.heappush(heap, (t, s))
        
        print(heap)


def main():
    solution([[0, 3], [1, 9], [2, 6]])

if __name__ == "__main__":
    main()