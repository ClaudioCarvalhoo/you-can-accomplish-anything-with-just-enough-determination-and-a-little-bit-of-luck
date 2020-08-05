# O(n)
# n = len(nums)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        res = 0
        
        for i in nums:
            if i in count and count[i] > 0:
                res += count[i]
                count[i] += 1
            else:
                count[i] = 1
            
        return res
        
        