# O(d*f*t)
# d = d | f = f | t = target


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return self.explore(d, f, target, {}) % ((10 ** 9) + 7)

    def explore(self, dices, faces, target, dp):
        if (dices, target) in dp:
            return dp[(dices, target)]
        if dices <= 0 or target <= 0:
            return 0
        if dices == 1:
            return 1 if target <= faces else 0

        res = 0
        for i in range(1, faces + 1):
            res += self.explore(dices - 1, faces, target - i, dp)
        dp[(dices, target)] = res
        return dp[(dices, target)]