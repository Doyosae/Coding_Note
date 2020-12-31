a, b, c = map(int, input().split())

if c > min(a, b):
    raise print("c는 a, b 무엇보다도 작아야 한다.")

N = ((a+1)*(b+1) // (c+1)) - 1
print(N)