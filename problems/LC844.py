# O(n+m) time | O(1) space
# n = len(s) | m = len(t)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = self.moveBackspaces(s, len(s)-1)
        p2 = self.moveBackspaces(t, len(t)-1)
        while p1 >= 0 and p2 >= 0:
            if s[p1] != t[p2]:
                return False
            p1 = self.moveBackspaces(s, p1-1)
            p2 = self.moveBackspaces(t, p2-1)
        return p1 < 0 and p2 < 0
                    
    def moveBackspaces(self, string, i):
        if string[i] == "#":
            backspaces = 1
            i -= 1
            while i >= 0 and (string[i] == "#" or backspaces > 0):
                if string[i] == "#":
                    backspaces += 1
                else:
                    backspaces -= 1
                i -= 1
        return i
