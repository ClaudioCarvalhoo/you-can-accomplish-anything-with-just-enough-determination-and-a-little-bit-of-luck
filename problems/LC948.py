# O(n log(n))
# n = len(tokens)


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:

        tokens.sort()

        unusedLargest = len(tokens) - 1
        points = 0

        for i in range(len(tokens)):
            if tokens[i] <= P:
                P -= tokens[i]
                points += 1
            else:
                if unusedLargest <= i:
                    return points
                while tokens[i] > P:
                    if unusedLargest <= i or points == 0:
                        return points
                    P += tokens[unusedLargest]
                    unusedLargest -= 1
                    points -= 1
                P -= tokens[i]
                points += 1

        return points