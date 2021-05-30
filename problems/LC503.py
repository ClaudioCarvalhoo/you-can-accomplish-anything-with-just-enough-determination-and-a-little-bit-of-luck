# O(n)
# n = len(nums)


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nextGreater = [-1 for _ in range(len(nums))]
        for i in range((len(nums) * 2) - 1, -1, -1):
            currentElem = nums[i % len(nums)]
            while len(stack) > 0 and stack[-1] <= currentElem:
                stack.pop()
            if len(stack) > 0:
                nextGreater[i % len(nums)] = stack[-1]
            stack.append(currentElem)
        return nextGreater