# O(n*m)
# n = len(strs) | m = maxLen(strs)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            goal = strs[0][i]
            for string in strs:
                if i >= len(string) or string[i] != goal:
                    return strs[0][:i]
        return strs[0]