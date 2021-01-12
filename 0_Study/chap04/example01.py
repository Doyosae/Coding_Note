from typing import Any

class FixedStack:
      class Empty(Exception):
            pass
      class Full(Exception):
            pass

      # 길이가 capacity인 스택 리스트 self.str를 정의
      # capacity는 self.capacity로 할당
      # self.ptr은 스택에 자료가 몇 개 채워져 있는지 카운팅하는 함수
      def __init__(self, capacity: int = 256) -> None:
            self.stk      = [None] * capacity
            self.capacity = capacity
            self.ptr      = 0

      # self.ptr은 곧 스택의 자료의 길이가 몇 인지 반환하는 것
      def __len__(self) -> int:
            return self.ptr

      # 스택이 비어있는지 판단
      # self.ptr == 0 이면 데이터가 없다는 의미이므로 비어 있다.
      def is_empty(self) -> bool:
            return self.ptr <= 0
      
      # 스택이 가득 차 있는지 판단
      def is_full(self) -> bool:
            return self.ptr >= self.capacity

      # 현재 스택에 있는 원소의 수 대로 self.ptr이 따라감 비어 있다면 self.ptr에 값을 부여하고 self.ptr은 하나 더 늘림
      # 즉 이전 상태는 self.stk[self.ptr - 1], self.ptr
      # 다음 상태는 self.stk[self.ptr], self.ptr + 1가 되는 것
      def push(self, value: Any) -> None:
            if self.is_full():
                  raise FixedStack.Full
            self.stk[self.ptr] = value
            self.ptr           = self.ptr + 1

      # 값을 뽑아내는 def pop 정의, def push와 반대의 과정
      # 뽑아 내고자 하는 것 self.ptr의 원래 데이터가 있는 이덱스에서 1를 뽑아내면 self.tpr - 1이고 이를 인덱스에 넣어서
      # pop()을 구현하는 것
      def pop(self) -> Any:
            if self.is_empty():
                  raise FixedStack.Empty
            self.ptr = self.ptr - 1
            return self.stk[self.ptr]
      
      def peek(self) -> Any:
            if self.is_empty():
                  raise FixedStack.Empty
            return self.stk[self.ptr - 1]
      
      # self.ptr = 0으로 만들면 모든게 클리어 된다고 하지만 어떤 원리일까?
      # self.ptr = 0이면 데이터의 갯수가 0이 되는 것을 의미
      def clear(self) -> None:
            self.ptr = 0
      
      def find(self, value: Any) -> Any:
            for i in range (self.ptr -1, -1, -1):
                  if self.stk[i] == value:
                        return i # 검색 성공
            return -1 # 검색 실패

      # self.ptr을 순회하면서 해당 i에 해당하는 self.stk 값이 value랑 일치하면 c를 늘림
      def count(self, value: Any) -> bool:
            c = 0
            for i in range (self.ptr):
                  if self.stk[i] == value:
                        c = c + 1
            return c
      
      def __contains__ (self, value: Any) -> bool:
            return self.count(value)

      def dump(self) -> None:
            if self.is_empty():
                  print("스택이 비어 있습니다.")
            else:
                  print(self.stk[:self.ptr])