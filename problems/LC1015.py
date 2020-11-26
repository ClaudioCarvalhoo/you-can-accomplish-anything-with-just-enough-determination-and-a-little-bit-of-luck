# O(K)


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0:
            return -1
        used = {}
        check = 1
        while True:
            rest = check % K
            if rest == 0:
                return len(str(check))
            elif rest in used:
                return -1
            else:
                used[rest] = True
            check = check * 10 + 1