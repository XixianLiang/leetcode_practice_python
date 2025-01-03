from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word[0]:
                    used[i][j] = True
                    if self.backtracking(word[1:], used, i, j):
                        return True
                    used[i][j] = False
        return False

    def backtracking(self, cur_word, used, i, j):
        if len(cur_word) == 0:
            return True

        ans = [False] * 4

        if (_i := i - 1) >= 0 and not used[_i][j]:
            if cur_word[0] == self.board[_i][j]:
                used[_i][j] = True
                ans[0] = self.backtracking(cur_word[1:], used, _i, j)
                used[_i][j] = False

        if (_j := j - 1) >= 0 and not used[i][_j]:
            if cur_word[0] == self.board[i][_j]:
                used[i][_j] = True
                ans[1] = self.backtracking(cur_word[1:], used, i, _j)
                used[i][_j] = False

        if (_j := j + 1) < self.cols and not used[i][_j]:
            if cur_word[0] == self.board[i][_j]:
                used[i][_j] = True
                ans[2] = self.backtracking(cur_word[1:], used, i, _j)
                used[i][_j] = False

        if (_i := i+1) < self.rows and not used[_i][j]:
            if cur_word[0] == self.board[_i][j]:
                used[_i][j] = True
                ans[3] = self.backtracking(cur_word[1:], used, _i, j)
                used[_i][j] = False

        return any(ans)


print(
    Solution().exist(
        board=[["A", "B", "C", "E"],
               ["S", "F", "C", "S"],
               ["A", "D", "E", "E"]],
        word="ABCCEDG"
    )
)
print(
    Solution().exist(
        board=[["A","B","C","E"],
               ["S","F","E","S"],
               ["A","D","E","E"]],
        word="ABCESEEEFS"
    )
)
