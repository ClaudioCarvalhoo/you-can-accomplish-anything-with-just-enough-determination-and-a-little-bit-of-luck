# O(n)
# n = len(s)


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != "0":
            return False

        endVisited = set()
        goal = len(s) - 1
        start = 0
        end = 0
        while end >= start and start <= goal:
            if end in endVisited:
                return False
            endVisited.add(end)
            if start <= goal and end >= goal:
                return True
            start += minJump
            end += maxJump
            start = self.trimStart(s, start)
            end = self.trimEnd(s, end, start)
        return False

    def trimStart(self, s, start):
        while start < len(s) and s[start] != "0":
            start += 1
        return start

    def trimEnd(self, s, end, start):
        while end < len(s) and end >= start and s[end] != "0":
            end -= 1
        return end