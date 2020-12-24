'''
퀵 정렬 만들기
    앞에서 본 분할 과정을 계속 반복하면 퀵 정렬이 된다.
'''

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    x  = a[(left+right) // 2]

    while pl <= pr:
        while a[pl] < x: pl = pl + 1
        while a[pr] > x: pr = pr - 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl = pl + 1
            pr = pr - 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a)-1)


if __name__ == "__main__":
    print("퀵 정렬을 수행합니다. ")
    num = int(input("원소 수를 입력하세요. : "))
    x   = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]  : '))
    
    quick_sort(x)

    print("오름차 순으로 정렬합니다.")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')