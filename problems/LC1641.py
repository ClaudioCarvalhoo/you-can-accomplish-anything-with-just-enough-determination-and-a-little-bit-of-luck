# O(n)
# n = n

class Solution:
    def countVowelStrings(self, n: int) -> int:
        endWith = {"a": {1: 1}, "e": {1: 1}, "i": {1: 1}, "o": {1: 1}, "u": {1: 1}}
        
        for i in range(2, n+1):
            endWith["a"][i] = endWith["a"][i-1]
            endWith["e"][i] = endWith["a"][i-1] + endWith["e"][i-1]
            endWith["i"][i] = endWith["a"][i-1] + endWith["e"][i-1] + endWith["i"][i-1]
            endWith["o"][i] = endWith["a"][i-1] + endWith["e"][i-1] + endWith["i"][i-1] + endWith["o"][i-1]
            endWith["u"][i] = endWith["a"][i-1] + endWith["e"][i-1] + endWith["i"][i-1] + endWith["o"][i-1] + endWith["u"][i-1]
            
        return endWith["a"][n] + endWith["e"][n] + endWith["i"][n] + endWith["o"][n] + endWith["u"][n]