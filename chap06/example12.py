'''
1. 퀵 정렬
    1. 어레이에서 피벗을 정하고, 피벗보다 작은 값은 앞에, 피벗보다 큰 값은 뒤에 배열
    2. 맨 앞, 맨 뒤에서 탐색하면서 큰 값, 작은 값 만날 때마다 자리 교환
'''

from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    n = len(a)
    pl = 0          # 왼쪽 커서
    pr = n-1        # 오른쪽 커서
    x  = a[n//2]    # 가운데 피벗

    while pl <= pr:
        while a[pl] < x: pl = pl+1 # a[pl]이 x보다 작으면 커서 한 칸 이동
        while a[pr] > x: pr = pr-1 # a[pr]이 x보다 크면 커서 한 칸 이동

        '''
        a[pl] > x인 경우와 a[pr] < x인 경우가 빠져나옴
        이때 pl <= pr이면 자리를 바꾸는 것이 마땅
        자리를 교환하고 빠져나옴
        '''
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl = pl + 1
            pr = pr - 1

    print(f'피벗은 {x}입니다. ')
    print('피벗 이하인 그룹입니다. ')
    print(*a[0 : pl])

    if pl > pr + 1:
        print("피벗과 일치하는 그룹입니다.")
        print(*a[pr + 1 : pl])

    print('피벗 이상인 그룹입니다.')
    print(*a[pr + 1 : n])

if __name__ == "__main__":
    print("배열을 나눕니다. ")
    num = int(input('원소 수를 입력하세요: '))
    x   = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:  '))
    
    partition(x)