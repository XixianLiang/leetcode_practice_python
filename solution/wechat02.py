


def find_best_profits(nums):
    if len(nums) <= 2:
        return max(nums)
    dp = [0 for _ in range(len(nums))]
    
    dp[0] = nums[0]
    dp[1] = nums[1]
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    return dp[-1]


print(find_best_profits(
    [20,70,90,30,10]
))
print(find_best_profits(
    [10,20,30,10]
))