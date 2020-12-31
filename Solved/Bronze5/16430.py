a, b = map(int, input().split())

if a > b:
    raise print("b가 a보다 커야 합니다.")

print(b-a, b)