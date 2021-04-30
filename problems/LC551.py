# O(n)
# n = len(s)


class Solution:
    def checkRecord(self, s: str) -> bool:
        absentBefore = False
        lateStreak = 0
        for day in s:
            if day == "A":
                if absentBefore:
                    return False
                absentBefore = True
            if day == "L":
                if lateStreak >= 2:
                    return False
                lateStreak += 1
            else:
                lateStreak = 0
        return True