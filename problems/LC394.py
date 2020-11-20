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
