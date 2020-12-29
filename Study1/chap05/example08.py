pos = [0] * 8
flag = [False] * 8
print(flag)

def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end = '')
    
    print()


def set(i: int) -> None:
    for j in range(8): # 행 8칸을 모두 순회

        # flag j번째 (즉, 각 행마다 말의 배치 여부를 순회) 에 말을 배치하지 않았다면
        # flag[j]가 False가 아니라면, 해당 i 열의 j 행에 말을 배치
        if not flag[j]:
            pos[i] = j

            # i == 7은 체스판 끝까지 탐색
            if i == 3:
                put() # 출력

            # 그렇지 않다면 말을 배치한 해당 플래그는 True로 바꾸고
            # 해당 플래그만 True인 상태에서 다시 if not flag[j] ~~ 를 시행
            # 이렇게 하면 True인 플래그만 피해서 말을 배치할 수 있다.
            else:
                flag[j] = True
                set(i+1)
                flag[j] = False # 어차피 True가 아닌 경우에 대해서만 나열 가능

set(0)
