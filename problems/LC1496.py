# O(n)
# n = len(path)


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        beenTo = set()
        beenTo.add((0, 0))
        x = 0
        y = 0
        for direction in path:
            if direction == "N":
                y += 1
            elif direction == "E":
                x += 1
            elif direction == "S":
                y -= 1
            else:
                x -= 1
            if (x, y) in beenTo:
                return True
            beenTo.add((x, y))
        return False