# O(n³)
# n = len(houses)


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        if len(houses) == 1:
            return 0

        clustersRes = {}
        for i in range(len(houses)):
            for j in range(i, len(houses)):
                median = houses[(i + j) // 2]
                clustersRes[(i, j)] = 0
                for t in range(i, j + 1):
                    clustersRes[(i, j)] += abs(houses[t] - median)

        return self.findCosts(clustersRes, 0, len(houses), k, {})

    def findCosts(self, clustersRes, i, numberOfHouses, remainingMailboxes, dp):
        if (i, remainingMailboxes) in dp:
            return dp[(i, remainingMailboxes)]
        if remainingMailboxes == 0:
            if i == numberOfHouses:
                return 0
            return float("inf")
        res = float("inf")
        for j in range(i, numberOfHouses):
            cost = clustersRes[(i, j)] + self.findCosts(
                clustersRes, j + 1, numberOfHouses, remainingMailboxes - 1, dp
            )
            res = min(res, cost)
        dp[(i, remainingMailboxes)] = res
        return res