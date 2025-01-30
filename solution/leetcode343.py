class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        dp = [1] + [_ for _ in range(1, n+1)]
        
        for i in range(n + 1):
            pass
            for j in range(1, i):
                dp[i] = max(dp[j] * dp[i - j], dp[i])
        
        return dp[-1]

print(Solution().integerBreak(5))