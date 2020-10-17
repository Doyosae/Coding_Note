# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:

      def __init__ (self, key: Any, value: key, next: Node):
            # 클래스 초기화
            self.key = key
            self.value = value
            self.next = next
      

class CHainHash:

      def __init__ (self, capacity: int) -> None:
            # 체인해시 초기화
            self.capacity = capacity
            self.table    = [None] * self.capacity

      def hash_value (self, key: Any) -> int:
            if isinstance(key, int):
                  return key % self.capacity
            return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
      
      def search (self, key: Any) -> Any:
            hash = self.has_value(key)
            p    = self.table[hash]

            # 키 값을 테이블의 크기로 나눈 나머지가 해시 테이블의 인덱스
            # 해시 테이블의 인덱스헤 해당하는 값을 받음
            # 이것이 None이 아니라면 
            while p is not None:
                  if p.key == key:
                        return p.value
                  p = p.next

            # 아무것도 없으면 None을 리턴
            return None

      def add (self, key: Any,value: Any) -> bool:
            hash = self.has_value(key)
            p    = self.table[hash]
            
            while p is not None:
                  if p.key == key:
                        return False
                  
                  p = p.next
            
            temp = Node(key, value, self.table[hash])
            self.table[hash] = temp
            return True

      def remove (self, key: Any) -> bool:
            hash = self.hash_value(key)
            p    = self.table[hash]
            pp   = None
            
            # 키의 해시값을 받으면 그 해시값(인덱스)의 p를 참조
            # pp = None으로 초기화, p가 None이 아니면 계속 탐색
            # p의 key가 key와 같고, pp가 None이면 self.table[hash]의 값을 p의 다음 값으로 참조
            while p is not None:
                  if p.key == key:
                        if pp is None:
                              self.table[hash] = p.next
                        else:
                              # pp가 None이 아니라면 p.next --> pp.next이다.
                              pp.next = p.next
                        
                        # 그리고 True
                        return True
                  
                  pp = p
                  p = p.next
            return False

      def dump (self) -> None:
            # 해시 테이블을 덤프
            for i in range (self.capacity):
                  p = self.table[i]
                  print(i, end = ' ')
                  while p is not None:
                        print(f'    -> {p.key}   ({p.value})', end = ' ')
                        p = p.next
                  print()