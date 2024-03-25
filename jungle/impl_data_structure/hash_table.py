class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # 해시 함수: key에 대해 해시 값을 리턴
    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self._hash_function(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_key].append([key, value])

    def search(self, key):
        hash_key = self._hash_function(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        hash_key = self._hash_function(key)
        for i, pair in enumerate(self.table[hash_key]):
            if pair[0] == key:
                del self.table[hash_key][i]
                return

# 예시로 해시 테이블을 사용해보겠습니다.
hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 10)

print(hash_table.search("apple"))  # 출력: 5
print(hash_table.search("banana"))  # 출력: 10

hash_table.insert("apple", 7)  # 이미 존재하는 키에 대해 값을 업데이트합니다.
print(hash_table.search("apple"))  # 출력: 7

hash_table.delete("banana")
print(hash_table.search("banana"))  # 출력: None (삭제된 키)
