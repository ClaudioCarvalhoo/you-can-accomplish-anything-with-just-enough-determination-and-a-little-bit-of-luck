# O(n)
# n = len(x)

import math

# Using string conversion
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        
        x = str(x)
        for i in range(math.floor(len(x)/2)):
            if x[i] == x[-1 * (i + 1)]:
                continue
            else:
                return False
            
        return True

# Without string conversion
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        
        initial = x
        reverse = 0
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = math.floor(x/10)
            
        return initial == reverse