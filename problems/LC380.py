import random


class RandomizedSet:

    # O(1)
    def __init__(self):
        self.elements = []
        self.elementPositions = {}

    # O(1)
    def insert(self, val: int) -> bool:
        if val in self.elementPositions:
            return False
        elif len(self.elements) == len(self.elementPositions.keys()):
            self.elements.append(val)
            self.elementPositions[val] = len(self.elements) - 1
        else:
            self.elements[len(self.elementPositions.keys())] = val
            self.elementPositions[val] = len(self.elementPositions.keys())
        return True

    # O(1)
    def remove(self, val: int) -> bool:
        if val not in self.elementPositions:
            return False
        else:
            self._swapElements(
                self.elementPositions[val], len(self.elementPositions.keys()) - 1
            )
            swappedElement = self.elements[self.elementPositions[val]]
            self.elementPositions[swappedElement] = self.elementPositions[val]
            del self.elementPositions[val]
            return True

    # O(1)
    def getRandom(self) -> int:
        return self.elements[random.randint(0, len(self.elementPositions.keys()) - 1)]

    # O(1)
    def _swapElements(self, i, j):
        self.elements[i], self.elements[j] = self.elements[j], self.elements[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()