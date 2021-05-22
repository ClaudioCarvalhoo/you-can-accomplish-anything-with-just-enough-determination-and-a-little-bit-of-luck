# O(~2ⁿ)
# n = n


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.explore(n, 0, [], res)
        return res

    def explore(self, toOpen, toClose, cur, res):
        if toOpen == 0 and toClose == 0:
            res.append("".join(cur))
        if toOpen > 0:
            cur.append("(")
            self.explore(toOpen - 1, toClose + 1, cur, res)
            cur.pop()
        if toClose > 0:
            cur.append(")")
            self.explore(toOpen, toClose - 1, cur, res)
            cur.pop()