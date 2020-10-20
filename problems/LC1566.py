# O(n)
# n = len(arr)


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if len(arr) < m * k:
            return False

        count = 0
        for i in range(len(arr)):
            if not i + m >= len(arr) and arr[i] == arr[i + m]:
                count += 1
            else:
                count = 0

            if count >= m * (k - 1):
                return True

        return False
