# O(n)
# n = n


class Solution:
    def numOfMinutes(
        self, n: int, headId: int, manager: List[int], informTime: List[int]
    ) -> int:
        subordinates = {employeeId: [] for employeeId in range(n)}
        for employeeId in range(n):
            if employeeId != headId:
                subordinates[manager[employeeId]].append(employeeId)
        return self.informBelow(headId, informTime, subordinates, 0)

    def informBelow(self, employeeId, informTime, subordinates, elapsedTime):
        res = elapsedTime + informTime[employeeId]
        for subordinateID in subordinates[employeeId]:
            res = max(
                res,
                self.informBelow(
                    subordinateID,
                    informTime,
                    subordinates,
                    elapsedTime + informTime[employeeId],
                ),
            )
        return res