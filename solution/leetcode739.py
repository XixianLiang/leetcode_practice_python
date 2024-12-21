from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_index_stack = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not t_index_stack:
                t_index_stack.append(i) 
            elif t <= temperatures[t_index_stack[-1]]:
                t_index_stack.append(i)
            else: 
                while t_index_stack:
                    if t <= temperatures[t_index_stack[-1]]:
                        break
                    j = t_index_stack.pop()
                    if t > temperatures[j]:
                        ans[j] = i - j 
                t_index_stack.append(i)
        print(ans)
        return ans
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_index_stack = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while t_index_stack and t > temperatures[t_index_stack[-1]]:
                j = t_index_stack.pop()
                if t > temperatures[j]:
                    ans[j] = i - j 
            t_index_stack.append(i)
        print(ans)
        return ans
            
Solution().dailyTemperatures([73,74,75,71,69,72,76,73])