a, b = map(int, input().split())

if (a <= 0 or 10 <= a) or (b <= 0 or 10 <= b):
    raise print("입력 오류")
print(a+b)