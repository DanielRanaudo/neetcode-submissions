class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        maxim = 0
        prod = 1
        for n in nums:
            prod *= n
            maxim = max(prod, maxim)
            if prod == 0:
                prod = 1

        
        
        prod = 1
        for n in reversed(nums):
            prod *= n
            maxim = max(prod, maxim)
            if prod == 0:
                prod = 1

        return maxim
            


            



        