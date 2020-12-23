'''
단순 선택 정렬 알고리즘
1. 배열에서 가장 작은 수를 골라서 맨 앞과 교환한다. -> 가장 작은 수 픽, 맨 앞자리 인덱스 픽
2. 두 번째로 가장 작은 수를 골라서 두 번째 인덱스의 수와 교환한다 -> 두 번째로 작은 수 픽, 두 번째 인덱스 픽
'''

from typing import MutableSequence

def selection_sort (a: MutableSequence) -> None:
    n = len(a)
    '''
    1. i가 0 1 2 3 4 순회
    2. 예를 들어서 i가 0인데 이를 일단 min에 할당
    3. j는 1, 2, 3, 4, ... n까지 순회
    4. 이때 임의의 j가 0보다 작다면, 0이 더 큰 셈이므로 자리를 바꾸어야 한다.
    5. 따라서 j를 min에 바꾸고
    6. a[i]와 a[min]을 교환
    '''
    for i in range (n-1):
        min = i # n-1를 순회하면서 현재 인덱스를 min에 할당하고
        for j in range(i+1, n): # i보다 큰 나머지 인덱스들을 모두 순회
            if a[j] < a[min]:   # 해당 인덱스가 a[min]보다 크다면 교환
                min = j
        a[i], a[min] = a[min], a[i]


if __name__ == "__main__":
    print("버블 정렬을 수행")

    num = int(input("원소 수를 입력하세요  "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    

    # 값을 입력한 마구잡이의 랜덤 배열을 삽입
    selection_sort(x)

    print("오름차순으로 정렬 완료")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')