# O(n)
# n = len(s)

# Sol 1
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opening = 0
        markToRemove = set()
        for i in range(len(s)):
            if s[i] == "(":
                opening += 1
            elif s[i] == ")":
                if opening == 0:
                    markToRemove.add(i)
                else:
                    opening -= 1

        closing = 0
        for i in range(len(s) - 1, -1, -1):
            if i not in markToRemove and s[i] == ")":
                closing += 1
            elif s[i] == "(":
                if closing == 0:
                    markToRemove.add(i)
                else:
                    closing -= 1

        res = []
        for i in range(len(s)):
            if i not in markToRemove:
                res.append(s[i])
        return "".join(res)


# Sol 2
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        markToRemove = set()
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) == 0:
                    markToRemove.add(i)
                else:
                    stack.pop()
        for i in stack:
            markToRemove.add(i)

        res = []
        for i in range(len(s)):
            if i not in markToRemove:
                res.append(s[i])
        return "".join(res)
