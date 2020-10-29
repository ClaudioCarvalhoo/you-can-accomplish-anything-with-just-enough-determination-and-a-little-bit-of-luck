# O(n)
# n = len(s)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = self.adjustLeftPointer(s, 0)
        right = self.adjustRightPointer(s, len(s) - 1)

        while left < right:
            if s[left].lower() != s[right].lower():
                return False

            left = self.adjustLeftPointer(s, left + 1)
            right = self.adjustRightPointer(s, right - 1)

        return True

    def adjustLeftPointer(self, s, left):
        while left < len(s) and not s[left].isalnum():
            left += 1
        return left

    def adjustRightPointer(self, s, right):
        while right >= 0 and not s[right].isalnum():
            right -= 1
        return right
