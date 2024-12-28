from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_lt = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            prefix_lt[i] = prefix_lt[i - 1] + nums[i - 1]

        hash_tab = dict()
        ans = 0

        for i, prefix in enumerate(prefix_lt):
            if hash_tab.get(prefix, None) is not None:
                ans += hash_tab[prefix]
            hash_tab[k + prefix] = hash_tab.get(k + prefix, 0) + 1
        return ans


print(Solution().subarraySum([1, 2, 3], 3))
print(Solution().subarraySum([1, -1, 0], 0))
