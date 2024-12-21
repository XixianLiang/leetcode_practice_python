from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        
        state_trans = {"right":"down", 
                       "down":"left",
                       "left":"up",
                       "up":"right"}
        
        if n == 1:
            return[[1]]
        else:
            i = j = 0
            count = 1
            state = "right"
            while True:
                if count == n**2 + 1:
                    break
                if state == "right":
                    matrix[i][j] = count
                    count += 1
                    j += 1
                    if j + 1 >= n or matrix[i][j+1]:
                        state = state_trans[state]
                elif state == "down":
                    matrix[i][j] = count
                    count += 1
                    i += 1
                    if i + 1 >= n or matrix[i + 1][j]:
                        state = state_trans[state]
                elif state == "left":
                    matrix[i][j] = count
                    count += 1
                    j -= 1
                    if j - 1 < 0 or matrix[i][j - 1]:
                        state = state_trans[state]
                elif state == "up":
                    matrix[i][j] = count
                    count += 1
                    i -= 1
                    if i - 1 < 0 or matrix[i - 1][j]:
                        state = state_trans[state]
        return matrix
                        
print(Solution().generateMatrix(3))