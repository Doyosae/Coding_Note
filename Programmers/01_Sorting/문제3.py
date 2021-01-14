# def solution(citations):
#     citations.sort(reverse = False)
#     print(citations)
#     # 기준 h회 이상 인용 논문수가 h개 이상
#     answer = []
#     for cit in range(len(citations)):
#         if citations[cit] <= len(citations[cit:]):
#             answer.append(citations[cit])
#         else:
#             pass
#     print(max(answer))

#     return answer


def solution(citations):
    citations = sorted(citations)
    print(citations)

    l = len(citations)
    for i in range(l):
        print(citations[i], l-i)
        if citations[i] >= l-i:
            print(citations[i], l-i)
            return l-i
    print(0)
    return 0

def main():
    ans = solution([3, 0, 6, 1, 5])
    ans = solution([2, 5, 1, 6, 6, 2, 3, 5, 2, 8])
    
if __name__ == "__main__":
    main()