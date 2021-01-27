def solution(answers):
    people1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    list = [people1, people2, people3]
    count = []
    for data in list:
        cnt = 0
        for index, number in enumerate(data):
            test = data[index : index + len(answers)]
            if len(test) != len(answers):
                break
            else:
                for ans, peak in zip(answers, test):
                    if ans == peak:
                        cnt = cnt + 1
                    else:
                        cnt = 0
            count.append(cnt)
        count.append("/")
    print(count)
    # print(count.index(max(count))+1)


    answer = []
    return answer

def main():
    solution([1,2,3,4,5])
    solution([1,3,2,4,2])
    solution([5,4,1,1,1])


if __name__ == "__main__":
    main()