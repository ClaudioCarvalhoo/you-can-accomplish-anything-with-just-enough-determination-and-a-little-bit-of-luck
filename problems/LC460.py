class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def getFirst(self):
        if self.head.next != self.tail:
            return self.head.next
        return None

    def insertInHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def insertInTail(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def insertAfter(self, newNode, afterNode):
        newNode.next = afterNode.next
        newNode.prev = afterNode
        afterNode.next.prev = newNode
        afterNode.next = newNode

    def insertBefore(self, newNode, beforeNode):
        newNode.next = beforeNode
        newNode.prev = beforeNode.prev
        beforeNode.prev.next = newNode
        beforeNode.prev = newNode

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.frequencyList = DoublyLinkedList()
        self.frequencyToNode = {}
        self.keysList = DoublyLinkedList()
        self.keyToNode = {}
        self.keyToFrequency = {}

    # O(1)
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self._updateUse(key)
            return self.cache[key]

    # O(1)
    def put(self, key: int, value: int) -> None:
        if self.capacity > 0:
            if key in self.cache:
                self._updateUse(key)
            else:
                if len(self.cache) + 1 > self.capacity:
                    self._removeLFU()
                keyNode = Node(key)
                if 1 in self.frequencyToNode:
                    frequencyNode = self.frequencyToNode[1]
                    self.keysList.insertAfter(keyNode, frequencyNode.val["last"])
                    frequencyNode.val["last"] = keyNode
                else:
                    frequencyNode = Node({"val": 1, "first": keyNode, "last": keyNode})
                    self.frequencyList.insertInHead(frequencyNode)
                    self.frequencyToNode[1] = frequencyNode
                    self.keysList.insertInHead(keyNode)
                self.keyToNode[key] = keyNode
                self.keyToFrequency[key] = 1
            self.cache[key] = value

    def _updateUse(self, key):
        frequency = self.keyToFrequency[key]
        self.keyToFrequency[key] += 1
        keyNode = self.keyToNode[key]
        frequencyNode = self.frequencyToNode[frequency]
        nextFrequencyNode = frequencyNode.next
        self._removeNodeFromFrequency(keyNode, frequencyNode)
        if (
            nextFrequencyNode.val is None
            or nextFrequencyNode.val["val"] != frequency + 1
        ):
            newFrequencyNode = Node(
                {"val": frequency + 1, "first": keyNode, "last": keyNode}
            )
            self.frequencyList.insertBefore(newFrequencyNode, nextFrequencyNode)
            self.keysList.removeNode(keyNode)
            if nextFrequencyNode.val is not None:
                self.keysList.insertBefore(keyNode, nextFrequencyNode.val["first"])
            else:
                self.keysList.insertInTail(keyNode)
            self.frequencyToNode[frequency + 1] = newFrequencyNode
        else:
            self.keysList.removeNode(keyNode)
            self.keysList.insertAfter(keyNode, nextFrequencyNode.val["last"])
            nextFrequencyNode.val["last"] = keyNode

    def _removeLFU(self):
        frequencyNode = self.frequencyList.getFirst()
        keyNode = frequencyNode.val["first"]
        self.keysList.removeNode(keyNode)
        del self.cache[keyNode.val]
        del self.keyToFrequency[keyNode.val]
        del self.keyToNode[keyNode.val]
        self._removeNodeFromFrequency(keyNode, frequencyNode)

    def _removeNodeFromFrequency(self, keyNode, frequencyNode):
        if (
            frequencyNode.val["first"] == keyNode
            and frequencyNode.val["last"] == keyNode
        ):
            self.frequencyList.removeNode(frequencyNode)
            del self.frequencyToNode[frequencyNode.val["val"]]
        elif frequencyNode.val["first"] == keyNode:
            frequencyNode.val["first"] = keyNode.next
        elif frequencyNode.val["last"] == keyNode:
            frequencyNode.val["last"] = keyNode.prev


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)