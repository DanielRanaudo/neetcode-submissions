class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        maxim = 0
        for i in range(len(nums)):
            if i < 2:
                dp[i] = nums[i]
                if i == 1:
                    dp[i] = max(dp[0], nums[i])
                maxim = max(maxim, dp[i])
                continue
            
            #otherwise, compare left with left left
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            maxim = max(maxim, dp[i])

        return maxim

        

            

        