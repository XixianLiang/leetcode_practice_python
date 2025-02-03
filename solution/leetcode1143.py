class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
        
        ans = 0
        
        t = 0
        while t < len(text1):
            if text1[t] == text2[0]:
                while t < len(text1):
                    dp[0][t] = 1
                    t += 1
                    ans = 1
            t += 1
        t = 0
        while t < len(text2):
            if text2[t] == text1[0]:
                while t < len(text2):
                    dp[t][0] = 1
                    t += 1
                    ans = 1
            t += 1
        
        
        for i in range(1, len(text2)):
            for j in range(1, len(text1)):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return ans
                    
print(Solution().longestCommonSubsequence("bl", "yby"))