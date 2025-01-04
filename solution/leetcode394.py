from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        s = "1[" + s + "]"
        stack_mul = []
        stack_str = []
        
        i = 0
        while i < len(s):
            ch = s[i]
            if ord(ch) in range(ord("0"), ord("9") + 1):
                mul_str = ch
                i += 1
                while ord(s[i]) in range(ord("0"), ord("9") + 1):
                    mul_str += s[i]
                    i += 1
                stack_mul.append(int(mul_str))
                continue
            elif ch == "[":
                stack_str.append("")
            elif ord(ch) in range(ord("a"), ord("z") + 1):
                stack_str[-1] += ch
            elif ch == "]":
                temp_str = stack_mul.pop() * stack_str.pop()
                if len(stack_str) == 0:
                    return temp_str
                else:
                    stack_str[-1] += temp_str
            i += 1
                

s = "10[leetcode]"
print(Solution().decodeString(s))