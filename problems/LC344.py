# O(n)
# n = len(s)


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            self.swap(s, i, len(s) - 1 - i)

    def swap(self, s, i, j):
        s[i], s[j] = s[j], s[i]
