# O(2ⁿ)
# n = len(s)


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        minRemovals = self.findNecessaryRemovals(s)
        res = set()
        self.explore(s, 0, 0, 0, [], minRemovals, res)
        return res

    def explore(self, s, pos, opened, closed, current, pendingRemovals, res):
        if pendingRemovals < 0:
            return
        if pos >= len(s):
            if pendingRemovals == 0 and opened == closed:
                res.add("".join(current))
            return

        if s[pos] == "(":
            self.explore(s, pos + 1, opened, closed, current, pendingRemovals - 1, res)
            current.append(s[pos])
            self.explore(s, pos + 1, opened + 1, closed, current, pendingRemovals, res)
            current.pop()
        elif s[pos] == ")":
            self.explore(s, pos + 1, opened, closed, current, pendingRemovals - 1, res)
            if closed < opened:
                current.append(s[pos])
                self.explore(
                    s, pos + 1, opened, closed + 1, current, pendingRemovals, res
                )
                current.pop()
        else:
            current.append(s[pos])
            self.explore(s, pos + 1, opened, closed, current, pendingRemovals, res)
            current.pop()

    def findNecessaryRemovals(self, s):
        res = 0
        opened = 0
        closed = 0
        for char in s:
            if char == "(":
                opened += 1
            elif char == ")":
                if opened > closed:
                    closed += 1
                else:
                    res += 1
        res += opened - closed
        return res