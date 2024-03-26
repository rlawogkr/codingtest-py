from __future__ import annotations
from typing import Any,Type
import hashlib

class Node:
    def __init__(self, key, value, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next #뒤쪽 노드를 참조

class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash] #해당 해시값에 대한 연결리스트의 첫번째 노드를 참조

        while p is not None:
            if p.key == key: 
                return p.value #key에 해당하는 값이 있을 경우 그 값 리턴
            p = p.next
        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash] #해시값을 가진 노드를 참조

        while p is not None:
            if p.key == key:
                return False #이미 key가 존재하므로 실패
            p = p.next

        temp = Node(key, value, self.table[hash]) #해당 키에 값이 없을 경우 새로운 노드를 만들어서 연결리스트의 맨 앞에 추가
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end = '')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end = '')
                p = p.next
            print()