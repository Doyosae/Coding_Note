a, b, c = map(int, input().split())
'''
노트북 1대의 새산 비용 = a + b
노트북 1대의 가격      = c
'''
cnt = 0
if c<=b:
    cnt = -1
else:
    cnt = a // (c-b) + 1

print(cnt)