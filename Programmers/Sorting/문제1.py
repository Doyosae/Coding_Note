import random

def random_list(size):
    result = []
    num    = random.randrange(0, size)
    for _ in range(size):
        while num in result:
            num = random.randrange(0, size)
        result.append(num)

    return result

def bubble_sort(array):
    for i in range (0, len(array)-1):
        for j in range (0, len(array)-1-i):
            if array[j] < array[j+1]:
                pass
            elif array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j]   = temp
    
    return array

def select_sort(array):
    for i in range(0, len(array)):
        index  = array.index(min(array[i : ]))
        temp         = array[i]
        array[i]     = array[index]
        array[index] = temp
    
    return array

def insert_sort(array):
    '''
    두 번째 원소부터 시작해서 바로 앞과 비교한다.
    조건을 만족하지 않으면 비교 원소를 뒤로 민다.
    조건을 만족하면 서로 자리를 바꾼다.
    '''
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], arr[j] = arr[j], arr[j-1]
        
    return array

# def shell_sort():

# def merge_sort():

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot                        = array[len(array) // 2]
    less_arr, equal_arr, big_arr = [], [], []

    for element in array:
        if element < pivot:
            less_arr.append(element)
        elif element > pivot:
            big_arr.append(element)
        else:
            equal_arr.append(element)
        
    '''
    먼저 피벗을 하나 잡고
    피벗보다 작으면 작은 어레이에, 피벗보다 크면 큰 어레이에 할당
        작은 어레이는 다시 작은 어레이에서 피벗을 잡고
        내부 피벗보다 작으면 왼쪽 어레이에
        내부 피벗보다 크면 오른쪽 어리에이에 할당
        이 부분은 재귀 함수로 구현
    '''
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)



def solution(array, commands):
    answer = []
    for index in range (len(commands)):
        array1 = array[commands[index][0]-1 : commands[index][1]]

        if len(array1) == 1:
            answer.append(array1)
        else:
            array1 = bubble_sort(array1)
            answer.append(array1)

    
    for index in range(len(commands)):
        answer[index] = answer[index][commands[index][2]-1]

    return answer

def main():
    solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    solution([9, 8, 7, 6, 5, 4, 3, 2, 1], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])

if __name__ == "__main__":
    # main()
    arr = random_list(20)
    print(arr)

    ans = quick_sort(arr)

    print(ans)