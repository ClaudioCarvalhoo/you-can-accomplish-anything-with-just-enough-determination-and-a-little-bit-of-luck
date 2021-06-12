# O(log(n))
# n = len(mountain)

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain: "MountainArray") -> int:
        peakIndex = self.findPeak(mountain)
        if mountain.get(peakIndex) == target:
            return peakIndex

        leftRes = self.binarySearch(mountain, 0, peakIndex, target, True)
        if leftRes is not None:
            return leftRes
        rightRes = self.binarySearch(
            mountain, peakIndex + 1, mountain.length(), target, False
        )
        if rightRes is not None:
            return rightRes
        return -1

    def findPeak(self, mountain):
        start = 0
        end = mountain.length()
        while start < end:
            midpoint = start + ((end - start) // 2)
            candidate = mountain.get(midpoint)
            if (
                mountain.get(midpoint - 1) < candidate
                and mountain.get(midpoint + 1) < candidate
            ):
                return midpoint
            elif candidate > mountain.get(midpoint - 1):
                start = midpoint + 1
            else:
                end = midpoint
        return start

    def binarySearch(sekf, mountain, start, end, target, ascending):
        while start < end:
            midpoint = start + ((end - start) // 2)
            if mountain.get(midpoint) == target:
                return midpoint
            elif mountain.get(midpoint) < target:
                if ascending:
                    start = midpoint + 1
                else:
                    end = midpoint
            else:
                if ascending:
                    end = midpoint
                else:
                    start = midpoint + 1
        return None