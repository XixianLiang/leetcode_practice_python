from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        l = 0
        p_bias = dict()
        for ch in p:
            p_bias[ch] = p_bias.get(ch, 0) + 1
        for i in range(len(p)):
            p_bias[s[i]] = p_bias.get(s[i], 0) - 1
        ans = []
        for l in range(len(s) - len(p) + 1):
            if not any(list(p_bias.values())):
                ans.append(l)
            if l < len(s) - len(p):
                p_bias[s[l]] += 1
                p_bias[s[l + len(p)]] = p_bias.get(s[l + len(p)], 0) - 1 
                l += 1
        return ans
                


print(Solution().findAnagrams("abab", "ab"))
