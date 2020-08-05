# O(n)
# n = len(candies)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if len(candies) == 1:
            return [True]
        
        greatest = 0
        for n in candies:
            if n > greatest:
                greatest = n
           
        res = []
        for kid in candies:
            if kid + extraCandies >= greatest:
                res.append(True)
            else:
                res.append(False)
                
        return res