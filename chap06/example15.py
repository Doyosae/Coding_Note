'''
퀵 정렬의 시간 복잡도는 분할 정복법이므로 O(nlogn)이다.
1. 원소 수가 9 이하이면 단순 삽입 정렬이 유리
2. 원소 수가 9보다 크면, Pivot을 잘 잡는다. 책의 교재를 참고
'''

from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: 
        a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
    
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    for i in range(left+1, right+1):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1] # a[j-1]이 a[i]인 a[j]보다 크므로 뒤로 보내야 한다.
            j = j - 1     # j를 1깍고 0보다 작아지만 while loop 빠져나옴

        a[j] = tmp
    
def qsort(a: MutableSequence, left: int, right: int) -> None:
    '''
    1. 원소 수가 9 이하이면 단순 삽입 정렬
    2. 원소 수가 9보다 크면 퀵 정렬
    '''

    if right-left < 9:
        insertion_sort(a, left, right)

    else:
        pl = left
        pr = right
        m  = sort3(a, pl, (pl + pr) // 2, pr)

        a[m], a[pr - 1] = a[pr - 1], a[m]
        pl = pl + 1
        pr = pr - 2
        while pl <= pr:
            while a[pl] < x: pl = pl + 1
            while a[pr] > x: pr = pr - 1

            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl = pl + 1
                pr = pr - 1
            
        if left < pr: qsort(a, left, pr)
        if right > pl: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a) - 1)

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