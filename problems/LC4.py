# O(log(n+m))
# n = len(nums1) | m = len(nums2)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        leftPartitionSize = math.ceil((len(nums1) + len(nums2)) / 2)
        isOdd = (len(nums1) + len(nums2)) % 2 != 0
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        p1SearchStart = 0
        p1SearchEnd = len(nums1)
        while True:
            p1 = (
                p1SearchStart + ((p1SearchEnd - p1SearchStart) // 2)
                if p1SearchEnd > 0
                else -1
            )
            p2 = leftPartitionSize - (p1 + 1) - 1
            if self.foundCorrectPartitions(nums1, nums2, p1, p2):
                if isOdd:
                    return self.getOddRes(nums1, nums2, p1, p2)
                else:
                    return self.getEvenRes(nums1, nums2, p1, p2)
            elif self.getValInPos(nums1, p1) > self.getValInPos(nums2, p2 + 1):
                p1SearchEnd = p1
            else:
                p1SearchStart = p1 + 1

    def getValInPos(self, array, pos):
        if pos < 0:
            return float("-inf")
        if pos >= len(array):
            return float("inf")
        return array[pos]

    def getOddRes(self, nums1, nums2, p1, p2):
        if p1 >= len(nums1) or p1 < 0:
            return nums2[p2]
        elif p2 >= len(nums2) or p2 < 0:
            return nums1[p1]
        else:
            return max(nums1[p1], nums2[p2])

    def getEvenRes(self, nums1, nums2, p1, p2):
        leftPartitionLast = None
        if p1 >= len(nums1) or p1 < 0:
            leftPartitionLast = nums2[p2]
        elif p2 >= len(nums2) or p2 < 0:
            leftPartitionLast = nums1[p1]
        else:
            leftPartitionLast = max(nums1[p1], nums2[p2])
        rightPartitionFirst = None
        if p1 + 1 >= len(nums1) or p1 + 1 < 0:
            rightPartitionFirst = nums2[p2 + 1]
        elif p2 + 1 >= len(nums2) or p2 + 1 < 0:
            rightPartitionFirst = nums1[p1 + 1]
        else:
            rightPartitionFirst = min(nums1[p1 + 1], nums2[p2 + 1])
        return (leftPartitionLast + rightPartitionFirst) / 2

    def foundCorrectPartitions(self, nums1, nums2, p1, p2):
        return self.getValInPos(nums1, p1) <= self.getValInPos(
            nums2, p2 + 1
        ) and self.getValInPos(nums2, p2) <= self.getValInPos(nums1, p1 + 1)
