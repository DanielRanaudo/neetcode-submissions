class Solution:
    def rob(self, nums: List[int]) -> int:
        maxim = 0
        if len(nums) < 4:
            for n in nums:
                maxim = max(maxim, n)
            return maxim


        #remove the two extremes, solve standard house robber
        prev, prevPrev = 0, 0
        for i in range(len(nums) - 1):
            temp = prev
            prev = max(prev, nums[i] + prevPrev)
            prevPrev = temp

        max1 = prev

        #reset
        prev, prevPrev = 0, 0
        for i in range(1, len(nums)):
            temp = prev
            prev = max(prev, nums[i] + prevPrev)
            prevPrev = temp

        max2 = prev

        return max(max1, max2)


        



        