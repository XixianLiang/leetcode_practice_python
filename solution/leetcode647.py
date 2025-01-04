class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ans = 0
        self.build_huiwen_dp(s)
        return self.ans
                    
    
    def build_huiwen_dp(self, s):
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            self.ans += 1
            if i > 0 and s[i-1] == s[i]:
                dp[i-1][i] = True
                self.ans += 1
        
        for i in reversed(range(len(s))):
            for j in range(i + 1, len(s)):
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    self.ans += 1
        
        self.dp = dp

print(Solution().countSubstrings("aaa"))