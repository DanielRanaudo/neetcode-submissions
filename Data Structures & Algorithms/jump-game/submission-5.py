class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = [False] * len(nums)
        res[len(nums) - 1] = True #base case

        for i in range(len(nums) - 2, -1, -1):
            val = nums[i]

            if i + val >= len(nums):
                res[i] = True
                continue
            for j in range(i, i + val + 1):
                if res[j] == True:
                    res[i] = True
                    continue
            

        return res[0]

        