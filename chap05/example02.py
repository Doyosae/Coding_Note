'''
유클리드 호제법
예를 들어 두 정수값의 최대 공약수를 구하는 문제가 있다.
22, 8
22를 8로 나누면 6이 남는다.
8, 6
8를 6으로 나누면 2가 남는다.
따라서 2가 8와 22의 최대 공약수이다.
'''

def gcd(x: int, y: int) -> int:
    # 정숫값 x와 y의 최대 공약수를 반환
    if y == 0: # 만약에 y가 0이면 x를 반환, 왜냐하면 (5, 0)의 최대공약수는 5이므로
        return x
    else: # 만약 입력값이 10, 5라면 5와 10 나누기 5의 나머지를 다시 gcd에 입력
        return gcd(y, x % y)

if __name__ == "__main__":
    print('두 정숫값의 최대 공약수를 구합니다')
    x = int(input("첫 번째 정숫값을 입력하세요"))
    y = int(input("두 번째 정숫값을 입력하세요"))
    print(f"두 정숫값의 최대 공약수는 {gcd(x, y)}입니다")