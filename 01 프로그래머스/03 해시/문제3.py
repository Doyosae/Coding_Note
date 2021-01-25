def solution(clothes):
    clothes_dictionary = {}
    for data1, data2 in clothes:
        if data2 in clothes_dictionary:
            clothes_dictionary[data2] += 1
        else:
            clothes_dictionary[data2] = 1
    
    mul = 1
    for keys in clothes_dictionary.values():
        mul = mul * (keys+1)
    answer = mul - 1

    print(answer)
    return answer

# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt    = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer

'''
1. 각각의 옷에 대해서 하나 씩만 입는 경우
2. 같은 종류는 서로 겹칠 수 없다.
아이디어
    1. 같은 종류의 옷이 몇 개인지 센다.
    2. 각 종류의 옷의 갯수 +1를 해서 누적곱을 한다.
    3. 마지막에는 - 1 (아무것도 안 입는 경우)
'''

def main():
    solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
    solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])

if __name__ == "__main__":
    main()