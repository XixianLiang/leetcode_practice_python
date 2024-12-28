from typing import List


class Solution:
    def get_bias(self, ch: str):
        return ord(ch) - 97

    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = [0 for _ in range(26)]
        for ch in p:
            p_counter[self.get_bias(ch)] += 1

        for i in range(len(p)):
            p_counter[self.get_bias(s[i])] -= 1

        ans = []
        i = 0
        while True:
            if all([_ == 0 for _ in p_counter]):
                ans.append(i)
            if i == len(s) - len(p):
                break

            p_counter[self.get_bias(s[i])] += 1
            p_counter[self.get_bias(s[i + len(p)])] -= 1
            i += 1

        return ans


print(Solution().findAnagrams("abab", "ab"))
