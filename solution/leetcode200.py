from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.query_grid = [[0] * len(grid[0]) for _ in range(len(grid))]

        count = 0
        i = j = 0
        while not all([all(q) for q in self.query_grid]):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if self.query_grid[i][j]:
                        continue
                    if self.grid[i][j] == "0":
                        self.query(i, j)
                        continue
                    if self.grid[i][j] == "1":
                        count += 1
                        self.assemble_land(i, j)
        print(count)
        return count
    
    def query(self, i, j):
        if self.query_grid[i][j]:
            return True
        self.query_grid[i][j] = 1
        return False

    def assemble_land(self, i, j):
        if i >= len(self.grid) or j >= len(self.grid[0]) or i < 0 or j < 0:
            return
        if self.query_grid[i][j]:
            return
        if self.grid[i][j] == "0":
            self.query(i, j)
            return
        if self.grid[i][j] == "1":
            self.query(i, j)
            self.assemble_land(i-1, j)
            self.assemble_land(i, j-1)
            self.assemble_land(i+1, j)
            self.assemble_land(i, j+1)



Solution().numIslands(
    [["1", "1", "0"],
     ["1", "1", "0"],
     ["0", "0", "1"]]
)
        