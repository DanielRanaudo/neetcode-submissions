class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for fixed in range(len(nums)):
            target = nums[fixed]
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue
            i = fixed + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + target == 0:
                    res.append([target, nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif nums[i] + nums[j] + target > 0:
                    j -= 1
                else:
                    i += 1


        return res



