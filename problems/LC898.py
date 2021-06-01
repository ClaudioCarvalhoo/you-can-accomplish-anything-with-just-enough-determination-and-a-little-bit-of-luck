# O(n*k)
# n = len(A) | k = maxBinaryLen(A)


class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res = set()
        previousResults = set()
        for num in A:
            res.add(num)
            temp = set([num])
            for prevResult in previousResults:
                value = num | prevResult
                temp.add(value)
                res.add(value)
            previousResults = temp
        return len(res)