class Solution:
    def isHappy(self, n: int) -> bool:
        table = set()
        while n != 1:
            if n in table:
                return False
            table.add(n)
            n = str(n)
            tmp = 0
            for i in n:
                tmp += int(i) ** 2
            n = tmp
        return True