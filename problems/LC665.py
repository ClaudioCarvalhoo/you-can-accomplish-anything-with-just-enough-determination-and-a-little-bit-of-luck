# O(n)
# n = len(nums)

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        
        modified = False
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if not modified:
                    if i == 0 or nums[i-1] <= nums[i+1]:
                        nums[i] = nums[i+1]
                    else:
                        nums[i+1] = nums[i]
                    modified = True
                else:
                    return False
                
        return True