# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    # O(1)
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
        self.nextElem = self.findNextElem()

    # O(n) technically if it's [[],[],[],[],[],[],[],[],[],[],[]]
    # n = len(nestedList)
    def next(self) -> int:
        result = self.nextElem
        self.nextElem = self.findNextElem()
        return result

    # O(1)
    def hasNext(self) -> bool:
        return self.nextElem is not None

    def findNextElem(self):
        if len(self.stack) > 0:
            curList, curPos = self.stack[-1]
            self.stack[-1][1] += 1
            if self.stack[-1][1] >= len(self.stack[-1][0]):
                self.stack.pop()
            if curList[curPos].isInteger():
                return curList[curPos].getInteger()
            else:
                if len(curList[curPos].getList()) > 0:
                    self.stack.append([curList[curPos].getList(), 0])
                return self.findNextElem()
        return None


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())