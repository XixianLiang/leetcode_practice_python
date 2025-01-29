from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = dict()
        nums = [1] + nums + [1]

        def get_max_coins(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            max_coins_k = 0
            for k in range(l + 1, r):
                temp_coins_k = get_max_coins(l, k) + nums[l]*nums[k]*nums[r] + get_max_coins(k, r)
                max_coins_k = max(max_coins_k, temp_coins_k)
            dp[(l, r)] = max_coins_k
            return dp[(l, r)]
        
        return get_max_coins(0, len(nums) - 1)

print(Solution().maxCoins([1, 5]))
print(Solution().maxCoins([3, 1, 5, 8]))