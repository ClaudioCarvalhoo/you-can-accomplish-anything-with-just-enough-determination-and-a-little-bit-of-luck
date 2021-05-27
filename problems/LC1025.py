# Sol 1
# O(n²)
# n = n
class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False, False]
        for i in range(2, n + 1):
            found = False
            for j in range(1, i):
                if i % j == 0 and not dp[i - j]:
                    found = True
                    break
            dp.append(found)
        return dp[n]


# Sol 2
# O(1)
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
