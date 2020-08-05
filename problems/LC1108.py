# O(n)
# n = len(address)

# Normal solution
class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for char in address:
            if char == ".":
                res += "[.]"
            else:
                res += char
        return res

# List comprehension solution     
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ''.join(['[.]' if x == '.' else x for x in address])