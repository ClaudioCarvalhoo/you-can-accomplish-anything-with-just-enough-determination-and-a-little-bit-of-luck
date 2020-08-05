class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if not haystack[i+j] == needle[j]:
                        break
                    elif j == len(needle) -1:
                        return i
        
        return -1