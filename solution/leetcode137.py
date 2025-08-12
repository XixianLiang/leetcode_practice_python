from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = 0
        minus = 0
        for num in nums:
            if num < 0:
                minus += 1
        
        for i in range(32):
            bit_i = sum(
                (abs(num) >> i) & 1 for num in nums
            ) % 3
            bits = (bits | (bit_i << i))
        
        return bits if minus % 3 == 0 else -bits

print(Solution().singleNumber(
    [5, 5, 5, -4, 6, 6, 6]
))