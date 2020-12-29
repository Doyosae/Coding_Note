result = []
for i in range(4):
    result.append(int(input()))

result = sum(result)

print(result//60)
print(result%60)