class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        expression = self.parseExpression(expression)
        return self.helper(expression, 0, len(expression) - 1)

    def helper(self, expression, start, end):
        if start == end:
            return [expression[start]]
        res = []
        for i in range(start + 1, end, 2):
            leftRes = self.helper(expression, start, i - 1)
            rightRes = self.helper(expression, i + 1, end)
            for l in leftRes:
                for r in rightRes:
                    res.append(self.makeOperation(l, expression[i], r))
        return res

    def parseExpression(self, expression):
        res = []
        curNum = 0
        for char in expression:
            if char.isdigit():
                curNum *= 10
                curNum += int(char)
            else:
                res.append(curNum)
                curNum = 0
                res.append(char)
        res.append(curNum)
        return res

    def makeOperation(self, num1, operator, num2):
        if operator == "+":
            return num1 + num2
        if operator == "-":
            return num1 - num2
        if operator == "*":
            return num1 * num2