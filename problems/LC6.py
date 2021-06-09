# O(n)
# n = len(s)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        curRow = 0
        goDown = False
        for char in s:
            rows[curRow].append(char)
            if curRow == 0 or curRow == numRows - 1:
                goDown = not goDown
            curRow += 1 if goDown else -1
        res = []
        for row in rows:
            for char in row:
                res.append(char)
        return "".join(res)
