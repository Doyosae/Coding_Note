'''
a   : 행렬의 갯수
b c : 행렬의 크기 1
d e : 행렬의 크기 2
f g : 행렬의 크기 3
'''
import sys

N         = int(input())
size_list = []
for i in range(N):
    a, b = map(int, input().split())
    if i != N-1:
        size_list.append(a)
    else:
        size_list.append(a)
        size_list.append(b) # 입력 받은 행렬의 사이즈를 size_list에 모두 나열 (중복 없이)

M = [[0 for x in range(4)] for y in range(N+1)]

for diag in range(1, 4):
    for i in range(1, 4-diag):
        j = i+diag
        M[i][j] = sys.maxsize
        for k in range(i,j):
            M[i][j] = min(M[i][j], M[i][k] + M[k+1][j] + size_list[i-1]*size_list[k]*size_list[j])
            
print(M)