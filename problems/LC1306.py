# O(n)
# n = len(arr)


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        canGetTo = set()
        return self.explore(arr, start, canGetTo)

    def explore(self, arr, i, canGetTo):
        if i in canGetTo or i < 0 or i >= len(arr):
            return False
        if arr[i] == 0:
            return True
        canGetTo.add(i)
        return self.explore(arr, i + arr[i], canGetTo) or self.explore(
            arr, i - arr[i], canGetTo
        )
