class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0 for _ in range(n)] for _ in range(n)]
        
        def cal_available(board):
            nonlocal n
            available = [[True for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if not available[i][j]:
                        continue
                    if board[i][j]:
                        for x in range(n):
                            available[i][x] = False
                            available[x][j] = False
                            if i + x < n and j + x < n:
                                available[i+x][j+x] = False
                            if i - x >= 0 and j - x >= 0:
                                available[i - x][j - x] = False
                            if i - x >= 0 and j + x < n:
                                available[i-x][j+x] = False
                            if i + x < n and j - x >= 0:
                                available[i+x][j-x] = False 
                                
            return available
                        
        
        ans = 0
        
        def traceback(cur_board, target):
            nonlocal ans
            if target == 0:
                ans += 1
                return
            available = cal_available(cur_board)
            i = n - target
            for j in range(n):
                if available[i][j]:
                    cur_board[i][j] = 1
                    traceback(cur_board, target-1)
                    cur_board[i][j] = 0
        
        traceback(board, n)
        return ans

print(Solution().totalNQueens(4))