# O(n * log(n))
# n = len(intervals)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: (interval[0], interval[1]))
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            current = res[-1]
            interval = intervals[i]
            if interval[0] <= current[1]:
                current[1] = max(current[1], interval[1])
            else:
                res.append(interval)
        return res
        