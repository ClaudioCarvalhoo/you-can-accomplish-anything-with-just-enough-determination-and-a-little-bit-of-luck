# O(log(n))
# n = len(letters)


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = self.searchForNextIndex(letters, target)
        return letters[index % len(letters)]

    def searchForNextIndex(self, letters, target):
        start = 0
        end = len(letters)
        while start < end:
            midpoint = start + ((end - start) // 2)
            if letters[midpoint] > target:
                end = midpoint
            else:
                start = midpoint + 1
        return start