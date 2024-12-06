from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i, num in enumerate(nums):
            if hash.get(num, None) is not None:
                return [i, hash[num]]
            else:
                hash[target - num] = i