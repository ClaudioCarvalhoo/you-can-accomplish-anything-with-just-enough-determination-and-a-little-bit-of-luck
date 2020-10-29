# O(n)
# n = len(intervals)

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        start = newInterval[0]
        finish = newInterval[1]

        firstPosition = None
        i = 0
        if start < intervals[0][0]:
            intervals = [[start, start]] + intervals
            firstPosition = 0
        else:
            for i in range(len(intervals)):
                current = intervals[i]
                if start >= current[0] and start <= current[1]:
                    firstPosition = i
                    break
                elif i + 1 < len(intervals) and start < intervals[i + 1][0]:
                    intervals = (
                        intervals[: i + 1] + [[start, start]] + intervals[i + 1 :]
                    )
                    firstPosition = i + 1
                    break
            if firstPosition == None:
                intervals.append([start, finish])
                return intervals

        finishPosition = None
        for i in range(len(intervals)):
            current = intervals[i]
            if finish >= current[0] and finish <= current[1]:
                finishPosition = i
                break
            elif i + 1 < len(intervals) and finish < intervals[i + 1][0]:
                intervals = intervals[: i + 1] + [[finish, finish]] + intervals[i + 1 :]
                finishPosition = i + 1
                break
        if finishPosition == None:
            intervals.append([finish, finish])
            finishPosition = len(intervals) - 1

        return (
            intervals[:firstPosition]
            + [[intervals[firstPosition][0], intervals[finishPosition][1]]]
            + intervals[finishPosition + 1 :]
        )
