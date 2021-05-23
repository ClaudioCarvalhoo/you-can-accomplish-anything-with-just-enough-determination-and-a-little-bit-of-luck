# O(n*log(k))
# n = len(dist) | k = max(max(dist), lastStretchTime)


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        start = 1
        lastStretchTime = math.ceil(dist[-1] / (hour % 1)) if hour % 1 > 0 else 0
        end = max(max(dist), lastStretchTime) + 1

        best = float("inf")
        while start < end:
            midpoint = start + (end - start) // 2
            if self.isPossible(dist, hour, midpoint):
                best = min(best, midpoint)
                end = midpoint
            else:
                start = midpoint + 1

        return best if best != float("inf") else -1

    def isPossible(self, dist, hour, midpoint):
        total = 0
        for i in range(len(dist)):
            if i != len(dist) - 1:
                total += math.ceil(dist[i] / midpoint)
            else:
                total += dist[i] / midpoint
        return total <= hour