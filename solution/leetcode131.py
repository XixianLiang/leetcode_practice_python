from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans:List[List[str]] = []
        self.build_huiwen_dp(s)
        
        self.traceback(0, s, [])
        return self.ans
    
    def traceback(self, i0, s, cur_lt:List[str]):
        if i0 == len(s):
            self.ans.append(cur_lt[:])
        for i in range(i0, len(s)):
            if self.dp[i0][i]:
                cur_lt.append(s[i0:i+1])
                self.traceback(i + 1, s, cur_lt)
                cur_lt.pop()   
    
    def build_huiwen_dp(self, s):
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i > 0 and s[i-1] == s[i]:
                dp[i-1][i] = True
        
        for i in reversed(range(len(s))):
            for j in range(i + 1, len(s)):
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
        
        self.dp = dp

print(Solution().partition("aaa"))