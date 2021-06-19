# O(n*m)
# n = len(maze) | m = len(maze[0])


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        return self.explore(
            maze, start[0], start[1], "stop", destination[0], destination[1], set()
        )

    def explore(self, maze, y, x, direction, destY, destX, visited):
        if (y, x, direction) in visited:
            return False
        if y == destY and x == destX and direction == "stop":
            return True

        visited.add((y, x, direction))
        if direction == "stop":
            for nextMove in self.getNextMovesStopped(maze, y, x):
                if self.explore(
                    maze, nextMove[0], nextMove[1], nextMove[2], destY, destX, visited
                ):
                    return True
        else:
            nextMove = self.getNextMoveMoving(maze, y, x, direction)
            if self.explore(
                maze, nextMove[0], nextMove[1], nextMove[2], destY, destX, visited
            ):
                return True
        return False

    def getNextMovesStopped(self, maze, y, x):
        res = []
        if y - 1 >= 0 and maze[y - 1][x] == 0:
            res.append((y - 1, x, "up"))
        if y + 1 < len(maze) and maze[y + 1][x] == 0:
            res.append((y + 1, x, "down"))
        if x - 1 >= 0 and maze[y][x - 1] == 0:
            res.append((y, x - 1, "left"))
        if x + 1 < len(maze[y]) and maze[y][x + 1] == 0:
            res.append((y, x + 1, "right"))
        return res

    def getNextMoveMoving(self, maze, y, x, direction):
        if direction == "up":
            if y - 1 < 0 or maze[y - 1][x] == 1:
                return (y, x, "stop")
            return (y - 1, x, "up")
        if direction == "down":
            if y + 1 >= len(maze) or maze[y + 1][x] == 1:
                return (y, x, "stop")
            return (y + 1, x, "down")
        if direction == "left":
            if x - 1 < 0 or maze[y][x - 1] == 1:
                return (y, x, "stop")
            return (y, x - 1, "left")
        if direction == "right":
            if x + 1 >= len(maze[y]) or maze[y][x + 1] == 1:
                return (y, x, "stop")
            return (y, x + 1, "right")
