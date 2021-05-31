# O(log(n))

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        return self.searchBadVersion(0, n, n)

    def searchBadVersion(self, start, end, earliestBad):
        i = start + math.floor((end - start) / 2)

        if isBadVersion(i):
            if i == start:
                return i
            else:
                return self.searchBadVersion(start, i - 1, i)
        else:
            if i == end:
                return earliestBad
            else:
                return self.searchBadVersion(i + 1, end, earliestBad)
