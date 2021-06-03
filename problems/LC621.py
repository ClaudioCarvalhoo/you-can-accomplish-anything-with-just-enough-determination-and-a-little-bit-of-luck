# O(n*log(t))
# n = n | t = len(set(tasks))

# Sol 1
import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        tasksCount = Counter(tasks)
        nextTasks = [(-tasksCount[task], task) for task in tasksCount]
        heapq.heapify(nextTasks)
        cooldownTasks = []
        while len(nextTasks) > 0 or len(cooldownTasks) > 0:
            if len(cooldownTasks) > 0 and res - cooldownTasks[0][0] > n:
                _, remainingTasks, task = heapq.heappop(cooldownTasks)
                heapq.heappush(nextTasks, (remainingTasks, task))
            if len(nextTasks) > 0:
                remainingTasks, task = heapq.heappop(nextTasks)
                remainingTasks += 1
                if remainingTasks < 0:
                    heapq.heappush(cooldownTasks, (res, remainingTasks, task))
            res += 1
        return res