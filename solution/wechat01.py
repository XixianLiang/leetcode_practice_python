from typing import List



class Solution:
    
    def find_subtrace(self, array: List[int], target:int):
        if target <= 0 and len(array) > 0:
            return 1
        
        cur = 0
        i = j = 0
        ans = float("inf")
        while j < len(array):
            cur += array[j]
            if cur >= target:
                while cur - array[i] >= target:
                    cur -= array[i]
                    i += 1
                ans = min(ans, j - i + 1)
            j += 1
        
        return 0 if ans == float("inf") else ans

print(Solution().find_subtrace([0, 1, 0, 1, 2000000000000000, 1], 2000000000000000))