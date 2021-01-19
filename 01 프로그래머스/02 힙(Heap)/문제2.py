import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key = lambda x: (x[1], x[0])))
    q     = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_time = 0, 0
    # deque([(3, 0), (9, 1), (6, 2)])
    # print(q) == [(3, 0)]
    # heapq.heappush(q, tasks.popleft()) 에서 heappush는 가장 작은 값을 왼쪽에서부터 밀어 넣는다.

    '''
    1. 들어오는 작업 라인을 큐로 만든다. (먼저 들어온 것이 먼저 나간다. deque -> popleft)
    2. deque에서 popleft로 뽑은 것을 heapq에 넣어서 minima root 완전 이진 트리로 구성
        왜 minima root로 구성??? 가장 작은 프로세스 스케줄링부터 나아가야하기 때문
    current_time           = mask(current_time + task_length, task_wait + task_length)
    에서 task_wait이 current_time보다 길면 기다리고 자시고 그냥 누적해야함
    그리고 누적하고 나서 실질적인 토탈 반응 시간
    .........|------------------------------>
    ....|--------------------> c             
    |----------> c                            

    ........._______________________|------------------------------> curreent time = task length1 + task length2 + task length3
    ...._______|--------------------> curreent time = task length1 + task length2 = current time + task length2
    |----------> curreent time = curreent time + task_length1 == 0 + task_length1

    total_time1 = task length1
    total_time2 = total time1 + (task length1 + task length2 - task time1)
    total_time3 = total time2 + (task length1 + task length2 + task length3 - task time2)

    3. 큐에서 가장 작은 작업들을 뽑을 때마다 current_time을 누적하고 task wait를 이용해서 total_time 계산
    '''

    while len(q) > 0:
        task_length, task_wait = heapq.heappop(q)
        current_time           = max(current_time + task_length, task_wait + task_length)
        total_time             = total_time + (current_time - task_wait)

        # 남은 tasks에서 current_time보다 작은 것 대기 시간을 가지는 것들을 모두 heap에 삽입
        # 따라서 남은 것들 중 고른 것을 작은 순대로 힙에 나열
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())

    return total_time // len(jobs) # 이것 역시 나도 공감


def main():
    print(solution([[0, 3], [1, 9], [2, 6]]))

if __name__ == "__main__":
    main()