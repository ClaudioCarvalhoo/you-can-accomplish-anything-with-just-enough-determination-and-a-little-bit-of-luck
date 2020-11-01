# O(n + n)
# n = len(arr) | m = len(pieces)


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        table = {}
        for i in range(len(pieces)):
            table[pieces[i][0]] = i

        i = 0
        while i < len(arr):
            cur = arr[i]
            if cur not in table:
                return False
            else:
                place = table[cur]
                for x in pieces[place]:
                    if arr[i] != x:
                        return False
                    i += 1

        return True