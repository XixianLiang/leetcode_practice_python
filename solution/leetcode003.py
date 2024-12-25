class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        ans = 0
        for i in range(len(s)):
            hash_tab = dict()
            for j in range(i, len(s)):
                hash_tab[s[j]] = hash_tab.get(s[j], 0) + 1
                if hash_tab[s[j]] > 1:
                    ans = max(ans, j - i)
                    break
                if j + 1 == len(s):
                    ans = max(ans, j + 1 - i)
        return ans


print(Solution().lengthOfLongestSubstring("a"))
