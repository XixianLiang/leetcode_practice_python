from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        state = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        def getAround(i, j):
            cnt = 0
            for x in range(max(i - 1, 0), min(len(board) - 1, i + 1) + 1):
                for y in range(max(j - 1, 0), min(len(board[0]) - 1, j + 1) + 1):
                    if x == i and y == j:
                        continue
                    cnt += board[x][y]
            return cnt

        for i in range(len(board)):
            for j in range(len(board[0])):
                around = getAround(i, j)
                if around < 2 or around > 3:
                    state[i][j] = 0
                    continue
                if board[i][j] == 0 and around == 2:
                    state[i][j] = 0
                    continue
                state[i][j] = 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = state[i][j]

Solution().gameOfLife(
    [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
)