# O(n)
# n = len(height)

# Sol 1 | O(n) Space
class Solution:
    def trap(self, height: List[int]) -> int:
        maxAfter = [0 for _ in height]
        for i in range(len(height) - 2, -1, -1):
            maxAfter[i] = max(maxAfter[i + 1], height[i + 1])

        res = 0
        previousMax = 0
        for i in range(1, len(height)):
            previousMax = max(previousMax, height[i - 1])
            res += max(0, min(previousMax, maxAfter[i]) - height[i])
        return res


# Sol 2 | O(1) Space
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        res = 0
        leftMax = height[0]
        rightMax = height[-1]
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                left += 1
                res += max(0, min(leftMax, rightMax) - height[left])
                leftMax = max(leftMax, height[left])
            else:
                right -= 1
                res += max(0, min(leftMax, rightMax) - height[right])
                rightMax = max(rightMax, height[right])
        return res
