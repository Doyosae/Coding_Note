from __future__ import annotations
from typing import Any, Type

class Node:

    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):

        self.key   = key
        self.value = value
        self.left  = left
        self.right = right

class BinarySearchTree:

    def __init__(self):

        self.root = None

    def search(self, key: Any) -> Any:
        
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:
        
        def add_node(node: Node, key: Any, value: Any) -> None:

            if key == node.key:
                return False

            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)

            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
                
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True

        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        '''
        노드를 삭제하는 과정
            1. 자식 노드가 없는 노드를 삭제
            2. 자식 노드가 1개인 노드를 삭제
            3. 자식 노드가 2개인 노드를 삭제

            1. 자식 노드가 없는 노드라면
                해당 노드가 부모의 왼쪽 자식이라면 parent.left = None
                해당 노드가 부모의 오른쪽 자식이라면 parent.left = None
            2. 자식 노드가 1개인 노드
                해당 노드가 부모의 왼쪽 자식이라면 parent.left = remove_node.자식
                해당 노드가 부모의 오른쪽 자식이라면 parent.right = remove_node.자식
            3. 자식 노드가 2개인 노드
                삭제하고자하는 서브 트리에서 가장 큰 자식을 선택하여, 삭제하고자하는 노드의 위치와 교환
                삭제하고자 하는 노드 아래의 서브 트리에서 가장 큰 노드는 계속 오른쪽 자식으로 가는 노드이다.
                이것을 삭제하고자 하는 노드의 자리로 옮긴다.
                    그리고 옮긴 노드는 
                        만약 자식이 없으면 1.를 수행
                        만약 자식이 1개이면 2.를 수행
        '''

        p             = self.root # 스캔 중인 노드
        parent        = None      # 스캔 중인 노드의 부모
        is_left_child = True      # p는 스캔 중인 노드의 왼쪽 자식 노드인지 확인

        while True:
            if p is None:
                return False
                # p가 None이면 더 이상 키가 존재하지 않는다. False를 리턴한다. (당연히 아무것도 없으므로)
            
            if key == p.key:
                break
                # 키와 노드 p의 키가 같다면 더 이상 탐색 작업을 진행할 이유가 없다. 따라서 break

            else:
                # p는 None이 아니고 (즉 존재) 동시에 key != p.key이므로 탐색한다.
                # 일단 현재 p를 parent라 두고
                # key가 p.key보다 작으면 왼쪽 노드로 가야한다. 따라서 is_left_chile = True이다.
                # 왼쪽 노드를 부모 노드로 하는 서브트리를 탐색하기 위해 p = p.left로 둔다.
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                
                # 그렇기 않다면 is_left_chilld = False이고 오른쪽 노드만 존재하므로 p = p.right라 한다.
                else:
                    is_left_child = False
                    p = p.right


        '''
        p.left가 None이라면 (왼쪽 자식 노드가 없다는 뜻이다.)
            p가 self.root 자기 자신이면, p.right를 self.root에 대입
            is_left_child == True이면 parent의 left가 있다는 뜻이다. 따라서 p.right를 parent.left에 대입
            is_left_chiled == False이면 parent의 left가 없다는 뜻이다. 따라서 p.right를 parent.right에 대입
        '''
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right

        # '''
        # p.right가 None이라는 의미는 왼쪽 노드들만 있다는 뜻이다.
        # '''
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
            
        # '''
        # 자식 노드가 2개인 경우, 노드를 삭제하는 것
        #     삭제할 노드의 서브 트리에서 가장 큰 노드를 찾아, 삭제할 노드와 자리를 교환
        # '''
        else:
            parent = p
            left   = p.left
            is_left_child = True

            while left.right is not None: # left의 right가 없을 때까지 parent = left, left = left.right 갱신
                parent = left
                left   = left.right
                is_left_child = False
            
            # 그렇게 찾은 가장 큰 right.right.right의 값은 left에 저장되어 있다.
            # left -> p에 모두 대입
            p.key   = left.key
            p.value = left.value

            # is_left_child == True이면 left.left -> parent.left를 참조하도록 변경
            # is_left_child == False이면 left.left -> parent.right에 참조하도록 변경
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
            
        return True

    def dump(self) -> None:

        def print_subtree(node: Node):

            if node is not None:
                print_subtree(node.left)
                print(f'{node.key}  {node.value}')
                print_subtree(node.right)

        print_subtree(self.root)

    def min_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root

        while p.left is not None:
            p = p.left

        return p.key

    def max_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root

        while p.right is not None:
            p = p.right

        return p.key