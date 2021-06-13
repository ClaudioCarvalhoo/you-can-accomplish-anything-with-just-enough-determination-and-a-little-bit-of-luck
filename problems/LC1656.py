class OrderedStream:

    # O(1)
    def __init__(self, n: int):
        self.elems = [None for _ in range(n)]
        self.nextElem = 0

    # O(n)
    def insert(self, idKey: int, value: str) -> List[str]:
        self.elems[idKey - 1] = value
        res = []
        while self.nextElem < len(self.elems) and self.elems[self.nextElem] is not None:
            res.append(self.elems[self.nextElem])
            self.nextElem += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)