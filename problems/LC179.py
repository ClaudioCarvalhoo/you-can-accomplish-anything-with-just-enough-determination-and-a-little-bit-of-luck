# O(n*log(n))

from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        nums.sort(key=cmp_to_key(self.sortCustom))
        res = ""
        for i in nums:
            res += str(i)
        return str(int(res))
            
            
    def sortCustom(self, num1, num2):
        res1 = int(str(num1) + str(num2))
        res2 = int(str(num2) + str(num1))
        if res1 >= res2:
            return -1
        else:
            return 1
        
        
