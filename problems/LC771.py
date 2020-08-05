# O(n + m)
# n = len(J) | m = len(S)

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {}
        count = 0
        for jewel in J:
            jewels[jewel] = True
            
        for stone in S:
            if stone in jewels:
                count += 1
                
        return count