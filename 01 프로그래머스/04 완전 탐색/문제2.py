from itertools import permutations
from itertools import combinations
import math

def check(number):
    k = math.sqrt(number)
    if number < 2:
        return False
    for i in range (2, int(k)+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    '''
    a = permutations(list(numbers), 2)
    print(a)
    a = list(map(''.join, a))
    print(a)
    '''
    for k in range(1, len(numbers) + 1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        # 1부터 len(number) + 1까지 모든 조합 만들어주고 (여기까지는 나와 동일)
        # 아직까지는 중복 고려하지 않음
        for i in list(set(perlist)): # 이제 n개 조합으로 구한 리스트마다 중복을 없애고 원소를 순회
            # 해당 원소가 소수라면
            if check(int(i)):
                
                # answer에 int 형으로 삽입, 이때 저장할때 000011도 11로, 011도 11로 해서 n permutation에 의한 중복을 만듬
                answer.append(int(i))

    # 인위로 만든 중복에 set을 주어서 다시 중복 생략
    answer = len(set(answer))
    return answer

def main():
    solution("17")
    solution("011")

if __name__ == "__main__":
    main()