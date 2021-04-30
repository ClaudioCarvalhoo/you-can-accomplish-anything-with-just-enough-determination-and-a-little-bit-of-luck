# O(g*log(g) + s*log(s))


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        currentCookie = 0
        satisfied = 0
        for childGreed in g:
            while currentCookie < len(s) and s[currentCookie] < childGreed:
                currentCookie += 1
            if currentCookie >= len(s):
                break
            satisfied += 1
            currentCookie += 1
        return satisfied