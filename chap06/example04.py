'''
정렬 알고리즘
    버블 정렬
    이웃한 두 원소의 대소를 비교해서 교환 -> 하나의 pass
    그 다음으로 큰 (작은) 원소를 나열하기 위해 이웃한 두 원소의 대소를 비교해서 교환 -> 두 번째 pass
'''

from typing import MutableSequence
'''
이번에 버블 정렬을 개선할 방법은
이미 정렬되어 있는 수들은 건너뛰고 정렬하는 것이다.
'''
def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n-1:
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
