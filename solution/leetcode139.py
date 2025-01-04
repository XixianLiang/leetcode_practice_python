from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        self.wordDict.sort(key= lambda x:len(x), reverse=True)
        return self.traceback(s)
    
    def traceback(self, s: str):
        if s in self.wordDict:
            return True
        
        ans = False
        for word in self.wordDict:
            if s.startswith(word):
                ans = ans or self.traceback(s[len(word):])
        return ans

print(Solution().wordBreak("catleetode", ["leetcode", "cat"]))