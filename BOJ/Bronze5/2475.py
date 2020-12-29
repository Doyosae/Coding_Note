# number = list(input())
a, b, c, d, e = map(int, input().split())
number = [a, b, c, d, e]
if len(number) - 1 > 5:
    raise print("길이 초과, 길이는 5 이하로")

# print(number)
result = 0
for i in number:
    result = result + int(i)**2

print(result%10)