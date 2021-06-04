# O(k*nᵏ)
# n = n | k = k


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.explore(n, k, 0, [], res)
        return res

    def explore(self, n, k, currentElem, combination, res):
        if len(combination) == k:
            res.append(combination[:])
        else:
            for i in range(currentElem + 1, (n + 1) - (k - len(combination) - 1)):
                combination.append(i)
                self.explore(n, k, i, combination, res)
                combination.pop()