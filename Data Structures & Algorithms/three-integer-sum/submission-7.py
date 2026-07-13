class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for fixed in range(len(nums)):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue
            j = len(nums) - 1
            i = fixed + 1
            while i < j:
                if nums[fixed] + nums[i] + nums[j] > 0:
                    j -= 1
                elif nums[fixed] + nums[i] + nums[j] < 0:
                    i += 1
                else:
                    res.append([nums[fixed], nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    
        return res

