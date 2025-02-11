from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        farest = dict()
        for i in reversed(range(len(s))):
            if farest.get(s[i], None) is None:
                farest[s[i]] = i
        
        ans = []
        start_i = 0
        next_i = -1
        while i < len(s):
            next_i = max(next_i, farest[s[i]])
            if i >= next_i:
                ans.append(i - start_i + 1)
                start_i = i + 1
            i += 1
        
        return ans

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))