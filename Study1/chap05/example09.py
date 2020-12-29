pos = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

def put() -> None:
    for j in range (8):
        for i in range (8):
            print("■" if pos[i] == j else '□', end = '')
        print()
    print()

def set(i: int) -> None:
    for j in range(8):

        # 열마다 퀸을 나열할때, 이제는 같은 flag_a, flag_b, flag_c 세 개의 값이 False가 아님에 주의
        if (not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+7]):
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False
            
set(0)