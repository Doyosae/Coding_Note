def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    '''
    각 작업은 100이 되면 배포 가능하다.
    앞에 있는 기능은 먼저 배포 가능하다.
    뒤에 있는 기능은 앞에 있는 기능이 배포될 때 같이 배포 가능하다.
        이 말은 앞에 있는 기능이 100을 넘어야 한다는 것
        100 120 150 60
        100 120 150이 한꺼번에 배포 [3, ]
        남은 것은 60이고 100이 되어야 배포 [3, 1]
        
        따라서 뒤에 있는 기능이 배포되는 것은
        앞에 있는 기능이 배포되기 까지 기다려야 되므로 스택 구조가 된다.
    '''
    answer = []
    time   = 0
    count  = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count = count + 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time = time + 1
    answer.append(count)
    return answer