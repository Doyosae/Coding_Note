from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        value = prices.popleft()
        count = 0
        
        for data in prices:
            if value > data:
                count = count + 1
                break
            count = count + 1
        
        answer.append(count)
    
    return answer

if __name__ == "__main__":
    answer = solution(prices = [1, 2, 3, 2, 3])
    print(answer)