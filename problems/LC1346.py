# O(n)
# n = len(arr)


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        table = {}
        for i in range(len(arr)):
            element = arr[i]
            if element in table:
                table[element].append(i)
            else:
                table[element] = [i]
        for i in range(len(arr)):
            target = arr[i] * 2
            if target in table:
                if len(table[target]) > 1 or table[target][0] != i:
                    return True
        return False