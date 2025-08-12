from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = Counter(t)


        def covered():
            nonlocal target
            return all(_ <= 0 for _ in target.values())


        i = j = 0
        ans = None
        while j < len(s):
            while j < len(s) and not covered():
                if s[j] in target:
                    target[s[j]] -= 1
                j += 1

            while i < j and covered():
                ans = s[i:j] if (ans is None or len(ans) > len(s[i:j])) else ans
                if s[i] in target:
                    target[s[i]] += 1
                    while i < j and s[i] not in target:
                        i += 1
                i += 1

        return ans




s = "BBA"
t = "AB"

print(Solution().minWindow(s, t))