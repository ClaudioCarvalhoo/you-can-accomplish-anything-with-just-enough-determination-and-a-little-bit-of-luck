# O(n*log(n))
# n = len(endTime)


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort(key=lambda x: x[1])

        maxProfitInTime = [(0, job[1]) for job in jobs]
        for i in range(len(jobs)):
            startTime, endTime, profit = jobs[i]
            maxProfitUpToStart = self.searchMaxProfitUpToTime(
                maxProfitInTime, i, startTime
            )
            maxProfitAtCurrentTime = max(
                maxProfitUpToStart + profit, maxProfitInTime[i - 1][0]
            )
            maxProfitInTime[i] = (maxProfitAtCurrentTime, endTime)
        return maxProfitInTime[-1][0]

    def searchMaxProfitUpToTime(self, maxProfitInTime, end, time):
        start = 0
        while start < end:
            midpoint = start + ((end - start) // 2)
            if (
                maxProfitInTime[midpoint][1] <= time
                and maxProfitInTime[midpoint + 1][1] > time
            ):
                return maxProfitInTime[midpoint][0]
            elif maxProfitInTime[midpoint][1] < time:
                start = midpoint + 1
            else:
                end = midpoint
        return 0