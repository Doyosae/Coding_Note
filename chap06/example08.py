'''
단순 삽입 정렬 알고리즘
1. 주어진 숫자 배열이 있다.
2. 주목하는 숫자보다 빠른 인덱스의 적절한 위치에 주목한 숫자를 삽입한다.
3. 종료 조건은 정렬된 배열의 왼쪽 끝에 도달한 경우 or tmp보다 작거나 같은 a[j-1]을 발견한 경우

'''

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    '''
    1. 
    '''
    for i in range (1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j = j - 1
        
        a[j] = tmp

if __name__ == "__main__":
    print("단순 삽입 정렬을 수행  ")
    num = int(input("원소 수를 삽입하세요. :  "))
    x = [None] * num
    for in range(num):
        x[i] = int(input(f'x[{i}]:  '))
    
    insertion_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')