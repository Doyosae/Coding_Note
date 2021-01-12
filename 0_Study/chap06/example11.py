'''
셸 정렬
    1. 삽입 정렬은 어레이가 거의 정렬되지 않고 원소 간 거리가 멀면 계산 비용이 크다.
    2. 따라서 2^n 단위로 대강 정리 한 번 씩 해주고 마지막에 단순 삽입 정렬

사실 h 값을 어떻게 정의하냐에 따라 효율성이 결정되는데,
h를 121, 40, 13, 4, 1 순으로 정리하면 효율적으로 정렬 가능
'''

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = 1
    while h < n//9:
        h = h * 3 +1
    
    while h>0:
        for i in range(h, n):
            j = i - h # 8을 2로 나눈 h = 4, 따라서 4부터 8까지 4, 5, 6, 7에 해당하는 j는 0, 1, 2, 3
            tmp = a[i]
            while j>=0 and a[j] > tmp:
                a[j+h] = a[j] # 앞 값이 뒷 값 보다 크면 앞 값을 뒷 값에 대입하고
                j = j-h
            a[j+h] = tmp # 앞 값에 tmp를 대입 (서로 순서 바꾸기 완료)

        h = h//3


if __name__ == "__main__":
    print("셀 정렬을 수행합니다 ")
    num = int(input("원소 수를 입력하세요. "))
    x   = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:  '))
    shell_sort(x)

    print("오름차순으로 정렬합니다. ")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')