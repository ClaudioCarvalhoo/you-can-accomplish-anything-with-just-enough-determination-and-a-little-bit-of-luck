# O(n)
# n = len(s)


class Solution:
    def calculate(self, s: str) -> int:
        buf = ""
        operations = []
        for i in range(len(s)):
            cur = s[i]
            if cur.isdigit():
                buf += cur
            elif cur == "+" or cur == "-" or cur == "*" or cur == "/":
                operations.append(int(buf))
                operations.append(cur)
                buf = ""
        operations.append(int(buf))

        secondOperations = []
        i = 0
        while i < len(operations):
            cur = operations[i]
            if cur == "*":
                a = secondOperations.pop()
                b = operations[i + 1]
                secondOperations.append(a * b)
                i += 1
            elif cur == "/":
                a = secondOperations.pop()
                b = operations[i + 1]
                secondOperations.append(a // b)
                i += 1
            else:
                secondOperations.append(cur)
            i += 1

        res = secondOperations[0]
        i = 1
        while i < len(secondOperations):
            cur = secondOperations[i]
            if cur == "+":
                res += secondOperations[i + 1]
                i += 1
            if cur == "-":
                res -= secondOperations[i + 1]
                i += 1
            i += 1

        return res