n, m = map(int, input().split())

if n >= 0 and m >= 0:
    if n > m:
        print(n-m)
    else:
        print(m-n)
elif n < 0 and m >= 0:
    print(m-n)
elif n >=0 and m < 0:
    print(n-m)
else:
    if n > m:
        print(n-m)
    else:
        print(m-n)