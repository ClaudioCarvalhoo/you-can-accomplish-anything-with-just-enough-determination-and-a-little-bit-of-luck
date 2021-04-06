# H-Tree Construction
# An H-tree is a geometric shape that consists of a repeating pattern resembles the letter “H”.

# It can be constructed by starting with a line segment of arbitrary length,
# drawing two segments of the same length at right angles to the first through its endpoints,
# and continuing in the same vein, reducing (dividing) the length of the line segments drawn at each stage by √2.

# Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates), a starting length, and depth.
# Assume that the starting line is parallel to the X-axis.

# Use the function drawLine provided to implement your algorithm.
# In a production code, a drawLine function would render a real line between two points.
# However, this is not a real production environment, so to make things easier,
# implement drawLine such that it simply prints its arguments (the print format is left to your discretion).

# Analyze the time and space complexity of your algorithm.
# In your analysis, assume that drawLine's time and space complexities are constant, i.e. O(1).

# Time:
# O(4^d)
# d = depth

# Space:
# O(d)
# d = depth


def drawHTree(x, y, length, depth):
    if depth == 0:
        return

    halfLineLength = length / 2
    leftX = x - halfLineLength
    rightX = x + halfLineLength
    upperY = y + halfLineLength
    lowerY = y - halfLineLength

    # Draw horizontal
    drawLine((leftX, y), (rightX, y))

    # Draw verticals
    drawLine((leftX, lowerY), (leftX, upperY))
    drawLine((rightX, lowerY), (rightX, upperY))

    # Call for each corner
    nextLength = length / sqrt(2)
    nextDepth = depth - 1
    drawHTree(leftX, lowerY, nextLength, nextDepth)
    drawHTree(leftX, upperY, nextLength, nextDepth)
    drawHTree(rightX, lowerY, nextLength, nextDepth)
    drawHTree(rightX, upperY, nextLength, nextDepth)


# O(4ˆN)
