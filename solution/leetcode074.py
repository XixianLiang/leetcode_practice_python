from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_t, r_b = 0, len(matrix) - 1
        c_l, c_r = 0, len(matrix[0]) - 1
        
        while r_t <= r_b:
            r_m = (r_t + r_b) // 2
            if matrix[r_m][0] == target:
                return True
            elif matrix[r_m][0] < target:
                r_t = r_m + 1
            else:
                r_b = r_m - 1
        
        row = r_b
        
        while c_l <= c_r:
            c_m = (c_l + c_r) // 2
            if matrix[row][c_m] == target:
                return True
            elif matrix[row][c_m] < target:
                c_l = c_m + 1
            else:
                c_r = c_m - 1
        
        return False

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))