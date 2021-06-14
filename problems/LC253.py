# O(n*log(n))
# n = len(intervals)

import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        nextAvailable = []
        intervals.sort(key=lambda x: x[0])
        res = 0
        for meeting in intervals:
            if len(nextAvailable) == 0 or nextAvailable[0] > meeting[0]:
                heapq.heappush(nextAvailable, meeting[1])
                res = max(res, len(nextAvailable))
            else:
                heapq.heappop(nextAvailable)
                heapq.heappush(nextAvailable, meeting[1])
        return res