a, b, c = map(int, input().split())
# 3개의 눈

if a == b == c:
    print(10000 + (a *1000))
elif (a==b and a!=c):
    print(1000 + (a*100))
elif (b==c and a!=b):
    print(1000 + (b*100))
elif (a==c and a!=b):
    print(1000 + (a*100))
else:
    result = max([a, b, c]) * 100
    print(result)