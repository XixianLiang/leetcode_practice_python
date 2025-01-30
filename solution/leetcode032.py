class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        l = r = 0
        max_forward  = 0
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            
            if l == r:
                max_forward  = max(max_forward, l * 2)
            elif l < r:
                l = r = 0
            
        
        l = r = 0
        max_backward = 0
        for i in reversed(range(len(s))):
            if s[i] == ")":
                r += 1
            else:
                l += 1
            
            if l == r:
                max_backward = max(max_backward, r * 2)
            elif r < l:
                l = r = 0
        
        return max(max_forward, max_backward)


print(Solution().longestValidParentheses("(()"))