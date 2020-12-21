# 고정 길이 큐 클래스 FixedQueue 구현하기
from typing import Any

class FixedQueue:

      class Empty(Exception):
            pass
      class Full(Exception):
            pass

      def __init__ (self, capacity: int) -> None:
            self.no       = 0
            self.front    = 0
            self.rear     = 0
            self.capacity = capacity
            self.que      = [None] * capacity
      
      def __len__ (self) -> int:
            return self.no

      # 큐가 비어 있으면 True를, 비어 있지 않으면 False를 내보낸다.
      def is_empty (self) -> bool:
            return self.no <= 0

      # 큐가 가득 차 있으면, 즉 self.capacity보다 이상이면 True를 반환한다.
      def is_full (self) -> bool:
            return self.no >= self.capacity

      def enque(self, x: Any) -> None:
            if self.is_full():
                  raise FixedQueue.Full

            # is_full()가 True, raise FixedQueu.Full
            # 큐의 rear에 데이터를 저장하고, self.rea는 1 늘린다.
            # 그리고 저장된 데이터가 1개 늘었으므로, self.no도 1 늘린다.
            self.que[self.rear] = x
            self.rear = self.rear + 1
            self.no   = self.no + 1

            # 만약 rear가 capacity와 같다면, self.rear = 0으로 되돌린다. 
            if self.rear == self.capacity:
                  self.rear = 0

      def deque(self) -> Any:
            if self.is_empty():
                  raise FixedQueue.Empty
            x = self.que[self.front]
            self.front = self.front + 1
            self.no    = self.no - 1
            if self.front == self.capacity:
                  self.front = 0
            return x
      
      def peek(self) -> Any:
            if self.is_empty():
                  raise FixedQueue.Empty
            return self.que[self.front]

      def find(self, value: Any) -> Any:
            # 큐에서 값을 찾아 인덱스를 반환하는 함수
            for i in range (self.no):
                  idx = (i + self.front) % self.capacity
                  if self.que[idx] == value:
                        return idx
            
            return -1

      def count(self, value: Any) -> bool:
            c = 0
            for i in range (self.no):
                  idx = (i + self.front) % self.capacity
                  # self.no를 순회하면서, 데이터의 맨 앞이 self.front이므로 이것의 인덱스를 계산해야함
                  # 예를 들어서 self.front == 1 이면 1 + 1에 self.capacity로 나누어서 현재의 인덱스를 구한다. (즉 2)
                  # self.front = 0이면 자료구조에서 맨 앞에 front가 있는 것이므로 인덱스가 1
                  if self.que[idx] == value:
                        c = c + 1
            
            return c

      def __contains__ (self, value: Any) -> bool:
            # 큐에 값이 있는지 판단.
            return self.count(value)

      def clear (self) -> None:
            self.no = self.front = self.rear = 0
      
      def dump (self) -> None:
            if self.is_empty():
                  print("큐가 비었습니다.")
            else:
                  for i in range (self.no):
                        print(self.que[(i + self.front) % self.capacity], end = ' ')
                  print()