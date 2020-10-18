# O(n)


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 5:
            return n

        ugly = [1]
        multipliers = [0, 0, 0]

        while len(ugly) < n:
            next2 = ugly[multipliers[0]] * 2
            next3 = ugly[multipliers[1]] * 3
            next5 = ugly[multipliers[2]] * 5

            realNext = min(next2, next3, next5)

            ugly.append(realNext)

            if next2 == realNext:
                multipliers[0] += 1
            if next3 == realNext:
                multipliers[1] += 1
            if next5 == realNext:
                multipliers[2] += 1

        return ugly[-1]