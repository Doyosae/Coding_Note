# '''
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
# '''
# from itertools import permutations
# from itertools import combinations

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     pivot                        = array[len(array) // 2]
#     less_arr, equal_arr, big_arr = [], [], []

#     for element in array:
#         if element < pivot:
#             less_arr.append(element)
#         elif element > pivot:
#             big_arr.append(element)
#         else:
#             equal_arr.append(element)
        
#     '''
#     먼저 피벗을 하나 잡고
#     피벗보다 작으면 작은 어레이에, 피벗보다 크면 큰 어레이에 할당
#         작은 어레이는 다시 작은 어레이에서 피벗을 잡고
#         내부 피벗보다 작으면 왼쪽 어레이에
#         내부 피벗보다 크면 오른쪽 어리에이에 할당
#         이 부분은 재귀 함수로 구현
#     '''
#     return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)

# def solution(numbers):
#     number = []
#     for data in list(permutations(numbers, len(numbers))):
#         value = ''
#         for num in data:
#             value = value + str(num)
#         number.append(int(value))

#     answer = quick_sort(number)
#     answer = str(max(answer))
#     print(answer)
        
#     return answer

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key = lambda x: x*3, reverse = True)
#     return str(int(''.join(numbers)))

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

def main():
    solution([6, 10, 2])
    solution([3, 30, 34, 5, 9])

if __name__ == "__main__":
    main()