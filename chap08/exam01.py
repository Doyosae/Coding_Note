'''
연결 리스트 구현하기
연결 리스트는 인스턴스에서 데이터에 대한 참조와 다음 노드에 대한 참조가 있다.
'''

from __future__ import annotations
from typing import Any, Type

class Node:

    def __init__ (self, data: Any = None, next: Node = None):
        '''
        1. 데이터와 노드를 입력받으면
        2. 데이터는 self.data에 참조하고
        3. 노드는 뒷 노드 self.next에 참조한다.
        '''
        self.data = data # 데이터
        self.next = next # 뒷쪽 포인트


class LinkedList:

    def __init__ (self) -> None:
        self.no      = 0        # 노드의 갯수
        self.head    = None     # 머리 노드
        self.current = None     # 현재 노드

    def __len__ (self) -> int:
        return self.no

    def search(self, data: Any) -> int:
        '''
        1. 원하는 data를 서치 함수에 입력한다.
        2. 일단 첫 번째 cnt는 0이고 ptr은 당연히 리스트의 헤드 노드를 가리킨다.
        3. 선형 검색으로 ptr이 None이 아닌 동안 (None이라면 해당 리스트에 원소가 없는 것이다.)
        4. ptr.data == data이면 self.current = ptr 할당학 cnt 리턴
        5. 같지 않다면 다음 노드로 가기 위해 cnt += 1하고 ptr.next를 ptr에 할당
        '''
        cnt = 0
        ptr = self.head

        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt = cnt + 1
            ptr = ptr.next

        return -1

    def __contains__ (self, data: Any) -> bool:
        return self.search(data) >= 0

    def add_first (self, data: Any) -> None:
        '''
        1. 맨 앞에 노드를 삽입하기 위해
        2. ptr = self.head를 할당하고
        3. self.head = self.current = Node(data, ptr)
            삽입하고자 하는 data가 들어가는 노드와, 이 노드가 참조하는 뒷 노드는 기존의 맨 앞 노드이다.
        4. 그렇게 하고 나서 self.no += 1로 노드 수 1개 늘리기
        '''
        ptr       = self.head
        self.head = self.current = Node(data, ptr)
        self.no   = self.no + 1

    def add_last (self, data: Any) -> None:
        if self.head is None:
            self.add_first(data)
        else:
            ptr      = self.head
            while ptr.next is not None: # ptr.next가 None이 아닌 동안 계속 순회
                ptr  = ptr.next         # 이 때의 ptr.next를 ptr에 할당 (즉 마지막 노드를 ptr에 할당)
            '''
            add_fisrt와는 다르게 ptr = ptr.next이고 ptr == ptr.next.next이다.
            여기에 주목노드커서를 옮기고 삽입하고자 하는 데이터와 None을 할당
            '''
            ptr.next = self.current = Node(data, None)
            self.no  = self.no + 1

    def remove_fisrt(self) -> None:
        '''
        1. 첫 번째 노드를 제거
        2. self.head의 next를 주목 노드로 옮기고 self.head로 할당
        '''
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no = self.no - 1

    def remove_last(self) -> None:
        if self.head is not None:
            if self.head.next is None:
                self.remove_fisrt()
            else:
                ptr = self.head
                pre = self.head

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next

                pre.next     = None # pre.next == ptr.next
                self.current = pre
                self.no      = self.no - 1

    def remove(self, p: Node) -> None:
        if self.head is not None:
            if p is self.head:
                self.remove_fisrt()
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next     = p.next
                self.current = ptr
                self.no      = self.no - 1
                
    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head is not None:
            self.remove_fisrt()
        self.current = None
        self.no      = 0

    def next(self) -> bool:
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True

    def print_current_node(self) -> None:
        if self.current is None:
            print("주목 노드가 없습니다.  ")
        else:
            print(self.curret.data)

    def print(self) -> None:
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next
        
    def __iter__ (self) -> LinkedListIterator:
        return LinkedListIterator(self.head)

class LinkedListIterator:

    def __init__ (self, head: None):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self
    
    def __next__ (self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data