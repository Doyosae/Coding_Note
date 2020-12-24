'''
병합 정렬

'''

from typing import Sequence, MutableSequence

def merge_sorted (a: Sequence, b: Sequence, c: MutableSequence) -> None:
    pa, pb, pc = 0, 0, 0
    na, nb, nc = len(a), len(b), len(c)

    '''
    pa가 na보다 작고, pb가 nb보다 작아야 루프문을 도는 의미가 있음
    이 조건에서 a[pa]가 b[pb]보다 작으면 c[pc]에 a[pa]를 삽입하고 pa는 1 더한다. pb는 유지한다.
    만약 그 반대라며 c[pc] = b[pb]를 삽입하고 pb를 1 더한다.
    그리고 c[pc]에 값을 채웠으므로 1 늘린다.
    '''
    while pa < na and pb < nb:
        if a[pa] < b[pb]:
            c[pc] = a[pa]
            pa = pa + 1
        else:
            c[pc] = b[pb]
            pb = pb + 1
        
        pc = pc + 1
    
    '''
    아직 정렬하지 못한 남은 원소 중 na가 더 크면 남은 것이 a에 있다. 따라서 남은 a[pa]를 c[pc]에 삽입
    '''
    while pa < na:
        c[pc] = a[pa]
        pa = pa + 1
        pc = pc + 1

    '''
    아직 정렬하지 못한 남은 원소 중 nb가 더 크면 남은 것이 b에 있다. 따라서 남은 b[pb]를 c[pc]에 삽입
    '''
    while pb < nb:
        c[pc] = b[pb]
        pb = pb + 1
        pc = pc + 1

if __name__ == "__main__":
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))

    print("정렬을 마친 두 배열의 병합을 수행합니다.")

    merge_sorted(a, b, c)

    print("병합 정렬을 마쳤습니다.")
    print(f'배열 a : {a}')
    print(f'배열 b : {b}')
    print(f'배열 c : {c}')