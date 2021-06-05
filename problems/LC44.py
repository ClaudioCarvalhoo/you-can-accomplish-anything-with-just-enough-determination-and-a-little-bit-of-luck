# O(2ⁿ⁺ᵐ)
# n = len(string) | m = len(pattern)


class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        cleanPattern = []
        for i in range(len(pattern)):
            if i == 0 or pattern[i] != "*" or pattern[i - 1] != "*":
                cleanPattern.append(pattern[i])
        return self.matchUpToWildcard(string, cleanPattern, 0, 0, {})

    def matchUpToWildcard(self, string, pattern, stringIndex, patternIndex, dp):
        dpPos = (stringIndex, patternIndex)
        if dpPos in dp:
            return dp[dpPos]

        while patternIndex < len(pattern):
            if pattern[patternIndex] == "*":
                dp[dpPos] = self.matchWildcard(
                    string, pattern, stringIndex, patternIndex, dp
                )
                return dp[dpPos]
            elif stringIndex >= len(string) or (
                pattern[patternIndex] != "?"
                and string[stringIndex] != pattern[patternIndex]
            ):
                dp[dpPos] = False
                return dp[dpPos]
            stringIndex += 1
            patternIndex += 1
        dp[dpPos] = stringIndex == len(string)
        return dp[dpPos]

    def matchWildcard(self, string, pattern, stringIndex, patternIndex, dp):
        while stringIndex <= len(string):
            if self.matchUpToWildcard(
                string, pattern, stringIndex, patternIndex + 1, dp
            ):
                return True
            stringIndex += 1
        return False