'''
정렬 알고리즘
    버블 정렬
    이웃한 두 원소의 대소를 비교해서 교환 -> 하나의 pass
    그 다음으로 큰 (작은) 원소를 나열하기 위해 이웃한 두 원소의 대소를 비교해서 교환 -> 두 번째 pass

해당 코드는 몇 번 교환이 일어나고 몇 번 비교를 했는지 카운팅하는 것
'''

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0

    n = len(a)
    for i in range (n-1):
        print(f'패스 {i+1}')

        for j in range (n-1, i, -1):
            for m in range (0, n-1):
                print(f'{a[m]:2}' + ('   ' if m != j-1 else '+' if a[j-1] > a[j] else ' -'), end = '')
                ccnt = ccnt + 1
            print(f'{a[n-1]:2}')
            if a[j-1] > a[j]:
                scnt = scnt + 1
                a[j-1], a[j] = a[j], a[j-1]

        for m in range (0, n-1):
            print(f'{a[m]:2}', end = '')
        print(f'{a[n-1]:2}')

    print(f'비교를 {ccnt}번 했습니다')
    print(f'교환을 {scnt}번 해습니다')

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