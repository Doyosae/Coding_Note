'''
사실 이 문제는 이해 자체를 잘 못하겠다...
'''
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score    = [0, 0, 0]
    result   = []

    for idx, answer in enumerate(answers):
        '''
        pattern3 and answers2

        [3,3,1,1,2,2,4,4,5,5]
        [1,3,2,4,2]
        [3,3,1,1,2,2,4,4,5,5]
          [1,3,2,4,2]
        [3,3,1,1,2,2,4,4,5,5]
            [1,3,2,4,2]
        [3,3,1,1,2,2,4,4,5,5]
              [1,3,2,4,2]
        '''
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            print(idx, answer, idx%len(pattern3))
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    print(result)

    return result

def main():
    solution([1,2,3,4,5])
    solution([1,3,2,4,2])
    solution([5,4,1,1,1])


if __name__ == "__main__":
    main()