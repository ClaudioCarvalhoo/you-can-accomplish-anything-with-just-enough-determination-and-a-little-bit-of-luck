# O(n)
# n = len(s)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.checkShiftedPalindrome(
                    s, left + 1, right
                ) or self.checkShiftedPalindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True

    def checkShiftedPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True