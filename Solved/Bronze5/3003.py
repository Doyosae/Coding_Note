king, queen, look, bishop, night, phone = map(int, input().split())
number  = [king, queen, look, bishop, night, phone]
default = [1, 1, 2, 2, 2, 8]

result = []
for data1, data2 in zip(default, number):
    result.append(data1 - data2)
print(result[0], result[1], result[2], result[3], result[4], result[5])