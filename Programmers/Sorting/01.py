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


def solution(array, commands):
    answer = []

    for index in range (len(commands)):
        array1 = array[commands[index][0]-1 : commands[index][1]]

        if len(array1) == 1:
            answer.append(array1)
        else:
            array1 = sort(array1)
            answer.append(array1)

    # print("먼저 잘라서 정렬한 리스트")
    # print(answer)
    
    for index in range(len(commands)):
        answer[index] = answer[index][commands[index][2]-1]
    
    # print("최종 답")
    # print(answer)
    return answer

def main():
    solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    solution([9, 8, 7, 6, 5, 4, 3, 2, 1], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
if __name__ == "__main__":
    main()
    # ans = sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    # print(ans)