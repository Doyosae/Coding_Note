'''
정렬 알고리즘
    버블 정렬
    이웃한 두 원소의 대소를 비교해서 교환 -> 하나의 pass
    그 다음으로 큰 (작은) 원소를 나열하기 위해 이웃한 두 원소의 대소를 비교해서 교환 -> 두 번째 pass
'''

from typing import MutableSequence

# 셰이커 정렬
def bubble_sort(a: MutableSequence) -> None:

    '''
    길이 10의 마구잡이 배열이 들어왔다면, left = 0, right = 9, last = 9
    '''
    left  = 0
    right = len(a) - 1
    last  = right

    while left < right:
        '''
        left가 right보다 작을 동안
        1. 9에서 left까지 -1 깍아가며 대소 비교로 교환
        2. 그리고 마지막으로 교환한 인덱스는 left = last
        3. left = 0에서 right까지 왼쪽이 오른쪽보다 크다면 계속 교환
        4. 마지막으로 교환한 인덱스 j를 right에 저장
        5. 이러다가 left > right가 되면 루프 탈출
        '''
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last
        
        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j], a[j-1] = a[j+1], a[j]
                last = j
        
        right = last


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
