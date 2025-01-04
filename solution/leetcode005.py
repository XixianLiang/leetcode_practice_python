class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ans = s[0]
        dp[len(s) - 1][0] = True

        for i in range(len(s)):
            dp[i][i] = True
            if i - 1 >= 0 and s[i - 1] == s[i]:
                dp[i - 1][i] = True
                ans = s[i - 1 : i + 1]
            if i + 1 < len(s) and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = s[i : i + 2]

        for i in range(len(s) - 2, -1, -1):
            for j in range(0, len(s)):
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if len(ans) < j - i + 1:
                        ans = s[i : j + 1]

        return ans
