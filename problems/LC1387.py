# O(unknown) https://en.wikipedia.org/wiki/Collatz_conjecture


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = {0: 1, 1: 0}
        arr = []
        for i in range(lo, hi + 1):
            self.calculatePower(i, powers)
            arr.append((i, powers[i]))
        return self.quickSelect(arr, k - 1, 0, len(arr) - 1)

    def calculatePower(self, i, powers):
        if i in powers:
            return powers[i]
        if i % 2 == 0:
            powers[i] = self.calculatePower(i // 2, powers) + 1
        else:
            powers[i] = self.calculatePower((3 * i) + 1, powers) + 1
        return powers[i]

    def quickSelect(self, arr, k, start, end):
        pivot = arr[end]
        i = start
        for j in range(start, end):
            if arr[j][1] < pivot[1] or (arr[j][1] == pivot[1] and arr[j][0] < pivot[0]):
                self.swap(arr, i, j)
                i += 1
        self.swap(arr, i, end)
        if i == k:
            return arr[i][0]
        elif i < k:
            return self.quickSelect(arr, k, i + 1, end)
        else:
            return self.quickSelect(arr, k, start, i - 1)

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
