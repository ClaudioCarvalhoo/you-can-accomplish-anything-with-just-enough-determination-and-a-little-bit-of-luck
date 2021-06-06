# O(n)
# n = len(mat)

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if self.isEqualMatrix(mat, target):
                return True
            self.rotate90(mat)
        return False
        
        
    def isEqualMatrix(self, mat, target):
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                if mat[y][x] != target[y][x]:
                    return False
        return True
    
        
    def rotate90(self, mat):
        for y in range(len(mat)):
            for x in range(y):
                mat[y][x], mat[x][y] = mat[x][y], mat[y][x]
        for y in range(len(mat)):
            for x in range(len(mat[y])//2):
                mat[y][x], mat[y][-x-1] = mat[y][-x-1], mat[y][x]
                
