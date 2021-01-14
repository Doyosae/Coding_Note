n = int(input('정수를 몇 개 저장할까요?: '))
a = [None] * n
cnt = 0
while True:
      a[cnt % n] = int(input(f'{cnt+1}번째 정수를 입력하세요.'))
      cnt        = cnt + 1
      retry      = input(f'계속 할까요?(Y ... ... Yes / N ... No): ')
      if retry in {"N", "n"}: # N이나 n을 입력하면 더 이상 값을 받지 않음
            break

i = cnt - n
if i < 0:
      i = 0

while i < cnt:
      print(f'{i + 1}번쨰 = {a[i % n]}')
      i = i + 1