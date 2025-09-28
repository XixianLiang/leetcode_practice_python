from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = j = 0
        zeros = 0
        ans = 0
        while j < len(nums):
            j = i if i > j else j
            while j < len(nums) and zeros < k:
                zeros += 1 if nums[j] == 0 else 0
                j += 1
            while j < len(nums) and nums[j] == 1:
                j += 1
            ans = max(ans, j - i)
            if zeros > 0:
                zeros -= 1 if nums[i] == 0 else 0
            i += 1
        return ans


Solution().longestOnes([0,0,1,1,1,0], 0)