from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        time = 0
        while True:
            if self.all_rot():
                return time
            if time > len(self.grid) * len(self.grid[0]):
                return -1
            needs_to_rot = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if self.grid[i][j] == 2:
                        needs_to_rot.append([i, j])
            for needs_to_rot_x_y in needs_to_rot:
                self.rots(*needs_to_rot_x_y)
            time += 1

    def all_rot(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    return False
        return True

    def rots(self, i, j):
        if i - 1 >= 0 and self.grid[i - 1][j] == 1:
            self.grid[i - 1][j] = 2
        if i + 1 < len(self.grid) and self.grid[i + 1][j] == 1:
            self.grid[i + 1][j] = 2
        if j - 1 >= 0 and self.grid[i][j - 1] == 1:
            self.grid[i][j - 1] = 2
        if j + 1 < len(self.grid[0]) and self.grid[i][j + 1] == 1:
            self.grid[i][j + 1] = 2


print(Solution().orangesRotting([[1, 2]]))
