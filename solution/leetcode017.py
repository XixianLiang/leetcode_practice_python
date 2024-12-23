from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.digits = digits
        self.mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.ans = []
        self.backtracking(0, "")
        return self.ans

    def backtracking(self, begin, cur: str):
        if begin == len(self.digits):
            return self.ans.append("".join(cur))

        for ch in self.mapping[self.digits[begin]]:
            self.backtracking(begin + 1, cur + ch)
