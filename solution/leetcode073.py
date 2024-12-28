from typing import List


class SettingZero:
    def __init__(self):
        self.x = set()
        self.y = set()

    def set_zero(self, x, y):
        self.x.add(x)
        self.y.add(y)

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        setting_zero = SettingZero()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    setting_zero.set_zero(i, j)

        for x in setting_zero.x:
            for col in range(len(matrix[0])):
                matrix[x][col] = 0
        for y in setting_zero.y:
            for row in range(len(matrix)):
                matrix[row][y] = 0
