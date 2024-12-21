from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ")", "[": "]", "{": "}"}
        for ch in s:
            if ch in ["(", "{", "["]:
                stack.append(mapping[ch])
            else:
                if stack[-1] != ch:
                    return False
                stack.pop(-1)

        return True if len(stack) == 0 else False
