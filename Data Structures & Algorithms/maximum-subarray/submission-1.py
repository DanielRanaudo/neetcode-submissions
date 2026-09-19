class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = nums[0]
        currSum = max(nums[0], 0)

        for r in range(1, len(nums)):
            currSum += nums[r]
            maxim = max(maxim, currSum)

            if currSum < 0:
                currSum = 0
        
        return maxim