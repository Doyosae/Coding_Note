from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        '''
        배열 a가 들어오고 init left = 0, init right = n-1이다.
            left < right이다.
                center는 left, right의 중간값이다.
                    다시 recursive하게 호출한다.
                        앞 부분은 left, center ~ 뒷 부분은 center+1, right
                            다시 recursive하게 호출한다.
                                앞 부분은 (left, (left+center)//2)와 ((left+center)//2 + 1, center)로 쪼개진다.
                                뒷 부분은 (center+1, (center+right)//2)와 ((center_right)//2 + 1, right)로 쪼개진다.

        
        이제 입력에 대해서 left < right이면
        p = j = 0, i = k = left로 선언하고 p와 j는 buff의 인덱스
        '''
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center+1, right)

            p = j = 0    # ?
            i = k = left # ?

            '''
            여기로 넘어오는 시점에서 이미 배열 a의 앞부분과 뒷부분은 모두 정렬된 것임
            이제 배열 a의 앞부분을 buff에 복사하고
                배열 a의 뒷부분과 buff의 배열a를 a에 덮어 씌우는 것
            '''
            while i < center:
                buff[p] = a[i]
                p += 1
                i += 1
            
            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

            
    n    = len(a)
    buff = [None] * n
    '''
    여기서 첫 시작
    '''
    _merge_sort(a, 0, n-1)

    del buff

if __name__ == "__main__":
    print("병합 정렬을 수행합니다. ")
    num = int(input("원소 수를 입력하세요. "))
    x   = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    merge_sort(x)

    print("오름차순으로 정렬했습니다. ")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
