'''
정렬 알고리즘
    버블 정렬
    이웃한 두 원소의 대소를 비교해서 교환 -> 하나의 pass
    그 다음으로 큰 (작은) 원소를 나열하기 위해 이웃한 두 원소의 대소를 비교해서 교환 -> 두 번째 pass

이번에 버블 정렬을 개선할 방법은
이미 정렬되어 있는 수들은 건너뛰고 정렬하는 것이다.
'''

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n-1:
        '''
        1. k = 0인데, n-1보다 작을 동안
        2. n-1을 last에 끼우고, 최초 루프는 (n-1, 0, -1) 전체를 탐색해서 버블 정렬
        3. 조건에 맞게 j-1이 j보다 크면 이 둘을 교환하고 교환할 때마다 인덱스 j를 last에 대입
        4. 교환이 다 끝나면 마지막으로 교환한 부분을 k에 저장
        5. 다시 (n-1, k, -1)으로 순회 시작
        6. 이렇게 하면 0, 1, 2, ... k 사이의 이미 정렬된 숫자들은 탐색 안해도 된다.
        '''
        last = n-1
        for j in range (n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        
        k = last

if __name__ == "__main__":
    print("버블 정렬을 수행")

    num = int(input("원소 수를 입력하세요  "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    

    # 값을 입력한 마구잡이의 랜덤 배열을 삽입
    bubble_sort(x)

    print("오름차순으로 정렬 완료")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
