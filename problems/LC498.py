# O(n*m)
# n = len(matrix) | m = len(matrix[0])

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        movingLeft = False
        res = []
        currentX = 0
        currentY = 0
        
        if len(matrix) == 0:
            return res
        
        while(len(res) < len(matrix) * len(matrix[0])):
            res.append(matrix[currentY][currentX])
            if movingLeft:
                currentX -= 1
                currentY += 1
            else:
                currentX += 1
                currentY -= 1
                
            # Top-right corner
            if currentY < 0 and currentX >= len(matrix[0]):
                currentY = 1
                currentX = len(matrix[0]) - 1
                movingLeft = True
            # Bottom-left corner
            elif currentY >= len(matrix) and currentX < 0:
                currentX = 1
                currentY = len(matrix) - 1
                movingLeft = False
            # Overflowed top going right
            elif currentY < 0:
                currentY = 0
                movingLeft = True
            # Overflowed bottom going left
            elif currentY >= len(matrix):
                currentY = len(matrix) - 1
                currentX += 2
                movingLeft = False
            # Overflowed left going down
            elif currentX < 0:
                currentX = 0
                movingLeft = False
            # Overflowed right going up
            elif currentX >= len(matrix[0]):
                currentX = len(matrix[0]) - 1
                currentY += 2
                movingLeft = True

        return res