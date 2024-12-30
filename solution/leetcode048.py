from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from math import floor
        self.matrix = matrix
        self.n = len(matrix)
        self.change_elements_coordinate = []
        if self.n % 2 != 0:
            matrix_r = floor(self.n / 2)
            print(matrix_r)
            for r in range(matrix_r):
                cur_change_elements = (matrix_r - r) * 2
                i, j = int(self.n / 2) - (matrix_r - r), int(self.n / 2) - (matrix_r - r)
                for k in range(cur_change_elements):
                    self.change_elements_coordinate.append((i, j))
                    i += 1
        else:
            matrix_r = self.n // 2
            for i in range(matrix_r):
                for j in range(matrix_r):
                    self.change_elements_coordinate.append((i, j))
        
        self.rotate_element()
        pass
        
    def rotate_element(self):
        for i, j in self.change_elements_coordinate:
            rotate_cooridinates = self.get_rotate_coordinate(i, j, self.n)
            # 获取每个元素的新值
            new_value = [None for _ in range(4)]
            for k in range(4):
                new_value_coordinate = rotate_cooridinates[(k + 3) % 4]
                new_value[k] = self.matrix[new_value_coordinate[0]][new_value_coordinate[1]]
            # 更新值
            for k in range(4):
                _i, _j = rotate_cooridinates[k]
                self.matrix[_i][_j] = new_value[k]
                
                
                
    
    def get_rotate_coordinate(self, i, j, n):
        rotate_coordinate = []
        rotate_coordinate.append((i, j))
        rotate_coordinate.append((j, n - i - 1))
        rotate_coordinate.append((n - i - 1, n - j - 1))
        rotate_coordinate.append((n - j - 1, i))
        return rotate_coordinate
                
            



# [0, 2, 3, 4, 5]
# [0, 0, 3, 4, 5]
# [0, 0, 0, 4, 5]
# [0, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]


# print(Solution().get_rotate_coordinate(2, 0, 7))

# 2, 0 -> 0, 4 -> 4, 6, -> 6, 2

# [1, 1, 1, 1, 1, 1 ,1]
# [1, 1, 1, 1, 1, 1 ,1]
# [1, 1, 1, 1, 1, 1 ,1]
# [1, 1, 1, 1, 1, 1 ,1]
# [1, 1, 1, 1, 1, 1 ,1]
# [1, 1, 1, 1, 1, 1 ,1]
# [1, 1, 1, 1, 1, 1 ,1]

Solution().rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
