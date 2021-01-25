def solution(participant, completion):
    hash_map = {}
    hash_val = 0
    for data in participant:
        hash_map[int(hash(data))] = data
        hash_val = hash_val + int(hash(data))
    
    for data in completion:
        hash_val = hash_val - int(hash(data))
    
    answer = hash_map[hash_val]
    print(answer)
    return answer

# def solution(participant, completion):
#     hash_map = []
#     hash_val = 0
#     answer   = 0
#     for data in participant:
#         hash_map.append([int(hash(data)), data])
    
#     for data in completion:
#         for x, y in hash_map:
#             if int(hash(data)) == x:
#                 hash_map.remove([int(hash(data)), data])
        
#     answer = hash_map[0][1]
#     return answer

'''
생각할 수 있는 또 다른 방법
1. 문자열 정렬로 일치하는 것 찾기
2. 해시 맵을 만들어서 해시 값을 누적 시킨 후, 비교 값의 해시 값들을 빼서 남은 거에 대한 키 값 획득
'''

def main():
    solution(["leo", "kiki", "eden"], ["eden", "kiki"])
    solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
    solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

if __name__ == "__main__":
    main()