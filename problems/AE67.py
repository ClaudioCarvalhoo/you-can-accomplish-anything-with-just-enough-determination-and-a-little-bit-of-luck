# Balanced Brackets

# O(n)
# n = len(string)


def balancedBrackets(string):
    relevant = set(["(", "[", "{", ")", "]", "}"])
    closingDict = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for i in range(len(string)):
        cur = string[i]
        if cur in relevant:
            if cur in closingDict:
                stack.append(closingDict[cur])
            elif len(stack) > 0 and stack[-1] == cur:
                stack.pop()
            else:
                return False
    return len(stack) == 0
