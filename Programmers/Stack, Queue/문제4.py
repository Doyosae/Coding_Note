# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     '''
#     순서대로 트럭 무게가 리스트 truck_weights에서 대기 (맨 앞에서 트럭을 뽑음)
#     다리가 견딜 수 있는 무게는 weight, 다리의 길이는 bridge_length
#         1. 트럭이 다리에서 한 칸을 지나갈 때마다 time = time + 1
#         2. 다리 위 트럭 무게의 합이 weight보다 크면 안된다. 이 부분 체크하고 time = time + 1
#     1. 다리 위에 1대만 지나갈 수 있으면 다리 길이 + 1초
#     2. 다리 위에 2대만 지나갈 수 있으면 다리 길이 + 2대(초) 2대는 빠져나가는 시간
#     '''
#     truck_weights = deque(truck_weights)
#     temp   = []
#     answer = 0
#     count  = 0
#     while len(truck_weights) > 0:
#         print("0  ", temp, truck_weights)
#         temp.append(truck_weights.popleft())
#         # print("1  ", temp, truck_weights)
#         if sum(temp) > weight:
#             res = temp.pop()
#             truck_weights.extendleft([res])
#             answer = answer + bridge_length + len(temp) - 1
#             # print("시간", answer)
#             temp = []

#         if len(truck_weights) == 0:
#             answer = answer + bridge_length + len(temp)

#     return answer

def solution(bridge_length, weight, truck_weights):
    temp = [0]*bridge_length # 다리 길이만큼 [000000] 을 설정
    sec  = 0                 # 시간 0초 초기화
    
    while temp:
        sec = sec + 1
        temp.pop(0) # 시간이 1초 지날 때마다 맨 앞의 원소를 뺌
        if truck_weights: # 트럭이 있다면
            if sum(temp) + truck_weights[0] <= weight:
                # 다리 위와 대기 중인 트럭의 맨 앞 트럭 무게 합이
                # 제한 중량보다 작으면 대기 중인 트럭 뽑아서 q에 삽입
                temp.append(truck_weights.pop(0))
            else:
                # 그렇지 않으면 대기 시키고, 다리는 진행
                temp.append(0)
    return sec

def main():
    answer = solution(2, 10, [7,4,5,6])
    print(answer)

    answer = solution(100, 100, [10])
    print(answer)

    answer = solution(100, 100, [10,10,10,10,10,10,10,10,10,10])
    print(answer)

if __name__ == "__main__":
    main()