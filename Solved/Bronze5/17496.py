N, T, C, P = map(int, input().split())
if N%T == 0:
    num = N//T - 1
else:
    num = N//T
print(num * C * P)