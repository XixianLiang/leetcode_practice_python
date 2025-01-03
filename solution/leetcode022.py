from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.traceback("", n, 0)
        return self.ans
    
    def traceback(self, cur_str, l_n, r_n):
        if l_n == 0 and r_n == 0:
            self.ans.append(cur_str)
            return
        if l_n > 0:
            cur_str += "("
            self.traceback(cur_str, l_n - 1, r_n + 1)
            cur_str = cur_str[:-1]
        if r_n > 0:
            cur_str += ")"
            self.traceback(cur_str, l_n, r_n - 1)
            cur_str = cur_str[:-1]

print(Solution().generateParenthesis(3))