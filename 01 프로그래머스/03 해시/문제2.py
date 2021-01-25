def solution(phone_book):
    answer = True
    dict   = {}
    for data in phone_book:
        dict[data] = 0

    for data in dict:
        temp_str = ''
        for number in data:
            temp_str = temp_str + number
            # print(number)
            if temp_str in dict and temp_str != data:
                answer = False

    print(answer)

    return answer


def main():
    solution(["119", "97674223", "1195524421"])
    solution(["123", "456", "789"])
    solution(["12", "123", "1235", "567", "88"])
if __name__ == "__main__":
    main()