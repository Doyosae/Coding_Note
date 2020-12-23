'''
정렬 알고리즘
    버블 정렬
    이웃한 두 원소의 대소를 비교해서 교환 -> 하나의 pass
    그 다음으로 큰 (작은) 원소를 나열하기 위해 이웃한 두 원소의 대소를 비교해서 교환 -> 두 번째 pass

해당 코드는 정렬하다가 더 이상 교환이 일어나지 않을 수 잇으면 아예 소팅을 멈추는 것
'''

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range (n-1):
        exchange = 0
        for j in range (n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchange = exchange + 1 # 교환이 일어났으면 교환 횟수에 1 더하기
        if exchange == 0:
            break


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
