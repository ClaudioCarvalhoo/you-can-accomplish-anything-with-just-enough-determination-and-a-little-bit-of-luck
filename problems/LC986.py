# O(n+m)
# n = len(firstList) | m = len(secondList)


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        res = []
        p1, p2 = 0, 0
        while p1 < len(firstList) and p2 < len(secondList):
            range1 = firstList[p1]
            range2 = secondList[p2]
            if range1[0] <= range2[0]:
                self.mergeRangesInRes(range1, range2, res)
            else:
                self.mergeRangesInRes(range2, range1, res)
            p1, p2 = self.movePointersToNextSmallestStart(firstList, secondList, p1, p2)
        return res

    def mergeRangesInRes(self, firstRange, secondRange, res):
        if firstRange[1] >= secondRange[0]:
            start = secondRange[0]
            end = min(firstRange[1], secondRange[1])
            if len(res) > 0 and start <= res[-1][1]:
                res[-1][1] = end
            else:
                res.append([start, end])

    def movePointersToNextSmallestStart(self, firstList, secondList, p1, p2):
        if p2 + 1 >= len(secondList):
            p1 += 1
        elif p1 + 1 >= len(firstList):
            p2 += 1
        elif firstList[p1 + 1][0] <= secondList[p2 + 1][0]:
            p1 += 1
        else:
            p2 += 1
        return (p1, p2)