# O(n)
# n = len(s)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        s = "1[" + s + "]"
        i = 0
        while i < len(s) - 1:
            char = s[i]
            if char.isdigit():
                digit = char
                while s[i + 1].isdigit():
                    digit += s[i + 1]
                    i += 1
                stack.append({"quant": int(digit), "string": ""})
                i += 1
            elif char == "]":
                toAdd = stack.pop()
                stack[-1]["string"] += toAdd["quant"] * toAdd["string"]
            elif char:
                stack[-1]["string"] += char
            i += 1

        return stack.pop()["string"]


class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        res, end = self.helper(s, 0, 1)
        return ''.join(res)
        
    def helper(self, s, start, repeats):
        i = start
        res = []
        while i < len(s) and s[i] != "]":
            if not s[i].isdigit():
                res.append(s[i])
            else:
                subRes, end = self.decodeSubsequence(s, i)
                res += subRes
                i = end
            i += 1
        return (res * repeats, i)
                
                
    def decodeSubsequence(self, s, start):
        i = start
        number = 0
        while s[i].isdigit():
            number = (number*10) + int(s[i])
            i += 1
        res, end = self.helper(s, i+1, number)
        return (res, end)
