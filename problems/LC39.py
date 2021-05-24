# O(Nᵗ)
# n = len(candidates) | t = target


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.explore(candidates, target, 0, [], 0, res)
        return res

    def explore(self, candidates, target, startAt, current, currentSum, res):
        if currentSum > target:
            return
        if currentSum == target:
            res.append(current[:])
        for i in range(startAt, len(candidates)):
            candidate = candidates[i]
            current.append(candidate)
            currentSum += candidate
            self.explore(candidates, target, i, current, currentSum, res)
            current.pop()
            currentSum -= candidate
