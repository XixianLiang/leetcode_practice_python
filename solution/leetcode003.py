class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        h = dict()
        l = r = 0
        ans = 0
        while r < len(s):
            while r < len(s) and not h.get(s[r], 0):
                h[s[r]] = h.get(s[r], 0) + 1
                r += 1
            
            ans = max(ans, r - l)
            
            while r < len(s) and l <= r:
                pop_ch = s[l]
                h[pop_ch] -= 1
                l += 1
                if pop_ch == s[r]:
                    break
        return ans


print(Solution().lengthOfLongestSubstring("aa"))
