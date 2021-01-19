def factorial (n: int) -> int:
    # 양의 정수 n의 팩토리얼 값을 재귀적으로 구현
    if n>0:
        return n * factorial(n-1)
    else:
        return 1

if __name__ == "__main__":
    n = int(input("출력할 팩토리얼 값을 입력하세요"))
    print(f'{n}의 팩토리얼은 {factorial(n)} 입니다.')

'''
자기 자신 함수 호츨을 그대로 하면 직접 재귀
def a()
def b()가 정의되어 있고

b에서 a를 호출하고
a에서 b를 호출하면 간접재귀
'''