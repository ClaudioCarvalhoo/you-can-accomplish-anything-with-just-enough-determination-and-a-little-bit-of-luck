# O(n)
# n = len(chalk)


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalkSum = sum(chalk)
        remainingChalk = k % chalkSum

        for i in range(len(chalk)):
            if remainingChalk < chalk[i]:
                return i
            remainingChalk -= chalk[i]
        return len(chalk) - 1
