from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                if self.bi_search(row, target):
                    return True
        return False
    
    def bi_search(self, row, target):
        i, j = 0, len(row) - 1
        while i <= j:
            m = (i + j) // 2
            if row[m] == target:
                return True
            elif row[m] < target:
                i = m + 1
            else:
                j = m - 1
        return False
        
                    


print(
    Solution().searchMatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        target=15,
    )
)
