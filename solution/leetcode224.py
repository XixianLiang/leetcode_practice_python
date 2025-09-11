class Solution:
    def calculate(self, s: str) -> int:

        def apply_op(sub_s):
            num_stack = []
            ops = 1
            
            i = 0
            while i < len(sub_s):
                if sub_s[i] >= "0" and sub_s[i] <= "9":
                    num = ""
                    while i < len(sub_s) and sub_s[i] >= "0" and sub_s[i] <= "9":
                        num += sub_s[i]
                        i += 1
                    num = int(num)
                    num_stack.append(ops * num)
                    ops = 1
                    continue
                elif sub_s[i] in ["-", "+"]:
                    if sub_s[i] == "-":
                        ops = -ops
                i += 1
            return sum(num_stack)
                    
        stack = []
        string = ""
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(string)
                string = ""
            elif s[i] == ")":
                sub_ans = apply_op(string)
                stack[-1] += str(sub_ans)
                string = stack.pop()
            elif s[i] == " ":
                continue
            else:
                string += s[i]
        return apply_op(string)


print(Solution().calculate("1-(     -2)"))