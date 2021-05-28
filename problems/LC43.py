# O(n*m)
# n = len(num1) | m = len(num2)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        if len(num2) > len(num1):
            num1, num2 = num2, num1

        parts = []
        for i in range(len(num2) - 1, -1, -1):
            n2 = self.digitToInt(num2[i])
            carry = 0
            part = []
            for j in range(len(num1) - 1, -1, -1):
                n1 = self.digitToInt(num1[j])
                res = (n1 * n2) + carry
                part.append(res % 10)
                carry = res // 10
            if carry > 0:
                part.append(carry)
            parts.append(part)

        res = []
        for i in range(len(parts)):
            part = parts[i]
            for j in range(len(part)):
                if i + j >= len(res):
                    res.append(part[j])
                else:
                    res[i + j] += part[j]

        carry = 0
        for i in range(len(res)):
            res[i] = res[i] + carry
            carry = res[i] // 10
            res[i] = str(res[i] % 10)
        if carry > 0:
            res.append(str(carry))

        res.reverse()
        return "".join(res)

    def digitToInt(self, n):
        return ord(n) - ord("0")
