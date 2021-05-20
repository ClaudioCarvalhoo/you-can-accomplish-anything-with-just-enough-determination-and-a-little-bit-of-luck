# Largest Rectangle Under Skyline

# O(n)
# n = len(buildings)


def largestRectangleUnderSkyline(buildings):
    maxArea = 0
    stack = []

    buildings.append(0)
    for i in range(len(buildings)):
        while len(stack) > 0 and buildings[stack[-1]] >= buildings[i]:
            height = buildings[stack.pop()]
            width = i if len(stack) <= 0 else i - stack[-1] - 1
            maxArea = max(maxArea, width * height)
        stack.append(i)
    return maxArea
