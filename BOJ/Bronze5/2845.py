'''
첫째 줄에는 1제곱미터당 사람 수와 파티장의 넓이가 주어진다.
둘째 줄에는 각 기사에 실려있는 참가자의 수가 주어진다.
10^6보다 작은 양의 정수 5개
'''
people_per, region = map(int, input().split())
a, b, c, d, e = map(int, input().split())

def calculate(people_per, region, a, b, c, d, e):
    result = int(people_per * region)
    print(a-result, b-result, c-result, d-result, e-result)

calculate(people_per, region, a, b, c, d, e)