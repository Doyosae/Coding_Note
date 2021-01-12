'''
1. 노드를 배열 안에 저장하고
2. 이전의 방법은 인스턴스를 내부에서 생성하고 소멸한다는 점에서 메모리 문제
3. 배열을 이용한 링크드 리스트는 배열 상에서 해당 인덱스의 원소와, 참조하는 다음 노드 데이터의 배열 상 인덱스만 기억 
'''

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:

    def __init__ (self, data = Null, next = Null, dnext = Null):
        self.data  = data   # 데이터
        self.next  = next   # 리스트의 뒷 쪽 포인터
        self.denxt = dnext  # 프리 리스트의 뒷 쪽 포인터
    
class ArrayLinkedList:
     
    def __init__ (self, capacity: int):
        self.head     = Null
        self.current  = Null
        self.max      = Null
        self.deleted  = Null
        self.capacity = capacity
        self.n        = [Node()] * self.capacity
        self.no       = 0

    def __len__(self) -> int:
        return self.no
    
    def get_insert_index(self):
        if self.deleted == Null:
            if self.max < self.capacity:
                self.max += 1
                return self.max
            else:
                return Null
        
        else:
            rec = self.deleted
            self.deleted = self.n[rec].denxt
            return rec

    def delete_index(self, idx: int) -> None:
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].denxt = Null
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[rec].denxt = rec
        
    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt = cnt + 1
            ptr = self.n[ptr].next
        
        return Null

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def add_first (self, data: Any):
        ptr = self.head
        rec = self.get_inser_index()

        if rec != Null:
            self.head = self.current = rec
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def remove_first(self) -> None:
        if self.head != Nul:
            ptr = self.n[self.head].next
            self.deleted_index(self.head)
            self.head = self.current = ptr
            self.no   = self.no - 1
    
    def remove_last(self) -> None:
        if self.head != Null:
            if self.n[self.head] == Null:
                self.remove_fisrt()
            else:
                ptr = self.head
                pre = self.head

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = Null
                self.delete_index(pre)
                self.current = pre
                self.no      = self.no - 1

    def remove(self, p: int) -> None:
        if self.head != Null:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return
                
                self.n[ptr].next = Null
                self.deleted_index(ptr)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no      = self.no - 1

    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head != Null:
            self.remove_fisrt()
        self.current = Null

    def next(self) -> bool:
        if self.current == Null or self.n[self.current].next == Null:
            return False
        self.current = self.n[self.current].next
        return True

    def print_current_node(self) -> None:
        if self.current == Null:
            print("주목 노드가 없습니다.")
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        ptr = self.head
        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        for i in self.n:
            print(f'[{i}]   {i.data} {i.next} {i.dnext}')
        
    def __iter__(self) -> ArrayLinkedListIterator:
        return ArrayLinkedListIterator(self.n, self.head)


class ArrayLinkedListIterator:

    def __init__(self, n: int, head: int):
        self.n       = n
        self.current = head

    def __iter__ (self) -> ArrayLinkedListIterator:
        return self

    def __next__ (self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data         = self.n[self.current].data
            self.current = self.n[self.current].next
            return data