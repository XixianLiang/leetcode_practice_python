import collections
from typing import Dict

class IncludesMap(Dict):
    def includes(self, target_map):
        for key in list(target_map.keys()):
            if self.get(key, 0) < target_map[key]:
                return False
        return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        included_map = IncludesMap()
        target_map = IncludesMap(collections.Counter(t))
        
        i = 0
        ans = "*" * int(1e6)
        has_ans = False
        for j in range(len(s)):
            if s[j] in t:
                included_map[s[j]] = included_map.get(s[j], 0) + 1
            while included_map.includes(target_map):
                has_ans = True
                ans = s[i: j+1] if j+1-i < len(ans) else ans
                
                if s[i] in t:
                    included_map[s[i]] = included_map.get(s[i], 0) - 1
                i += 1
        return ans if has_ans else ""

s = "ADOBECODEBANC"
t = "ABC"

print(Solution().minWindow(s, t))