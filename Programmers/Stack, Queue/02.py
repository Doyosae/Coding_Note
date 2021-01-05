def solution(prices):
    answer = []
    
    for i in range (len(prices)):
        cnt = 0
        for j in range (i+1, len(prices)):
            
            if prices[i] <= prices[j]: # 다음 가격이 크다면 계속 1 늘림
                cnt = cnt + 1
            else: # 크기가 작아진다면 그래도 1초는 머무른 것이므로 1 늘리고 break해서 for 문을 빠져나온다.
                cnt = cnt + 1
                break
                
        answer.append(cnt)
        
    return answer