# O(x * y)

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:
    def findSolution(self, customfunction: "CustomFunction", z: int) -> List[List[int]]:
        res = []
        x = 1
        y = 1

        while customfunction.f(x, y) <= z:
            initX = x
            initY = y

            if customfunction.f(x, y) == z:
                res.append([x, y])

            x += 1
            while customfunction.f(x, initY) <= z:
                if customfunction.f(x, initY) == z:
                    res.append([x, initY])
                x += 1

            y += 1
            while customfunction.f(initX, y) <= z:
                if customfunction.f(initX, y) == z:
                    res.append([initX, y])
                y += 1

            x = initX + 1
            y = initY + 1

        return res
