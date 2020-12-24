from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    '''
    1. 무작위 어레이를 배열 받고 나서
    2. 배열 어레이 a의 길이는 n
    부모 : a[(i-1) // 2]
    왼쪽 : a[2*i + 1]
    우측 : a[2*1 + 2]
    '''
    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        # down_heap(a, i, n-1) -> down_heap(a, left, right)
        temp   = a[left]
        parent = left

        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl

            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent    = child
        a[parent] = temp


    n = len(a)

    '''
    a[i]부터 a[n-1]까지 힙으로 만들기
    가정) n = 10이라면
    for i in range (9//2, -1, -1): --> 4에서부터 -1씩 깍으며 4, 3, 2, 1, 0 순으로 내려간다.
    1. i = 5에서 down_heap(a, 4, 9)
        temp   = a[4] # (n-1)//2 가 parent를 가리킴
        parent = left
        
        while parent < (right+1) // 2이면:
            cl = parnet * 2 + 1 --> 왼쪽 자시
            cr = cl + 1         --> 오른쪽
            만약에 a[cr] > a[cl]이면 a[오른쪽] 자식이 더 큰 셈이므로 child = cr에 할당
            만약에 a[cr] < a[cl]이면 a[왼쪽] 자식이 더 큰 셈이므로 child = cl에 할당

            그렇지만 부모가 큰 자식 값보다 크면 부모 > 큰 자식 > 작은 자식
                Heap으로 바꾸어야 할 필요가 없으므로 break

            그렇지 않다면, 즉 부모가 자식 노드보다 작으면... Heap으로 정렬 해주어야 한다.
            a[부모 인덱스]에 a[큰 자식 인덱스] 값을 할당하고
            a[큰 자식 인덱스]에 temp (원래 부모의 값을 할당) 해서 서로 위치를 바꾸어준다.
    
    --> 이 과정을 i 마다 반복 하는 것 이렇게 해서 무작위 어레이를 Heap으로 바꾼다.
    '''
    for i in range((n-1) // 2, -1, -1):
        down_heap(a, i, n-1)
    

    '''
    최댓값인 a[0]와 마지막 원소를 교환
    a[0] ~ a[i-1]를 힙으로 만들기
    
    Heap으로 정렬된 tree를 이제
    1. 맨 앞 원소가 가장 꼭대기에 있는 parent이고, 맨 뒤의 자식 노드와 위치 교환
    2. 맨 뒤로 옮겨간 가장 큰 parent를 제외하고 (즉, a, 0, i-1)으로 남은 tree끼리 다시 Heap 정렬
    3. 과정을 반복하면 서서히 작은 값부터 큰 값으로 정렬된다.
    '''
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)

if __name__ == "__main__":
    print("힙 정렬을 수행합니다. ")
    num = int(input("원소 수를 입력하세요. "))
    x   = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    heap_sort(x)

    print("오름차순으로 정렬하세요. ")
    for i in range(num):
        print(f'x[{i}]  = {x[i]}')