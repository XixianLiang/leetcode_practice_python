class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for row in range(1, len(word1) + 1):
            dp[row][0] = row
        for col in range(1, len(word2) + 1):
            dp[0][col] = col
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min([
                        dp[i-1][j] + 1,
                        dp[i][j-1] + 1,
                        dp[i-1][j-1] + 1
                    ])
        
        return dp[-1][-1]
        

print(Solution().minDistance("horse", "ros"))