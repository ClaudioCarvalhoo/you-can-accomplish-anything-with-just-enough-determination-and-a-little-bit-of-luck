class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, key):
        node = Node(key)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        return node

    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.size -= 1
        return node.value

    def removeTail(self):
        return self.remove(self.tail)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.nodeInLru = {}
        self.lru = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            self._updateLRU(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self._updateLRU(key)
        self.cache[key] = value
        if self.lru.size > self.capacity:
            removed = self.lru.removeTail()
            del self.cache[removed]
            del self.nodeInLru[removed]

    def _updateLRU(self, key):
        if key in self.cache:
            self.lru.remove(self.nodeInLru[key])
        newNode = self.lru.add(key)
        self.nodeInLru[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)