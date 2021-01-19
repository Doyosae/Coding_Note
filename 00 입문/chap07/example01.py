'''
브루트 포스법
흔히 알고 있는 모든 경우를 대입해서 솔루션을 찾는 방법
'''

def bf_match(txt: str, pat: str) -> int:
    pt = 0 # 텍스트를 따라가는 커서
    pp = 0 # pat를 따라가는 커서

    while pt != len(txt) and pp != len(pat):

        '''
        1. 패턴의 첫 번째 인덱스가 보고자 하는 텍스트의 문자와 일치하면 그 상태에서 각각의 인덱스 1 늘리기
        2. 그 다음 문자 패턴을 검사
        3. 일치하지 않다면 텍스트 커서에서 pat의 커서를 빼고 1 더한 것이 현재의 텍스트로 옮겨가는 것을 말함
        4. 일치하지 않다면 패턴의 커서 인덱스는 0으로 초기화
        '''
        if txt[pt] == pat[pp]:
            pt = pt + 1
            pp = pp + 1
        
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1

if __name__ == "__main__":
    s1 = input("텍스트를 입력하세요. ")
    s2 = input("패턴을 입력하세요. ")

    idx = bf_match(s1, s2)

    if idx == -1:
        print("텍스트 안에 패턴이 없습니다. ")
    else:
        print(f'{(idx+1)}번째 문자가 일치합니다. ')